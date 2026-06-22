# ===== ai_notes/note_store.py — 笔记存取模块 =====
"""负责笔记的增删查：JSON 文件读写"""

import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "notes.json")


def _load() -> list[dict]:
    """从 JSON 文件加载所有笔记"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def _save(notes: list[dict]):
    """保存所有笔记到 JSON 文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)


def _next_id(notes: list[dict]) -> int:
    """生成下一个可用的笔记 ID"""
    if not notes:
        return 1
    return max(n["id"] for n in notes) + 1


def add_note(content: str, title: str, tags: list[str]) -> dict:
    """添加一条笔记，返回完整的笔记对象"""
    notes = _load()
    note = {
        "id": _next_id(notes),
        "content": content,
        "title": title,
        "tags": tags,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    notes.insert(0, note)  # 新笔记放最前面
    _save(notes)
    return note


def get_all() -> list[dict]:
    """获取所有笔记（按时间倒序）"""
    return _load()


def get_today() -> list[dict]:
    """获取今天的笔记"""
    today = datetime.now().strftime("%Y-%m-%d")
    return [n for n in _load() if n["created_at"].startswith(today)]


def get_by_tag(tag: str) -> list[dict]:
    """按标签搜索笔记"""
    tag_lower = tag.strip().lower()
    return [n for n in _load() if any(tag_lower in t.lower() for t in n.get("tags", []))]


def get_by_date(date_str: str) -> list[dict]:
    """按日期搜索笔记（格式：2026-06-11）"""
    return [n for n in _load() if n["created_at"].startswith(date_str)]


def delete_note(note_id: int) -> bool:
    """删除一条笔记"""
    notes = _load()
    before = len(notes)
    notes = [n for n in notes if n["id"] != note_id]
    if len(notes) == before:
        raise ValueError(f"没有找到 ID={note_id} 的笔记")
    _save(notes)
    return True

def update_note(note_id: int, new_content: str) -> dict:
    """修改一条笔记的内容，返回修改后的笔记"""
    notes = _load()
    for note in notes:
        if note["id"] == note_id:
            note["content"] = new_content
            _save(notes)
            return note
    raise ValueError(f"没有找到 ID={note_id} 的笔记")

def count() -> int:
    """笔记总数"""
    return len(_load())
