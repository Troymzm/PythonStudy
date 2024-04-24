class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area

class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def __str__(self):
        return f'房子的地理位置在{self.address},房屋面积是{self.area},剩余面积是{self.free_area},家具有{self.furniture}'
    
    def add_furniture(self, item):
        """容纳家具"""
        # 如果 家具占地面积 <= 房屋剩余面积 可以搬入 家具列表添加家具名字数据并更新房屋剩余面积
        # 房屋剩余面积 - 该家具的占地面积
        # 否则 提示用户家具太大 剩余面积不足 无法容纳
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('家具太大, 面积不足, 无法容纳')


# 双人床 6
bed = Furniture('双人床', 6)
# 沙发 10
sofa = Furniture('沙发', 10)
# 椅子 5
chair = Furniture('椅子', 5)

# 房子1 北京 15
jia1 = Home('北京', 20)
jia1.add_furniture(bed)
print(jia1)
jia1.add_furniture(sofa)
print(jia1)
jia1.add_furniture(chair)
print(jia1)