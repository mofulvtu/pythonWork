"""
   desc: 掷骰子 两个骰子  可视化
   author: Liuzg
   date: 2019/3/8
"""

import random
import matplotlib.pyplot as plt


def roll_dice():
    """
        模拟掷骰子
    """
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 100

    # 初始化列表
    result_list = [0] * 11

    # 初始化点数列表
    roll_list = list(range(2, 13))

    roll1_list = []
    roll2_list = []

    # zip()函数用于将对应的元素打包成一个元组
    roll_dict = dict(zip(roll_list, result_list))

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll = roll1 + roll2

        roll1_list.append(roll1)
        roll2_list.append(roll2)

        for j in roll_list:
            if roll == j:
                roll_dict[j] += 1

    # 遍历字典
    for i, result in roll_dict.items():
        print("点数{}出现次数：{}，频率为：{}".format(i, result, result / total_times))

    # 数据可视化
    x = range(1, total_times + 1)
    plt.scatter(x, roll1_list, c="red", alpha=0.5)
    plt.scatter(x, roll2_list, c="blue", alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()
