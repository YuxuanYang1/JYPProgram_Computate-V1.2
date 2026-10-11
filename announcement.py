from utils import wpa, wp

def show_announcement():
    wpa("欢迎使用计算练习程序\n")
    print("上次更新：2026-09-19")
    print("当前版本：V1.2-0918")
    print("描述：做成了分模块模式，完善了记录功能\n")
    wpa("公告：")
    print("欢迎回来，亲爱的朋友。")
    print("经过更新，我们现在已经支持：")
    print("--基本的整数四则运算训练。")
    print("--计时统计等功能。")
    print("--以及较为完善的登录系统。\n")
    print("其他功能有待后续补充。")
    wpa("使用过程中，可以随时在提示框中输入'返回/退出登录'以达到相应效果\n")
    wp("正在加载模块，请稍候……", 3)
    wpa("加载完毕！\n")

if __name__ == "__main__":
    print("=== announcement.py 测试 ===")
    show_announcement()
