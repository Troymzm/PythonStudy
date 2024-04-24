# 需求 函数3个参数name age gender
def user_info(name, age, gender):
    print(f'您的姓名是{name}, 年龄是{age}, 性别是{gender}')

# 位置参数不能出现在关键字参数之后
user_info('Tom', age = 20, gender = '男')
user_info('Tom', gender = '男', age = 20)  # 关键字参数之间不分先后顺序