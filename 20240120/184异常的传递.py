import time
try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 如果在读取文件的过程中 产生了异常 那么就会捕捉到
        # 按ctrl + C终止
        print('意外终止了读取数据')
    finally:
        f.close()
        print('关闭文件')
except:
    print('文件不存在')