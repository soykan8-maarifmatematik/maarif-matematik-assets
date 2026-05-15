from manim import *
import numpy as np

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class CarpmaIslemiScene(Scene):
    def construct(self):
        self.camera.background_color = '#000000'

        # 1. GÖRSEL HİYERARŞİ VE BAŞLIK STANDARTI
        header = Paragraph(
            'ÇARPMA İŞLEMİ\nİKİ BASAMAKLI SAYILAR',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # 2. DİKEY İŞLEM KURALI VE MİLMETRİK YERLEŞİM
        # X ekseninde LEFT * 0.5 merkez alınarak hizalama yapılıyor.
        center_x = -0.5
        spacing_x = 0.8
        
        # 34
        num1_3 = MathTex('3', color='#FFFFFF').scale(1.7).move_to(RIGHT * (center_x - spacing_x/2) + UP * 1.5)
        num1_4 = MathTex('4', color='#FFFFFF').scale(1.7).move_to(RIGHT * (center_x + spacing_x/2) + UP * 1.5)
        
        # 12
        num2_1 = MathTex('1', color='#FFFFFF').scale(1.7).move_to(RIGHT * (center_x - spacing_x/2) + UP * 0.3)
        num2_2 = MathTex('2', color='#FFFFFF').scale(1.7).move_to(RIGHT * (center_x + spacing_x/2) + UP * 0.3)
        
        times_sign = MathTex('\\times', color='#FFFFFF').scale(1.7).next_to(num2_1, LEFT, buff=0.6)
        line1 = Line(times_sign.get_left(), num2_2.get_right() + RIGHT*0.2, color='#FFFFFF').next_to(num2_1, DOWN, buff=0.3)
        
        # 68 (34 x 2)
        prod1_8 = MathTex('8', color='#FFFFFF').scale(1.7).move_to(RIGHT * (center_x + spacing_x/2) + DOWN * 0.9)
        prod1_6 = MathTex('6', color='#FFFFFF').scale(1.7).move_to(RIGHT * (center_x - spacing_x/2) + DOWN * 0.9)
        
        # 34 (34 x 1) - Kaydırma Kuralı (Onlar basamağının altına)
        prod2_4 = MathTex('4', color='#FFFFFF').scale(1.7).move_to(RIGHT * (center_x - spacing_x/2) + DOWN * 2.1)
        prod2_3 = MathTex('3', color='#FFFFFF').scale(1.7).move_to(RIGHT * (center_x - spacing_x*1.5) + DOWN * 2.1)
        
        # Toplama Çizgisi ve İşareti
        line2 = Line(prod2_3.get_left() + LEFT*0.5, prod1_8.get_right() + RIGHT*0.2, color='#FFFFFF').next_to(prod2_4, DOWN, buff=0.3)
        plus_sign = MathTex('+', color='#FFFFFF').scale(1.7).next_to(line2, LEFT, buff=0.2).shift(UP * 0.4)
        
        # Final Sonuç: 408
        res_8 = MathTex('8', color='#FFFF00').scale(1.8).move_to(RIGHT * (center_x + spacing_x/2) + DOWN * 3.7)
        res_0 = MathTex('0', color='#FFFF00').scale(1.8).move_to(RIGHT * (center_x - spacing_x/2) + DOWN * 3.7)
        res_4 = MathTex('4', color='#FFFF00').scale(1.8).move_to(RIGHT * (center_x - spacing_x*1.5) + DOWN * 3.7)
        
        # Elde
        carry_1 = MathTex('1', color='#FFFF00').scale(0.8).next_to(prod2_3, UP, buff=0.15).shift(LEFT * 0.2)

        # --- ANİMASYON (KİLİTLİ VE SABIRLI) ---
        self.play(Write(header))
        self.wait(3.0)
        
        self.play(Write(num1_3))
        self.wait(1.0)
        self.play(Write(num1_4))
        self.wait(1.0)
        
        self.play(Write(num2_1))
        self.wait(1.0)
        self.play(Write(num2_2))
        self.wait(1.0)
        
        self.play(Write(times_sign))
        self.wait(1.0)
        self.play(Write(line1))
        self.wait(4.0)
        
        # 2 x 4 İşlemi
        self.play(num2_2.animate.set_color('#FFFF00'), num1_4.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(Write(prod1_8))
        self.wait(1.0)
        self.play(num1_4.animate.set_color('#FFFFFF'))
        self.wait(1.0)
        
        # 2 x 3 İşlemi
        self.play(num1_3.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(Write(prod1_6))
        self.wait(1.0)
        self.play(num2_2.animate.set_color('#FFFFFF'), num1_3.animate.set_color('#FFFFFF'))
        self.wait(4.0)
        
        # Geçiş Sinyali (Onlar Basamağı)
        self.wait(3.0)
        
        # 1 x 4 İşlemi
        self.play(num2_1.animate.set_color('#00FFFF'), num1_4.animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.play(Write(prod2_4))
        self.wait(1.0)
        self.play(num1_4.animate.set_color('#FFFFFF'))
        self.wait(1.0)
        
        # 1 x 3 İşlemi
        self.play(num1_3.animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.play(Write(prod2_3))
        self.wait(1.0)
        self.play(num2_1.animate.set_color('#FFFFFF'), num1_3.animate.set_color('#FFFFFF'))
        self.wait(4.0)
        
        # Toplama Aşaması
        self.play(Write(plus_sign))
        self.wait(1.0)
        self.play(Write(line2))
        self.wait(4.0)
        
        self.play(Write(res_8))
        self.wait(1.0)
        
        self.play(Write(res_0))
        self.wait(1.0)
        self.play(Write(carry_1))
        self.wait(1.0)
        
        self.play(Write(res_4))
        self.wait(4.0)
        
        # Statik Kapanış
        self.wait(8.0)
