"""
   desc: 密码强弱判断
   author: Liuzg
   date: 2019/03/05
   version: v1

"""


def check_number_exit(password_str):
    """
    判断是否存在数字

    """
    for c in password_str:
        if c.isnumeric():
            return True
    return False


def check_letter_exit(password_str):
    """
     判断是否存在字母

    """
    for c in password_str:
        if c.isalpha():
            return True
    return False


def main():
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


if __name__ == '__main__':
    main()
