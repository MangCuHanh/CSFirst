hoc_sinh = {
            "Bình": 8,
            "Bảo": 7,
            "An": 10,
            "Phong": 6,
            "Vy": 5
        }

student_grades = {}
for jk in hoc_sinh:
    if hoc_sinh[jk] == 10:
        student_grades[jk] = "xuất sắc"
    elif hoc_sinh[jk] == 9:
        student_grades[jk] = "giỏi"
    elif hoc_sinh[jk] <= 8 and hoc_sinh[jk] >= 6:
        student_grades[jk] = "khá"
    elif hoc_sinh[jk] <= 5 and hoc_sinh[jk] >= 0:
        student_grades[jk] = "trung bình"
        
        
        

for key in student_grades:
    print(key)
    print(student_grades[key])
    print()