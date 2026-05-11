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

        # Ana Sayılar (534 x 246)
        n534 = MathTex('5', '3', '4', color='#FFFFFF').scale(1.7).move_to(UP * 2.5 + LEFT * 0.5)
        n246 = MathTex('2', '4', '6', color='#FFFFFF').scale(1.7).next_to(n534, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign_mult = MathTex('\\times', color='#FFFFFF').scale(1.3).next_to(n246, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(n246, DOWN, buff=0.2)

        # Satırlar ve Hizalama (Merdiven Düzeni)
        res1 = MathTex('3', '2', '0', '4', color='#FFFFFF').scale(1.5).next_to(line1, DOWN, buff=0.4).align_to(n534[2], RIGHT)
        res2 = MathTex('2', '1', '3', '6', color='#FFFFFF').scale(1.5).next_to(res1, DOWN, buff=0.4).align_to(n534[1], RIGHT)
        res3 = MathTex('1', '0', '6', '8', color='#FFFFFF').scale(1.5).next_to(res2, DOWN, buff=0.4).align_to(n534[0], RIGHT)

        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(2.0).next_to(res3, DOWN, buff=0.2).align_to(line1, RIGHT)
        sign_add = MathTex('+', color='#FFFFFF').scale(1.5).next_to(line2, LEFT, buff=0.3).shift(UP * 0.4)

        final_res = MathTex('1', '3', '1', '3', '6', '4', color='#FFFF00').scale(1.8).next_to(line2, DOWN, buff=0.4).align_to(res1, RIGHT)

        # Eldeler (Carries)
        c2_1 = MathTex('+2', color='#FFFF00').scale(0.8).next_to(n534[1], UP, buff=0.1)
        c2_2 = MathTex('+2', color='#FFFF00').scale(0.8).next_to(n534[0], UP, buff=0.1)
        c1_1 = MathTex('+1', color='#00FFFF').scale(0.8).next_to(n534[1], UP, buff=0.1)
        c1_2 = MathTex('+1', color='#00FFFF').scale(0.8).next_to(n534[0], UP, buff=0.1)

        self.play(Write(header))
        self.play(Write(n534), Write(n246), Write(sign_mult))
        self.play(Create(line1))

        # 1. Basamak: x6 (Tam Senkron)
        self.play(n246[2].animate.set_color('#FFFF00'))
        self.wait(3.5)
        self.play(Write(res1[3]), run_time=0.8) # 4
        self.play(Write(c2_1))
        self.wait(4.0)
        self.play(Write(res1[2]), run_time=0.8) # 0
        self.play(FadeOut(c2_1), Write(c2_2))
        self.wait(3.5)
        self.play(Write(res1[1]), Write(res1[0]), run_time=1.5) # 32
        self.play(FadeOut(c2_2))
        self.wait(3.0)

        # 2. Basamak: x4
        self.play(n246[2].animate.set_color('#FFFFFF'), n246[1].animate.set_color('#00FFFF'))
        self.wait(3.5)
        self.play(Write(res2[3]), run_time=0.8) # 6
        self.play(Write(c1_1))
        self.wait(3.5)
        self.play(Write(res2[2]), run_time=0.8) # 3
        self.play(FadeOut(c1_1), Write(c1_2))
        self.wait(3.5)
        self.play(Write(res2[1]), Write(res2[0]), run_time=1.5) # 21
        self.play(FadeOut(c1_2))
        self.wait(3.0)

        # 3. Basamak: x2
        self.play(n246[1].animate.set_color('#FFFFFF'), n246[0].animate.set_color('#FFFF00'))
        self.wait(3.5)
        self.play(Write(res3[3]), run_time=0.8) # 8
        self.wait(3.0)
        self.play(Write(res3[2]), run_time=0.8) # 6
        self.wait(3.0)
        self.play(Write(res3[1]), Write(res3[0]), run_time=1.5) # 10
        self.wait(3.0)
        self.play(n246[0].animate.set_color('#FFFFFF'))

        # Toplama Aşaması
        self.play(Create(line2), Write(sign_add))
        self.wait(2.5)
        for i in range(5, -1, -1):
            self.play(Write(final_res[i]), run_time=0.9)
            self.wait(2.0)
        
        self.wait(8.0)