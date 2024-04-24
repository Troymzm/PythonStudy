class Student(object):
    def __init__(self, name, gender, tel) -> None:
        # 姓名 性别 手机号
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self) -> str:
        return f'{self.name}, {self.gender}, {self.tel}'
    
