# 1. 包裹位置传递
# 接收所有位置参数, 返回一个元组
def user_info1(*args):
    print(args)

user_info1('Tom')
user_info1('Tom', 20)
user_info1('Tom', 20, 'man')
user_info1()

# 2. 包裹关键字传递
# 接收所有关键字参数, 返回一个字典
def user_info2(**kwargs):
    print(kwargs)

user_info2(name = 'Tom')
user_info2(name = 'Tom', age = 20)
user_info2(name = 'Tom', age = 20, gender = 'man')
user_info2()

# 无论是包裹位置传递还是包裹关键字传递都是一个组包的过程