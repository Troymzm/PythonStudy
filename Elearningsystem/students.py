class StudentInfo(object):
    # 设置对象属性 姓名 性别 学号 课程 密码 成绩 邮箱地址 电话
    def __init__(self, name, gender, id, password, email, tel, classes=[], grades=[]) -> None:
        self.name = name
        self.gender = gender
        self.id = id
        self.classes = classes
        self.password = password
        self.grades = grades
        self.email = email
        self.tel = tel

    def __str__(self) -> str:
        return f'{self.name}, {self.gender}, {self.id}, {self.password}, {self.email}, {self.tel}, {self.classes}, {self.grades}'