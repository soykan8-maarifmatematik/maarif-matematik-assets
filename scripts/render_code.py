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
            color=WHITE,
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.0)

        footer = Paragraph(
            'Maarif Matematik ile\nAdım Adım Öğren!',
            alignment='center',
            line_spacing=0.8,
            color=WHITE,
            weight=BOLD
        ).scale_to_fit_width(6.0).to_edge(DOWN, buff=1.2)

        n74 = MathTex('7', '4', color=WHITE).scale(1.7).move_to(UP * 1.8 + LEFT * 0.5)
        n53 = MathTex('5', '3', color=WHITE).scale(1.7).next_to(n74, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign = MathTex('\\times', color=WHITE).scale(1.3).next_to(n53, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color=WHITE).scale(1.5).next_to(n53, DOWN, buff=0.2)

        res1_2_1 = MathTex('2', color=WHITE).scale(1.7).next_to(line1, DOWN, aligned_edge=RIGHT, buff=0.4)
        res1_2_2 = MathTex('2', color=WHITE).scale(1.7).next_to(res1_2_1, LEFT, buff=0.5)
        res1_2_3 = MathTex('2', color=WHITE).scale(1.7).next_to(res1_2_2, LEFT, buff=0.5)

        res2_0 = MathTex('0', color=WHITE).scale(1.7).next_to(res1_2_2, DOWN, buff=0.45)
        res2_7 = MathTex('7', color=WHITE).scale(1.7).next_to(res2_0, LEFT, buff=0.5)
        res2_3 = MathTex('3', color=WHITE).scale(1.7).next_to(res2_7, LEFT, buff=0.5)

        line2 = Line(LEFT, RIGHT, color=WHITE).scale(1.8).next_to(res2_0, DOWN, buff=0.2)
        line2.align_to(line1, RIGHT)
        
        final_res = MathTex('3', '9', '2', '2', color=YELLOW).scale(2.1).next_to(line2, DOWN, buff=0.4)
        final_res.align_to(res1_2_1, RIGHT)

        carry_1 = MathTex('+1', color=YELLOW).scale(0.8).next_to(n74[0], UP, buff=0.1)
        carry_2 = MathTex('+2', color=CYAN).scale(0.8).next_to(n74[0], UP, buff=0.1)

        self.play(Write(header))
        self.play(Write(n74), Write(n53), Write(sign))
        self.play(Create(line1))
        
        self.play(n53[1].animate.set_color(YELLOW))
        self.play(Write(res1_2_1), run_time=0.5)
        self.play(Write(carry_1))
        self.wait(1.5)
        self.play(Write(res1_2_2), Write(res1_2_3), run_time=0.6)
        self.wait(2.2)
        self.play(FadeOut(carry_1), n53[1].animate.set_color(WHITE))

        self.play(n53[0].animate.set_color(CYAN))
        self.play(Write(res2_0), run_time=0.5)
        self.play(Write(carry_2))
        self.wait(1.5)
        self.play(Write(res2_7), Write(res2_3), run_time=0.6)
        self.wait(2.2)
        self.play(FadeOut(carry_2), n53[0].animate.set_color(WHITE))

        self.play(Create(line2))
        self.play(Write(final_res, run_time=1.5))
        self.play(Write(footer))
        self.wait(4.0)