from manim import *
import numpy as np

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # Başlık Standartı (V44 Mühürlü)
        header = Paragraph(
            'ÇARPMA İŞLEMİ\nİKİ BASAMAKLI SAYILAR',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # Ana Sayılar (Her rakam ayrı nesne - Zincirleme Yasak)
        num1_3 = MathTex('3', color='#FFFFFF').scale(1.7)
        num1_4 = MathTex('4', color='#FFFFFF').scale(1.7)
        
        num2_2 = MathTex('2', color='#FFFFFF').scale(1.7)
        num2_5 = MathTex('5', color='#FFFFFF').scale(1.7)

        # Dikey İşlem Kuralı ve Milmetrik Hizalama
        num1_4.move_to(LEFT * 0.5 + UP * 2.0)
        num1_3.next_to(num1_4, LEFT, buff=0.5)

        num2_5.next_to(num1_4, DOWN, buff=0.5)
        num2_2.next_to(num2_5, LEFT, buff=0.5)
        num2_2.align_to(num1_3, RIGHT)

        times_sign = MathTex('\\times', color='#FFFFFF').scale(1.7).next_to(num2_2, LEFT, buff=0.5)
        line1 = Line(times_sign.get_left(), num1_4.get_right() + RIGHT*0.2, color='#FFFFFF').next_to(num2_5, DOWN, buff=0.3)

        # 1. Satır (170)
        r1_0 = MathTex('0', color='#FFFFFF').scale(1.7).next_to(line1, DOWN, buff=0.5).align_to(num2_5, RIGHT)
        r1_7 = MathTex('7', color='#FFFFFF').scale(1.7).next_to(r1_0, LEFT, buff=0.5).align_to(num2_2, RIGHT)
        r1_1 = MathTex('1', color='#FFFFFF').scale(1.7).next_to(r1_7, LEFT, buff=0.5)

        elde_2 = MathTex('2', color='#FFFF00').scale(0.8).next_to(num1_3, UP, buff=0.3)

        # 2. Satır (68)
        r2_8 = MathTex('8', color='#FFFFFF').scale(1.7).next_to(r1_7, DOWN, buff=0.5).align_to(r1_7, RIGHT)
        r2_6 = MathTex('6', color='#FFFFFF').scale(1.7).next_to(r2_8, LEFT, buff=0.5).align_to(r1_1, RIGHT)

        # Toplama Çizgisi ve İşareti
        line2 = Line(r1_1.get_left() + LEFT*0.5, r1_0.get_right() + RIGHT*0.2, color='#FFFFFF').next_to(r2_8, DOWN, buff=0.3)
        plus_sign = MathTex('+', color='#FFFFFF').scale(1.7).move_to(line2.get_left() + UP * 0.4 + RIGHT * 0.2)

        # Sonuç (850)
        res_0 = MathTex('0', color='#FFFF00').scale(1.8).next_to(line2, DOWN, buff=0.5).align_to(r1_0, RIGHT)
        res_5 = MathTex('5', color='#FFFF00').scale(1.8).next_to(res_0, LEFT, buff=0.5).align_to(r2_8, RIGHT)
        res_8 = MathTex('8', color='#FFFF00').scale(1.8).next_to(res_5, LEFT, buff=0.5).align_to(r2_6, RIGHT)

        elde_1 = MathTex('1', color='#00FFFF').scale(0.8).next_to(r1_1, LEFT, buff=0.3).shift(UP*0.2)

        # --- ANİMASYON AKIŞI ---
        self.play(Write(header))
        self.wait(3.0)

        self.play(Write(num1_3))
        self.wait(1.0)
        self.play(Write(num1_4))
        self.wait(1.0)

        self.play(Write(num2_2))
        self.wait(1.0)
        self.play(Write(num2_5))
        self.wait(1.0)

        self.play(Write(times_sign))
        self.wait(1.0)
        self.play(Write(line1))
        self.wait(4.0)

        # 5x4 = 20 İşlemi
        self.play(num2_5.animate.set_color('#FFFF00'), num1_4.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(Write(r1_0))
        self.wait(1.0)
        self.play(Write(elde_2))
        self.wait(1.0)
        self.play(num2_5.animate.set_color('#FFFFFF'), num1_4.animate.set_color('#FFFFFF'))
        self.wait(1.0)

        # 5x3 = 15 + 2 = 17 İşlemi
        self.play(num2_5.animate.set_color('#FFFF00'), num1_3.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(elde_2.animate.set_color('#FFFFFF'))
        self.wait(1.0)
        self.play(Write(r1_7))
        self.wait(1.0)
        self.play(Write(r1_1))
        self.wait(4.0)
        self.play(num2_5.animate.set_color('#FFFFFF'), num1_3.animate.set_color('#FFFFFF'))
        self.wait(1.0)

        # Geçiş Sinyali Beklemesi
        self.wait(3.0)

        # 2x4 = 8 İşlemi
        self.play(num2_2.animate.set_color('#00FFFF'), num1_4.animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.play(Write(r2_8))
        self.wait(1.0)
        self.play(num2_2.animate.set_color('#FFFFFF'), num1_4.animate.set_color('#FFFFFF'))
        self.wait(1.0)

        # 2x3 = 6 İşlemi
        self.play(num2_2.animate.set_color('#00FFFF'), num1_3.animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.play(Write(r2_6))
        self.wait(4.0)
        self.play(num2_2.animate.set_color('#FFFFFF'), num1_3.animate.set_color('#FFFFFF'))
        self.wait(1.0)

        # Toplama Aşaması
        self.play(Write(line2))
        self.wait(1.0)
        self.play(Write(plus_sign))
        self.wait(4.0)

        self.play(Write(res_0))
        self.wait(1.0)

        self.play(Write(res_5))
        self.wait(1.0)
        self.play(Write(elde_1))
        self.wait(1.0)

        self.play(Write(res_8))
        self.wait(4.0)

        # Kapanış Beklemesi (Shorts Fix)
        self.wait(8.0)