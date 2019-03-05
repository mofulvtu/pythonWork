"""
   desc: 密码强弱判断
   author: Liuzg
   date: 2019/03/05
   version: v2
"""


def check_number_exit(password_str):
    """
    判断是否存在数字

    """
    result = False
    for c in password_str:
        if c.isnumeric():
            result = True
            break
    return result


def check_letter_exit(password_str):
    """
     判断是否存在字母

    """
    result = False
    for c in password_str:
        if c.isalpha():
            result = True
            break
    return result


def main():
    input_times = 5
    while input_times > 0:
        password = input("输入密码：")

        pwd_strength = 0

        if len(password) >= 8:
            pwd_strength += 1
        else:
            print("密码至少8位")

        if check_number_exit(password):
            pwd_strength += 1
        else:
            print("密码需要包含数字")

        if check_letter_exit(password):
            print("密码符合要求！")
        else:
            print("密码需要包含字母")

        input_times -= 1

    print("输入次数已经达到5次,不能再次输入！")


if __name__ == '__main__':
    main()
