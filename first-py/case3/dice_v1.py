"""
   desc: 掷骰子概率
   author: Liuzg
   date: 2019/3/8
"""

import random


def roll_dice():
    """
        模拟掷骰子
    """
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 100000

    # 初始化列表
    result_list = [0] * 6

    for i in range(total_times):
        roll = roll_dice()
        for j in range(1, 7):
            if roll == j:
                result_list[j - 1] += 1

    for i, result in enumerate(result_list):
        print("点数{}出现次数：{}，频率为：{}".format(i + 1, result, result / total_times))


if __name__ == '__main__':
    main()
