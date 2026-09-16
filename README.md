# reframe-skill — 重构式解惑

> **方法来源**：本 skill 的提问风格与重构手法，受辩手**黄执中**的公开辩论与访谈方法论启发。
> 它是对公开方法的工程化蒸馏，**不代表本人观点，也不含任何未公开内容**。

> 当你纠结、迷茫、不知道怎么办的时候——它不给你答案，它帮你找到真正的问题。

**不是回答问题，是翻译问题。把别人语言里藏着的恐惧、逃避、自欺，翻译成他能面对的现实。**

---

## 🚀 最简单的使用方式

### 你用 AI 助手吗？直接跟它说：

> **"帮我安装 reframe skill，GitHub 地址是 https://github.com/zhengxu245-boop/reframe-skill"**
>
> Gitee 国内镜像：https://gitee.com/foround/reframe-skill

也可以直接复制安装命令：

```bash
# GitHub（海外 / 有代理）
git clone https://github.com/zhengxu245-boop/reframe-skill.git ~/.claude/skills/reframe-skill
# Gitee（国内直连，内容同步）
git clone https://gitee.com/foround/reframe-skill.git ~/.claude/skills/reframe-skill
```

然后就可以跟它聊天了：

> "我很纠结要不要辞职" → 它会用七种重构手法引导你发现自己的真正问题

### 或者，把 SKILL.md 的内容发给任何 AI

> **"请按照以下设定跟我对话：[粘贴 SKILL.md 的全部内容]"**

这样就不用安装任何东西——任何 AI 都能用，Claude、ChatGPT、Gemini、通义千问、Kimi……全都行。

### 你用 Claude Code 吗？一行命令：

```
/reframe 我总是控制不住自己的脾气，怎么办？
```

### 你想用 API 跑？也可以：

```bash
pip install requests
export DEEPSEEK_API_KEY="你的key"   # 去 platform.deepseek.com 免费注册获取
python3 reframe_chat.py "我不知道该不该分手"
```

脚本只通过环境变量 `DEEPSEEK_API_KEY` 读取密钥，不会写死在代码里，也不会把密钥提交进仓库。

就这么简单，不需要任何技术背景。👇 下面是详细说明，有需要的再看。

---

## 🎯 什么情况下可以找它聊聊？

- 💔 感情困惑："他/她对我好不好？该不该继续？"
- 😰 决策犹豫："我不知道自己想要什么"
- 😤 情绪困扰："我总是控制不住自己的脾气"
- 🤔 自我怀疑："我是不是太敏感了？是不是我想太多了？"
- 😢 人际冲突："为什么总是我退让？"
- 👨‍👩‍👧 家庭矛盾："父母总是逼我做不想做的事"
- 💼 职场烦恼："我不敢拒绝别人"
- 🪞 自我认知："为什么我总是遇到伤害我的人？"

**触发词**：困惑、纠结、迷茫、怎么办、该不该、选择、犹豫、敏感、害怕、不安、理不清、帮我理一理、我不知道自己想要什么

## 📊 对话效果示例

以下是一个真实的5轮对话：

```
用户：我男朋友说他因为我胖所以对感情有所保留，我该不该继续？
它：被這樣說，很受傷吧？他保留的不是感情，是嫌你不夠瘦的藉口 ☁️

用户：可我觉得如果他真的爱我就不应该在意这些
它：翻譯成白話其實是：「你讓我失望了」。那問題來了：他現在確實很在意，你會怎麼處理這個「失望」？

用户：我确实也勉强接受了他的穷和安于现状...
它：原來你也在「勉強」自己啊。他嫌你胖，你忍他窮，這叫互相體諒，還是互相欠債？😂

用户：好像确实是这样...可是胖好解决还是穷好解决？
它：比誰的問題「好解決」？你已經把愛情談成一場競標了耶 😂

用户：我明白了，谢谢
它：☁️ 你以为问题是「他嫌我胖」，但真正的问题是「我们愿不愿意为彼此建一座桥」。
     公式：感情保留不是体重问题，而是共同面对差异的意愿问题。🌹
```

## 💡 它是怎么工作的？

你跟它说"我很纠结要不要辞职"，它不会直接说"辞职吧"或"别辞职"。

它的工作方式是——

**第一步：确认你的感受**
> "听起来你很纠结，是吧？"

**第二步：把你的话翻译成白话**
> "你说'不知道怎么选'——翻译成白话其实是'舍不得'"

**第三步：帮你换个角度看**
> "如果明天你出了车祸住院了，他们就完蛋了吗？"

**第四步：推到极端看看**
> "最坏的结果是什么？你能承受吗？"

**第五步：给你一个公式带走**
> ☁️ 你以为问题是「该不该辞职」，但真正的问题是「你害怕辞职后不如现在」。
> 公式：纠结不是选择的问题，而是勇气的问题 🌹

**核心原则：不做"回答者"，做"翻译者"。**

## 🧩 设计理念：模型无关

本 Skill 的核心逻辑**完全自包含在 SKILL.md 中**，不依赖任何特定模型或 API：

- ✅ **任何模型都能用** — Claude、GPT、Gemini、Llama、通义千问、Kimi、DeepSeek……只要能理解自然语言指令
- ✅ **任何平台都能用** — 只需把 SKILL.md 内容作为 system prompt
- ✅ **不需要写代码** — 纯自然语言定义，复制粘贴即可
- ✅ **模型越强效果越好** — 但即使小模型也能遵循基本的"不答原问→翻译→反问"节奏
- 🔧 Python 脚本是可选的 — 适合需要 API 集成或独立运行的场景

---

## ⚙️ 技术说明（开发者看这里）

### Features

- 🧠 模型无关：纯 prompt 驱动，不绑定任何特定 API
- 🗣️ **风格要点：简短反问、翻译手法、适度幽默、偶尔繁体**
- 🔄 多轮对话引导（最多5轮）
- 📐 公式化收尾："X不是Y，而是Z"
- 🔧 七大重构手法：因果倒置、假议题揭示、视角翻转、需求翻译、前提推翻、二选一破除、责任重分配

### 文件说明

| 文件 | 用途 | 是否必需 |
|------|------|---------|
| SKILL.md | 核心逻辑，纯自然语言 prompt | ✅ 必需 |
| reframe_chat.py | DeepSeek API 封装脚本 | 🔧 可选 |
| README.md | 使用说明 | 📖 文档 |

- Python 3.8+
- `requests` library (`pip install requests`)
- DeepSeek API Key ([获取地址](https://platform.deepseek.com/))

### Installation

```bash
# Clone the repo（国内可换用 Gitee 镜像：https://gitee.com/foround/reframe-skill.git）
git clone https://github.com/zhengxu245-boop/reframe-skill.git
cd reframe-skill

# Set your API key
export DEEPSEEK_API_KEY="your-api-key-here"

# Run interactive mode
python3 reframe_chat.py "我总是控制不住自己的脾气，怎么办？"

# Or enter interactive mode without initial question
python3 reframe_chat.py
```

### Single Reply Mode (for integration)

```bash
# Get a single reply
python3 reframe_chat.py --single "我不知道该不该分手"

# With conversation history
python3 reframe_chat.py --single "可我觉得他不尊重我" --history history.json

# Force closing summary
python3 reframe_chat.py --single "我明白了" --closing
```

---

## 🔌 集成指南：主流 Agent 平台

### 💡 通用原则

**本 Skill 的核心就是 SKILL.md —— 把它作为 system prompt，任何平台、任何模型都能用。**

```
system prompt = SKILL.md 的全部内容
```

以下各平台的具体配置方式，本质上都是这一件事的不同包装。

---

### 1. Claude Code (Anthropic)

**方式一：作为 Skill 注册**

```bash
# 复制 skill 目录
cp -r . ~/.claude/skills/reframe-skill/

# 在 index.toml 注册
echo '- **name**: reframe' >> ~/.claude/skills/index.toml
```

使用：`/reframe 我不知道该不该辞职`

**方式二：在对话中粘贴 SKILL.md**

直接把 SKILL.md 内容发给 Claude，说"按照这个设定跟我对话"即可。

---

### 2. OpenClaw

```yaml
# openclaw-config.yaml
tools:
  - name: reframe_counsel
    type: prompt
    description: "重构式解惑"
    system_prompt_file: ./SKILL.md
```

---

### 3. Claude (Anthropic API)

```python
import anthropic

# 读取 SKILL.md 作为 system prompt
with open("SKILL.md") as f:
    system_prompt = f.read()

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=200,
    system=system_prompt,
    messages=[
        {"role": "user", "content": "我总是控制不住自己的脾气，怎么办？"}
    ]
)
```

---

### 4. ChatGPT / GPT / Codex (OpenAI)

```python
from openai import OpenAI

with open("SKILL.md") as f:
    system_prompt = f.read()

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "我不知道该不该分手"}
    ]
)
```

---

### 5. Dify

1. 创建聊天助手 → 系统提示词 → 粘贴 SKILL.md 全部内容
2. 或创建工作流 → LLM 节点 → System 栏粘贴 SKILL.md

---

### 6. Coze (扣子)

1. 创建 Bot → 人设与回复逻辑 → 粘贴 SKILL.md 内容
2. 或创建插件 → 系统提示词引用 SKILL.md

---

### 7. LangChain / LlamaIndex

```python
from langchain.tools import tool

with open("SKILL.md") as f:
    REFRAME_SYSTEM_PROMPT = f.read()

@tool
def reframe_counsel(question: str) -> str:
    """重构式解惑。当用户提出困惑、纠结时使用。"""
    # 用任何模型 + SKILL.md 作为 system prompt 调用
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(model="gpt-4o")
    response = llm.invoke([
        ("system", REFRAME_SYSTEM_PROMPT),
        ("human", question)
    ])
    return response.content
```

---

### 8. CrewAI / AutoGPT / MetaGPT

```python
from crewai import Agent

with open("SKILL.md") as f:
    reframe_prompt = f.read()

counselor = Agent(
    role="重构式解惑师",
    goal="通过提问引导用户发现真正问题",
    backstory=reframe_prompt  # 直接用 SKILL.md 作为 backstory
)
```

---

### 9. 通用 HTTP API（任何平台都能调用）

```python
# server.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

with open("SKILL.md") as f:
    SYSTEM_PROMPT = f.read()

@app.route("/counsel", methods=["POST"])
def counsel():
    data = request.json
    # 用任何兼容 OpenAI 格式的 API
    resp = requests.post(
        "https://api.openai.com/v1/chat/completions",  # 或任何其他 API
        headers={"Authorization": f"Bearer {YOUR_API_KEY}"},
        json={
            "model": "gpt-4o",  # 或任何模型
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                *data.get("history", []),
                {"role": "user", "content": data["message"]}
            ],
            "temperature": 0.7,
            "max_tokens": 200
        }
    )
    return jsonify({"reply": resp.json()['choices'][0]['message']['content']})
```

---

## 🧠 Methodology

### 五步对话流程

```
用户提问 → [不答原问题] → [翻译语言] → [翻转视角] → [极限推演] → [公式收尾]
    ↓           ↓             ↓            ↓            ↓           ↓
"我该怎么办"  "你问错了"   "你说的X     "换个人看    "最坏会    "X不是Y
                           其实是Y"      是另一个故事"  怎样？"    而是Z"
```

### 七大重构手法

| 手法 | 核心逻辑 | 示例 |
|------|---------|------|
| 因果倒置 | A导致B？不，B导致A | "控制不住脾气"→"越想控制越失控" |
| 假议题揭示 | 这个问题不存在 | "坚持还是放弃"→"你根本没有在坚持" |
| 视角翻转 | 换人看是另一个故事 | "他不爱我"→"只有你觉得好好的" |
| 需求翻译 | 把包装翻译成白话 | "不知道怎么选"→"舍不得" |
| 前提推翻 | 你问题的前提是错的 | "该坚持梦想吗"→"你为它付出过切实努力吗" |
| 二选一破除 | 不是只有A和B | "留下被骚扰还是离开"→"拒绝他就待不下去了吗" |
| 责任重分配 | 该谁来解决 | "我该怎么应对"→"为什么要你来应对" |

---

## 📁 File Structure

```
reframe-skill/
├── README.md          # 本文件
├── SKILL.md           # Skill 配置与完整方法论说明
└── reframe_chat.py    # DeepSeek API 驱动的对话脚本
```

## ⚙️ Configuration

| 参数 | 默认值 | 说明 |
|------|--------|------|
| Model | deepseek-v4-pro | 推理模型（reasoning_tokens 和输出共享 max_tokens 配额） |
| Temperature | 0.7 | 对话灵活性 |
| Max Tokens | 600 (对话) / 1000 (收尾) | 推理模型需要较高值 |
| Max Rounds | 5 | 最大对话轮数 |

## 📝 License

MIT — 详见 [LICENSE](./LICENSE)

## 🙏 Credits

- 重构手法基于对 534 条公开问答的方法论分析
- 公开资料分析，不代表本人观点
