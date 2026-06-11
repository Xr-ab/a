# # ===== Day 1：变量、输入输出 =====

# # 1. 变量和数据类型
# name = "你的名字"
# age = 22
# height = 1.75
# is_student = True

# print(f"我叫{name}，今年{age}岁，身高{height}米")
# print(f"学生身份：{is_student}")

# # 2. input 输入
# user_name = input("你叫什么名字？")
# print(f"你好，{user_name}！欢迎开始AI学习之旅")

# # 3. 简单计算器
# a = float(input("输入第一个数字："))
# b = float(input("输入第二个数字："))
# print(f"相加={a+b}，相乘={a*b}，平均值={(a+b)/2}")

# ===== Day 2：猜数字游戏 =====
# import random

# target = random.randint(1, 100)
# guess_count = 0

# print("我想了一个1-100之间的数字，你猜是多少？")

# while True:
#     guess = int(input("你的猜测："))
#     guess_count += 1

#     if guess < target:
#         print("太小了，再大一点")
#     elif guess > target:
#         print("太大了，再小一点")
#     else:
#         print(f"猜对了！你一共猜了{guess_count}次")
#         break

#     if guess_count >= 10:
#         print(f"已经猜了10次了，答案是{target}，Game Over")
#         break

# ===== Day 3：学生成绩管理系统 =====

# students = []  # 每个元素 {"name": str, "score": float}

# def add_student(name, score):
#     students.append({"name": name, "score": score})
#     print(f"已添加：{name}，成绩：{score}")

# def get_average():
#     if not students:
#         return 0
#     total = sum(s["score"] for s in students)
#     return total / len(students)

# def get_top_student():
#     if not students:
#         return None
#     return max(students, key=lambda s: s["score"])

# def show_all():
#     print("\n===== 成绩单 =====")
#     for i, s in enumerate(students, 1):
#         print(f"{i}. {s['name']}: {s['score']}分")
#     print(f"平均分：{get_average():.1f}")
#     top = get_top_student()
#     if top:
#         print(f"最高分：{top['name']}（{top['score']}分）")

# # 测试
# add_student("张三", 85)
# add_student("李四", 92)
# add_student("王五", 78)
# show_all()

# # ===== Day 4：成绩持久化 =====
# import json
# import os

# DATA_FILE = "students.json"

# def load_data():
#     if os.path.exists(DATA_FILE):
#         with open(DATA_FILE, "r", encoding="utf-8") as f:
#             return json.load(f)
#     return []

# def save_data(data):
#     with open(DATA_FILE, "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=2)

# # 改造 Day3 的系统：启动时 load_data()，每次增删后 save_data()
# students = load_data()

# def add_student(name, score):
#     students.append({"name": name, "score": score})
#     save_data(students)

# n1 = 255
# print(hex(n1))
# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x

# print(my_abs(-1))

# import math

# def quadratic(a, b, c):
#     # 计算判别式
#     discriminant = b**2 - 4*a*c
#     if discriminant < 0:
#         return None  # 无实数解
#     elif discriminant == 0:
#         x = -b / (2*a)
#         return (x,)  # 返回一个元组
#     else:
#         sqrt_discriminant = math.hypot(0, discriminant)  # 更安全的平方根计算
#         x1 = (-b + sqrt_discriminant) / (2*a)
#         x2 = (-b - sqrt_discriminant) / (2*a)
#         return (x1, x2)

# # 测试:
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')

# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s

# power(5, 2)  # 25
# power(5)     # 25，默认参数n=2

# # N! = 1 * 2 * 3 * ... * N
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)

# print('fact(1) =', fact(1))
# print('fact(5) =', fact(5))
# print('fact(10) =', fact(10))

# # 鍒╃敤閫掑綊鍑芥暟绉诲姩姹夎濉�:
# def move(n, a, b, c):
#     if n == 1:
#         print('move', a, '-->', c)
#     else:
#         move(n-1, a, c, b)
#         move(1, a, b, c)
#         move(n-1, b, a, c)

# move(4, 'A', 'B', 'C')

# ===== Day 5：用类管理成绩 =====
# import json

# class StudentManager:
#     def __init__(self, data_file="students.json"):
#         self.data_file = data_file
#         self.students = self._load()

#     def _load(self):
#         try:
#             with open(self.data_file, "r", encoding="utf-8") as f:
#                 return json.load(f)
#         except (FileNotFoundError, json.JSONDecodeError):
#             return []

#     def _save(self):
#         with open(self.data_file, "w", encoding="utf-8") as f:
#             json.dump(self.students, f, ensure_ascii=False, indent=2)

#     def add(self, name, score):
#         if not isinstance(score, (int, float)) or score < 0 or score > 100:
#             raise ValueError("成绩必须在0-100之间")
#         self.students.append({"name": name, "score": score})
#         self._save()

#     def average(self):
#         if not self.students:
#             return 0
#         return sum(s["score"] for s in self.students) / len(self.students)

#     def remove(self, name):
#         before = len(self.students)
#         self.students = [s for s in self.students if s["name"] != name]
#         if len(self.students) == before:
#             raise ValueError(f"没有找到学生：{name}")
#         self._save()

# # 测试
# manager = StudentManager()
# try:
#     manager.add("张三", 85)
#     manager.add("李四", 92)
#     print(f"平均分：{manager.average():.1f}")
#     manager.remove("张三")
#     manager.add("王五", 90)  # 会报错
# except ValueError as e:
#     print(f"出错了：{e}")


# ===== Day 6 已拆分为独立文件 =====
# 运行方式：python main.py
# 文件结构：
#   student_manager.py → 类定义（工具）
#   main.py            → 交互菜单（只用不造）


import json

class GradeManager:
    def __init__(self, file="grades.json"):
        self.file = file
        self.data = self._load()
    
    def _load(self):
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    
    def _save(self):
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
    
    def add_student(self, name):
        """添加学生"""
        sid = str(len(self.data) + 1)
        self.data[sid] = {"name": name, "scores": {}}
        self._save()
        return sid
    
    def add_score(self, sid, subject, score):
        """添加成绩"""
        if sid not in self.data:
            raise ValueError("学生不存在")
        self.data[sid]["scores"][subject] = score
        self._save()
    
    def get_avg(self, sid):
        """获取学生平均分"""
        scores = self.data[sid]["scores"].values()
        return sum(scores) / len(scores) if scores else 0
    
    def get_all(self):
        """获取所有学生"""
        return self.data
    
    def delete(self, sid):
        """删除学生"""
        if sid in self.data:
            del self.data[sid]
            self._save()


import json
from datetime import datetime
from typing import List, Dict, Optional

class TodoManager:
    """待办事项管理器"""
    
    def __init__(self, data_file="todos.json"):
        self.data_file = data_file
        self.todos = self._load()
        self._next_id = self._get_next_id()
    
    def _load(self) -> List[Dict]:
        """从文件加载数据"""
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _save(self):
        """保存数据到文件"""
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(self.todos, f, ensure_ascii=False, indent=2)
    
    def _get_next_id(self) -> int:
        """获取下一个可用的ID"""
        if not self.todos:
            return 1
        return max(todo["id"] for todo in self.todos) + 1
    
    def add(self, title: str, description: str = "") -> Dict:
        """
        添加待办事项
        :param title: 标题（必填）
        :param description: 描述（可选）
        :return: 添加的事项
        """
        if not title or not title.strip():
            raise ValueError("标题不能为空")
        
        todo = {
            "id": self._next_id,
            "title": title.strip(),
            "description": description.strip(),
            "status": "pending",  # pending, in_progress, completed
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.todos.append(todo)
        self._save()
        self._next_id += 1
        
        return todo
    
    def get_all(self) -> List[Dict]:
        """获取所有待办事项"""
        return self.todos.copy()
    
    def get_by_id(self, todo_id: int) -> Optional[Dict]:
        """根据ID获取事项"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                return todo.copy()
        return None
    
    def get_by_status(self, status: str) -> List[Dict]:
        """根据状态获取事项"""
        valid_statuses = ["pending", "in_progress", "completed"]
        if status not in valid_statuses:
            raise ValueError(f"状态必须是以下之一: {valid_statuses}")
        
        return [todo for todo in self.todos if todo["status"] == status]
    
    def update(self, todo_id: int, title: str = None, description: str = None, status: str = None) -> Dict:
        """
        更新待办事项
        :param todo_id: 事项ID
        :param title: 新标题（可选）
        :param description: 新描述（可选）
        :param status: 新状态（可选）
        :return: 更新后的事项
        """
        for todo in self.todos:
            if todo["id"] == todo_id:
                if title is not None and title.strip():
                    todo["title"] = title.strip()
                if description is not None:
                    todo["description"] = description.strip()
                if status is not None:
                    valid_statuses = ["pending", "in_progress", "completed"]
                    if status not in valid_statuses:
                        raise ValueError(f"状态必须是以下之一: {valid_statuses}")
                    todo["status"] = status
                
                todo["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self._save()
                return todo.copy()
        
        raise ValueError(f"未找到ID为 {todo_id} 的事项")
    
    def delete(self, todo_id: int) -> bool:
        """
        删除待办事项
        :param todo_id: 事项ID
        :return: 是否删除成功
        """
        before = len(self.todos)
        self.todos = [todo for todo in self.todos if todo["id"] != todo_id]
        
        if len(self.todos) == before:
            raise ValueError(f"未找到ID为 {todo_id} 的事项")
        
        self._save()
        return True
    
    def complete(self, todo_id: int) -> Dict:
        """标记事项为已完成（快捷方法）"""
        return self.update(todo_id, status="completed")
    
    def get_statistics(self) -> Dict:
        """获取统计信息"""
        total = len(self.todos)
        pending = len(self.get_by_status("pending"))
        in_progress = len(self.get_by_status("in_progress"))
        completed = len(self.get_by_status("completed"))
        
        return {
            "total": total,
            "pending": pending,
            "in_progress": in_progress,
            "completed": completed,
            "completion_rate": (completed / total * 100) if total > 0 else 0
        }
    
    def clear_all(self) -> bool:
        """清空所有事项（慎用）"""
        confirm = input("确认清空所有事项？(yes/no): ")
        if confirm.lower() == "yes":
            self.todos = []
            self._next_id = 1
            self._save()
            return True
        return False


# ===== Day 7-8 参考代码结束 =====
# GradeManager 和 TodoManager 为参考代码，非独立完成
# 能读懂逻辑，但关掉参考自己写还有困难

# ===== Day 7-8：自己独立写的猜数字（含 try/except 改进） =====
if __name__ == "__main__":
    import random
    secret = random.randint(1, 100)
    guess_count = 0
    print("猜数字游戏！数字在1-100之间")
    while True:
        try:
            guess = int(input("请输入你的猜测: "))
            guess_count += 1
            if guess < secret:
                print("太小了！")
            elif guess > secret:
                print("太大了！")
            else:
                print(f"恭喜！猜对了！数字就是{secret}")
                print(f"你总共猜了 {guess_count} 次")
                break
        except ValueError:
            print("请输入有效的数字！")
