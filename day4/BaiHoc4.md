# Danh sách - ngẫu nhiên

## Giới thiệu game oẵn tù tì

- nhập lựa chọn của bạn (0=búa, 1=bao, 2=kéo)
- in ra lựa chọn của bạn, và lựa chọn của máy
    - máy sẽ xử lý ntnao?
- kết quả thắng thua

## Giới thiệu số ngẫu nhiên

```python
import random

a = random.randint(1,10)
print(a)
```

## Bài tập

1. số chẳn lẽ
    - 1 số ngẫu nhiên
    - Số đó là số chẵn hay số lẻ, in ra màn hình chữ "số chẵn", "số lẻ"

## Giới thiệu cấu trúc dữ liệu - danh sách

### kiểu dữ liệu
- a = 3
- b = hello

### Cấu trúc dữ liệu
danh sách các tỉnh thành của Viet Nam
- HCM
- Hà Nội
- ...



danh sách trái cây:
- sầu riêng
- vải
- xoài
- cam
- đào

danh sách học sinh trường Duy Tân
- Kiến Văn
- Phú Khánh
- Minh Hoàng
- Gia Mẫn

```python
TinhThanh = ["HCM", "Hà Nội", "Bình Dương"]
print(TinhThanh)
print(TinhThanh[0])
print(TinhThanh[1])
print(TinhThanh[-1])

TinhThanh[1] = "Hà Bá"
print(TinhThanh[1])

TinhThanh.append("Hà Giang")
TinhThanh.extend(["aaa", "bbb"])

```

## Bài tập

2. ai sẽ kao ăn hôm nay
    - cho danh sách tên các bạn
    - chọn ngẫu nhiên 1 bạn trong đó
    - in ra tên người bạn đó sẽ kao mọi người ăn

3. vé số
    - nhập 6 số của tờ vé số
    - kết quả vé số hôm nay là [X X X X X X]
    - in ra kết quả: bạn trúng, hông trúng

### Các lỗi thường gặp đối với danh sách

    list index out of range

## Bài tập

4. Bản đồ kho báu
    - in ra bản đồ 10x10, vidu
```
aaaaaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaaaaaaaaa
```
    - nhập vào tọa độ kho báu
    - in ra bản đồ với toa độ kho báu là dấu X, vidu tọa độ kho báu 5x6
```
aaaaaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaaaaXaaaa
aaaaaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaaaaaaaaa
```

5. game oẵn tù tì

## Làm việc với Danh sách

### thêm phần tử vào vị trí

LIST.insert(vitri, value)
vitri: sẽ thêm vào ngay trước vị trí này
value: nội dung thêm vào

```python
dsChuCai = ["a", "b", "c", "d", "e", "a"]
dsChuCai.insert(2, "them")
print(f"dsChuCai = {dsChuCai}")
#ds = ['a', 'them', 'd', 'a']
```

### Nối 2 danh sách
```python
ds1 = ["1", "a"]
ds2 = ["nắng", "mưa", "bão"]
dsTong = ds1 + ds2
print(f"dsTong = {dsTong}")
#dsTong = ['1', 'a', 'nắng', 'mưa', 'bão']
```

### Đếm số lần xuất hiện
```python
dsChuCai = ["a", "b", "c", "d", "e", "a"]
DemSoLanXuatHien = dsChuCai.count("a")
print(f"DemSoLanXuatHien = {DemSoLanXuatHien}")
#DemSoLanXuatHien = 2
```

### Tạo danh sách con
```python
dsChuCai = ["a", "b", "c", "d", "e", "a"]

# lấy ra 3 phần tử của danh sách
ds3 = dsChuCai[:3]
print(f"dsCon = {ds3}")
#dsCon = ['a', 'b', 'c']
```

### Chiều dài danh sách
```python
dsChuCai = ["a", "b", "c", "d", "e", "a"]
do_dai_ds = len(dsChuCai)
print(f"độ dài ds = {do_dai_ds}")
#độ dài ds = 6
```

### List Slicing - cắt danh sách

myList[START_NUMBER:END_NUMBER]
START_NUMBER: vị trí bắt đầu
END_NUMBER: vị trí kết thúc (lấy trước cai1 kết thúc)

```python
dsChuCai = ["a", "b", "c", "d", "e", "a"]
dsCon2 = dsChuCai[1:2]
print(f"dsCon2 = {dsCon2}")
#dsCon2 = ['b']
```

### Xóa 1 phần tử trong danh sách
```python
dsChuCai = ["a", "b", "c", "d", "e", "b"]
#xóa phần tử đầu tiên
dsChuCai.remove("b")
print(f"dsChuCai sau khi remove = {dsChuCai}")
#dsChuCai sau khi remove = ['a', 'c', 'd', 'e', 'b']

#xóa tại vị trí
del dsChuCai[1]
print(dsChuCai)
#['a', 'd', 'e', 'b']
```

### Lấy 1 phần tử ra khỏi danh sách
```python
dsChuCai = ["a", "b", "c", "d", "e", "a"]
LayRa = dsChuCai.pop(2)
print(f"dsChuCai = {dsChuCai}")
print(LayRa)
#dsChuCai = ['a', 'b', 'd', 'e', 'a']
#c
```

### ddd
```python
dsChuCai = ["a", "b", "c", "d", "e", "a"]
ds = dsChuCai[::2]
print(f"ds = {ds}")
#ds = ['a', 'c', 'e']
```