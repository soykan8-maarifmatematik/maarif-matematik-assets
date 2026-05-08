from manim import *
import numpy as np

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        header = Paragraph(
            'ADIM ADIM\nÇARPMA İŞLEMİ',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # Ana Sayılar
        n86 = MathTex('8', '6', color='#FFFFFF').scale(1.7).move_to(UP * 1.5 + LEFT * 0.5)
        n47 = MathTex('4', '7', color='#FFFFFF').scale(1.7).next_to(n86, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign = MathTex('x', color='#FFFFFF').scale(1.3).next_to(n47, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(n47, DOWN, buff=0.2)

        # 1. Satır (602)
        res1 = MathTex('6', '0', '2', color='#FFFFFF').scale(1.7).next_to(line1, DOWN, aligned_edge=RIGHT, buff=0.4)

        # 2. Satır (344) - Onlar basamağının altına hizalandı
        res2 = MathTex('3', '4', '4', color='#FFFFFF').scale(1.7).next_to(res1[1], DOWN, aligned_edge=CENTER, buff=0.45)

        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.8).next_to(res2, DOWN, buff=0.2)
        # Çizgiyi en sağa hizala
        line2.align_to(res1, RIGHT)

        # Final Sonuç Rakamları (4042) - Tek tek ve birler basamağı res1'in altına kilitli
        final_2 = MathTex('2', color='#FFFF00').scale(2.1).next_to(line2, DOWN, buff=0.4).align_to(res1, RIGHT)
        final_4_onlar = MathTex('4', color='#FFFF00').scale(2.1).next_to(final_2, LEFT, buff=0.6)
        final_0 = MathTex('0', color='#FFFF00').scale(2.1).next_to(final_4_onlar, LEFT, buff=0.6)
        final_4_binler = MathTex('4', color='#FFFF00').scale(2.1).next_to(final_0, LEFT, buff=0.6)

        # Eldeler
        carry_1 = MathTex('+4', color='#FFFF00').scale(0.8).next_to(n86[0], UP, buff=0.1)
        carry_2 = MathTex('+2', color='#00FFFF').scale(0.8).next_to(n86[0], UP, buff=0.1)
        carry_3 = MathTex('+1', color='#FFFF00').scale(0.8).next_to(res2[0], UP, buff=0.2) # Toplama eldesi

        self.play(Write(header))
        self.play(Write(n86), Write(n47), Write(sign))
        self.play(Create(line1))
        self.wait(1.0)
        
        # Çarpma 1 (7 ile)
        self.play(n47[1].animate.set_color('#FFFF00'))
        self.wait(1.5)
        self.play(Write(res1[2]), run_time=0.8)
        self.play(Write(carry_1))
        self.wait(2.5)
        self.play(Write(res1[0]), Write(res1[1]), run_time=1.5)
        self.wait(3.5)
        self.play(FadeOut(carry_1), n47[1].animate.set_color('#FFFFFF'))

        # Çarpma 2 (4 ile)
        self.play(n47[0].animate.set_color('#00FFFF'))
        self.wait(1.5)
        self.play(Write(res2[2]), run_time=0.8)
        self.play(Write(carry_2))
        self.wait(2.5)
        self.play(Write(res2[0]), Write(res2[1]), run_time=1.5)
        self.wait(3.5)
        self.play(FadeOut(carry_2), n47[0].animate.set_color('#FFFFFF'))

        # Toplama İşlemi
        self.play(Create(line2))
        self.wait(1.0)
        self.play(Write(final_2), run_time=0.8)
        self.wait(1.5)
        self.play(Write(final_4_onlar), run_time=0.8)
        self.wait(1.5)
        self.play(Write(final_0), run_time=0.8)
        self.play(Write(carry_3))
        self.wait(1.5)
        self.play(Write(final_4_binler), run_time=0.8)
        self.play(FadeOut(carry_3))
        self.wait(8.0)