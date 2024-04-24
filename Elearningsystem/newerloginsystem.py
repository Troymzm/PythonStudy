from students import *
from managers import *
from classes import *
class Newer_Login(object):
    # 以列表形式存储学生和教师信息
    def __init__(self) -> None:
        self.student_infolist = []
        self.manager_infolist = []
    

    # 程序入口函数
    def run(self):
        while True:
            # 显示菜单
            self.showmenu_newer()

            # 用户输入功能序号
            newermenu_num = int(input('请输入您需要的功能序号: '))

            # 根据用户输入的序号执行不同的功能
            if newermenu_num == 1:
                flag = 0
                self.load_info_student()
                self.add_info_student()
                
                while True:
                    self.showmenu_newer_1()
                    save_num = int(input('请输入您需要的功能序号: '))
                    if save_num == 1:
                        self.save_info_student()
                        flag = 1
                        print('保存成功!')
                    elif save_num == 2:
                        if flag == 0:
                            print('您的注册信息未保存,确认退出？')
                            save_num_1 = int(input('确认退出请输入0: '))
                            if save_num_1 == 0:
                                self.load_info_student()
                                break
                        elif flag == 1:
                            break
            elif newermenu_num == 2:
                flag = 0
                self.load_info_manager()
                self.add_info_manager()
                
                while True:
                    self.showmenu_newer_1()
                    save_num = int(input('请输入您需要的功能序号: '))
                    if save_num == 1:
                        self.save_info_manager()
                        flag = 1
                        print('保存成功!')
                    elif save_num == 2:
                        if flag == 0:
                            print('您的注册信息未保存,确认退出？')
                            save_num_1 = int(input('确认退出请输入0: '))
                            if save_num_1 == 0:
                                self.load_info_manager()
                                break
                        elif flag == 1:
                            break
            elif newermenu_num == 3:
                break

    def save_info_student(self):
        """保存学生信息"""
        # 1. 打开文件
        path = 'E:\\code\\Python\\Elearningsystem\\student.data'
        f = open(path, 'w')

        # 2. 文件写入数据
        # 2.1 [学员对象] 转换成 [字典]
        new_list = [i.__dict__ for i in self.student_infolist] 

        # 2.2 文件写入 字符串数据
        f.write(str(new_list))

        # 3. 关闭文件
        f.close()

    def load_info_student(self):
        """加载学生信息"""
        # 1. 打开文件 尝试r打开 如果有异常w
        try:
            path = 'E:\\code\\Python\\Elearningsystem\\student.data'
            f = open(path, 'r')
        except:
            path = 'E:\\code\\Python\\Elearningsystem\\student.data'
            f = open(path, 'w')
        else:
            # 2. 读取数据 文件读取出的数据是字符串 还原列表类型 [{}] 转换 [学员对象]
            data = f.read()  # 字符串
            if len(data) == 0:
                self.student_infolist = []
            else:
                new_list = eval(data)
                self.student_infolist = [StudentInfo(i['name'], i['gender'], i['id'], i['password'], i['email'], i['tel'], i['classes'], i['grades']) for i in new_list]
                for i in self.student_infolist:
                    class_list = [ClassInfo(j['number'], j['name'], j['teacher'], j['position'], j['time']) for j in i.classes]
                i.classes = class_list
        finally:
            # 3. 关闭文件
            f.close()

        
    def add_info_student(self):
        """添加学生信息"""
        while True:
            new_id = input('请输入学号(8位数字): ')
            if len(new_id) == 8:
                for i in self.student_infolist:
                    if new_id == i.id:
                        # 报错
                        print('您输入的学号已经存在,注册失败!')
                        newnum = int(input('重新输入请输入1,退出请输入0: '))
                        if newnum == 0:
                            return
                else:
                    break
            else:
                print('您输入的学号不为8位, 请重新输入')
        new_name = input('请输入姓名: ')
        new_gender = input('请输入性别(“男”或“女”): ')
        new_email = input('请输入电子邮箱: ')
        new_tel = input('请输入电话: ')
        while True:
            new_password = input('请设置长度为6位及以上的登录密码: ')
            new_password_1 = input('请确认您设置的登录密码: ')
            if new_password != new_password_1:
                # 报错
                print('您两次输入的密码不一致, 请重新输入')
            else:
                if len(new_password) < 6:
                    print('您的登录密码过短, 安全风险较高, 请重新输入')
                else:
                    break
        new_student = StudentInfo(new_name, new_gender, new_id, new_password, new_email, new_tel)
        self.student_infolist.append(new_student)

    def add_info_manager(self):
        """添加教师信息"""
        while True:
            new_id = input('请输入工号(8位数字): ')
            if len(new_id) == 8:
                for i in self.manager_infolist:
                    if new_id == i.id:
                        # 报错
                        print('您输入的工号已经存在,注册失败!')
                        newnum = int(input('重新输入请输入1,退出请输入0: '))
                        if newnum == 0:
                            return
                else:
                    break
            else:
                print('您输入的工号不为8位, 请重新输入')
        new_name = input('请输入姓名: ')
        new_gender = input('请输入性别(“男”或“女”): ')
        new_email = input('请输入电子邮箱: ')
        new_tel = input('请输入电话: ')
        while True:
            new_password = input('请设置长度为6位及以上的登录密码: ')
            new_password_1 = input('请确认您设置的登录密码: ')
            if new_password != new_password_1:
                # 报错
                print('您两次输入的密码不一致, 请重新输入')
            else:
                if len(new_password) < 6:
                    print('您的登录密码过短, 安全风险较高, 请重新输入')
                else:
                    break
        new_manager = ManagerInfo(new_name, new_gender, new_id, new_password, new_email, new_tel)
        self.manager_infolist.append(new_manager)

    def load_info_manager(self):
        """加载教师信息"""
        # 1. 打开文件 尝试r打开 如果有异常w
        try:
            path = 'E:\\code\\Python\\Elearningsystem\\manager.data'
            f = open(path, 'r')
        except:
            path = 'E:\\code\\Python\\Elearningsystem\\manager.data'
            f = open(path, 'w')
        else:
            # 2. 读取数据 文件读取出的数据是字符串 还原列表类型 [{}] 转换 [学员对象]
            data = f.read()  # 字符串
            new_list = eval(data)
            self.manager_infolist = [ManagerInfo(i['name'], i['gender'], i['id'], i['password'], i['email'], i['tel']) for i in new_list]
        finally:
            # 3. 关闭文件
            f.close()
        
    def save_info_manager(self):
        """保存教师信息"""
        # 1. 打开文件
        path = 'E:\\code\\Python\\Elearningsystem\\manager.data'
        f = open(path, 'w')

        # 2. 文件写入数据
        # 2.1 [教师对象] 转换成 [字典]
        new_list = [i.__dict__ for i in self.manager_infolist] 

        # 2.2 文件写入 字符串数据
        f.write(str(new_list))

        # 3. 关闭文件
        f.close()

    def showmenu_newer(self):
        """显示新用户注册页面主菜单"""
        print('请选择如下功能: ')
        print('1: 学生注册')
        print('2: 教师注册')
        print('3: 返回主界面')
    def showmenu_newer_1(self):
        """显示新用户注册后所需功能"""
        print('请选择如下功能: ')
        print('1: 保存注册信息')
        print('2: 返回注册界面')
    