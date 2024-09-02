import sys
dsChuCai = ["a", "b", "c", "d", "e", "a", "h", "a"]
#            0    1    2    3    4    5    6    7
# def count_adjacent_repeats(alist):

# Example usage:
# alist = [1, 2, 2, 3, 3, 5, 6]
# result = count_adjacent_repeats(alist)
# print(f"Number of adjacent repeated elements: {result}")

# in ra vitri của tất cả a trong danh sách
tam = 0
while tam < len(dsChuCai):
        if dsChuCai[tam] == 'a':
            print("a",end="")
            print(tam)   
        tam +=1

tam = 0
while tam < len(dsChuCai):
    if dsChuCai[tam] == 'a':
        print("a ",end="")
        print(tam)   
    tam +=1
        
        
# for bf in range(len(dsChuCai)):
#     if dsChuCai[bf] == "a":
#         print(f"{dsChuCai[bf]} {bf}")

# tam = 0
# for af in dsChuCai:
#     if af == 'a':
#         print("a ",end="")
#         print(tam)   
#     tam+=1

# # afs = dsChuCai.index("a")
# # for dsCshuCai in range(len(dsChuCai)):
# #     dfghjkla = dsChuCai.count("a")
# #     if dsCshuCai == afs:
# #         print(dsChuCai[dsCshuCai],end="")
# #         print(dsCshuCai)    
# #         dsChuCai[afs] = 's'
# #         if dfghjkla == 0:
# #             sys.exit()    
# #         else:
# #             afs = dsChuCai.index("a")
       
                                                        