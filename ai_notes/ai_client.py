# ===== ai_notes/ai_client.py — AI 调用模块 =====
"""封装 DeepSeek API 调用，提供标题生成和总结功能"""

import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# .env 放在项目根目录（ai_notes/ 的上一级）
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

_client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)


def _sanitize(text: str) -> str:
    """处理 API 返回值中的非法字符（surrogate 等）"""
    if not text:
        return ""
    return text.encode("utf-8", errors="replace").decode("utf-8")


def _chat(system_prompt: str, user_content: str, temperature: float = 0.3) -> str:
    """通用 AI 调用（内部函数，外面不直接用）"""
    try:
        response = _client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
            temperature=temperature,
        )
        return _sanitize(response.choices[0].message.content or "")
    except Exception as e:
        # 如果 API 调用本身失败，把错误抛出去让调用方处理
        raise RuntimeError(f"API调用失败: {e}") from e


def generate_title_and_tags(note_content: str) -> tuple[str, list[str]]:
    """根据笔记内容，让 AI 自动生成标题和标签
    返回：(标题, [标签列表])
    """
    prompt = f"""根据以下笔记内容，生成一个简短的标题（10字以内）和2-4个标签。

回复格式必须严格如下（不要加其他内容）：
标题：xxx
标签：tag1, tag2, tag3

笔记内容：
{note_content}"""

    reply = _chat(
        system_prompt="你是一个笔记整理助手，请用中文回复。只输出要求的格式，不要额外解释。",
        user_content=prompt,
        temperature=0.3,
    )

    # 解析 AI 返回的格式
    title = ""
    tags = []
    for line in reply.strip().split("\n"):
        line = line.strip()
        if line.startswith("标题：") or line.startswith("标题:"):
            title = line.split("：", 1)[-1].split(":", 1)[-1].strip()
        elif line.startswith("标签：") or line.startswith("标签:"):
            tag_str = line.split("：", 1)[-1].split(":", 1)[-1].strip()
            tags = [t.strip() for t in tag_str.replace("，", ",").split(",") if t.strip()]

    if not title:
        title = note_content[:20]  # 兜底：取内容前20字
    return title, tags


def summarize_notes(notes_text: str) -> str:
    """让 AI 总结今天的笔记"""
    reply = _chat(
        system_prompt="你是一个学习助手，擅长提炼和总结知识要点。",
        user_content=f"请总结以下笔记的核心内容，分点列出关键知识点（控制在200字以内）：\n\n{notes_text}",
        temperature=0.5,
    )
    return reply
