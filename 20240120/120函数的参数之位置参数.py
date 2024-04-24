# 需求 函数3个参数name age gender
def user_info(name, age, gender):
    print(f'您的姓名是{name}, 年龄是{age}, 性别是{gender}')

user_info('Tom', 20, '男')

# 个数定义和传入不一致会报错
# 顺序也和定义必须是一致的 否则无意义