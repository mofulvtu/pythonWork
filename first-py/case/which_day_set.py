"""
   desc: 判断一年之中第几天——set
   author； Liuzg
   date: 2019/03/04

"""

from datetime import datetime


def is_leap_year(year):
    is_leap = False

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True

    return is_leap


def main():
    input_date_str = input("请输入日期(yyyy/MM/dd):")
    input_date = datetime.strptime(input_date_str, "%Y/%m/%d")

    year = input_date.year
    month = input_date.month
    day = input_date.day

    _30_days_month_set = {4, 6, 9, 11}
    _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}

    days = 0

    for i in range(1, month):
        if i in _30_days_month_set:
            days += 30
        elif i in _31_days_month_set:
            days += 31
        else:
            days += 28

    if is_leap_year(year):
        days += 1

    days += day
    print("这是{}年第{}天".format(year, days))


if __name__ == '__main__':
    main()
