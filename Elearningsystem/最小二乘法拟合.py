import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 原始数据
x = np.array([25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45])
y = np.array([2.33, 5.28, 8.33, 11.02, 13.98, 16.93, 19.25, 22.10, 25.26, 27.92, 30.28])
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)  # 相关系数

print(f'斜率为', slope)
print(f'截距为', intercept)
print(f'相关系数为', r_value)
print(f'不确定度为', p_value)
