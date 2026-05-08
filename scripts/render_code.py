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

        n86 = MathTex('8', '6', color='#FFFFFF').scale(1.7).move_to(UP * 1.5 + LEFT * 0.5)
        n47 = MathTex('4', '7', color='#FFFFFF').scale(1.7).next_to(n86, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign_mult = MathTex('\\times', color='#FFFFFF').scale(1.3).next_to(n47, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(n47, DOWN, buff=0.2)

        res1 = MathTex('6', '0', '2', color='#FFFFFF').scale(1.7).next_to(line1, DOWN, buff=0.4)
        res1.align_to(n86, RIGHT)
        
        res2 = MathTex('3', '4', '4', color='#FFFFFF').scale(1.7).next_to(res1, DOWN, buff=0.45)
        res2.align_to(res1[1], RIGHT)

        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.8).next_to(res2, DOWN, buff=0.2)
        sign_add = MathTex('+', color='#FFFFFF').scale(1.5).next_to(line2, LEFT, buff=0.3)

        final_res = MathTex('4', '0', '4', '2', color='#FFFF00').scale(2.1).next_to(line2, DOWN, buff=0.4)
        final_res.align_to(res1, RIGHT)

        carry_1 = MathTex('+4', color='#FFFF00').scale(0.8).next_to(n86[0], UP, buff=0.1)
        carry_2 = MathTex('+2', color='#00FFFF').scale(0.8).next_to(n86[0], UP, buff=0.1)
        carry_add = MathTex('+1', color='#FFFF00').scale(0.8).next_to(res2[0], UP, buff=0.1)

        self.play(Write(header))
        self.play(Write(n86), Write(n47), Write(sign_mult))
        self.play(Create(line1))
        self.wait(1.0)
        
        self.play(n47[1].animate.set_color('#FFFF00'))
        self.wait(1.5)
        self.play(Write(res1[2]), run_time=0.8)
        self.play(Write(carry_1), run_time=0.8)
        self.wait(2.5)
        self.play(Write(res1[0]), Write(res1[1]), run_time=1.5)
        self.wait(3.5)
        self.play(FadeOut(carry_1), n47[1].animate.set_color('#FFFFFF'))

        self.play(n47[0].animate.set_color('#00FFFF'))
        self.wait(1.5)
        self.play(Write(res2[2]), run_time=0.8)
        self.play(Write(carry_2), run_time=0.8)
        self.wait(2.5)
        self.play(Write(res2[0]), Write(res2[1]), run_time=1.5)
        self.wait(3.5)
        self.play(FadeOut(carry_2), n47[0].animate.set_color('#FFFFFF'))

        self.play(Create(line2), Write(sign_add))
        self.wait(1.5)
        
        self.play(Write(final_res[3]), run_time=0.8)
        self.wait(1.5)
        self.play(Write(final_res[2]), run_time=0.8)
        self.wait(1.5)
        self.play(Write(final_res[1]), run_time=0.8)
        self.play(Write(carry_add), run_time=0.8)
        self.wait(1.5)
        self.play(Write(final_res[0]), run_time=0.8)
        self.play(FadeOut(carry_add))
        self.wait(8.0)