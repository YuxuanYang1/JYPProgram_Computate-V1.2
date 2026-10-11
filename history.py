# history.py(V1.2-0918)
import config
from utils import wpa

def show_history(user=None, mode=None):
    if not config.HistoryList:
        print("暂无历史记录。")
        return
    if user:
        if user not in config.HistoryList:
            print(f"用户 {user} 没有历史记录。")
            return
        users = [user]
    else:
        users = list(config.HistoryList.keys())

    print("\n=== 历史记录 ===")
    total_correct = 0
    total_wrong = 0
    total_time = 0
    for u in users:
        records = config.HistoryList[u]
        if mode:
            records = [r for r in records if r["mode"] == mode]
        if not records:
            continue
        print(f"\n【{u}】")
        for i, r in enumerate(records, 1):
            print(f"  {i}. {r['mode']} | 正确{r['correct']}题，错误{r['wrong']}题 | 用时{r['time']:.2f}秒 | 得分{r['score']}")
            total_correct += r["correct"]
            total_wrong += r["wrong"]
            total_time += r["time"]
    print(f"\n总计：正确{total_correct}题，错误{total_wrong}题，总用时{total_time:.2f}秒")

def show_wrong(user=None):
    if not config.WrongList:
        print("错题本为空。")
        return
    if user:
        if user not in config.WrongList:
            print(f"用户 {user} 没有错题。")
            return
        users = [user]
    else:
        users = list(config.WrongList.keys())

    print("\n=== 错题本 ===")
    for u in users:
        records = config.WrongList[u]
        if not records:
            continue
        print(f"\n【{u}】")
        for i, r in enumerate(records, 1):
            print(f"  {i}. {r['question']} 正确答案：{r['correct']}，你的答案：{r['your']}")

if __name__ == "__main__":
    from data import load_history
    print("=== history.py 测试 ===")
    load_history()
    print("1. 显示所有历史")
    show_history()
    print("2. 显示指定用户历史")
    show_history(user=config.NameList[0] if config.NameList else None)
    print("3. 显示指定运算历史")
    show_history(mode="+")
    print("4. 显示错题本")
    show_wrong()
    print("测试结束。")
