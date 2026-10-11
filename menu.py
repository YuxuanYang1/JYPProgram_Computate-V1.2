# menu.py(V1.2-0918)
import config
from utils import judgeOut
from zbo import BasicOperation
from data import save_history

def show_rank():
    if len(config.NameList) == 0:
        print("暂无用户数据。")
        return
    rank = sorted(zip(config.NameList, config.ScoreList), key=lambda x: x[1], reverse=True)
    print("\n=== 排行榜 ===")
    for i, (name, score) in enumerate(rank[:10], 1):
        print(f"{i}. {name}：{score}分")
    print()

def main():
    SingleScore = 0
    while True:
        print("\n---练习菜单---")
        print("1.1 整数加法")
        print("1.2 整数减法")
        print("1.3 整数乘法")
        print("1.4 整数除法")
        print("2.  排行榜")
        print("3.  历史记录")
        print("4.  错题本\n")
        mode = input("请选择模式：（填入序号）")
        if mode in config.Specificians:
            result = judgeOut(mode, SingleScore, 1)
            if result[0] is None:
                continue
            return result
        elif mode in config.BasicSeries:
            result = BasicOperation(config.BasicSeries[mode])
            order = result[0]
            PartScore = result[1]
            correct_count = result[2]
            wrong_count = result[3]
            total_time = result[4]
            SingleScore += PartScore
            print(f"\n本次练习：正确{correct_count}题，错误{wrong_count}题，总用时{total_time:.2f}秒")

            if config.CurrentUser and (correct_count + wrong_count > 0):
                if config.CurrentUser not in config.HistoryList:
                    config.HistoryList[config.CurrentUser] = []
                config.HistoryList[config.CurrentUser].append({
                    "mode": config.BasicSeries[mode],
                    "correct": correct_count,
                    "wrong": wrong_count,
                    "time": round(total_time, 2),
                    "score": PartScore
                })
                save_history()

            if order in config.Specificians:
                if order == "返回":
                    continue
                return [order, SingleScore]
        elif mode == "2":
            show_rank()
        elif mode == "3":
            from history import show_history
            show_history(user=config.CurrentUser)
        elif mode == "4":
            from history import show_wrong
            show_wrong(user=config.CurrentUser)
        else:
            print("命令无效，请重新输入")

if __name__ == "__main__":
    print("=== menu.py 测试 ===")
    print("1. 测试 show_rank")
    show_rank()
    print("2. 测试 main")
    print(f"   返回：{main()}")
    print("测试结束。")
