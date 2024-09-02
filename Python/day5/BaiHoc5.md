# vòng lặp

## Giới thiệu về chương trình tạo mật khẩu phức tạp

##  Lệnh FOR

Cách viết vòng lặp for
```python
for item in list_of_item:
    print(item)
```

vidu
```python
dsBan = ["KienVan", "GiaMan", "PhuKhanh"]

for ten in dsBan:
    print(ten)
```

### Bài mẫu vui


```python
import random
dsBan = ["KienVan", "GiaMan", "PhuKhanh"]
dsLoiKhen = ["đẹp trai", "ham ăn", "nói nhiều"]
for ten in dsBan:
    print(ten)
    idx = random.randint(0, len(dsLoiKhen))
    print(f"{ten} {dsLoiKhen[idx]}")
```

### Bài tập

1. tính trung bình chiều cao của danh sách sau [159, 143, 123, 144, 160, 165, 118]

2. in ra chiều cao cao nhất, và chiều cao thấp nhất trong danh sách sau [159, 143, 123, 144, 160, 165, 118]

3. sắp xếp lại danh sách sau theo thứ tự từ lớn đến bé [159, 143, 123, 144, 160, 165, 118], ra in ra danh sách sau khi đã sắp xếp

## For loop with range

Cách viết vòng lặp với range
```python
for number in range([start], [stop], [step]):
    print(number)
```

vidu
```python
for number in range(1, 100, 5):
    print(number)
```

### bài tập

4. in ra đáp số của bài toán sau
    - 1 + 2 + 3 + 4 + 5 + ..... + 98 + 99 + 100

5. in ra đáp số của bài toán sau
    - 2 + 4 + 6 + 8 + 10 + ..... + 96 + 98 + 100

6. FizzBuzz game 
    chương trình in ra từ 1 tới 100
    - lúc in đến số chia hết cho 3 thì sẽ in ra chữ Fizz
    - lúc in đến số chia hết cho 5 thì sẽ in ra chữ Buzz
    - lúc in đến số chia hết cho 3 và 5 thì sẽ in ra chữ FizzBuzz

    vidu
    ```
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    ...
    ```

7. Password Generator - chương trình giúp tạo mật khẩu phức tạp
- yêu cầu:
    - nhập số lượng ký tự chữ
    - nhấp số lượng ký tự đặc biệt
    - nhấp số lượng ký tự số
    - in ra mật khẩu phức tạp
