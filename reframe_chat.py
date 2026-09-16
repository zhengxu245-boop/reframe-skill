#!/usr/bin/env python3
"""
reframe — 重构式解惑对话脚本
通过多轮提问把「以为的问题」重构为「真正的问题」
使用 DeepSeek V4 Pro 模型驱动对话
"""

import sys
import os
import json
import requests
import argparse
from pathlib import Path

API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
if not API_KEY:
    sys.exit(
        "错误: 未设置 DEEPSEEK_API_KEY 环境变量。\n"
        "请先执行: export DEEPSEEK_API_KEY='你的key'\n"
        "获取地址: https://platform.deepseek.com/"
    )
API_URL = "https://api.deepseek.com/v1/chat/completions"
MODEL = "deepseek-v4-pro"

# 方法论来源：同目录的 SKILL.md（唯一权威定义）
# 脚本不再内嵌人格 prompt —— 改 SKILL.md 即可同步生效，避免两处规则漂移
_SKILL_PATH = Path(__file__).resolve().parent / "SKILL.md"

# 回退用精简 prompt（仅当 SKILL.md 缺失时启用）
_FALLBACK_PROMPT = """你是一位擅长重构提问的对话者。你不直接给答案，而是把对方「以为的问题」重构为「真正的问题」。

规则：
- 每次回复不超过 80 字，先确认感受，再反问或翻译
- 绝不直接给建议，绝不站队评判，绝不鸡汤安慰
- 善用翻译手法：把包装过的情绪翻译成白话
- 收尾用「X不是Y，而是Z」的公式结构

七大重构手法：因果倒置、假议题揭示、视角翻转、需求翻译、前提推翻、二选一破除、责任重分配。"""


def reframe_system_prompt():
    """读取 SKILL.md 作为 system prompt（带缓存）"""
    try:
        return _SKILL_PATH.read_text(encoding="utf-8")
    except Exception:
        return _FALLBACK_PROMPT


CLOSING_SYSTEM_PROMPT = """现在是对话的最后一轮，你需要给出总结。

格式要求：
1. 先用 ☁️ 开头
2. 用「X不是Y，而是Z」的公式结构总结核心洞察
3. 用一句温暖的话收尾，加 🌹
4. 总长度不超过150字

示例：
☁️ 你以为问题是「该不该坚持」，
但真正的问题是「你有没有为它付出过切实的努力」。

公式：你问的不是「能不能坚持」，而是「愿不愿意开始」。

关注骆驼，不要关注稻草 🌹"""


def chat(user_input, history=None, is_closing=False):
    """调用 DeepSeek API 生成回复"""
    if history is None:
        history = []

    system = CLOSING_SYSTEM_PROMPT if is_closing else reframe_system_prompt()

    messages = [{"role": "system", "content": system}]
    for h in history:
        messages.append(h)
    messages.append({"role": "user", "content": user_input})

    try:
        resp = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": MODEL,
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 1000 if is_closing else 600,
            },
            timeout=60
        )

        if resp.status_code == 200:
            return resp.json()['choices'][0]['message']['content']
        else:
            return f"[API错误: {resp.status_code}]"
    except Exception as e:
        return f"[错误: {e}]"


def is_closing_signal(user_input):
    """判断用户是否表示领悟或想结束对话"""
    signals = ['明白了', '懂了', '谢谢', '理解了', '原来如此', '恍然大悟',
               '清晰了', '知道了', '想通了', '开窍了', '悟了']
    return any(s in user_input for s in signals)


def interactive_mode(initial_question):
    """交互式对话模式"""
    print("\n" + "="*50)
    print("  reframe — 重构式解惑")
    print("  输入你的困惑，开始对话")
    print("  输入 'q' 结束对话")
    print("="*50 + "\n")

    history = []
    turn = 0
    max_turns = 5

    # If initial question provided, start with it
    if initial_question:
        user_input = initial_question
    else:
        user_input = input("你: ").strip()
        if not user_input or user_input == 'q':
            return

    while turn < max_turns:
        # Generate response
        is_last = (turn >= max_turns - 1) or is_closing_signal(user_input)
        reply = chat(user_input, history, is_closing=is_last)

        print(f"\n执中: {reply}\n")

        # Update history
        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": reply})

        # Keep only last 4 turns
        if len(history) > 8:
            history = history[-8:]

        if is_last:
            break

        turn += 1

        # Get next user input
        user_input = input("你: ").strip()
        if not user_input or user_input == 'q':
            # Generate closing
            closing = chat("用户想结束对话了，请给出最后的公式总结。",
                          history, is_closing=True)
            print(f"\n执中: {closing}\n")
            break


def single_reply(user_input, history=None):
    """单次回复模式（供 skill 调用）"""
    if history is None:
        history = []

    is_closing = is_closing_signal(user_input)
    reply = chat(user_input, history, is_closing=is_closing)

    return reply


def main():
    parser = argparse.ArgumentParser(description="reframe — 重构式解惑")
    parser.add_argument('question', nargs='?', help="初始问题")
    parser.add_argument('--history', type=str, help="对话历史JSON文件路径")
    parser.add_argument('--single', action='store_true', help="单次回复模式")
    parser.add_argument('--closing', action='store_true', help="强制收尾模式")
    args = parser.parse_args()

    if args.single:
        # Single reply mode for skill integration
        user_input = args.question or input().strip()
        history = []
        if args.history and os.path.exists(args.history):
            with open(args.history) as f:
                history = json.load(f)
        reply = chat(user_input, history, is_closing=args.closing)
        print(reply)
    else:
        # Interactive mode
        interactive_mode(args.question)


if __name__ == "__main__":
    main()
