"""
   desc: 掷骰子 两个骰子
          直方图可视化
   author: Liuzg
   date: 2019/3/10
"""

import random
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


def roll_dice():
    """
        模拟掷骰子
    """
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 10000

    # 初始化点数列表
    roll_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll_list.append(roll1 + roll2)

    # 数据可视化
    # bins 边界  density 概率
    plt.title("骰子点数统计")
    plt.ylabel("频率")
    plt.xlabel("点数")
    plt.hist(roll_list, bins=range(2, 14), density=1, edgecolor='black', linewidth=1)
    plt.show()


if __name__ == '__main__':
    main()
