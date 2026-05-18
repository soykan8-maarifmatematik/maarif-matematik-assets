from manim import *
import numpy as np

# DIKEY FORMAT KESIN KILIT (9:16)
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class KesirlerdeToplama(Scene):
    def construct(self):
        self.camera.background_color = '#000000'

        # Başlık (V52 Agnostik Standart)
        header = Paragraph(
            'KESİRLERDE\nTOPLAMA İŞLEMİ',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # --- İLK DENKLEM (Üst Kısım) ---
        # 1/2
        cizgi1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).move_to(UP * 2.0 + LEFT * 2.0)
        pay1 = MathTex('1', color='#FFFFFF').scale(2.0).next_to(cizgi1, UP, buff=0.3)
        payda1 = MathTex('2', color='#FFFFFF').scale(2.0).next_to(cizgi1, DOWN, buff=0.3)

        # +
        arti = MathTex('+', color='#FFFFFF').scale(2.0).next_to(cizgi1, RIGHT, buff=0.8)

        # 1/4
        cizgi2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(arti, RIGHT, buff=0.8)
        pay2 = MathTex('1', color='#FFFFFF').scale(2.0).next_to(cizgi2, UP, buff=0.3)
        payda2 = MathTex('4', color='#FFFFFF').scale(2.0).next_to(cizgi2, DOWN, buff=0.3)

        # Genişletme (2)
        genisletme_parantez_sol = MathTex('(', color='#FFFF00').scale(1.2).next_to(payda1, DOWN, buff=0.5).shift(LEFT*0.3)
        genisletme_sayi = MathTex('2', color='#FFFF00').scale(1.2).next_to(genisletme_parantez_sol, RIGHT, buff=0.1)
        genisletme_parantez_sag = MathTex(')', color='#FFFF00').scale(1.2).next_to(genisletme_sayi, RIGHT, buff=0.1)

        # Oklar
        ok_pay = CurvedArrow(genisletme_sayi.get_left() + LEFT*0.1, pay1.get_left() + LEFT*0.1, angle=PI/2, color='#FFFF00')
        ok_payda = CurvedArrow(genisletme_sayi.get_right() + RIGHT*0.1, payda1.get_right() + RIGHT*0.1, angle=-PI/2, color='#FFFF00')

        # --- İKİNCİ DENKLEM (Alt Kısım) ---
        # 2/4
        yeni_cizgi1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).move_to(DOWN * 2.5 + LEFT * 3.0)
        yeni_pay1 = MathTex('2', color='#FFFFFF').scale(2.0).next_to(yeni_cizgi1, UP, buff=0.3)
        yeni_payda1 = MathTex('4', color='#FFFFFF').scale(2.0).next_to(yeni_cizgi1, DOWN, buff=0.3)

        # +
        yeni_arti = MathTex('+', color='#FFFFFF').scale(2.0).next_to(yeni_cizgi1, RIGHT, buff=0.8)

        # 1/4
        yeni_cizgi2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(yeni_arti, RIGHT, buff=0.8)
        yeni_pay2 = MathTex('1', color='#FFFFFF').scale(2.0).next_to(yeni_cizgi2, UP, buff=0.3)
        yeni_payda2 = MathTex('4', color='#FFFFFF').scale(2.0).next_to(yeni_cizgi2, DOWN, buff=0.3)

        # =
        esittir = MathTex('=', color='#FFFFFF').scale(2.0).next_to(yeni_cizgi2, RIGHT, buff=0.8)

        # 3/4 (Sonuç - En büyük ölçek)
        sonuc_cizgi = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.0).next_to(esittir, RIGHT, buff=0.8)
        sonuc_pay = MathTex('3', color='#00FFFF').scale(2.5).next_to(sonuc_cizgi, UP, buff=0.3)
        sonuc_payda = MathTex('4', color='#FFFFFF').scale(2.5).next_to(sonuc_cizgi, DOWN, buff=0.3)

        # --- ANİMASYON AKIŞI (SENKRON KİLİTLİ VE ZİNCİRLEMESİZ) ---
        self.play(Write(header))
        self.wait(1.0)
        self.wait(4.5) # 'Merhaba, bugün Maarif Matematik ile...' girişini bekle

        self.play(Write(pay1))
        self.wait(1.0)
        self.play(Write(cizgi1))
        self.wait(1.0)
        self.play(Write(payda1))
        self.wait(1.0)

        self.play(Write(arti))
        self.wait(1.0)

        self.play(Write(pay2))
        self.wait(1.0)
        self.play(Write(cizgi2))
        self.wait(1.0)
        self.play(Write(payda2))
        self.wait(1.0)

        self.wait(4.5) # 'Örneğimiz: bir bölü iki artı bir bölü dört. Dikkatle izle.' bekle
        self.wait(3.0) # Geçiş

        self.play(Write(genisletme_parantez_sol))
        self.wait(1.0)
        self.play(Write(genisletme_sayi))
        self.wait(1.0)
        self.play(Write(genisletme_parantez_sag))
        self.wait(1.0)

        self.wait(4.5) # 'Toplama yapabilmek için paydaların aynı olması gerekir...' bekle

        self.play(Create(ok_pay))
        self.wait(1.0)
        self.wait(4.5) # 'İki kere bir, iki yapar. Yeni payımız iki oldu.' bekle

        self.play(Create(ok_payda))
        self.wait(1.0)
        self.wait(4.5) # 'İki kere iki, dört yapar. Yeni paydamız dört oldu.' bekle

        self.wait(3.0) # Geçiş

        self.play(Write(yeni_pay1))
        self.wait(1.0)
        self.play(Write(yeni_cizgi1))
        self.wait(1.0)
        self.play(Write(yeni_payda1))
        self.wait(1.0)

        self.play(Write(yeni_arti))
        self.wait(1.0)

        self.play(Write(yeni_pay2))
        self.wait(1.0)
        self.play(Write(yeni_cizgi2))
        self.wait(1.0)
        self.play(Write(yeni_payda2))
        self.wait(1.0)

        self.wait(4.5) # 'Şimdi işlemimiz iki bölü dört artı bir bölü dört haline geldi.' bekle
        self.wait(3.0) # Geçiş

        self.play(Write(esittir))
        self.wait(1.0)

        self.play(yeni_pay1.animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.play(yeni_pay2.animate.set_color('#00FFFF'))
        self.wait(1.0)

        self.wait(4.5) # 'Paydalar eşitlendiğine göre payları topluyoruz...' bekle

        self.play(Write(sonuc_pay))
        self.wait(1.0)
        self.play(Write(sonuc_cizgi))
        self.wait(1.0)
        self.play(Write(sonuc_payda))
        self.wait(1.0)

        self.wait(4.5) # 'Payda ise aynen kalır. Sonucumuz: üç bölü dört...' bekle

        self.wait(8.0) # Instagram/Shorts Fix statik bekleme
