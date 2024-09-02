năm =int(input("hãy nhập một năm bất kỳ:"))
if năm % 4 == 0:
    if năm % 100 == 0:
        if năm % 400 == 0:
          print("năm nhuận")
        else:            
            print("năm không nhuận")
    else:
        print("năm nhuận")
else:
    print("năm không nhuận")