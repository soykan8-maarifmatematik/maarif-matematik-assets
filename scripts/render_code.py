from manim import *
import numpy as np

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class DinamikKesirDonusum(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # BASLIK (Kilitli standartlara uygun)
        header = Paragraph(
            'TAM SAYILI KESRİ\nBİLEŞİK KESRE ÇEVİRME',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)
        
        self.play(Write(header))
        self.wait(1.0)
        self.wait(4.5) # Ses senkronu: Giris cumlesi

        # KESIR ELEMANLARI (Zincirleme yasak, her adim sonrasi 1.0s bekleme)
        tam = MathTex('2', color='#FFFFFF').scale(2.2).move_to(LEFT * 1.5)
        self.play(Write(tam))
        self.wait(1.0)
        
        cizgi = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(tam, RIGHT, buff=0.3)
        self.play(Create(cizgi))
        self.wait(1.0)
        
        pay = MathTex('3', color='#FFFFFF').scale(1.8).next_to(cizgi, UP, buff=0.3)
        self.play(Write(pay))
        self.wait(1.0)
        
        payda = MathTex('4', color='#FFFFFF').scale(1.8).next_to(cizgi, DOWN, buff=0.3)
        self.play(Write(payda))
        self.wait(1.0)
        self.wait(4.5) # Ses senkronu: Ornegimiz iki tam uc bolu dort...

        # GECIS SINYALI
        self.wait(3.0)

        # 1. ADIM: CARPMA ISLEMI (Vurgu 1: Sari #FFFF00)
        ok_alt = CurvedArrow(payda.get_bottom() + DOWN*0.1 + LEFT*0.2, tam.get_bottom() + DOWN*0.1 + RIGHT*0.2, angle=PI/2, color='#FFFF00')
        self.play(GrowArrow(ok_alt))
        self.wait(1.0)
        
        carp_is = MathTex('\\times', color='#FFFF00').scale(1.2).next_to(ok_alt, DOWN, buff=0.2)
        self.play(Write(carp_is))
        self.wait(1.0)
        
        self.play(payda.animate.set_color('#FFFF00'))
        self.wait(1.0)
        
        self.play(tam.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.wait(4.5) # Ses senkronu: Dort kere iki sekiz...

        # GECIS SINYALI
        self.wait(3.0)

        # 2. ADIM: TOPLAMA ISLEMI (Vurgu 2: Turkuaz #00FFFF)
        ok_ust = CurvedArrow(tam.get_top() + UP*0.1 + RIGHT*0.2, pay.get_top() + UP*0.1 + LEFT*0.2, angle=-PI/2, color='#00FFFF')
        self.play(GrowArrow(ok_ust))
        self.wait(1.0)
        
        topla_is = MathTex('+', color='#00FFFF').scale(1.2).next_to(ok_ust, UP, buff=0.2)
        self.play(Write(topla_is))
        self.wait(1.0)
        
        self.play(pay.animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.wait(4.5) # Ses senkronu: Sekiz uc daha on bir yapar...

        # GECIS SINYALI
        self.wait(3.0)

        # 3. ADIM: SONUC KESRI (En buyuk olcek: 2.5)
        esit = MathTex('=', color='#FFFFFF').scale(2.0).next_to(cizgi, RIGHT, buff=1.0)
        self.play(Write(esit))
        self.wait(1.0)
        
        f_cizgi = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.2).next_to(esit, RIGHT, buff=1.0)
        self.play(Create(f_cizgi))
        self.wait(1.0)
        
        f_pay = MathTex('11', color='#FFFF00').scale(2.5).next_to(f_cizgi, UP, buff=0.3)
        self.play(Write(f_pay))
        self.wait(1.0)
        self.wait(4.5) # Ses senkronu: Iste bu on bir sayisi yeni payimiz...
        
        f_payda = MathTex('4', color='#FFFFFF').scale(2.5).next_to(f_cizgi, DOWN, buff=0.3)
        self.play(Write(f_payda))
        self.wait(1.0)
        self.wait(4.5) # Ses senkronu: Payda ise hic degismiyor...

        self.wait(4.5) # Ses senkronu: Kapanis cumleleri...

        # SHORTS FIX: Kapanis statik bekleme
        self.wait(8.0)