a = 'hello ban Kien Van'
print(a.upper())

# TODO   
a = 'hello ban Kien Van'
# for a2t7777 in a:
#     if a2t7777 == " ":
#         print(".......",end="")
#     else:
#         print(a2t7777,end="")
print(a.replace(" ","..........."))

a = 'hello ban Kien Van'
print(a.replace(" ",""))

# for á in a:
#     if á == 'h':
#         print("H",end="")
#     elif á == 'b':
#         print("B",end="")
#     elif á == ' ':
#         print("",end="")
#     else:
#         print(á,end="")

a = 'hello ban Kien Van'
print(a.title().replace(" ", ""))


a = 'hello ban Kien Van'
e = a.replace(" ","").replace("e", "")
print(e) 

a = 'hello ban Kien Van dieu'
f = a.replace("e", "", 1)
print(f)

a = 'hello ban Kien Van'
g = a.split("")
print(g)

a = 'hello?ban?Kien Van '
g = a.split("?")
print(g)