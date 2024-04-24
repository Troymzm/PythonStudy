import requests

url = 'http://www.baidu.com'

response = requests.get(url)

# 打印源码的str类型数据
print(response.text)