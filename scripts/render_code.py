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
        n427 = MathTex('4', '2', '7', color='#FFFFFF').scale(1.7).move_to(UP * 2.5 + LEFT * 0.5)
        n58 = MathTex('5', '8', color='#FFFFFF').scale(1.7).next_to(n427, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign_mult = MathTex('\\times', color='#FFFFFF').scale(1.3).next_to(n58, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(n58, DOWN, buff=0.2)

        # Satırlar
        res1 = MathTex('3', '4', '1', '6', color='#FFFFFF').scale(1.7).next_to(line1, DOWN, buff=0.4).align_to(n427[2], RIGHT)
        res2 = MathTex('2', '1', '3', '5', color='#FFFFFF').scale(1.7).next_to(res1, DOWN, buff=0.4).align_to(n427[1], RIGHT)

        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(2.0).next_to(res2, DOWN, buff=0.2).align_to(line1, RIGHT)
        sign_add = MathTex('+', color='#FFFFFF').scale(1.5).next_to(line2, LEFT, buff=0.3).shift(UP * 0.4)

        # Sonuç (24766)
        final_res = MathTex('2', '4', '7', '6', '6', color='#FFFF00').scale(1.8).next_to(line2, DOWN, buff=0.4).align_to(res1, RIGHT)

        self.play(Write(header))
        self.play(Write(n427), Write(n58), Write(sign_mult))
        self.play(Create(line1))
        self.wait(2.0)

        # Adım 1 (x8)
        self.play(n58[1].animate.set_color('#FFFF00'))
        self.wait(3.5)
        self.play(Write(res1[3]), run_time=0.8) # 6
        self.wait(2.5)
        self.play(Write(res1[2]), run_time=0.8) # 1
        self.wait(2.5)
        self.play(Write(res1[1]), Write(res1[0]), run_time=1.6) # 34
        self.wait(3.5)

        # Adım 2 (x5)
        self.play(n58[1].animate.set_color('#FFFFFF'), n58[0].animate.set_color('#00FFFF'))
        self.wait(3.5)
        self.play(Write(res2[3]), run_time=0.8) # 5
        self.wait(2.5)
        self.play(Write(res2[2]), run_time=0.8) # 3
        self.wait(2.5)
        self.play(Write(res2[1]), Write(res2[0]), run_time=1.6) # 21
        self.wait(3.5)
        self.play(n58[0].animate.set_color('#FFFFFF'))

        # Toplama
        self.play(Create(line2), Write(sign_add))
        self.wait(3.5)
        
        # Sağdan sola toplama işlemi
        for i in range(4, -1, -1):
            self.play(Write(final_res[i]), run_time=0.8)
            self.wait(2.0)
        
        self.wait(8.0)