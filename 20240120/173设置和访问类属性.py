# 1. 定义类 定义类属性
class Dog(object):
    tooth = 10

# 2. 创建对象
wangcai = Dog()
xiaohei = Dog()

# 3. 访问类属性  类和对象
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)

# 类属性的优点 记录的某项数据始终保持一致时 则定义类属性 类属性比实例属性更加节省内存空间