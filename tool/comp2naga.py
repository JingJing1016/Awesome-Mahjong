# 功能：将联赛谱转为平场谱跑naga，南场 -> 东场，四家分数 -> 25000
# 输入：input.txt, json格式的联赛牌谱
# 输出：output.txt, json格式的平场牌谱
# 时间：2023.12.21

import re
import json
from datetime import datetime


def transform(input_text):
    # 从文本中提取 JSON 部分
    output_text = ""
    matches = re.findall(r'#json=(\{.*\})', input_text)
    if matches:
        for match in matches:
            data = json.loads(match)

            # 修改 log 部分
            log = data.get('log', [])
            if log[0][0][0] >= 4:
                log[0][0][0] -= 4
            log[0][1] = [25000, 25000, 25000, 25000]

            # 更新修改后的 log 到原始数据中
            data['log'] = log
            modified_json = json.dumps(
                data, ensure_ascii=False, separators=(',', ':'))
            output_text += 'https://tenhou.net/6/#json=' + modified_json+'\n'
    else:
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(f'[-] {formatted_time}：input.txt中不是合法的json格式牌谱，请使用现有插件转换。')
        return

    with open('./output.txt', 'w', encoding='utf-8') as file:
        file.write(output_text)

    # 转换成功
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[+] {formatted_time}：转换成功！")

    return


if __name__ == '__main__':
    input("功能：将联赛谱转为平场谱跑naga，南场 -> 东场，四家分数 -> 25000.\n\
      程序将自动读取当前目录下的 input.txt，将转化后的牌谱保存至 output.txt.\n\
      请准备好input.txt后，按 回车键 开始转换。\n")

    while (1):
        # 读input进行转换
        try:
            with open('./input.txt', 'r', encoding='utf-8') as file:
                input_text = file.read()
            transform(input_text)
        except:
            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"[-] {formatted_time}：文件不存在！")

        # 用户选择继续转换 或者 退出
        input("    修改input.txt并保存后，按 回车键 继续转换。或者按 Ctrl+C 退出…\n")
