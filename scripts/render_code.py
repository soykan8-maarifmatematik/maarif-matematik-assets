from manim import *
import numpy as np

# DIKEY FORMAT KESIN KILIT (9:16)
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class KesirToplama(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # Başlık (V52 Agnostik Standart)
        header = Paragraph(
            'FARKLI PAYDALI\nKESİRLERİ TOPLAMA',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # Merkez Artı İşareti
        plus_sign = MathTex('+', color='#FFFFFF').scale(2.0).move_to(LEFT * 1.5)

        # 1. Kesir (1/2)
        f1_line = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(plus_sign, LEFT, buff=0.5)
        f1_pay = MathTex('1', color='#FFFFFF').scale(2.0).next_to(f1_line, UP, buff=0.3)
        f1_payda = MathTex('2', color='#FFFFFF').scale(2.0).next_to(f1_line, DOWN, buff=0.3)

        # 2. Kesir (1/3)
        f2_line = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(plus_sign, RIGHT, buff=0.5)
        f2_pay = MathTex('1', color='#FFFFFF').scale(2.0).next_to(f2_line, UP, buff=0.3)
        f2_payda = MathTex('3', color='#FFFFFF').scale(2.0).next_to(f2_line, DOWN, buff=0.3)

        # Genişletme Sayıları
        exp1 = MathTex('(3)', color='#FFFF00').scale(1.0).next_to(f1_payda, DOWN, buff=0.4)
        exp2 = MathTex('(2)', color='#00FFFF').scale(1.0).next_to(f2_payda, DOWN, buff=0.4)

        # Genişletilmiş 1. Kesir (3/6)
        nf1_pay = MathTex('3', color='#FFFF00').scale(2.0).move_to(f1_pay)
        nf1_payda = MathTex('6', color='#FFFF00').scale(2.0).move_to(f1_payda)

        # Genişletilmiş 2. Kesir (2/6)
        nf2_pay = MathTex('2', color='#00FFFF').scale(2.0).move_to(f2_pay)
        nf2_payda = MathTex('6', color='#00FFFF').scale(2.0).move_to(f2_payda)

        # Sonuç Grubu
        eq_sign = MathTex('=', color='#FFFFFF').scale(2.0).next_to(f2_line, RIGHT, buff=0.5)
        res_line = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.0).next_to(eq_sign, RIGHT, buff=0.5)
        res_pay = MathTex('5', color='#FFFFFF').scale(2.5).next_to(res_line, UP, buff=0.3)
        res_payda = MathTex('6', color='#FFFFFF').scale(2.5).next_to(res_line, DOWN, buff=0.3)

        # --- ANİMASYON AKIŞI (SENKRON KİLİTLİ) ---
        self.play(Write(header))
        self.wait(1.0)
        self.wait(5.0) # 'Merhaba, bugün Maarif Matematik ile...' bekle
        
        # ZİNCİRLEME YASAK KURALI İLE TEK TEK YAZIM
        self.play(Write(f1_pay))
        self.wait(1.0)
        self.play(Write(f1_line))
        self.wait(1.0)
        self.play(Write(f1_payda))
        self.wait(1.0)
        
        self.play(Write(plus_sign))
        self.wait(1.0)
        
        self.play(Write(f2_pay))
        self.wait(1.0)
        self.play(Write(f2_line))
        self.wait(1.0)
        self.play(Write(f2_payda))
        self.wait(1.0)
        self.wait(5.0) # 'Örneğimiz: bir bölü iki artı bir bölü üç...' bekle

        self.wait(3.0) # GEÇİŞ SİNYALİ

        self.play(Write(exp1))
        self.wait(1.0)
        self.play(Write(exp2))
        self.wait(1.0)
        self.wait(6.0) # 'İlk kesrimizi üç ile, ikinci kesrimizi iki ile genişletiyoruz...' bekle

        self.wait(3.0) # GEÇİŞ SİNYALİ

        # 1. Kesri Genişletme
        self.play(Transform(f1_pay, nf1_pay))
        self.wait(1.0)
        self.play(Transform(f1_payda, nf1_payda))
        self.wait(1.0)
        self.wait(6.0) # 'Birinci kesrin hem payını hem paydasını üç ile çarpalım...' bekle

        # 2. Kesri Genişletme
        self.play(Transform(f2_pay, nf2_pay))
        self.wait(1.0)
        self.play(Transform(f2_payda, nf2_payda))
        self.wait(1.0)
        self.wait(6.0) # 'Şimdi ikinci kesri iki ile çarpalım...' bekle

        self.wait(3.0) # GEÇİŞ SİNYALİ

        # Sonuç Adımı
        self.play(Write(eq_sign))
        self.wait(1.0)
        self.play(Write(res_line))
        self.wait(1.0)
        self.play(Write(res_pay))
        self.wait(1.0)
        self.wait(6.0) # 'Artık paydalarımız eşit. Payları topluyoruz...' bekle

        self.play(Write(res_payda))
        self.wait(1.0)
        self.wait(7.0) # 'Payda ise değişmez, altı olarak kalır...' bekle

        # INSTAGRAM/SHORTS FIX
        self.wait(8.0)