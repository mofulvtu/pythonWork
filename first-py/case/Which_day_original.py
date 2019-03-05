"""
   desc: 判断一年之中第几天—— 内置函数实现
   author； Liuzg
   date: 2019/03/05

"""

import datetime


def function(year, month, day):  # 直接使用Python内置模块datetime的格式转换功能得到结果
    date = datetime.date(year, month, day)
    return date.strftime('%j')


def main():
    input_date_str = input("请输入日期(yyyy/MM/dd):")
    input_date = datetime.datetime.strptime(input_date_str, "%Y/%m/%d")

    year = input_date.year
    month = input_date.month
    day = input_date.day

    days = function(year, month, day)
    print("{}年中第{}天".format(year, days))


if __name__ == '__main__':
    main()
