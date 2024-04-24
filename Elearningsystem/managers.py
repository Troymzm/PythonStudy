class ManagerInfo(object):
    # 设置对象属性 姓名 性别 工号  密码 邮箱地址 电话
    def __init__(self, name, gender, id, password, email, tel) -> None:
        self.name = name
        self.gender = gender
        self.id = id
        self.password = password
        self.email = email
        self.tel = tel

    def __str__(self) -> str:
        return f'{self.name}, {self.gender}, {self.id}, {self.password}, {self.email}, {self.tel}'