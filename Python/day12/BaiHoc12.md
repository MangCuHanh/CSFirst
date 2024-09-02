# Namespace: Local vs Global Scope

không gian tên
Local scope - phạm vi cục bộ
Global scope - phạm vi toàn cục

ví dụ 1
```python
a = 1

def tang_a():
    a = 2
    print(f"a (bên trong hàm tăng a) là {a}")

tang_a()
    print(f"a (bên ngoài) là {a}")
```

ví dụ 2 - **local scope**
```python
def thoi_tiet():
    hom_nay = "trời mưa"
    print(hom_nay)

thoi_tiet()
print(hom_nay)
```

ví dụ 2 - **global scope**
```python
máu_người_chơi = 10

def game():
    def ăn_máu():
        bình_máu = 2
        print(máu_người_chơi)

ăn_máu()
print(máu_người_chơi)
```

## Bài tập

1. Game đoán số
    - Nhập chế độ (dễ, vừa, khó)
        - dễ có 10 lần đoán
        - vừa có 5 lần đoán
        - khó có 3 lần đoán
    - Random một số từ 1 đến 100
    - Nhập số bạn đoán
        - nếu lớn hơn số random thì in ra "bạn đoán số cao quá"
        - nếu nhỏ hơn số random, in ra "bạn đoán số nhỏ hơn rồi"
        - nếu đoán đúng số random, in ra "chính xác". Kết thúc game