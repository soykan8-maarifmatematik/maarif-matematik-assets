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
        n524 = MathTex('5', '2', '4', color='#FFFFFF').scale(1.7).move_to(UP * 2.5 + LEFT * 0.5)
        n136 = MathTex('1', '3', '6', color='#FFFFFF').scale(1.7).next_to(n524, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign_mult = MathTex('\\times', color='#FFFFFF').scale(1.7).next_to(n136, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.7).next_to(n136, DOWN, buff=0.2)

        # Satırlar ve Hizalama
        res1 = MathTex('3', '1', '4', '4', color='#FFFFFF').scale(1.7).next_to(line1, DOWN, buff=0.4).align_to(n524[2], RIGHT)
        res2 = MathTex('1', '5', '7', '2', color='#FFFFFF').scale(1.7).next_to(res1, DOWN, buff=0.4).align_to(n524[1], RIGHT)
        res3 = MathTex('5', '2', '4', color='#FFFFFF').scale(1.7).next_to(res2, DOWN, buff=0.4).align_to(n524[0], RIGHT)

        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(2.2).next_to(res3, DOWN, buff=0.2).align_to(line1, RIGHT)
        sign_add = MathTex('+', color='#FFFFFF').scale(1.7).next_to(line2, LEFT, buff=0.3).shift(UP * 0.4)

        final_res = MathTex('7', '1', '2', '6', '4', color='#FFFF00').scale(1.8).next_to(line2, DOWN, buff=0.4).align_to(res1, RIGHT)

        # Eldeler (Carries)
        c2 = MathTex('+2', color='#FFFF00').scale(0.8).next_to(n524[1], UP, buff=0.1)
        c1_1 = MathTex('+1', color='#FFFF00').scale(0.8).next_to(n524[0], UP, buff=0.1)
        c1_2 = MathTex('+1', color='#00FFFF').scale(0.8).next_to(n524[1], UP, buff=0.1)

        self.play(Write(header))
        self.play(Write(n524), Write(n136), Write(sign_mult))
        self.play(Create(line1))

        # x6
        self.play(n136[2].animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(Write(res1[3]), run_time=0.8)
        self.play(Write(c2), run_time=0.8)
        self.wait(1.5)
        self.play(Write(res1[2]), run_time=0.8)
        self.play(FadeOut(c2), Write(c1_1))
        self.wait(1.5)
        self.play(Write(res1[1]), run_time=0.8)
        self.play(Write(res1[0]), run_time=0.8)
        self.play(FadeOut(c1_1))
        self.wait(3.5)

        # x3
        self.play(n136[2].animate.set_color('#FFFFFF'), n136[1].animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.play(Write(res2[3]), run_time=0.8)
        self.play(Write(c1_2), run_time=0.8)
        self.wait(1.5)
        self.play(Write(res2[2]), run_time=0.8)
        self.play(FadeOut(c1_2))
        self.wait(1.5)
        self.play(Write(res2[1]), run_time=0.8)
        self.play(Write(res2[0]), run_time=0.8)
        self.wait(3.5)

        # x1
        self.play(n136[1].animate.set_color('#FFFFFF'), n136[0].animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(Write(res3[2]), run_time=0.8)
        self.wait(1.0)
        self.play(Write(res3[1]), run_time=0.8)
        self.wait(1.0)
        self.play(Write(res3[0]), run_time=0.8)
        self.wait(3.5)

        # Toplama
        self.play(Create(line2), Write(sign_add))
        self.wait(1.0)
        for i in range(4, -1, -1):
            self.play(Write(final_res[i]), run_time=0.8)
            self.wait(1.5)
        
        self.wait(8.0)