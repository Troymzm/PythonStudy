mystr = "hello world and itcast and itheima and Python"

# 1. startswith()
print(mystr.startswith('hello'))
print(mystr.startswith('hel'))
print(mystr.startswith('hels'))

# 2. endswith()
print(mystr.endswith('Python'))
print(mystr.endswith('thon'))
print(mystr.endswith('Pythons'))

# 3. isalpha() 都是字母
print(mystr.isalpha())

# 4. isdigit() 都是数字
mystr1 = "111111"
print(mystr1.isdigit())

# 5. isalnum() 都是数字,字母,或组合
mystr1 = "shk1111"
print(mystr1.isalnum())
print(mystr.isalnum())

# 6. isspace() 都是空格
mystr1 = "      "
print(mystr1.isspace())
print(mystr.isspace())