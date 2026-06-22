# ===== ai_notes/main.py — 主程序入口 =====
"""AI 笔记工具：命令行交互菜单"""

from ai_client import generate_title_and_tags, summarize_notes
from note_store import add_note, get_all, get_today, get_by_tag, get_by_date, delete_note, update_note, count


def cmd_write():
    """1. 写笔记 → AI 自动生成标题和标签"""
    content = input("\n请输入笔记内容：\n> ").strip()
    if not content:
        print("[SKIP] 内容为空，已取消")
        return

    print("\n[AI] 正在生成标题和标签...")
    try:
        title, tags = generate_title_and_tags(content)
        note = add_note(content, title, tags)
        print(f"\n[OK] 笔记已保存！")
        print(f"     ID={note['id']} | 标题: {title} | 标签: {', '.join(tags)}")
    except Exception as e:
        print(f"[ERROR] AI 调用失败: {e}")


def cmd_today():
    """2. 查看今日笔记"""
    notes = get_today()
    _print_notes(notes, "今日笔记")


def cmd_all():
    """3. 查看全部笔记"""
    notes = get_all()
    _print_notes(notes, f"全部笔记（共 {len(notes)} 条）")


def cmd_tag():
    """4. 按标签搜索"""
    tag = input("请输入标签关键词：").strip()
    if not tag:
        print("[SKIP] 输入为空")
        return
    notes = get_by_tag(tag)
    _print_notes(notes, f"标签「{tag}」的搜索结果")


def cmd_date():
    """5. 按日期搜索"""
    date_str = input("请输入日期（格式 2026-06-11）：").strip()
    if not date_str:
        print("[SKIP] 输入为空")
        return
    notes = get_by_date(date_str)
    _print_notes(notes, f"日期「{date_str}」的搜索结果")


def cmd_summarize():
    """6. AI 总结今日笔记"""
    notes = get_today()
    if not notes:
        print("今天还没有笔记")
        return

    # 拼成一段文本喂给 AI
    text = "\n\n---\n\n".join(
        f"《{n['title']}》\n{n['content']}" for n in notes
    )
    print("\n[AI] 正在总结今日笔记...")
    try:
        summary = summarize_notes(text)
        print(f"\n===== AI 总结 =====\n{summary}")
    except Exception as e:
        print(f"[ERROR] AI 调用失败: {e}")


def cmd_delete():
    """7. 删除笔记"""
    nid_str = input("请输入要删除的笔记 ID：").strip()
    try:
        nid = int(nid_str)
        delete_note(nid)
        print(f"[OK] 笔记 ID={nid} 已删除")
    except ValueError:
        print("[ERROR] ID 必须是数字")
    except Exception as e:
        print(f"[ERROR] {e}")

def cmd_update():
    """8. 修改笔记内容"""
    nid_str = input("请输入要修改的笔记 ID：").strip()
    try:
        nid = int(nid_str)
        new_content = input("请输入新内容：\n> ").strip()
        if not new_content:
            print("[SKIP] 内容为空，已取消")
            return
        note = update_note(nid, new_content)
        print(f"[OK] 笔记 ID={nid} 已更新 → 标题: {note['title']}")
    except ValueError as e:
        print(f"[ERROR] {e}")

def _print_notes(notes: list[dict], title: str):
    """格式化打印笔记列表"""
    print(f"\n===== {title} =====")
    if not notes:
        print("（暂无笔记）")
        return
    for n in notes:
        tags = ", ".join(n.get("tags", [])) if n.get("tags") else "无标签"
        print(f"  [{n['id']}] {n['title']}")
        print(f"      标签: {tags}  |  {n['created_at']}")
        print(f"      内容: {n['content'][:80]}{'...' if len(n['content']) > 80 else ''}")
        print()


def main():
    menu = """
+----------------------+
|   AI 笔记工具         |
+----------------------+
| 1. 写笔记            |
| 2. 查看今日          |
| 3. 查看全部          |
| 4. 按标签搜索        |
| 5. 按日期搜索        |
| 6. AI 总结今日       |
| 7. 删除笔记           |
| 8. 修改笔记           |
| 0. 退出              |
+----------------------+"""

    actions = {
        "1": cmd_write,
        "2": cmd_today,
        "3": cmd_all,
        "4": cmd_tag,
        "5": cmd_date,
        "6": cmd_summarize,
        "7": cmd_delete,
        "8": cmd_update,
    }

    print(f"\n当前共有 {count()} 条笔记")

    while True:
        print(menu)
        choice = input("请选择 (0-8): ").strip()

        if choice == "0":
            print("再见！")
            break
        elif choice in actions:
            try:
                actions[choice]()
            except Exception as e:
                print(f"[ERROR] {e}")
        else:
            print("无效选择，请重新输入")


if __name__ == "__main__":
    main()
