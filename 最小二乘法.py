import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 原始数据
T_squared = np.array([25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45])  # 周期的平方 (s^2)
l = np.array([2.33, 5.28, 8.33, 11.02, 13.98, 16.93, 19.25, 22.10, 25.26, 27.92, 30.28])  # 单摆的摆长 l (m)

slope, intercept, r_value, p_value, std_err = stats.linregress(T_squared, l)  # 相关系数

fit_line = slope * T_squared + intercept

# 计算重力加速度和相关系数 r
g = slope * 4 * np.pi**2  # 重力加速度

# 绘制图像
plt.title('Statistical Chart')
plt.xlabel('$T^2$ (s$^2$)')
plt.ylabel('$l(m)$')
plt.scatter(T_squared, l, color='blue', label='Original data')
plt.plot(T_squared, fit_line, color='red', label='Fitted line through origin')

plt.legend()
plt.show()

print("所预估的重力加速度 g 为:", g, "相关系数 r 为:", r_value)

