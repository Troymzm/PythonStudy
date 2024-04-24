"""
1. 导入模块os
2. 使用模块内功能
"""

import os

# 1. rename() : 重命名  (旧名字, 新名字)
os.rename('1.txt', '10.txt')

# 2. remove() : 删除文件
os.remove('1.txt')

# 3. mkdir(): 创建文件夹
os.mkdir('aa')

# 4. rmdir(): 删除文件夹
os.rmdir('aa')

# 5. getcwd(): 返回当前文件所在目录路径
print(os.getcwd())

# 6. chdir(): 改变目录路径
# 需求: 在20240120文件夹里创建bb文件夹
# (1)  切换目录到20240120
os.chdir(20240120)
# (2)  创建aa
os.mkdir('aa')

# 7. listdir(): 获取某个文件夹下所有文件 返回一个列表
print(os.listdir())
print(os.listdir('20240120'))

# 8. rename() : 重命名文件夹
os.rename('20240120', '20240121')