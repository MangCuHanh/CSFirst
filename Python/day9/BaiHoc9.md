# Từ điển - dictionaries

cú pháp

```python
ten_bien = {"key": "value"}
```

Cách sử dụng

```python
tudien = {"teacher": "giáo viên", 
          "water": "nước",
          9999: "bốn số 9"}
print(tudien["teacher"])
print(tudien[9999])

#cập nhật value của 1 key trong từ điển
tudien["teacher"] = "thầy Tony"
print(tudien["teacher"])

#từ điển với vòng lặp 
for key in tudien:
    print(key)
    print(tudien[key])

#thêm key
tudien["sun"] = "mặt trời"

#xóa 1 key
del tudien["water"]
```

# Bài tập

1. [Đánh giá học sinh](b1_DanhGiaHocSinh.py)
    - cho dictionaries như sau
        student_scores = {
            "Harry": 8,
            "Ron": 7,
            "Hermione": 10,
            "Draco": 6,
            "Neville": 5
        }
    - tạo 1 dictionary rỗng là student_grades
    - viết code để đánh giá học sinh dựa theo điểm số và lưu vào dictionary student_grades
        10: hs xuất sắc
        8-9: hs giỏi
        6-7: hs khá
        5: hs trung bình


# Nested list (danh sách lồng nhau) and dictionaries

```python
cappitals = {
    "Vietnam": "???",
    "Campuchia": "???",
    "Thailand": "???",
    "France": "???",
    "Germany": "???"
}

travel_log = {
    "vietnam": ["TPHCM", "Lagi", "Nha Trang", "Vũng Tàu", "Cần Thơ"]
    "bạn": {"bạn cùng lớp": ["MH", "PK", "Minh Quân"],
            "bạn cùng xóm": ["Lán", "Kiều", "chị nắng", "anh Seo"]
    }
}

# challenge tạo 1 ds dùng dictionary lưu
tên nước - các thành phố đã đi qua, số lần đã đi


```

## Bài tập

2. Đấu giá - Auction
    - Nhập tên của người đấu giá
    - Nhập số tiền đấu giá
    - Còn nhà đấu giá nào khác hông? nhập **yes** hoặc **no**
        lặp lại 2 bước trên
    - khi không còn nhà đấu giá khác thì in ra tên người có số tiền đấu giá cao nhất và số tiền đó
        ví dụ "Người thắng trong cuộc đấu giá này là {} với số tiền là {}"
    - HINT: bạn có thể dùng hàm **clear()** để xóa màn hình output của console