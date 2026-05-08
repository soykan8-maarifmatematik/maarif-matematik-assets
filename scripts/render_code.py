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
        ).scale_to_fit_width(7.0).to_edge(UP, buff=0.8)

        n74 = MathTex('7', '4', color='#FFFFFF').scale(1.7).move_to(UP * 1.5 + LEFT * 0.5)
        n53 = MathTex('5', '3', color='#FFFFFF').scale(1.7).next_to(n74, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign = MathTex('\\times', color='#FFFFFF').scale(1.3).next_to(n53, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(n53, DOWN, buff=0.2)

        res1_2_1 = MathTex('2', color='#FFFFFF').scale(1.7).next_to(line1, DOWN, aligned_edge=RIGHT, buff=0.4)
        res1_2_2 = MathTex('2', color='#FFFFFF').scale(1.7).next_to(res1_2_1, LEFT, buff=0.5)
        res1_2_3 = MathTex('2', color='#FFFFFF').scale(1.7).next_to(res1_2_2, LEFT, buff=0.5)

        res2_0 = MathTex('0', color='#FFFFFF').scale(1.7).next_to(res1_2_2, DOWN, buff=0.45)
        res2_7 = MathTex('7', color='#FFFFFF').scale(1.7).next_to(res2_0, LEFT, buff=0.5)
        res2_3 = MathTex('3', color='#FFFFFF').scale(1.7).next_to(res2_7, LEFT, buff=0.5)

        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.8).next_to(res2_0, DOWN, aligned_edge=RIGHT, buff=0.2)
        final_res = MathTex('3', '9', '2', '2', color='#FFFF00').scale(2.1).next_to(line2, DOWN, aligned_edge=RIGHT, buff=0.4)

        carry_1 = MathTex('+1', color='#FFFF00').scale(0.8).next_to(n74[0], UP, buff=0.1)
        carry_2 = MathTex('+2', color='#00FFFF').scale(0.8).next_to(n74[0], UP, buff=0.1)

        self.play(Write(header))
        self.play(Write(n74), Write(n53), Write(sign))
        self.play(Create(line1))
        self.wait(3.5)
        
        self.play(n53[1].animate.set_color('#FFFF00'))
        self.wait(2.5)
        
        self.play(Write(res1_2_1), run_time=0.8) 
        self.wait(2.0)
        
        self.play(Write(carry_1), run_time=0.8)
        self.wait(3.5)
        
        self.play(Write(res1_2_2), run_time=0.8)
        self.play(Write(res1_2_3), run_time=0.8)
        self.wait(3.5)
        
        self.play(FadeOut(carry_1), n53[1].animate.set_color('#FFFFFF'))
        self.play(n53[0].animate.set_color('#00FFFF'))
        self.wait(2.5)
        
        self.play(Write(res2_0), run_time=0.8)
        self.wait(2.0)
        
        self.play(Write(carry_2), run_time=0.8)
        self.wait(3.5)
        
        self.play(Write(res2_7), run_time=0.8)
        self.play(Write(res2_3), run_time=0.8)
        self.wait(3.5)
        
        self.play(FadeOut(carry_2), n53[0].animate.set_color('#FFFFFF'))
        self.play(Create(line2))
        self.wait(2.0)
        
        self.play(Write(final_res[3]), run_time=0.8)
        self.play(Write(final_res[2]), run_time=0.8)
        self.play(Write(final_res[1]), run_time=0.8)
        self.play(Write(final_res[0]), run_time=0.8)
        
        self.wait(6.0)
