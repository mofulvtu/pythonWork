"""
   desc: 判断一年之中第几天—— dictionary
   author； Liuzg
   date: 2019/03/05

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

    days_month_dic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    days = 0
    days += day
    for i in range(1, month):
        days += days_month_dic[i]

    if is_leap_year(year):
        if month > 2:
            days += 1

    print("这是{}年第{}天".format(year, days))


if __name__ == '__main__':
    main()
