# 类属性只能通过类对象修改 不能通过实例对象修改 通过实例对象修改实际上添加了一个实例属性
class Dog(object):
    tooth = 10

wangcai = Dog()
xiaohei = Dog()

# 1. 通过类对象修改  类.类属性 = 值
Dog.tooth = 20

print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)

# 2. 通过实例对象修改
wangcai.tooth = 30

print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)