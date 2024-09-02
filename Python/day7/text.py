
def tinh_quang_duong1(v, t):
    s = v*t
    print(f"quang duong di duoc la: {s} km")

def tinh_quang_duong2(tham_so1, tham_so2):
    return tham_so1 * tham_so2

abc = tinh_quang_duong1(10, 0.5)

quangduong_AB = tinh_quang_duong2(10, 0.5)
print(quangduong_AB)



# a--->------------------------------------<--c
# bat dau tu luc 7h
# nguoi1 chay tu a den c trong 30p voi van toc 100km/h
# nguoi2 chay tu c den a trong 1h voi van toc 50km/h
# gap nhau la luc 8h
# hoi quang duong AC la bao nhieu

con_ran = [(0,2), (0,1), (0,0)]
a, b = con_ran[1]
# a sẽ bằng 0
# b sẽ bằng 1
con_ran[-1]

del(con_ran[-1])
# con_ran.insert(0, (cot_moi, hang_moi))





for khuc in range(0, len(con_ran)):
    x, y = con_ran[khuc]
    print(f"khúc {khuc} của con rắn có tọa độ là {x}, {y}")

i = 0
for x, y in con_ran:
    # x, y = con_ran[khuc]
    print(f"khúc {i} của con rắn có tọa độ là {x}, {y}")
    i += 1

