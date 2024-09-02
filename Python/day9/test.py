tudien = {"teacher": "giáo viên", 
          "water": "nước",
          9999: "bốn số 9"}
print(tudien["teacher"])
print(tudien[9999])


tudien["teacher"] = "thầy Tony"
print(tudien["teacher"])


#từ điển với vòng lặp 
for key in tudien:
    print(key)
    print(tudien[key])


for key in tudien:
    print(key)
    print(tudien[key])

#TODO thêm key???
tudien["sun"] = "mặt trời"

#TODO xóa 1 key
del tudien["water"]


#từ điển với vòng lặp 
for key in tudien:
    print(key)
    print(tudien[key])
