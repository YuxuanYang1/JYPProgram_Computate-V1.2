# admin.py(V1.2-0918)
import hashlib
import config
from data import load_data, load_history, save_data, save_history
from utils import wpa, getkey

def show_users():
    if len(config.NameList) == 0:
        print("暂无用户。")
        return
    print("\n=== 用户列表 ===")
    for i, (name, score) in enumerate(zip(config.NameList, config.ScoreList)):
        print(f"{i}. {name}：{score}分")

def delete_user():
    show_users()
    if len(config.NameList) == 0:
        return
    idx = input("输入要删除的用户序号：")
    if not idx.isdigit():
        print("无效输入。")
        return
    idx = int(idx)
    if 0 <= idx < len(config.NameList):
        name = config.NameList[idx]
        config.NameList.pop(idx)
        config.KeyList.pop(idx)
        config.ScoreList.pop(idx)
        save_data()
        print(f"已删除用户：{name}")
    else:
        print("序号超出范围。")

def modify_score():
    show_users()
    if len(config.NameList) == 0:
        return
    idx = input("输入要修改的用户序号：")
    if not idx.isdigit():
        print("无效输入。")
        return
    idx = int(idx)
    if 0 <= idx < len(config.NameList):
        new_score = input("输入新分数：")
        try:
            config.ScoreList[idx] = int(new_score)
            save_data()
            print(f"已修改 {config.NameList[idx]} 的分数为 {new_score}")
        except ValueError:
            print("分数必须是整数。")
    else:
        print("序号超出范围。")

def reset_password():
    show_users()
    if len(config.NameList) == 0:
        return
    idx = input("输入要重置的用户序号：")
    if not idx.isdigit():
        print("无效输入。")
        return
    idx = int(idx)
    if 0 <= idx < len(config.NameList):
        newkey = getkey("输入新密码（4-10字符）：")
        if not (4 <= len(newkey) <= 10):
            print("密码长度不和。")
            return
        config.KeyList[idx] = hashlib.sha256(newkey.encode()).hexdigest()
        save_data()
        print(f"已重置 {config.NameList[idx]} 的密码")
    else:
        print("序号超出范围。")

def clear_all():
    confirm = input("确定清空所有用户数据？输入 YES 确认：")
    if confirm == "YES":
        config.NameList.clear()
        config.KeyList.clear()
        config.ScoreList.clear()
        save_data()
        print("已清空所有数据。")
    else:
        print("已取消。")

def clear_user_history():
    if not config.HistoryList:
        print("暂无历史记录。")
        return
    print("\n=== 有历史的用户 ===")
    for i, u in enumerate(config.HistoryList.keys(), 1):
        print(f"{i}. {u}")
    target = input("输入要清空的用户名：")
    if target in config.HistoryList:
        confirm = input(f"确定清空 {target} 的所有历史？输入 YES 确认：")
        if confirm == "YES":
            del config.HistoryList[target]
            save_history()
            print(f"已清空 {target} 的历史记录。")
        else:
            print("已取消。")
    else:
        print("用户不存在。")

def clear_user_wrong():
    if not config.WrongList:
        print("暂无错题记录。")
        return
    print("\n=== 有历史的用户 ===")
    for i, u in enumerate(config.WrongList.keys(), 1):
        print(f"{i}. {u}")
    target = input("输入要清空的用户名：")
    if target in config.WrongList:
        confirm = input(f"确定清空 {target} 的所有历史？输入 YES 确认：")
        if confirm == "YES":
            del config.WrongList[target]
            save_history()
            print(f"已清空 {target} 的历史记录。")
        else:
            print("已取消。")
    else:
        print("用户不存在。")

def admin_menu():
    load_data()
    load_history()
    
    def admin_history():
        from history import show_history
        user = input("输入用户名（回车显示所有）：")
        show_history(user if user else None)
    
    def admin_wrong():
        from history import show_wrong
        user = input("输入用户名（回车显示所有）：")
        show_wrong(user if user else None)
    
    admin_modes = {
        "1": show_users,
        "2": delete_user,
        "3": modify_score,
        "4": reset_password,
        "5": clear_all,
        "6": admin_history,
        "7": clear_user_history,
        "8": admin_wrong,
        "9": clear_user_wrong
    }
    
    while True:
        print("\n---数据管理---")
        print("1. 查看所有用户")
        print("2. 删除用户")
        print("3. 修改用户分数")
        print("4. 重置用户密码")
        print("5. 清空所有数据")
        print("6. 查看历史记录")
        print("7. 清空指定用户历史")
        print("8. 查看错题本")
        print("9. 清空指定用户错题")
        print("10. 返回")
        mode = input("请选择：")
        if mode == "10":
            print("退出界面。")
            return
        if mode in admin_modes:
            admin_modes[mode]()
        else:
            print("命令无效。")

if __name__ == "__main__":
    print("=== admin.py 测试 ===")
    admin_menu()
