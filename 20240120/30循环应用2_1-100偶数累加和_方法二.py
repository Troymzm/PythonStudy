# 计数器控制 让偶数累加
"""
1. 准备要累加的数字 
2. 准备保存结果的变量result
3. 循环计算
4. 输出结果
"""
i = 0
result = 0
while i <= 100:
    result += i
    i += 2
print(result)