from math import sqrt
pi = 3.1416
i = 1
list_l = [71.732, 71.620, 71.851, 71.832, 71.882, 71.900]
list_T = [42.58, 42.57, 42.54, 42.65, 42.51, 42.58]
# while i <= 6 :
#     list_l.append(float(input(f'输入第{i}个数据--摆长(单位cm)')))
#     i += 1
# i = 1
# while i <= 6 :
#     list_T.append(float(input(f'输入第{i}个数据--周期(25个周期)')))
#     i += 1
i = 0
while i < 6 :
    list_l[i] /= 100.0
    i += 1
i = 0
while i < 6 :
    list_T[i] /= 25.0
    i += 1
sum_l = 0.0
for i in list_l:
    sum_l += i
average_l = sum_l / 6.0
sum_T = 0.0
for i in list_T:
    sum_T += i
average_T = sum_T / 6.0
l_square = 0.0
for i in list_l:
    l_square += ((i - average_l) ** 2)
u_l = sqrt(l_square / 30.0 + (0.2 / 300) ** 2) 
T_square = 0.0
for i in list_T:
    T_square += ((i - average_T) ** 2)
u_T = sqrt(T_square / 30.0 + (0.2 / 3) ** 2 + (0.01 / 3) ** 2) / 25
g = 4 * pi * pi * average_l / (average_T ** 2)
u_g = g * sqrt((u_l / average_l) ** 2 + 4 * ((u_T / average_T) ** 2))
print(g)
print(u_l)
print(u_T)
print(u_g / g)