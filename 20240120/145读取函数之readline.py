f = open('test.txt', 'r')

con = f.readline()  # 写一次读一行
print(con)

con = f.readline()  
print(con)

con = f.readline()  
print(con)

f.close()