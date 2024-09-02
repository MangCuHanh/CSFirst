# bài Jun sửa:
a = float(input("nhập cân nặng của bạn:"))
b = float(input("nhập chiều cao của bạn:"))
c = round(a / b ** 2)
if c < 18.5:
    print(f"BMI của bạn là {c},bạn bị gầy")
elif c < 25:
    print(f"BMI của bạn là {c},bạn bình thường")
elif c < 30:
    print(f"BMI của bạn là {c},bạn quá cân")
elif c < 35:
    print(f"BMI của bạn là {c},bạn bị béo phì")
else:
    print(f"BMI của bạn là {c},bạn quá béo phì")