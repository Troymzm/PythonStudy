from students import *
from classes import *
class Student_Login(object):
    # 以列表形式存储学生信息
    def __init__(self) -> None:
        self.student_infolist = []
        self.class_infolist = []
        

    # 程序入口函数
    def run(self):
        print('统一身份认证:--------')
        # 身份认证
        my_student = self.test_password()
        while my_student != False:
            # 认证成功后显示菜单
            self.showmenu_student()

            # 用户输入功能序号
            student_menu_num = int(input('请输入您需要的功能序号: '))

            # 根据用户输入的序号执行不同的功能
            if student_menu_num == 1:
                while True:
                    self.showmenu_student_info()

                    select_num = int(input('请输入您需要的功能序号: '))

                    if select_num == 1:
                        self.show_infostudent(my_student)

                    elif select_num == 2:
                        while True:
                            self.showmenu_student_info_modify()
                        
                            select_num_1 = int(input('请输入您需要的功能序号: '))
                            if select_num_1 == 4:
                                break
                            else:
                                if select_num_1 == 1:
                                    select_mode = 'password'
                                elif select_num_1 == 2:
                                    select_mode = 'email'
                                elif select_num_1 == 1:
                                    select_mode = 'tel'
                                self.modify_infostudent(my_student, select_mode)
                    elif select_num == 3:
                        if self.clear_infostudent(my_student) == False:
                            return
                    elif select_num == 4:
                        break


            elif student_menu_num == 2:
                while True:
                    self.showmenu_student_classes()

                    select_num = int(input('请输入您需要的功能序号: '))

                    if select_num == 1:
                        self.add_student_classes(my_student)
                    elif select_num == 2:
                        self.del_student_classes(my_student)
                    elif select_num == 3:
                        self.print_student_classes(my_student)
                    elif select_num == 4:
                        self.print_info_classes()
                    elif select_num == 5:
                        break

            elif student_menu_num == 3:
                while True:
                    self.showmenu_student_grades()

                    select_num = int(input('请输入您需要的功能序号: '))

                    if select_num == 1:
                        self.search_grade_student(my_student)
                    elif select_num == 2:
                        break
            
            elif student_menu_num == 4:
                break




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
            new_list = eval(data)
            self.student_infolist = [StudentInfo(i['name'], i['gender'], i['id'], i['password'], i['email'], i['tel'], i['classes'], i['grades']) for i in new_list]
            for i in self.student_infolist:
                class_list = [ClassInfo(j['number'], j['name'], j['teacher'], j['position'], j['time']) for j in i.classes]
                i.classes = class_list
        finally:
            # 3. 关闭文件
            f.close()

    def showmenu_student(self):
        """显示学生登录页面主菜单"""
        print('请选择如下功能: ')
        print('1: 个人信息')
        print('2: 选课')
        print('3: 成绩')
        print('4: 返回主界面')

    def showmenu_student_info(self):
        """显示学生个人信息页面菜单"""
        print('请选择如下功能: ')
        print('1: 查看个人信息')
        print('2: 修改个人信息')
        print('3: 注销个人账户')
        print('4: 返回学生登录界面')
    
    def showmenu_student_info_modify(self):
        """显示学生修改个人信息页面菜单"""
        print('请选择如下功能: ')
        print('1: 修改登录密码')
        print('2: 修改个人邮箱')
        print('3: 修改个人电话')
        print('4: 返回学生个人信息界面')

    def showmenu_student_classes(self):
        """显示学生选课页面菜单"""
        print('请选择如下功能: ')
        print('1: 选课')
        print('2: 退课')
        print('3: 查看选课结果')
        print('4: 查看所有可选课程')
        print('5: 返回学生登录界面')

    def showmenu_student_grades(self):
        """显示学生成绩页面菜单"""
        print('请选择如下功能: ')
        print('1: 查询成绩')
        # print('2: 查看GPA')
        print('2: 返回学生登录界面')

    def showmenu_student_info_modify_1(self):
        """显示学生修改信息后所需功能"""
        print('请选择如下功能: ')
        print('1: 保存修改后的信息')
        print('2: 返回修改信息界面')

    def showmenu_student_info_modify_2(self):
        """显示学生选课后所需功能"""
        print('请选择如下功能: ')
        print('1: 保存选课信息')
        print('2: 返回选课界面')

    def showmenu_student_info_modify_3(self):
        """显示学生退课后所需功能"""
        print('请选择如下功能: ')
        print('1: 保存退课信息')
        print('2: 返回退课界面')

    def test_password(self):
        self.load_info_student()
        """学生身份认证"""
        try_num = 5
        while try_num >= 0:
            try_id = input('请输入您的学号(8位数字): ')
            try_password = input('请输入您的登录密码: ')
            try_num -= 1
            for i in self.student_infolist:
                if (try_id == i.id) and (try_password == i.password):
                    return i
            else:
                print(f'您输入的学号或密码有误, 剩余尝试次数为:{try_num}次')
                newnum = int(input('重新输入请输入1,退出请输入0: '))
                if newnum == 0:
                    return False
        return False
    
    def show_infostudent(self, current_student):
        """查看个人信息"""
        self.load_info_student()
        idnum = current_student.id
        for i in self.student_infolist:
            if idnum == i.id:
                print(f'您的姓名为:{current_student.name}')
                print(f'您的性别为:{current_student.gender}')
                print(f'您的学号为:{current_student.id}')
                print(f'您的邮箱为:{current_student.email}')
                print(f'您的电话为:{current_student.tel}')

    def modify_infostudent(self, current_student, info):
        """修改学生个人信息"""
        self.load_info_student()
        idnum = current_student.id
        flag = 0
        for i in self.student_infolist:
            if idnum == i.id:
                if info == 'password':
                    new_password = input(f'请输入您的新密码: ')
                    
                    while True:
                        new_password_1 = input('请确认您的新密码: ')
                        if new_password != new_password_1:
                            # 报错
                            print('您两次输入的密码不一致, 请重新输入')
                        else:
                            if len(new_password) < 6:
                                print('您的登录密码过短, 安全风险较高, 请重新输入')
                            else:
                                    break
                    i.password = new_password

                elif info == 'email':
                    new_email = input(f'请输入您修改后的邮箱: ')
                    i.email = new_email
                elif info == 'tel':
                    new_tel = input(f'请输入您修改后的电话: ')
                    i.tel = new_tel
                while True:
                    self.showmenu_student_info_modify_1()
                 
                    save_num = int(input('请输入您需要的功能序号: '))
                    if save_num == 1:
                        self.save_info_student()
                        flag = 1
                        print('保存成功!')
                    elif save_num == 2:
                        if flag == 0:
                            print('您的更改信息未保存,确认退出？')
                            save_num_1 = int(input('确认退出请输入0: '))
                            if save_num_1 == 0:
                                self.load_info_student()
                                break
                        elif flag == 1:
                            break
        
    
    def save_info_student(self):
        """保存学生信息"""
        # 1. 打开文件
        path = 'E:\\code\\Python\\Elearningsystem\\student.data'
        f = open(path, 'w')

        # 2. 文件写入数据
        # 2.1 [学员对象] 转换成 [字典]
        new_list = []
        for i in self.student_infolist:
            class_list = []
            for j in i.classes:
                class_list.append(j.__dict__)
            i.classes = class_list
            new_list.append(i.__dict__)
        
        # 2.2 文件写入 字符串数据
        f.write(str(new_list))

        # 3. 关闭文件
        f.close()
    def clear_infostudent(self, current_student):
        """注销账户"""
        self.load_info_student()
        clear_idnum = current_student.id
        clear_select_num = int(input('确认注销? 确认注销请输入1 退出请输入0: '))
        if clear_select_num == 1:
            for i in self.student_infolist:
                if clear_idnum == i.id:
                    self.student_infolist.remove(i)
                break
            self.save_info_student()
            print('注销成功!')
            return False
        else:
            return True
        
    def load_info_class(self):
        """加载课程信息"""
        # 1. 打开文件 尝试r打开 如果有异常w
        try:
            path = 'E:\\code\\Python\\Elearningsystem\\class.data'
            f = open(path, 'r')
        except:
            path = 'E:\\code\\Python\\Elearningsystem\\class.data'
            f = open(path, 'w')
        else:
            # 2. 读取数据 文件读取出的数据是字符串 还原列表类型 [{}] 转换 [学员对象]
            data = f.read()  # 字符串
            new_list = eval(data)
            self.class_infolist = [ClassInfo(i['number'], i['name'], i['teacher'], i['position'], i['time']) for i in new_list]
        finally:
            # 3. 关闭文件
            f.close()
    
    def add_student_classes(self, current_student):
        self.load_info_student()
        self.load_info_class()
        idnum = current_student.id
        flag = 0
        for i in self.student_infolist:
            if idnum == i.id:
                class_list = i.classes
                classnumber = input('请输入所要添加的课程号: ')
                for j in self.class_infolist:
                    if classnumber == j.number:
                        while True:
                            self.showmenu_student_info_modify_2()

                            save_num = int(input('请输入您需要的功能序号: '))
                            if save_num == 1:
                                class_list.append(j)
                                i.classes = class_list
                                self.save_info_student()
                                flag = 1
                                print('选课成功!')
                            elif save_num == 2:
                                if flag == 0:
                                    print('您的更改信息未保存,确认退出？')
                                    save_num_1 = int(input('确认退出请输入0: '))
                                    if save_num_1 == 0:
                                        break
                                elif flag == 1:
                                    break
                
                        break
                else:
                    print('您输入的课程号不存在!')
                
    
    def del_student_classes(self, current_student):
        self.load_info_student()
        idnum = current_student.id
        flag = 0
        for i in self.student_infolist:
            if idnum == i.id:
                class_list = i.classes
                classnumber = input('请输入所要退课的课程号: ')
                for j in class_list:
                    if classnumber == j.number:
                        while True:
                            self.showmenu_student_info_modify_3()

                            save_num = int(input('请输入您需要的功能序号: '))
                            if save_num == 1:
                                class_list.remove(j)
                                i.classes = class_list
                                self.save_info_student()
                                flag = 1
                                print('退课成功!')
                            elif save_num == 2:
                                if flag == 0:
                                    print('您的更改信息未保存,确认退出？')
                                    save_num_1 = int(input('确认退出请输入0: '))
                                    if save_num_1 == 0:
                                        break
                                elif flag == 1:
                                    break
                                
                        break
                else:
                    print('您输入的课程号不存在!')

    def print_student_classes(self, current_student):
        self.load_info_student()
        self.load_info_class()
        idnum = current_student.id
        flag = 0
        for i in self.student_infolist:
            if idnum == i.id:
                for j in i.classes:
                    flag += 1
                    print(f'{flag}.')
                    print(f'课程号: {j.number}')
                    print(f'课程名称: {j.name}')
                    print(f'授课教师: {j.teacher}')
                    print(f'上课地点: {j.position}')
                    print(f'上课时间: {j.time}')
        if flag == 0:
            print('您没有选择任何课程')

    def print_info_classes(self):
        self.load_info_class()
        flag = 0
        for i in self.class_infolist:
            flag += 1
            print(f'{flag}.')
            print(f'课程号: {i.number}')
            print(f'课程名称: {i.name}')
            print(f'授课教师: {i.teacher}')
            print(f'上课地点: {i.position}')
            print(f'上课时间: {i.time}')
        if flag == 0:
            print('当前无任何课程')

    def search_grade_student(self, current_student):
        self.load_info_student()
        idnum = current_student.id
        for i in self.student_infolist:
            if idnum == i.id:
                if len(i.grades) == 0:
                    print(f'学号为{i.id}的学生{i.name}目前无成绩')
                else:
                    flag = 0
                    print(f'学号为{i.id}的学生{i.name}历次考试成绩如下: ')
                    for j in i.grades:
                        flag += 1
                        print(f'第{flag}次成绩: {j}分')

                break
        
