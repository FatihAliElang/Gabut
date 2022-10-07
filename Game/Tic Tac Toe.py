from tkinter import Y
from turtle import Screen
import pygame, sys
import numpy as np

pygame.init()

lebar = 600
tinggi = 600
lebar_line = 15
baris = 3
kolom = 3
radius_lingkaran = 60
lebar_lingkaran = 15
lebar_silang = 25
space = 55
#warna dalam rgb
hitam = (33, 36, 61)
merah = (255, 124, 124)
biru = (136, 225, 242)
kuning = (255, 208, 130)

#layar game
layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption( 'TIC TAC TOE')
layar.fill( hitam )

#papan
papan = np.zeros((baris, kolom))


#untuk garis
def draw_lines():
    pygame.draw.line( layar, kuning, (0, 200), (600, 200), lebar_line) # horizontal pertama
    pygame.draw.line( layar, kuning, (0, 400), (600, 400), lebar_line) # horizontal kedua
    pygame.draw.line( layar, kuning, (200, 0), (200, 600), lebar_line) # vertikal pertama
    pygame.draw.line( layar, kuning, (400, 0), (400, 600), lebar_line) # vertikal kedua

draw_lines()

def gambar():
    for Baris in range(baris):
        for Kolom in range(kolom):
            if papan[Baris][Kolom] == 1:
                pygame.draw.circle( layar, biru, (int( Kolom * 200 + 100 ), int( Baris * 200 + 100 )), radius_lingkaran, lebar_lingkaran)
            elif papan[Baris][Kolom] == 2:
                pygame.draw.line( layar, merah, (Kolom * 200 + space, Baris * 200 + 200 - space), (Kolom * 200 + 200 - space, Baris * 200 + space), lebar_silang)
                pygame.draw.line( layar, merah, (Kolom * 200 + space, Baris * 200 + space ), (Kolom * 200 + 200 - space, Baris * 200 + 200 - space), lebar_silang)



def ngisi(baris, kolom, pemain):
    papan[baris][kolom] = pemain

def kosong(baris, kolom):
    return papan[baris][kolom] == 0

def kotak_full():
    for Baris in range(baris):
        for Kolom in range(kolom):
            if papan[Baris][Kolom] == 0:
                return False

    return True

pemain = 1
game_over = False

def cek(pemain):
    #menang vertikal
    for Kolom in range(kolom):
        if papan[0][Kolom] == pemain and papan[1][Kolom] == pemain and papan[2][Kolom] == pemain:
            menang_ver(Kolom, pemain)
            return True

    #menang horizontal
    for Baris in range(baris):
        if papan[Baris][0] == pemain and papan[Baris][1] == pemain and papan[Baris][2] == pemain:
            menang_hor(Baris, pemain)
            return True

    #menang diagonal naik
    if papan[2][0] == pemain and papan[1][1] == pemain and papan[0][2] == pemain:
        menang_dia_naik(pemain)
        return True

    #menang diagonal turun
    if papan[0][0] == pemain and papan [1][1] == pemain and papan[2][2] == pemain:
        menang_dia_tur(pemain)
        return True

    return False


def menang_ver(Kolom, pemain):
    posX = Kolom * 200 + 100
    if pemain == 1:
        warna = biru
    elif pemain == 2:
        warna = merah

    pygame.draw.line(layar, warna, (posX, 15), (posX, tinggi - 15), 15)

def menang_hor(Baris, pemain):
    posY = Baris * 200 + 100
    if pemain == 1:
        warna = biru
    elif pemain == 2:
        warna = merah
    
    pygame.draw.line(layar, warna, (15, posY), (lebar - 15, posY), 15)

def menang_dia_naik(pemain):
    if pemain == 1:
        warna = biru
    elif pemain == 2:
        warna = merah

    pygame.draw.line(layar, warna, (15, tinggi - 15), (lebar - 15, 15), 15)


def menang_dia_tur(pemain):
    if pemain == 1:
        warna = biru
    elif pemain == 2:
        warna = merah

    pygame.draw.line(layar, warna, (15, 15), (lebar - 15, tinggi - 15), 15)


def restart():
    layar.fill ( hitam )
    draw_lines()
    pemain = 1
    for Baris in range(baris):
        for Kolom in range(kolom):
            papan[Baris][Kolom] = 0


#untuk mengulang atau selalu menampilkan layar
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] #x
            mouseY = event.pos[1] #y

            klik_baris = int(mouseY // 200)
            klik_kolom = int(mouseX // 200)

            if kosong(klik_baris, klik_kolom):
                if pemain == 1:
                    ngisi(klik_baris,klik_kolom, 1)
                    if cek(pemain):
                        game_over = True
                    pemain = 2

                elif pemain == 2:
                    ngisi(klik_baris, klik_kolom, 2)
                    if cek(pemain):
                        game_over = True
                    pemain = 1
                gambar()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                restart()
                game_over = False
                



    pygame.display.update()
