from newerloginsystem import *
from studentloginsystem import *
from managerloginsystem import *
class Login(object):
    # 程序入口函数
    def run(self):
        print('欢迎进入学生管理系统!')
        while True:
            # 显示主菜单
            self.showmenu_main()

            # 用户输入功能序号
            mainmenu_num = int(input('请输入您需要的功能序号: '))

            # 根据用户输入的序号执行不同的功能

            # 学生登录
            if mainmenu_num == 1:
                student = Student_Login()
                student.run()

            # 教师登录
            elif mainmenu_num == 2:
                manager = Manager_Login()
                manager.run()

            # 新用户注册
            elif mainmenu_num == 3:
                newperson = Newer_Login()
                newperson.run()

            # 退出系统
            elif mainmenu_num == 4:
                print('确认退出系统? 确认退出请输入0')
                exit_num = int(input())
                if exit_num == 0:
                    break

    def showmenu_main(self):
        """显示主菜单"""
        print('请选择如下功能: ')
        print('1: 学生登录')
        print('2: 教师登录')
        print('3: 新用户注册')
        print('4: 退出系统')