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

        subtitle = Paragraph(
            'Matematiği Keşfet!',
            alignment='center',
            color='#FFFFFF'
        ).to_edge(DOWN, buff=1.2)

        n86_8 = MathTex('8', color='#FFFFFF').scale(1.7)
        n86_6 = MathTex('6', color='#FFFFFF').scale(1.7)
        n86 = VGroup(n86_8, n86_6).arrange(RIGHT, buff=0.5).move_to(UP * 1.8 + LEFT * 0.5)
        
        n47_4 = MathTex('4', color='#FFFFFF').scale(1.7).move_to(n86_8.get_center() + DOWN * 1.0)
        n47_7 = MathTex('7', color='#FFFFFF').scale(1.7).move_to(n86_6.get_center() + DOWN * 1.0)
        
        sign = MathTex('\\times', color='#FFFFFF').scale(1.3).next_to(n47_4, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(n47_4, DOWN, buff=0.3).shift(RIGHT * 0.5)

        res1_2 = MathTex('2', color='#FFFFFF').scale(1.7).move_to(n47_7.get_center() + DOWN * 1.2)
        res1_0 = MathTex('0', color='#FFFFFF').scale(1.7).move_to(n47_4.get_center() + DOWN * 1.2)
        res1_6 = MathTex('6', color='#FFFFFF').scale(1.7).next_to(res1_0, LEFT, buff=0.5)

        res2_4_right = MathTex('4', color='#FFFFFF').scale(1.7).move_to(res1_0.get_center() + DOWN * 1.0)
        res2_4_left = MathTex('4', color='#FFFFFF').scale(1.7).move_to(res1_6.get_center() + DOWN * 1.0)
        res2_3 = MathTex('3', color='#FFFFFF').scale(1.7).next_to(res2_4_left, LEFT, buff=0.5)

        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.8).next_to(res2_4_right, DOWN, buff=0.3).shift(LEFT * 0.5)

        final_2 = MathTex('2', color='#FFFF00').scale(2.1).match_x(res1_2).match_y(line2).shift(DOWN * 0.8)
        final_4 = MathTex('4', color='#FFFF00').scale(2.1).match_x(res2_4_right).match_y(final_2)
        final_0 = MathTex('0', color='#FFFF00').scale(2.1).match_x(res2_4_left).match_y(final_2)
        final_4_left = MathTex('4', color='#FFFF00').scale(2.1).match_x(res2_3).match_y(final_2)

        carry_1 = MathTex('+4', color='#FFFF00').scale(0.8).next_to(n86_8, UP, buff=0.3)
        carry_2 = MathTex('+2', color='#00FFFF').scale(0.8).next_to(n86_8, UP, buff=0.3)

        self.play(Write(header), Write(subtitle))
        self.play(Write(n86), Write(n47_4), Write(n47_7), Write(sign))
        self.play(Create(line1))
        self.wait(1.0)
        
        self.play(n47_7.animate.set_color('#FFFF00'), run_time=0.5)
        self.play(Write(res1_2), run_time=0.5)
        self.play(Write(carry_1), run_time=0.5)
        self.wait(2.2)
        
        self.play(Write(res1_0), run_time=0.4)
        self.play(Write(res1_6), run_time=0.4)
        self.wait(2.2)
        self.play(FadeOut(carry_1), n47_7.animate.set_color('#FFFFFF'))

        self.play(n47_4.animate.set_color('#00FFFF'), run_time=0.5)
        self.play(Write(res2_4_right), run_time=0.5)
        self.play(Write(carry_2), run_time=0.5)
        self.wait(2.2)
        
        self.play(Write(res2_4_left), run_time=0.4)
        self.play(Write(res2_3), run_time=0.4)
        self.wait(2.2)
        self.play(FadeOut(carry_2), n47_4.animate.set_color('#FFFFFF'))

        self.play(Create(line2))
        self.play(
            Write(final_4_left, run_time=0.5),
            Write(final_0, run_time=0.5),
            Write(final_4, run_time=0.5),
            Write(final_2, run_time=0.5)
        )
        self.wait(4.0)