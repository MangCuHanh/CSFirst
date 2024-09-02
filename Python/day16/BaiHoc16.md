# OOP Object Oriented Programming - Lập trình hướng đối tượng

Cú pháp

```python
class ten_class:
    #hàm khởi tạo
    def __init__(tham_so1, tham_so2, ...):
        self.ts1 = tham_so1
        self.ts2 = tham_so2
```

Ví dụ

```python
class ConNguoi:
    power = 0
    HP = 0
    MP = 0
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
        print(f"em tên là {self.name}, em {self.age} tuổi")

kv = ConNguoi("KienVan", 12, 34)
gm = ConNguoi("GiaMan", 10, 46)

print(kv.name)
kv.gioi_thieu_ban_than()
print(gm.age)
```