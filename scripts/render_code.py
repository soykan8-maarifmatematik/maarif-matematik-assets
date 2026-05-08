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
        n346 = MathTex('3', '4', '6', color='#FFFFFF').scale(1.7).move_to(UP * 2.5 + LEFT * 0.5)
        n215 = MathTex('2', '1', '5', color='#FFFFFF').scale(1.7).next_to(n346, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign_mult = MathTex('\\times', color='#FFFFFF').scale(1.3).next_to(n215, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(n215, DOWN, buff=0.2)

        # 1. Satır (1730)
        res1 = MathTex('1', '7', '3', '0', color='#FFFFFF').scale(1.5).next_to(line1, DOWN, buff=0.4)
        res1.align_to(n346[2], RIGHT)

        # 2. Satır (346) - Bir basamak kaydı (Onlar basamağı hizası)
        res2 = MathTex('3', '4', '6', color='#FFFFFF').scale(1.5).next_to(res1, DOWN, buff=0.4)
        res2.align_to(n346[1], RIGHT)

        # 3. Satır (692) - Bir basamak daha kaydı (Yüzler basamağı hizası)
        res3 = MathTex('6', '9', '2', color='#FFFFFF').scale(1.5).next_to(res2, DOWN, buff=0.4)
        res3.align_to(n346[0], RIGHT)

        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(2.0).next_to(res3, DOWN, buff=0.2)
        line2.align_to(line1, RIGHT)
        sign_add = MathTex('+', color='#FFFFFF').scale(1.5).next_to(line2, LEFT, buff=0.3).shift(UP * 0.4)

        # Final Sonuç (74390)
        final_res = MathTex('7', '4', '3', '9', '0', color='#FFFF00').scale(1.8).next_to(line2, DOWN, buff=0.4)
        final_res.align_to(res1, RIGHT)

        self.play(Write(header))
        self.play(Write(n346), Write(n215), Write(sign_mult))
        self.play(Create(line1))

        # Adım 1 (x5)
        self.play(n215[2].animate.set_color('#FFFF00'))
        self.wait(2.0)
        self.play(Write(res1[3]), run_time=0.8)
        self.play(Write(res1[2]), run_time=0.8)
        self.play(Write(res1[1]), run_time=0.8)
        self.play(Write(res1[0]), run_time=0.8)
        self.wait(3.5)

        # Adım 2 (x1)
        self.play(n215[2].animate.set_color('#FFFFFF'), n215[1].animate.set_color('#00FFFF'))
        self.wait(2.0)
        self.play(Write(res2[2]), run_time=0.8)
        self.play(Write(res2[1]), run_time=0.8)
        self.play(Write(res2[0]), run_time=0.8)
        self.wait(3.5)

        # Adım 3 (x2)
        self.play(n215[1].animate.set_color('#FFFFFF'), n215[0].animate.set_color('#FFFF00'))
        self.wait(2.0)
        self.play(Write(res3[2]), run_time=0.8)
        self.play(Write(res3[1]), run_time=0.8)
        self.play(Write(res3[0]), run_time=0.8)
        self.wait(3.5)
        self.play(n215[0].animate.set_color('#FFFFFF'))

        # Toplama İşlemi
        self.play(Create(line2), Write(sign_add))
        self.wait(1.5)
        for i in range(4, -1, -1):
            self.play(Write(final_res[i]), run_time=0.8)
            self.wait(1.2)
        
        self.wait(8.0)