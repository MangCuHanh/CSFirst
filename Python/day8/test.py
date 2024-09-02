def tinh_tong_inra(tham_so1, tham_so2):
    print(f"{tham_so1 + tham_so2}")

def tinh_tong_ca_trave(tham_so1, tham_so2):
    tong = tham_so1 + tham_so2
    return tong

#a ---> b v*t???
#b--->c 10km
lan1 = tinh_tong_inra(2, 3)
lan4 = lan1
print(f"lần 1: {lan1}")
lan2 = tinh_tong_ca_trave(2, 3)
print(f"lần 2: {lan2}")
lan3 = lan2 + 10
print()