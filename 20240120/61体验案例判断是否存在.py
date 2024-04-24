name_list = ['Tom', 'Lily', 'Rose']

# 需求：注册邮箱，用户输入一个账号名，判断这个账户名是否存在，如果存在，提示用户，否则提示可以注册

name = input('请输入您的账户名:')

if name in name_list:
    print(f'您输入的名字是{name},此用户已经存在')
else:
    print(f'您输入的名字是{name},可以注册')