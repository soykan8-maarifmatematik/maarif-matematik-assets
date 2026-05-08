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

        # Ana Sayılar (Sola Çekilmiş)
        n584 = MathTex('5', '8', '4', color='#FFFFFF').scale(1.7).move_to(UP * 2.5 + LEFT * 0.5)
        n46 = MathTex('4', '6', color='#FFFFFF').scale(1.7).next_to(n584, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign_mult = MathTex('\\times', color='#FFFFFF').scale(1.7).next_to(n46, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.7).next_to(n46, DOWN, buff=0.2)

        # Satırlar ve Milmetrik Hizalama
        res1 = MathTex('3', '5', '0', '4', color='#FFFFFF').scale(1.7).next_to(line1, DOWN, buff=0.4).align_to(n584[2], RIGHT)
        # 2. satırın birler basamağı, üstteki sayının onlar basamağının altına kilitlenir
        res2 = MathTex('2', '3', '3', '6', color='#FFFFFF').scale(1.7).next_to(res1, DOWN, buff=0.4).align_to(n584[1], RIGHT)

        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(2.0).next_to(res2, DOWN, buff=0.2).align_to(line1, RIGHT)
        # Toplama işareti sol üst boşluğa hizalı
        sign_add = MathTex('+', color='#FFFFFF').scale(1.7).next_to(line2, LEFT, buff=0.3).shift(UP * 0.4)

        final_res = MathTex('2', '6', '8', '6', '4', color='#FFFF00').scale(1.8).next_to(line2, DOWN, buff=0.4).align_to(res1, RIGHT)

        # Eldeler (Carries)
        c2 = MathTex('+2', color='#FFFF00').scale(0.8).next_to(n584[1], UP, buff=0.1)
        c5 = MathTex('+5', color='#FFFF00').scale(0.8).next_to(n584[0], UP, buff=0.1)
        c1 = MathTex('+1', color='#00FFFF').scale(0.8).next_to(n584[1], UP, buff=0.1)
        c3 = MathTex('+3', color='#00FFFF').scale(0.8).next_to(n584[0], UP, buff=0.1)

        self.play(Write(header))
        self.play(Write(n584), Write(n46), Write(sign_mult))
        self.play(Create(line1))

        # x6 İşlemi
        self.play(n46[1].animate.set_color('#FFFF00'))
        self.wait(3.5)
        self.play(Write(res1[3], run_time=0.8))
        self.play(Write(c2, run_time=0.8))
        self.wait(2.5)
        self.play(Write(res1[2], run_time=0.8))
        self.play(FadeOut(c2), Write(c5, run_time=0.8))
        self.wait(2.5)
        self.play(Write(res1[1], run_time=0.8), Write(res1[0], run_time=0.8))
        self.play(FadeOut(c5))
        self.wait(3.5)

        # x4 İşlemi
        self.play(n46[1].animate.set_color('#FFFFFF'), n46[0].animate.set_color('#00FFFF'))
        self.wait(3.5)
        self.play(Write(res2[3], run_time=0.8))
        self.play(Write(c1, run_time=0.8))
        self.wait(2.5)
        self.play(Write(res2[2], run_time=0.8))
        self.play(FadeOut(c1), Write(c3, run_time=0.8))
        self.wait(2.5)
        self.play(Write(res2[1], run_time=0.8), Write(res2[0], run_time=0.8))
        self.play(FadeOut(c3))
        self.wait(3.5)

        # Toplama İşlemi
        self.play(n46[0].animate.set_color('#FFFFFF'))
        self.play(Create(line2), Write(sign_add))
        self.wait(3.5)
        
        # Sağdan sola adım adım toplama
        for i in range(4, -1, -1):
            self.play(Write(final_res[i], run_time=0.8))
            self.wait(1.5)
        
        # Instagram Fix (Statik Bekleme)
        self.wait(8.0)