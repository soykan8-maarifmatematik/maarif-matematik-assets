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
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.0)

        n86 = MathTex('8', '6', color='#FFFFFF').scale(1.7).move_to(UP * 1.8 + LEFT * 0.5)
        n47 = MathTex('4', '7', color='#FFFFFF').scale(1.7).next_to(n86, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign = MathTex('\\times', color='#FFFFFF').scale(1.3).next_to(n47, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(n47, DOWN, buff=0.2)

        res1_2 = MathTex('2', color='#FFFFFF').scale(1.7).next_to(line1, DOWN, aligned_edge=RIGHT, buff=0.4)
        res1_0 = MathTex('0', color='#FFFFFF').scale(1.7).next_to(res1_2, LEFT, buff=0.5)
        res1_6 = MathTex('6', color='#FFFFFF').scale(1.7).next_to(res1_0, LEFT, buff=0.5)

        res2_4_1 = MathTex('4', color='#FFFFFF').scale(1.7).next_to(res1_2, DOWN, buff=0.45).shift(LEFT * 0.8)
        res2_4_2 = MathTex('4', color='#FFFFFF').scale(1.7).next_to(res2_4_1, LEFT, buff=0.5)
        res2_3 = MathTex('3', color='#FFFFFF').scale(1.7).next_to(res2_4_2, LEFT, buff=0.5)

        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.8).next_to(res2_4_1, DOWN, aligned_edge=RIGHT, buff=0.2).shift(RIGHT * 0.8)
        final_res = MathTex('4', '0', '4', '2', color='#FFFF00').scale(2.1).next_to(line2, DOWN, aligned_edge=RIGHT, buff=0.4)

        carry_1 = MathTex('+4', color='#FFFF00').scale(0.8).next_to(n86[0], UP, buff=0.1)
        carry_2 = MathTex('+2', color='#00FFFF').scale(0.8).next_to(n86[0], UP, buff=0.1)

        self.play(Write(header))
        self.play(Write(n86), Write(n47), Write(sign))
        self.play(Create(line1))
        
        # 1. BLOK ANİMASYONU
        self.play(n47[1].animate.set_color('#FFFF00'))
        self.play(Write(res1_2), run_time=0.6)
        self.play(Write(carry_1))
        self.wait(1.0)
        self.play(Write(res1_0), Write(res1_6), run_time=1.2)
        self.wait(2.2)
        self.play(FadeOut(carry_1), n47[1].animate.set_color('#FFFFFF'))

        # 2. BLOK ANİMASYONU
        self.play(n47[0].animate.set_color('#00FFFF'))
        self.play(Write(res2_4_1), run_time=0.6)
        self.play(Write(carry_2))
        self.wait(1.0)
        self.play(Write(res2_4_2), Write(res2_3), run_time=1.2)
        self.wait(2.2)
        self.play(FadeOut(carry_2), n47[0].animate.set_color('#FFFFFF'))

        # TOPLAMA VE SONUÇ
        self.play(Create(line2))
        self.play(Write(final_res, run_time=2.0))
        self.wait(4.0)