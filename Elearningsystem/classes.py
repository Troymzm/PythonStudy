class ClassInfo(object):
    
    def __init__(self, number, name, teacher, position, time) -> None:
        self.number = number
        self.name = name
        self.teacher = teacher
        self.position = position
        self.time = time
        
        

    def __str__(self) -> str:
        return f'{self.number}, {self.name}, {self.teacher}, {self.position}, {self.time}'