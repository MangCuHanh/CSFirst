# Cú pháp hàm với tham số

```python
def ten_ham(tham_so1, tham_so2):
    print(tham_so1)
    print(tham_so2)
```

Vidu

```python
def tinh_quang_duong(v, t):
    """
    Tính quãng đường theo công thức S = V x T
    Các tham số:
        V (int or float): vận tốc (km/giờ)
        T (int or float): thời gian (giờ)
    In ra:
        int or float: quãng đường (km)
    """
    s = v*t
    print(f"quang duong di duoc la: {s} km")

tinh_quang_duong(10, 0.5)

```

# Cú pháp hàm với tham số có trả về

```python
def tinh_tong(tham_so1, tham_so2):
    return tham_so1 + tham_so2

tinh_tong(2, 3)
```
## Bài tập
1. viết 1 hàm để tính số lượng thùng sơn phải mua để sơn tường
    - biết 1 thùng sơn có thể sơn được 5m vuông
    - cho nhập chiều dài, chiều rộng bức tường
    - in ra số lượng thùng sơn phải đi mua (làm tròn lên)

2. viết hàm tính thời gian chạy xe theo công thức S = V * T
    - nhập độ dài quãng đường
    - nhập vận tốc xe chạy
    - in ra thời gian xe chạy

3. viết hàm kiểm tra số nguyên tố (số chia hết cho 1 và cho chính nó)
    - nhập 1 số nguyên dương
    - in ra số đó có phải là số nguyên tố hông

4. mật mã Caesar
    - bạn muốn mã hóa hay giải mã
    - nhập 1 đoạn văn bản
    - nhập key mã hóa/giải mã
    - in ra đoạn văn bản đã mã hóa/giải mã