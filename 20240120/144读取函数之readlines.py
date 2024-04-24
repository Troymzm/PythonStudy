f = open('test.txt', 'r')

con = f.readlines()  # 每一行数据为列表一个元素
print(con)

f.close()