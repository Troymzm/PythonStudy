# 需求 函数3个参数name age gender
def user_info(name, age, gender='男'):
    print(f'您的姓名是{name}, 年龄是{age}, 性别是{gender}')

user_info('Tom', 20)
user_info('Tom', 20, '女')

# 函数调用时 如果为缺省参数传值则修改默认参数值 否则使用这个默认值
# 所有的位置参数必须出现在默认参数前 包括函数定义和调用