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

        self.play(Write(header))
        self.wait(1)

        n74 = MathTex('7', '4', color='#FFFFFF').scale(1.7).move_to(UP * 1.5 + LEFT * 0.5)
        n53 = MathTex('5', '3', color='#FFFFFF').scale(1.7).next_to(n74, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign = MathTex('\\times', color='#FFFFFF').scale(1.3).next_to(n53, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(n53, DOWN, buff=0.3).align_to(n74, RIGHT).shift(RIGHT*0.2)

        self.play(
            Write(n74[0], run_time=0.8),
            Write(n74[1], run_time=0.8)
        )
        self.play(
            Write(n53[0], run_time=0.8),
            Write(n53[1], run_time=0.8)
        )
        self.play(Write(sign), Create(line1))
        self.wait(2)

        # Adım 1: 3 x 4 = 12
        self.play(n53[1].animate.set_color('#FFFF00'), n74[1].animate.set_color('#FFFF00'))
        self.wait(1)

        res1_birler = MathTex('2', color='#FFFFFF').scale(1.7).next_to(line1, DOWN, buff=0.5).align_to(n74[1], RIGHT)
        carry1 = MathTex('1', color='#FFFF00').scale(0.8).next_to(n74[0], UP, buff=0.4)

        self.play(Write(res1_birler, run_time=0.8))
        self.play(Write(carry1, run_time=0.8))
        self.play(n53[1].animate.set_color('#FFFFFF'), n74[1].animate.set_color('#FFFFFF'))
        self.wait(1)

        # Adım 2: 3 x 7 = 21, +1 = 22
        self.play(n53[1].animate.set_color('#FFFF00'), n74[0].animate.set_color('#FFFF00'))
        self.wait(1)

        res1_onlar = MathTex('2', color='#FFFFFF').scale(1.7).next_to(res1_birler, LEFT, buff=0.3)
        res1_yuzler = MathTex('2', color='#FFFFFF').scale(1.7).next_to(res1_onlar, LEFT, buff=0.3)

        self.play(Write(res1_onlar, run_time=0.8))
        self.play(Write(res1_yuzler, run_time=0.8))
        self.play(carry1.animate.set_opacity(0.3))
        self.play(n53[1].animate.set_color('#FFFFFF'), n74[0].animate.set_color('#FFFFFF'))
        
        self.wait(3.5)

        # Adım 3: 5 x 4 = 20
        self.play(n53[0].animate.set_color('#00FFFF'), n74[1].animate.set_color('#00FFFF'))
        self.wait(1)

        # MİLMETRİK HİZALAMA: 2. satırın ilk rakamı, 1. satırın onlar basamağının tam altına
        res2_birler = MathTex('0', color='#FFFFFF').scale(1.7).next_to(res1_onlar, DOWN, buff=0.5)
        carry2 = MathTex('2', color='#00FFFF').scale(0.8).next_to(carry1, UP, buff=0.2)

        self.play(Write(res2_birler, run_time=0.8))
        self.play(Write(carry2, run_time=0.8))
        self.play(n53[0].animate.set_color('#FFFFFF'), n74[1].animate.set_color('#FFFFFF'))
        self.wait(1)

        # Adım 4: 5 x 7 = 35, +2 = 37
        self.play(n53[0].animate.set_color('#00FFFF'), n74[0].animate.set_color('#00FFFF'))
        self.wait(1)

        res2_onlar = MathTex('7', color='#FFFFFF').scale(1.7).next_to(res2_birler, LEFT, buff=0.3)
        res2_yuzler = MathTex('3', color='#FFFFFF').scale(1.7).next_to(res2_onlar, LEFT, buff=0.3)

        self.play(Write(res2_onlar, run_time=0.8))
        self.play(Write(res2_yuzler, run_time=0.8))
        self.play(carry2.animate.set_opacity(0.3))
        self.play(n53[0].animate.set_color('#FFFFFF'), n74[0].animate.set_color('#FFFFFF'))
        
        self.wait(3.5)

        # Adım 5: Toplama İşlemi
        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(2.0).next_to(res2_birler, DOWN, buff=0.3).align_to(line1, RIGHT)
        plus = MathTex('+', color='#FFFFFF').scale(1.3).next_to(res2_yuzler, LEFT, buff=0.6)

        self.play(Create(line2), Write(plus))
        self.wait(1)

        fin_birler = MathTex('2', color='#FFFFFF').scale(2.1).next_to(line2, DOWN, buff=0.5).align_to(res1_birler, RIGHT)
        fin_onlar = MathTex('2', color='#FFFFFF').scale(2.1).next_to(fin_birler, LEFT, buff=0.3).align_to(res2_birler, RIGHT)
        fin_yuzler = MathTex('9', color='#FFFFFF').scale(2.1).next_to(fin_onlar, LEFT, buff=0.3).align_to(res2_onlar, RIGHT)
        fin_binler = MathTex('3', color='#FFFFFF').scale(2.1).next_to(fin_yuzler, LEFT, buff=0.3).align_to(res2_yuzler, RIGHT)

        self.play(Write(fin_birler, run_time=0.8))
        self.play(Write(fin_onlar, run_time=0.8))
        self.play(Write(fin_yuzler, run_time=0.8))
        self.play(Write(fin_binler, run_time=0.8))

        final_box = SurroundingRectangle(VGroup(fin_binler, fin_yuzler, fin_onlar, fin_birler), color='#FFFF00', buff=0.2)
        self.play(Create(final_box))
        
        self.wait(3.5)
