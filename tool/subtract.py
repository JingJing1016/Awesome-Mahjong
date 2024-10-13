import re
from datetime import datetime

# HACK: 荒莳队员名单
our_players = [
    "静静静静静啊",
    "古户絵梨花7mi",
    "盐与糖的最佳比例",
    "朔月灰",
    "缺幺少玖",
    "韩厅好",
    "初妆",
    "甲鱼半圈",
    "Piki_p",
    "jp孙笑川258",
    "刚刚123",
    "此丶间",
    "谜拟Q侠",
    "(~v~)",
    "你牌打的太好喇",
    "千反田える",
]


def subtract(player_scores: str) -> None:
    """
    计算并打印其他人和荒莳的点差

    Args:
        player_scores (str): 包含四家分数的指定格式的字符串，建议直接从联赛群复制机器人消息
    """

    # 提取四家名字和分数
    pattern = re.compile(r"([^\n\r ,]+) (\d+)")
    match = pattern.findall(player_scores)

    # 检测队员 index
    index = -1
    for i in range(4):
        if match[i][0] in our_players:
            index = i
            break

    # 计算点差并打印
    print("\n")
    fmt_str = "{0:<10}{1}"
    for i in range(4):
        if i == index:
            continue
        diff = int(match[index][1]) - int(match[i][1])
        if diff <= 0:
            sign = "+"
            diff = -diff
            color_code = "\033[0;31m"  # 红色
        else:
            sign = "-"
            color_code = "\033[0;32m"  # 绿色
        print(
            fmt_str.format(match[i][0], f"{color_code}{sign}{diff}\033[0m")
        )
    print("\n")


if __name__ == "__main__":
    print(
        """
===============================================================

    示例输入：
    谜拟Q侠 123500,悦颖嘉熙 105000,济士白 113800,破败军团 57700
    
    提示：
    - 建议直接复制机器人消息
    - 必须包含荒莳队员的雀魂名称

===============================================================

"""
    )
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        # user_input = console.input(f"[{current_time}] :glowing_star: 请输入：")
        user_input = input(f"[{current_time}] 请输入：")
        try:
            subtract(user_input)
        except Exception as e:
            # console.print(f":hankey: 输入格式错误\n")
            print(f"输入格式错误\n")
