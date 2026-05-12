from manim import *
import numpy as np

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class CarpmaIslemiScene(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # 1. GÖRSEL HİYERARŞİ VE MİLMETRİK YERLEŞİM
        header = Paragraph(
            'ÇARPMA İŞLEMİ',
            alignment='center',
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # Dikey İşlem Kuralı: Sola Çekik (LEFT * 0.5)
        num1_4 = MathTex('4', color='#FFFFFF').scale(1.7)
        num1_5 = MathTex('5', color='#FFFFFF').scale(1.7)
        num1_group = VGroup(num1_4, num1_5).arrange(RIGHT, buff=0.1).move_to(LEFT * 0.5 + UP * 2.0)

        num2_2 = MathTex('2', color='#FFFFFF').scale(1.7)
        num2_3 = MathTex('3', color='#FFFFFF').scale(1.7)
        num2_group = VGroup(num2_2, num2_3).arrange(RIGHT, buff=0.1).next_to(num1_group, DOWN, buff=0.5).align_to(num1_group, RIGHT)

        times = MathTex('\\times', color='#FFFFFF').scale(1.7).next_to(num2_group, LEFT, buff=0.5)
        line1 = Line(times.get_left(), num2_group.get_right(), color='#FFFFFF').next_to(num2_group, DOWN, buff=0.2)

        # 1. Satır (135) - Milmetrik Hizalama
        r1_5 = MathTex('5', color='#FFFFFF').scale(1.7).next_to(line1, DOWN, buff=0.5).align_to(num2_3, RIGHT)
        r1_3 = MathTex('3', color='#FFFFFF').scale(1.7).next_to(r1_5, LEFT, buff=0.2)
        r1_1 = MathTex('1', color='#FFFFFF').scale(1.7).next_to(r1_3, LEFT, buff=0.2)

        # Eldeler (Ölçek: 0.8)
        carry1 = MathTex('1', color='#FFFF00').scale(0.8).next_to(num1_4, UP, buff=0.3)
        carry2 = MathTex('1', color='#00FFFF').scale(0.8).next_to(carry1, UP, buff=0.1)

        # 2. Satır (90) - Milmetrik Hizalama (Onlar basamağının altı)
        r2_0 = MathTex('0', color='#FFFFFF').scale(1.7).next_to(r1_5, DOWN, buff=0.5).align_to(num2_2, RIGHT)
        r2_9 = MathTex('9', color='#FFFFFF').scale(1.7).next_to(r2_0, LEFT, buff=0.2)

        # Toplama Çizgisi ve İşareti (+ işareti kuralı)
        line2 = Line(r2_9.get_left() + LEFT * 0.5, r1_5.get_right(), color='#FFFFFF').next_to(r2_0, DOWN, buff=0.2)
        plus = MathTex('+', color='#FFFFFF').scale(1.7).next_to(line2, LEFT, buff=0.2).shift(UP * 0.4)

        # Final Sonuç (1035) - Ölçek: 1.8
        res_5 = MathTex('5', color='#FFFF00').scale(1.8).next_to(line2, DOWN, buff=0.5).align_to(r1_5, RIGHT)
        res_3 = MathTex('3', color='#FFFF00').scale(1.8).next_to(res_5, LEFT, buff=0.2)
        res_0 = MathTex('0', color='#FFFF00').scale(1.8).next_to(res_3, LEFT, buff=0.2)
        res_1 = MathTex('1', color='#FFFF00').scale(1.8).next_to(res_0, LEFT, buff=0.2)

        # --- 2. KESİN SENKRON VE BLOK-KİLİT SİSTEMİ ---
        
        self.play(Write(header))
        self.wait(1.0)

        # Zincirleme Yasak: Her rakam tek başına
        self.play(Write(num1_4))
        self.wait(1.0)
        self.play(Write(num1_5))
        self.wait(1.0)

        self.play(Write(num2_2))
        self.wait(1.0)
        self.play(Write(num2_3))
        self.wait(1.0)

        self.play(Write(times))
        self.wait(1.0)
        self.play(Write(line1))
        self.wait(4.0) # Blok Sonu Bekleme

        # 3 x 5 İşlemi
        self.play(num2_3.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(num1_5.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(Write(r1_5))
        self.wait(1.0)
        self.play(Write(carry1))
        self.wait(1.0)
        self.play(num1_5.animate.set_color('#FFFFFF'))
        self.wait(1.0)

        # 3 x 4 İşlemi
        self.play(num1_4.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(Write(r1_3))
        self.wait(1.0)
        self.play(Write(r1_1))
        self.wait(1.0)
        self.play(num1_4.animate.set_color('#FFFFFF'))
        self.wait(1.0)
        self.play(num2_3.animate.set_color('#FFFFFF'))
        self.wait(4.0) # Blok Sonu Bekleme

        # Geçiş Sinyali
        self.wait(3.0)

        # 2 x 5 İşlemi
        self.play(num2_2.animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.play(num1_5.animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.play(Write(r2_0))
        self.wait(1.0)
        self.play(Write(carry2))
        self.wait(1.0)
        self.play(num1_5.animate.set_color('#FFFFFF'))
        self.wait(1.0)

        # 2 x 4 İşlemi
        self.play(num1_4.animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.play(Write(r2_9))
        self.wait(1.0)
        self.play(num1_4.animate.set_color('#FFFFFF'))
        self.wait(1.0)
        self.play(num2_2.animate.set_color('#FFFFFF'))
        self.wait(4.0) # Blok Sonu Bekleme

        # Toplama İşlemi
        self.play(Write(plus))
        self.wait(1.0)
        self.play(Write(line2))
        self.wait(1.0)

        self.play(Write(res_5))
        self.wait(1.0)
        self.play(Write(res_3))
        self.wait(1.0)
        self.play(Write(res_0))
        self.wait(1.0)
        self.play(Write(res_1))
        self.wait(4.0) # Blok Sonu Bekleme

        # Instagram/Shorts Fix
        self.wait(8.0)