#config(V1.2-0918)
NameList = []
KeyList = []
ScoreList = []

DATA_FILE = "user_data.json"
HISTORY_FILE = "user_history.json"

ADMIN_KEY_HASH = '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9'
#即admin123

Specificians = ["结束", "返回", "退出登录"]
BasicSeries = {"1.1": "+", "1.2": "-", "1.3": "*", "1.4": "/"}
Difficulty = {
    "1": {"name": "5以内的", "start": 1, "end": 5},
    "2": {"name": "10以内的运算", "start": 1, "end": 10},
    "3": {"name": "20以内的运算", "start": 0, "end": 20},
    "4": {"name": "100以内的运算", "start": 0, "end": 100},
    "5": {"name": "10000以内的运算", "start": 0, "end": 10000},
    "6": {"name": "极限模式", "start": -100000000, "end": 100000000}
}

CurrentUser = ""

HistoryList = {}
WrongList = {}
Achievements = {}

if __name__ == "__main__":
    print("=== config.py 测试 ===")
    print(f"用户数：{len(NameList)}")
    print(f"用户名：{NameList}")
    print(f"分数：{ScoreList}")
    print(f"数据文件：{DATA_FILE}")
    print(f"难度档位：{list(Difficulty.keys())}")
