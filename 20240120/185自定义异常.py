# 1. 自定义异常类  继承Exception 魔法方法为init和str 设置异常描述信息
class ShortInputError(Exception):
    def __init__(self, length, min_len) -> None:
        # 用户输入的密码长度
        self.length = length
        # 系统要求的最少长度
        self.min_len = min_len

    # 设置异常描述信息
    def __str__(self) -> str:
        return f'您输入的密码长度是{self.length}, 密码不能少于{self.min_len}'

def main():
    # 2. 抛出异常 尝试执行 用户输入密码 如果长度小于3 抛出异常
    try:
        con = input('请输入密码: ')
        if len(con) < 3:
            # 抛出异常类创建的对象
            raise ShortInputError(len(con), 3)
    # 3. 捕获该异常
    except Exception as result:
        print(result)
    else:
        print('密码输入完成')


main()