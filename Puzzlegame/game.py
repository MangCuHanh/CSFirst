import os
import sys
import random
import pygame
import settings


def kiem_tra_ket_thuc(bang, kich_thuoc):
    assert isinstance(kich_thuoc, int)
    so_o = kich_thuoc * kich_thuoc
    for hat_dit in range(so_o - 1):
        if bang[hat_dit] != hat_dit:
            return False
    return True


def qua_phai(bang, vi_tri_o_trang, vi_tri_cot):
    if vi_tri_o_trang % vi_tri_cot == 0:
        return vi_tri_o_trang
    bang[vi_tri_o_trang - 1], bang[vi_tri_o_trang] = (
        bang[vi_tri_o_trang],
        bang[vi_tri_o_trang - 1],
    )
    return vi_tri_o_trang


def qua_trai(bang, vi_tri_o_trang, vi_tri_cot):
    if (vi_tri_o_trang + 1) % vi_tri_cot == 0:
        return vi_tri_o_trang
    bang[vi_tri_o_trang + 1], bang[vi_tri_o_trang] = (
        bang[vi_tri_o_trang],
        bang[vi_tri_o_trang + 1],
    )
    return vi_tri_o_trang + 1


def di_xuong(bang, vi_tri_o_trang, vi_tri_cot):
    if vi_tri_o_trang < vi_tri_cot == 0:
        return vi_tri_o_trang
    bang[vi_tri_o_trang - vi_tri_cot], bang[vi_tri_o_trang] = (
        bang[vi_tri_o_trang],
        bang[vi_tri_o_trang - vi_tri_cot],
    )
    return vi_tri_o_trang - vi_tri_cot


def di_len(bang, vi_tri_o_trang, so_dong, vi_tri_cot):
    if vi_tri_o_trang >= (so_dong - 1) * vi_tri_cot:
        return vi_tri_o_trang
    bang[vi_tri_o_trang + vi_tri_cot], bang[vi_tri_o_trang] = (
        bang[vi_tri_o_trang],
        bang[vi_tri_o_trang + vi_tri_cot],
    )
    return vi_tri_o_trang + vi_tri_cot


def tao_bang(so_dong, vi_tri_cot, so_o):
    bang = []
    for i in range(so_o):
        bang.append(i)
    vi_tri_o_trang = so_o - 1
    bang[vi_tri_o_trang] = -1
    for i in range(settings.hinh_toi_da):
        direction = random.randint(0, 3)
        if direction == 0:
            vi_tri_o_trang = qua_trai(bang, vi_tri_o_trang, vi_tri_cot)
        elif direction == 1:
            qua_phai(bang, vi_tri_o_trang, vi_tri_cot)
        elif direction == 2:
            di_len(bang, vi_tri_o_trang, vi_tri_cot, so_dong)
        elif direction == 3:
            di_xuong(bang, vi_tri_o_trang, vi_tri_cot)
    return bang, vi_tri_o_trang


def lay_duong_dan_cua_hinh(thu_muc_goc):
    ten_hinh = os.listdir(thu_muc_goc)
    assert len(ten_hinh) > 0
    return os.path.join(thu_muc_goc, random.choice(ten_hinh))


def giaodien_ketthuc(man_hinh, chieu_rong, chieu_cao):
    man_hinh.fill(settings.mau_nen)
    font = pygame.font.Font(settings.kieu_chu, chieu_rong / 15)
    tieu_de = font.render("You won", True, (233, 150, 122))
    hinh_chu_nhat = tieu_de.get_rect()
    hinh_chu_nhat.midtop = (chieu_rong / 2, chieu_cao / 2.5)
    man_hinh.blit(tieu_de, hinh_chu_nhat)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (
                event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE
            ):
                pygame.quit()
                sys.exit()
        pygame.display.update()


def giaodien_batdau(man_hinh, rong, cao):
    man_hinh.fill(settings.mau_nen)

    kieuchu_tieude = pygame.font.Font(settings.kieu_chu, rong // 4)
    chu_tieude = kieuchu_tieude.render("Puzzle", True, settings.mau_do)

    kieuchu_c = pygame.font.Font(settings.kieu_chu, rong // 30)
    chu_noidung1 = kieuchu_c.render(
        "Bấm [K]hó [T]rung bình [D]ễ để chọn độ khó", True, settings.mau_xanhduong
    )
    chu_noidung2 = kieuchu_c.render("K=5x5 T=4x4 D=3x3", True, settings.mau_xanhduong)

    trect = chu_tieude.get_rect()
    trect.midtop = (rong / 2, cao / 10)
    c1rect = chu_noidung1.get_rect()
    c1rect.midtop = (rong / 2, cao / 2.2)
    c2rect = chu_noidung2.get_rect()
    c2rect.midtop = (rong / 2, cao / 1.8)

    man_hinh.blit(chu_tieude, trect)
    man_hinh.blit(chu_noidung1, c1rect)
    man_hinh.blit(chu_noidung2, c2rect)

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (
                event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE
            ):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.type == ord("k"):
                    return 5
                elif event.type == ord("t"):
                    return 4
                elif event.type == ord("d"):
                    return 3
        pygame.display.update()
        
def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    sudung_hinh = pygame.image.load(lay_duong_dan_cua_hinh(settings.thu_muc_hinh))
    sudung_hinh = pygame.transform.scale(sudung_hinh, settings.kich_thuoc_man_hinh)
    sudung_hinh_rect = sudung_hinh.get_rect()
    
    man_hinh = pygame.display.set_mode(settings.kich_thuoc_man_hinh)
    pygame.display.set_caption("Game Puzzle cua tui")
    
    kichthuoc = giaodien_batdau(man_hinh, sudung_hinh_rect.width, sudung_hinh_rect.height)
    assert isinstance(kichthuoc, int)
    
    sodong, socot = kichthuoc, kichthuoc
    so_o = kichthuoc * kichthuoc
    
    chieurong_o = sudung_hinh_rect.width//socot
    chieucao_o = sudung_hinh_rect.height//sodong
    
    while True:
        gameboard, vitri_otrang = tao_bang(sodong, socot, so_o)
        if not kiem_tra_ket_thuc(gameboard,kichthuoc):
            break
        
is_running = True

if __name__ == "__main__":
    main()
