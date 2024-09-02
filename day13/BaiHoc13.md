# **DEBUGGING**

**Describe Problem**
```python
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()
```

**Reproduce the Bug**
```python
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])
```

**Play Computer**
```python
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")
```

**Fix the Errors**
```python
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")
```

**Print is Your Friend**
```python
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
```

**Use a Debugger**
```python
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
```

**Tách chuỗi - in trước**
```python
cau = "hôm nay trời mưa hoài"

for kytu in cau:
    print(kytu,end="")
    if(kytu == " "):
        print("...",end="")

#Mong muốn kết quả
#hôm...nay...trời...mưa...hoài
```

**Tách chuỗi - if**
```python
cau = "hôm nay Trời Mưa Hoài"
for kytu in cau:
    if kytu == 'h':
        print("H",end="")
    if kytu == 'n':
        print("N",end="")
    # ---
    if kytu == ' ':
        print("",end="")
    else:
        print(kytu,end="")
    # ---
#Mong muốn kết quả
#HômNayTrờiMưaHoài
``` 

**Tách if phức tạp để debug**
```python
a = "abce"
b = "b44444"
c = 4455

# dk1 = a.count(a) != 1
# dk2 = b.isnumeric()
# dk3 = c.is_integer()

# dkTạm = dk1 and dk2
# dkCuoiCung = dkTạm and dk3

if(a.count(a) != 1 and b.isnumeric() and c.is_integer()):
    print("hahaha")
```

**SyntaxError**
```python
so = int(input("Nhập 1 số bạn muốn ktra chẵn lẻ: "))
if so % 2 = 0:
    print("số chẵn")
else:
    print("số lẻ")
```

**Debug Leapyear**
```python
year = input("Nhập năm để ktra: ")
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("năm nhuận.")
        else:
            print("không phải năm nhuận")
    else:
        print("năm nhuận")
else:
    print("không phải năm nhuận")
```

**Debug FizzBuzz**
```python
for so in range(1, 101):
    if so % 3 == 0 or so % 5 == 0:
        print("FizzBuzz")
    if so % 3 == 0:
        print("Fizz")
    if so % 5 == 0:
        print("Buzz")
    else:
        print([so])
```