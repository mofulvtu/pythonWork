"""
   desc: 密码强弱判断——面向对象封装
   author: Liuzg
   date: 2019/03/07
   version: v3
"""


class PasswordTool:
    """
        密码工具类
    """
    def __init__(self, password):
        # 类的属性
        self.password = password
        self.strength_level = 0

    def process_password(self):
        if len(self.password) >= 8:
            self.strength_level+= 1
        else:
            print("密码至少8位")

        if self.check_number_exit():
            self.strength_level += 1
        else:
            print("密码需要包含数字")

        if self.check_letter_exit():
            self.strength_level += 1
        else:
            print("密码需要包含字母")

    def check_number_exit(self):
        """
        判断是否存在数字
        """
        result = False
        for c in self.password:
            if c.isnumeric():
                result = True
                break
        return result

    def check_letter_exit(self):
        """
         判断是否存在字母
        """
        result = False
        for c in self.password:
            if c.isalpha():
                result = True
                break
        return result


def main():
    # 试错次数
    input_times = 5
    while input_times > 0:
        password = input("输入密码：")

        # 实例化密码工具
        password_tool = PasswordTool(password)
        password_tool.process_password()

        f = open("password_v5.txt", "a")
        f.write("password:{} strength:{}".format(password, password_tool.strength_level)+"\n")
        f.close()

        if password_tool.strength_level == 3:
            print("密码符合要求！")
            break
        else:
            input_times -= 1

    if input_times == 0:
        print("输入次数已经达到5次,不能再次输入！")


if __name__ == '__main__':
    main()
