import random
import time
from os import system

dsCauHoi = [
    "Nước nào giành chiến thắng trong cuộc thi Miss World 2009",
    "Ông được biết đến với các tác phẩm \"Thuốc\", \"Nhật ký người điên\", \"Cố Hương\"",
    "Hội nghị Ianta diễn ra tháng 2/1945 giữa 3 cường quốc là Mỹ, Liên Xô và..",
    "Vị vua cho lập Văn Miếu ở kinh đô Thăng Long vào năm 1070",
    "Ai là người đầu tiên quan sát thấy tế bào động vật bằng kính hiển vi?",
    "Thành phố nào được giải phóng ngày 29/3/1975?",
    "Điền từ thích hợp vào chỗ chấm:.....là đạng địa hình phổ biến của Trái Đất, chiếm 52% diện tích Châu Á và 24% bề mặt cảu Trái Đất.",
    "\"Đầu tôi chưa rơi xuống đất, xin bệ hạ đừng lo\". hãy cho biết đây là câu nói của ai?",
    "Ở các nước theo chế độ \"tam quyền phan lập\", quyền lập pháp thuộc về nghị viện (quốc hội), quyền hành pháp thuộc chính phủ (nội các), quyền tư pháp thuộc về....",
    "Trong triết học Marx lenin, phạm trù này là tổng hoà của các quan hệ xã hội.",
    "Cùng với tiêu chí \"y tế\" và \"thu nhập bình quân đầu người\", tiêu chí này hình thành nên chỉ số phát triển con người HDI của Liên hợp quốc",
    "Bản giao hưởng \"Anh hùng\" Beethoven sáng tác ban đầu tặng cho một vị tướng nước nào?",
    "Hiện vật tiêu biểu cho văn hoá Đông Sơn?",
    "Ngày 21/6/1925 Nguyễn Ái Quốc sáng lập và trực tiếp chỉ đạo xuất bản tờ báo..., đó là cơ quan của Hội Việt Nam cách mạng thanh niên, chính thức đặt nền móng cho báo chí cách mạng Việt Nam.",
    "\"Tát nước đầu đình\" thuộc loại bài ca giao duyên dù ở đây không có hình thức đối đáp nam nữ mà chỉ có lời của ai?",
    "Chỉ số nào đặc trưng cho tính chống kích nổ của nhiên liệu động cơ, chỉ số này càng cao khả năng chống nổ càng tốt?",
    "\"Ngư tiều y thuật vấn đáp\" là tác phẩm của ai?",
    "Khi hoà tan amoni nitrat vào nước, nhiệt độ dung dịch sẽ thay đổi như thế nào?",
    "Câu ca dao về nạn giặc cướp: \"Thương em anh cũng muốn vô/Sợ chuông nhà Hồ, sợ phá....\"",
    "Cáp quang là dây dẫn sáng ứng dụng hiện tượng gì để truyền tín hiệu trong thông tin.",
    "EURO lần đầu tiên tổ chức tại quốc gia nào?",
    "Khi vị trí mặt trời, mặt trăng, trái đất có vị trí như thế nào thì dao động của thuỷ triều là lớn nhất.",
    "Nằm bên dãy Hoàng Liên Sơn, Mù Cang Chải là huyện vùng sâu vùng xa của tỉnh nào?",
    "Dirichlet là người nước nào?",
    "Who is the \"Queen of Pop\"?",
    "Gió Lào có tên gọi khác là gì?",
    "Đèo Hải Vân cắt ngang dãy núi nào của Trường Sơn?",
    "Thành phố Cố đô của Nhật Bản?",
    "Vịnh Cam Ranh nằm ở địa phận tỉnh nào?",
    "Môn võ này có nguồn gốc từ Nhật Bản và dùng tay khi đối kháng.",
    "Nụ cười trong bức ảnh \"Nụ cười chiến thắng\" nổi tiếng của ai?",
    "Đàn độc huyền là tên gọi khác của loại đàn nào?",
]

dsCauTraLoi = [
    "Nga",
    "Lỗ Tấn",
    "Anh",
    "Lý Thánh Tông",
    "Lovenhuc",
    "Đà Nẵng",
    "núi",
    "Thái sư Trần Thủ Độ",
    "Toà án",
    "Con người",
    "Giáo dục",
    "Pháp",
    "Trống đồng",
    "báo thanh niên",
    "Chàng trai",
    "Octan",
    "Nguyễn Đình Chiểu",
    "Giảm",
    "Tam Giang",
    "phản xạ toàn phần",
    "Pháp",
    "thẳng hàng",
    "Yên Bái",
    "Đức",
    "Madona",
    "Gió phơn Tây Nam",
    "Dãy Bạch Mã",
    "Kyoto",
    "Khánh Hoà",
    "Karatedo",
    "Võ Thị Thắng",
    "Đàn bầu"
]

dsCauTraLoiTheoKyTu = [
    "nga",
    "lo tan",
    "anh",
    "ly thanh tong",
    "Lovenhuc",
    "da nang",
    "nui",
    "thai su tran thu do",
    "toa an",
    "con nguoi",
    "giao duc",
    "phap",
    "trong dong",
    "bao thanh nien",
    "chang trai",
    "octan",
    "nguyen dinh chieu",
    "giam",
    "tam giang",
    "phan xa toan phan",
    "phap",
    "thang hang",
    "yen bai",
    "duc",
    "madona",
    "gio phon tay nam",
    "day bach ma",
    "kyoto",
    "khanh hoa",
    "karatedo",
    "vo thi thang",
    "dau bau"
]

print ("bắt đầu chơi game chiếc nón kỳ diệu nhé!")

#chờ 1 giây
time.sleep(1)
print ("Chuẩn bị câu hỏi...")
time.sleep(0.5)

#random ra 1 số trong danh sách câu hỏi
vitriCauHoi = random.randint(0, len(dsCauHoi) - 1)
cauhoi = dsCauHoi[vitriCauHoi]
traloi = dsCauTraLoi[vitriCauHoi]
traloikytu = dsCauTraLoiTheoKyTu[vitriCauHoi]

#biến lưu những từ mà người chơi đã nhập đúng
nguoi_choi_da_doan = ''

#số lượt còn lại
luot = 10

#vòng lặp game, bắt đầu đoán các ký tự
while luot > 0:         
    system("cls")
    cac_o_chua_doan = 0             

    #in ra câu hỏi đã random
    print()
    print(dsCauHoi[vitriCauHoi])
    print()

    #in ra các ô đã đoán
    for char in traloikytu:      

    # see if the character is in the players guess
        if char in nguoi_choi_da_doan:    
            # print then out the character
            idx = traloikytu.index(char)
            print (traloi[idx],end=""),    

        else:
            print ("_",end=""),     
            cac_o_chua_doan += 1    
    print()
    print()


    # nếu các ô đã đoán đúng hết, thì in ra WIN
    if cac_o_chua_doan == 0:        
        print ("Bạn thắng")
        #thoát vòng lặp game 
        break            

    # nhập đoán ký tự
    print(f"Bạn còn {luot} để đoán")
    guess = input("đoán 1 ký tự:") 

    # lưu lại các ký tự người chơi đã đoán (đúng hay sai đều lưu hết)
    nguoi_choi_da_doan += guess                    

    # nếu lượt đoán này trong có trong kết quả
    if guess.lower() not in traloikytu:  
        # giảm số lượt có thể đoán được đi 1
        luot -= 1        
        print ("Sai")  
        time.sleep(1)

        # nếu hết lượt đoán
        if luot == 0:           
            print ("Bạn thua")
    else:
        print ("Đúng")  
        time.sleep(1)