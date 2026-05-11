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

        n483 = MathTex('4', '8', '3', color='#FFFFFF').scale(1.7).move_to(UP * 2.5 + LEFT * 0.5)
        n256 = MathTex('2', '5', '6', color='#FFFFFF').scale(1.7).next_to(n483, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign_mult = MathTex('\\times', color='#FFFFFF').scale(1.3).next_to(n256, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(n256, DOWN, buff=0.2)

        res1 = MathTex('2', '8', '9', '8', color='#FFFFFF').scale(1.5).next_to(line1, DOWN, buff=0.4).align_to(n483[2], RIGHT)
        res2 = MathTex('2', '4', '1', '5', color='#FFFFFF').scale(1.5).next_to(res1, DOWN, buff=0.4).align_to(n483[1], RIGHT)
        res3 = MathTex('9', '6', '6', color='#FFFFFF').scale(1.5).next_to(res2, DOWN, buff=0.4).align_to(n483[0], RIGHT)

        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(2.0).next_to(res3, DOWN, buff=0.2).align_to(line1, RIGHT)
        sign_add = MathTex('+', color='#FFFFFF').scale(1.5).next_to(line2, LEFT, buff=0.3).shift(UP * 0.4)

        final_res = MathTex('1', '2', '3', '6', '4', '8', color='#FFFF00').scale(1.8).next_to(line2, DOWN, buff=0.4).align_to(res1, RIGHT)

        c1_1 = MathTex('+1', color='#FFFF00').scale(0.8).next_to(n483[1], UP, buff=0.1)
        c1_4 = MathTex('+4', color='#FFFF00').scale(0.8).next_to(n483[0], UP, buff=0.1)
        c2_1 = MathTex('+1', color='#00FFFF').scale(0.8).next_to(n483[1], UP, buff=0.1)
        c2_4 = MathTex('+4', color='#00FFFF').scale(0.8).next_to(n483[0], UP, buff=0.1)
        c3_1 = MathTex('+1', color='#FFFF00').scale(0.8).next_to(n483[0], UP, buff=0.1)

        self.play(Write(header))
        self.play(Write(n483))
        self.play(Write(n256))
        self.play(Write(sign_mult))
        self.play(Create(line1))

        # --- 1. BLOK ---
        self.play(n256[2].animate.set_color('#FFFF00'))
        self.wait(3.0)
        self.play(Write(res1[3], run_time=0.8))
        self.wait(0.5)
        self.play(Write(c1_1, run_time=0.8))
        self.wait(3.5)
        self.play(Write(res1[2], run_time=0.8))
        self.wait(0.5)
        self.play(FadeOut(c1_1))
        self.play(Write(c1_4, run_time=0.8))
        self.wait(3.5)
        self.play(Write(res1[1], run_time=0.8))
        self.wait(0.5)
        self.play(Write(res1[0], run_time=0.8))
        self.wait(0.5)
        self.play(FadeOut(c1_4))
        self.wait(5.0)

        # --- 2. BLOK ---
        self.play(n256[2].animate.set_color('#FFFFFF'))
        self.play(n256[1].animate.set_color('#00FFFF'))
        self.wait(3.0)
        self.play(Write(res2[3], run_time=0.8))
        self.wait(0.5)
        self.play(Write(c2_1, run_time=0.8))
        self.wait(3.5)
        self.play(Write(res2[2], run_time=0.8))
        self.wait(0.5)
        self.play(FadeOut(c2_1))
        self.play(Write(c2_4, run_time=0.8))
        self.wait(3.5)
        self.play(Write(res2[1], run_time=0.8))
        self.wait(0.5)
        self.play(Write(res2[0], run_time=0.8))
        self.wait(0.5)
        self.play(FadeOut(c2_4))
        self.wait(5.0)

        # --- 3. BLOK ---
        self.play(n256[1].animate.set_color('#FFFFFF'))
        self.play(n256[0].animate.set_color('#FFFF00'))
        self.wait(3.0)
        self.play(Write(res3[2], run_time=0.8))
        self.wait(0.5)
        self.wait(2.0)
        self.play(Write(res3[1], run_time=0.8))
        self.wait(0.5)
        self.play(Write(c3_1, run_time=0.8))
        self.wait(3.5)
        self.play(Write(res3[0], run_time=0.8))
        self.wait(0.5)
        self.play(FadeOut(c3_1))
        self.wait(5.0)
        self.play(n256[0].animate.set_color('#FFFFFF'))

        # --- TOPLAMA ---
        self.play(Create(line2))
        self.play(Write(sign_add))
        self.wait(3.0)
        
        self.play(Write(final_res[5], run_time=0.8))
        self.wait(0.5)
        self.wait(2.5)
        
        self.play(Write(final_res[4], run_time=0.8))
        self.wait(0.5)
        self.wait(2.5)
        
        self.play(Write(final_res[3], run_time=0.8))
        self.wait(0.5)
        self.wait(2.5)
        
        self.play(Write(final_res[2], run_time=0.8))
        self.wait(0.5)
        self.wait(2.5)
        
        self.play(Write(final_res[1], run_time=0.8))
        self.wait(0.5)
        self.wait(2.5)
        
        self.play(Write(final_res[0], run_time=0.8))
        self.wait(0.5)
        self.wait(4.0)
        
        self.wait(8.0)