from manim import *
import numpy as np

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # 1. BAŞLIK STANDARTI (V44)
        header = Paragraph(
            'İKİ BASAMAKLI SAYILARLA\nÇARPMA İŞLEMİ',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # 2. DİKEY İŞLEM KURALI VE MİLMETRİK YERLEŞİM
        # Üst Sayı (45)
        num1_4 = MathTex('4', color='#FFFFFF').scale(1.7)
        num1_5 = MathTex('5', color='#FFFFFF').scale(1.7)
        num1 = VGroup(num1_4, num1_5).arrange(RIGHT, buff=0.1).move_to(LEFT * 0.5 + UP * 2)

        # Alt Sayı (23)
        num2_2 = MathTex('2', color='#FFFFFF').scale(1.7)
        num2_3 = MathTex('3', color='#FFFFFF').scale(1.7)
        num2 = VGroup(num2_2, num2_3).arrange(RIGHT, buff=0.1).next_to(num1, DOWN, buff=0.5).align_to(num1, RIGHT)

        # Çarpma Çizgisi ve İşareti
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(num2, DOWN, buff=0.3).align_to(num1, RIGHT).shift(RIGHT * 0.5)
        times_sign = MathTex('\\times', color='#FFFFFF').scale(1.7).next_to(num2, LEFT, buff=0.5)

        # 1. Satır (135)
        row1_5 = MathTex('5', color='#FFFF00').scale(1.7).next_to(line1, DOWN, buff=0.3).align_to(num1_5, RIGHT)
        row1_3 = MathTex('3', color='#FFFF00').scale(1.7).next_to(row1_5, LEFT, buff=0.2)
        row1_1 = MathTex('1', color='#FFFF00').scale(1.7).next_to(row1_3, LEFT, buff=0.2)
        
        # 1. Elde
        carry1 = MathTex('1', color='#FFFF00').scale(0.8).next_to(num1_4, UP, buff=0.3)

        # 2. Satır (90) - MİLMETRİK HİZALAMA (0, 3'ün tam altına)
        row2_0 = MathTex('0', color='#00FFFF').scale(1.7).next_to(row1_5, DOWN, buff=0.5).align_to(row1_3, RIGHT)
        row2_9 = MathTex('9', color='#00FFFF').scale(1.7).next_to(row2_0, LEFT, buff=0.2)
        
        # 2. Elde
        carry2 = MathTex('1', color='#00FFFF').scale(0.8).next_to(num1_4, UP, buff=0.8)

        # Toplama Çizgisi ve İşareti (+ işareti kuralı)
        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(row2_0, DOWN, buff=0.3).align_to(line1, RIGHT)
        plus_sign = MathTex('+', color='#FFFFFF').scale(1.5).next_to(line2, LEFT, buff=0.2).shift(UP * 0.4)

        # Final Sonuç (1035)
        res_5 = MathTex('5', color='#FFFFFF').scale(1.8).next_to(line2, DOWN, buff=0.3).align_to(row1_5, RIGHT)
        res_3 = MathTex('3', color='#FFFFFF').scale(1.8).next_to(res_5, LEFT, buff=0.2)
        res_0 = MathTex('0', color='#FFFFFF').scale(1.8).next_to(res_3, LEFT, buff=0.2)
        res_1 = MathTex('1', color='#FFFFFF').scale(1.8).next_to(res_0, LEFT, buff=0.2)

        # --- KESİN SENKRON VE BLOK-KİLİT SİSTEMİ ---
        
        # Başlık ve Giriş
        self.play(Write(header))
        self.wait(3.0)

        # Sayıların Yazılması (Zincirleme Yasak, Her Rakam Sonrası Es)
        self.play(Write(num1_4))
        self.wait(1.0)
        self.play(Write(num1_5))
        self.wait(1.0)
        
        self.play(Write(num2_2))
        self.wait(1.0)
        self.play(Write(num2_3))
        self.wait(1.0)

        self.play(Write(times_sign))
        self.wait(1.0)
        self.play(Write(line1))
        self.wait(4.0) # Blok Sonu Bekleme

        # 1. Çarpma Bloğu (3 x 45)
        self.play(num2_3.animate.set_color('#FFFF00'), num1_5.animate.set_color('#FFFF00'))
        self.play(Write(row1_5))
        self.wait(1.0)
        self.play(Write(carry1))
        self.wait(4.0)

        self.play(num1_5.animate.set_color('#FFFFFF'), num1_4.animate.set_color('#FFFF00'))
        self.play(Write(row1_3))
        self.wait(1.0)
        self.play(Write(row1_1))
        self.wait(4.0)

        # Geçiş Sinyali
        self.play(num2_3.animate.set_color('#FFFFFF'), num1_4.animate.set_color('#FFFFFF'))
        self.wait(3.0) # Onlar basamağına geçiş beklemesi

        # 2. Çarpma Bloğu (2 x 45)
        self.play(num2_2.animate.set_color('#00FFFF'), num1_5.animate.set_color('#00FFFF'))
        self.play(Write(row2_0))
        self.wait(1.0)
        self.play(Write(carry2))
        self.wait(4.0)

        self.play(num1_5.animate.set_color('#FFFFFF'), num1_4.animate.set_color('#00FFFF'))
        self.play(Write(row2_9))
        self.wait(4.0)

        self.play(num2_2.animate.set_color('#FFFFFF'), num1_4.animate.set_color('#FFFFFF'))

        # Toplama Bloğu
        self.play(Write(line2))
        self.wait(1.0)
        self.play(Write(plus_sign))
        self.wait(4.0)

        # Final Sonuç Bloğu
        self.play(Write(res_5))
        self.wait(1.0)
        self.play(Write(res_3))
        self.wait(1.0)
        self.play(Write(res_0))
        self.wait(1.0)
        self.play(Write(res_1))
        self.wait(4.0)

        # INSTAGRAM/SHORTS FIX
        self.wait(8.0)