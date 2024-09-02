# Danh sách đặc biệt

lý do
```python
con_ran = [(0,2), (0,1), (0,0)]
a, b = con_ran[1]
# a sẽ bằng 0
# b sẽ bằng 1

for khuc in range(0, len(con_ran)):
    x, y = con_ran[khuc]
    print(f"khúc {khuc} của con rắn có tọa độ là {x}, {y}")

i = 0
for x, y in con_ran:
    # x, y = con_ran[khuc]
    print(f"khúc {0} của con rắn có tọa độ là {x}, {y}")
    i += 1
```

