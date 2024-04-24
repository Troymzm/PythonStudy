from managers import *
from students import *
from classes import *
class Manager_Login(object):
    # 以列表形式存储信息
    def __init__(self) -> None:
        self.student_infolist = []
        self.manager_infolist = []
        self.class_infolist = []

    # 程序入口函数
    def run(self):
        print('统一身份认证:--------')
        # 身份认证
        my_manager = self.test_password()
        while my_manager != False:
            # 认证成功后显示菜单
            self.showmenu_manager()

            # 用户输入功能序号
            manager_menu_num = int(input('请输入您需要的功能序号: '))

            # 根据用户输入的序号执行不同的功能
            if manager_menu_num == 1:
                while True:
                    self.showmenu_manager_info()

                    select_num = int(input('请输入您需要的功能序号: '))

                    if select_num == 1:
                        self.show_infomanager(my_manager)

                    elif select_num == 2:
                        while True:
                            self.showmenu_manager_info_modify()
                        
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
                                self.modify_infomanager(my_manager, select_mode)
                    elif select_num == 3:
                        if self.clear_infomanager(my_manager) == False:
                            return
                    elif select_num == 4:
                        break


            elif manager_menu_num == 2:
                while True:
                    self.showmenu_manager_classes()

                    select_num = int(input('请输入您需要的功能序号: '))

                    if select_num == 1:
                        self.add_info_class()
                    elif select_num == 2:
                        self.del_info_class()
                    elif select_num == 3:
                        self.print_info_classes()
                    elif select_num == 4:
                        break


            elif manager_menu_num == 3:
                while True:
                    self.showmenu_manager_grades()

                    select_num = int(input('请输入您需要的功能序号: '))

                    if select_num == 1:
                        self.add_grade_student()
                    elif select_num == 2:
                        self.search_grade_student()
                    elif select_num == 3:
                        break
                    
            
            elif manager_menu_num == 4:
                break




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
            # 2. 读取数据 文件读取出的数据是字符串 还原列表类型 [{}] 转换 [教师对象]
            data = f.read()  # 字符串
            new_list = eval(data)
            self.manager_infolist = [ManagerInfo(i['name'], i['gender'], i['id'], i['password'], i['email'], i['tel']) for i in new_list]
        finally:
            # 3. 关闭文件
            f.close()

    def showmenu_manager(self):
        """显示教师登录页面主菜单"""
        print('请选择如下功能: ')
        print('1: 个人信息')
        print('2: 课程管理')
        print('3: 学生成绩')
        print('4: 返回主界面')

    def showmenu_manager_info(self):
        """显示教师个人信息页面菜单"""
        print('请选择如下功能: ')
        print('1: 查看个人信息')
        print('2: 修改个人信息')
        print('3: 注销个人账户')
        print('4: 返回教师登录界面')
    
    def showmenu_manager_info_modify(self):
        """显示教师修改个人信息页面菜单"""
        print('请选择如下功能: ')
        print('1: 修改登录密码')
        print('2: 修改个人邮箱')
        print('3: 修改个人电话')
        print('4: 返回教师个人信息界面')

    def showmenu_manager_classes(self):
        """显示教师课程管理页面菜单"""
        print('请选择如下功能: ')
        print('1: 添加课程信息')
        print('2: 删除课程信息')
        print('3: 查看所有课程')
        print('4: 返回教师登录界面')

    def showmenu_manager_grades(self):
        """显示教师成绩页面菜单"""
        print('请选择如下功能: ')
        print('1: 提交学生成绩')
        print('2: 查询学生成绩')
        print('3: 返回教师登录界面')
        

    def showmenu_manager_info_modify_1(self):
        """显示教师修改信息后所需功能"""
        print('请选择如下功能: ')
        print('1: 保存修改后的信息')
        print('2: 返回修改信息界面')

    def showmenu_manager_info_modify_2(self):
        """显示教师修改信息后所需功能"""
        print('请选择如下功能: ')
        print('1: 保存添加的成绩')
        print('2: 返回修改信息界面')

    def test_password(self):
        self.load_info_manager()
        """教师身份认证"""
        try_num = 5
        while try_num >= 0:
            try_id = input('请输入您的工号(8位数字): ')
            try_password = input('请输入您的登录密码: ')
            try_num -= 1
            for i in self.manager_infolist:
                if (try_id == i.id) and (try_password == i.password):
                    return i
            else:
                print(f'您输入的工号或密码有误, 剩余尝试次数为:{try_num}次')
                newnum = int(input('重新输入请输入1,退出请输入0: '))
                if newnum == 0:
                    return False
        return False
    
    def show_infomanager(self, current_manager):
        self.load_info_manager()
        print(f'您的姓名为:{current_manager.name}')
        print(f'您的性别为:{current_manager.gender}')
        print(f'您的工号为:{current_manager.id}')
        print(f'您的邮箱为:{current_manager.email}')
        print(f'您的电话为:{current_manager.tel}')

    def modify_infomanager(self, current_manager, info):
        """修改教师个人信息"""
        self.load_info_manager()
        idnum = current_manager.id
        flag = 0
        for i in self.manager_infolist:
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
                    self.showmenu_manager_info_modify_1()
                 
                    save_num = int(input('请输入您需要的功能序号: '))
                    if save_num == 1:
                        self.save_info_manager()
                        flag = 1
                        print('保存成功!')
                    elif save_num == 2:
                        if flag == 0:
                            print('您的更改信息未保存,确认退出？')
                            save_num_1 = int(input('确认退出请输入0: '))
                            if save_num_1 == 0:
                                self.load_info_manager()
                                break
                        elif flag == 1:
                            break
    
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
    def clear_infomanager(self, current_manager):
        """注销教师账户"""
        self.load_info_manager()
        clear_idnum = current_manager.id
        clear_select_num = int(input('确认注销? 确认注销请输入1 退出请输入0: '))
        if clear_select_num == 1:
            for i in self.manager_infolist:
                if clear_idnum == i.id:
                    self.manager_infolist.remove(i)
                break
            self.save_info_manager()
            print('注销成功!')
            return False
        else:
            return True
        
    def save_info_class(self):
        """保存课程信息"""
        # 1. 打开文件
        path = 'E:\\code\\Python\\Elearningsystem\\class.data'
        f = open(path, 'w')

        # 2. 文件写入数据
        # 2.1 [课程对象] 转换成 [字典]
        new_list = [i.__dict__ for i in self.class_infolist] 

        # 2.2 文件写入 字符串数据
        f.write(str(new_list))

        # 3. 关闭文件
        f.close()

    def add_info_class(self):
        """添加课程信息"""
        self.load_info_class()
        while True:
            new_num = input('请输入课程号(8位数字): ')
            if len(new_num) == 8:
                for i in self.class_infolist:
                    if new_num == i.number:
                        # 报错
                        print('您输入的课程号已经存在,添加失败!')
                        newnum = int(input('重新添加请输入1,退出请输入0: '))
                        if newnum == 0:
                            return
                else:
                    break
            else:
                print('您输入的课程号不为8位, 请重新输入')
        new_name = input('请输入课程名: ')
        new_teacher = input('请输入任课教师: ')
        new_position = input('请输入上课地点: ')
        new_time = input('请输入上课时间: ')
        new_class = ClassInfo(new_num, new_name, new_teacher, new_position, new_time)
        self.class_infolist.append(new_class)
        while True:
            self.showmenu_manager_info_modify_1()

            save_num = int(input('请输入您需要的功能序号: '))
            if save_num == 1:
                self.save_info_class()
                flag = 1
                print('保存成功!')
            elif save_num == 2:
                if flag == 0:
                    print('您的课程信息未保存,确认退出？')
                    save_num_1 = int(input('确认退出请输入0: '))
                    if save_num_1 == 0:
                        self.load_info_class()
                        break
                elif flag == 1:
                    break
        

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

    def del_info_class(self):
        """删除课程信息"""
        self.load_info_class()
        del_num = input('请输入需要删除的课程号(8位数字): ')
        for i in self.class_infolist:
            if del_num == i.number:
                flag = 0
                while True:
                    self.showmenu_manager_info_modify_1()

                    save_num = int(input('请输入您需要的功能序号: '))
                    if save_num == 1:
                        self.class_infolist.remove(i)
                        self.save_info_class()
                        flag = 1
                        print('保存成功!')
                    elif save_num == 2:
                        if flag == 0:
                            print('您的课程信息未保存,确认退出？')
                            save_num_1 = int(input('确认退出请输入0: '))
                            if save_num_1 == 0:
                                self.load_info_class()
                                break
                        elif flag == 1:
                            break
                    
                break
            
        else:
            print('未查询到您输入的课程号, 删除失败!')

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

    def add_grade_student(self):
        self.load_info_student()
        add_grade_student_id = input('输入添加成绩的学生的学号: ')
        for i in self.student_infolist:
            if i.id == add_grade_student_id:
                flag = 0
                add_grade = int(input('输入添加的成绩: '))
                while True:
                    self.showmenu_manager_info_modify_2()

                    save_num = int(input('请输入您需要的功能序号: '))
                    if save_num == 1:
                        i.grades.append(add_grade)
                        self.save_info_student()
                        flag = 1
                        print('保存成功!')
                    elif save_num == 2:
                        if flag == 0:
                            print('您添加的成绩未保存,确认退出？')
                            save_num_1 = int(input('确认退出请输入0: '))
                            if save_num_1 == 0:
                                break
                        elif flag == 1:
                            break
                break
        else:
            print('未查询到您输入的学号, 添加成绩失败!')

    def search_grade_student(self):
        self.load_info_student()
        add_grade_student_id = input('输入查询成绩的学生的学号: ')
        for i in self.student_infolist:
            if i.id == add_grade_student_id:
                flag = 0
                if len(i.grades) == 0:
                    print(f'学号为{i.id}的学生{i.name}目前无成绩')
                else:
                    print(f'学号为{i.id}的学生{i.name}历次考试成绩如下: ')
                    for j in i.grades:
                        flag += 1
                        print(f'第{flag}次成绩: {j}分')
                break
        else:
            print('未查询到您输入的学号, 查询成绩失败!')
                
                