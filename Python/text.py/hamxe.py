class xe:
    #1. deu la XE
    #2. co banh 2 4 4
    #3. van toc 30-40 100-150 180-200
    #4. binh xang ko, 5lit, 10-20lit
    vantoc =0
    binhxang = 0
    # def __init__(self,v,q,name):
    #     self.v = v
    #     self.q = q
    #     ưe = self.thoi = q // v
    #     self.t = ưe
    #     self.van = q // ưe
    #     self.quang = ưe * v
    #     self.xang = 1
    #     self.name = name
    #     if  self.van > 50 and self.quang > (self.van * 3):
    #         self.xang -=  0.3
    #     if self.van < 50 and self.quang > (self.van * 3):
    #         self.xang -= 0.2
    #     if self.van < 50 and self.quang < (self.van * 3):
    #         self.xang -= 0.1
    def __init__(self, ten, sobanhxe, vantoc, dungtichbinhxang):
        self.name = ten
        self.banhxe = sobanhxe
        self.vantoc = vantoc
        self.binhxang = dungtichbinhxang
    def gioithieuxe(self):
        print(f"vận tốc {self.name} là: {self.van}km/h,quãng đường chạy được:{self.quang}km")    
        