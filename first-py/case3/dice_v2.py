"""
   desc: 掷骰子概 两个骰子
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
    total_times = 10000

    # 初始化列表
    result_list = [0] * 11

    # 初始化点数列表
    roll_list = list(range(2, 13))

    # zip()函数用于将对应的元素打包成一个元组
    roll_dict = dict(zip(roll_list, result_list))

    for i in range(total_times):
        roll = roll_dice() + roll_dice()
        for j in roll_list:
            if roll == j:
                roll_dict[j] += 1

    # 遍历字典
    for i, result in roll_dict.items():
        print("点数{}出现次数：{}，频率为：{}".format(i, result, result / total_times))


if __name__ == '__main__':
    main()
