class ConNguoi:
    power = 0
    HP = 0
    MP = 0
    level = 0
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.power = age + 2
        self.HP = age * weight
        if weight - age < 0:
            self.MP = 0
        else:
            self.MP = weight - age
            
    def gioi_thieu_ban_than(self):
        print(f"em tên là {self.name}, em {self.age} tuổi, HP của em là {self.HP}")
    
    def len_level(self):
        self.level += 1
    
    def kynang(self):
        if self.level == 0:
            print(f"{self.name} không có kỹ năng")
        if self.level == 1:
            print(f"{self.name} có kỹ năng uống sữa")
        if self.level == 2:
            print(f"{self.name} có kỹ năng bẹt bẹt")
    