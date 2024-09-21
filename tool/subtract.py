import re
from rich.traceback import install

install(extra_lines=2)

from rich.console import Console
from rich.table import Table
from rich.box import SIMPLE

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


def substract(player_scores: str) -> None:
    """
    计算并打印其他人和荒莳的点差

    Args:
        player_scores (str): 包含四家分数的指定格式的字符串，建议直接从联赛群复制机器人消息

    Raises:
        ValueError: 输入玩家数量不为4
        ValueError: 输入不包含荒莳队员雀魂id
    """

    console = Console()

    # 提取四家名字和分数
    pattern = re.compile(r"([^\n\r ,]+) (\d+)")
    match = pattern.findall(player_scores)
    if len(match) != 4:
        raise ValueError("输入玩家数量不为4")

    # 检测队员 index
    index = -1
    for i in range(4):
        if match[i][0] in our_players:
            index = i
            break
    if index == -1:
        raise ValueError("输入不包含荒莳队员雀魂id")

    # 设置表格
    table = Table(
        title=f"\n{match[index][0]}", title_style="bold", box=SIMPLE, show_header=False
    )

    # 计算点差并打印
    for i in range(4):
        if i == index:
            continue
        diff = int(match[index][1]) - int(match[i][1])
        if diff <= 0:
            sign = "[indian_red1]+"
            diff = -diff
        else:
            sign = "[green]-"
        table.add_row(match[i][0], f"{sign}{str(diff)}")
    console.print(table)


if __name__ == "__main__":
    user_input = input(
        """
包含如“谜拟Q侠 123500,悦颖嘉熙 105000,济士白 113800,破败军团 57700”的字符串
以英文逗号分隔玩家，以空格分隔每个玩家的昵称和分数

请输入四家分数: """
    )
    substract(user_input)
