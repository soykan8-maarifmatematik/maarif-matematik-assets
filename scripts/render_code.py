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

        n427 = MathTex('4', '2', '7', color='#FFFFFF').scale(1.7).move_to(UP * 2.5 + LEFT * 0.5)
        n53 = MathTex('5', '3', color='#FFFFFF').scale(1.7).next_to(n427, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign_mult = MathTex('\\times', color='#FFFFFF').scale(1.7).next_to(n53, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(n53, DOWN, buff=0.2)

        res1 = MathTex('1', '2', '8', '1', color='#FFFFFF').scale(1.7).next_to(line1, DOWN, buff=0.4).align_to(n427[2], RIGHT)
        res2 = MathTex('2', '1', '3', '5', color='#FFFFFF').scale(1.7).next_to(res1, DOWN, buff=0.4).align_to(n427[1], RIGHT)

        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(2.0).next_to(res2, DOWN, buff=0.2).align_to(line1, RIGHT)
        sign_add = MathTex('+', color='#FFFFFF').scale(1.7).next_to(line2, LEFT, buff=0.3).shift(UP * 0.4)

        final_res = MathTex('2', '2', '6', '3', '1', color='#FFFF00').scale(1.8).next_to(line2, DOWN, buff=0.4).align_to(res1, RIGHT)

        c2 = MathTex('+2', color='#FFFF00').scale(0.8).next_to(n427[1], UP, buff=0.1)
        c3 = MathTex('+3', color='#00FFFF').scale(0.8).next_to(n427[1], UP, buff=0.1)
        c1 = MathTex('+1', color='#00FFFF').scale(0.8).next_to(n427[0], UP, buff=0.1)
        c1_add = MathTex('+1', color='#FFFF00').scale(0.8).next_to(res1[1], UP, buff=0.1)

        self.play(Write(header))
        self.play(Write(n427), Write(n53), Write(sign_mult))
        self.play(Create(line1))
        self.wait(1.0)

        # 1. Basamak (3)
        self.play(n53[1].animate.set_color('#FFFF00'))
        self.wait(2.0)
        self.play(Write(res1[3]), run_time=0.8)
        self.play(Write(c2), run_time=0.8)
        self.wait(2.5)
        self.play(Write(res1[2]), run_time=0.8)
        self.play(FadeOut(c2))
        self.wait(2.5)
        self.play(Write(res1[1]), run_time=0.8)
        self.play(Write(res1[0]), run_time=0.8)
        self.wait(3.5)

        # 2. Basamak (5)
        self.play(n53[1].animate.set_color('#FFFFFF'), n53[0].animate.set_color('#00FFFF'))
        self.wait(3.0)
        self.play(Write(res2[3]), run_time=0.8)
        self.play(Write(c3), run_time=0.8)
        self.wait(2.5)
        self.play(Write(res2[2]), run_time=0.8)
        self.play(FadeOut(c3), Write(c1))
        self.wait(2.5)
        self.play(Write(res2[1]), run_time=0.8)
        self.play(Write(res2[0]), run_time=0.8)
        self.play(FadeOut(c1))
        self.wait(3.5)
        self.play(n53[0].animate.set_color('#FFFFFF'))

        # Toplama İşlemi
        self.play(Create(line2), Write(sign_add))
        self.wait(2.5)
        
        # Birler
        self.play(Write(final_res[4]), run_time=0.8)
        self.wait(2.0)
        
        # Onlar
        self.play(Write(final_res[3]), run_time=0.8)
        self.play(Write(c1_add), run_time=0.8)
        self.wait(2.5)
        
        # Yüzler
        self.play(Write(final_res[2]), run_time=0.8)
        self.play(FadeOut(c1_add))
        self.wait(2.5)
        
        # Binler
        self.play(Write(final_res[1]), run_time=0.8)
        self.wait(2.0)
        
        # On Binler
        self.play(Write(final_res[0]), run_time=0.8)
        self.wait(3.5)
        
        self.wait(8.0)