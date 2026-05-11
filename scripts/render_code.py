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
        n458 = MathTex('4', '5', '8', color='#FFFFFF').scale(1.7).move_to(UP * 2.5 + LEFT * 0.5)
        n327 = MathTex('3', '2', '7', color='#FFFFFF').scale(1.7).next_to(n458, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign_mult = MathTex('\\times', color='#FFFFFF').scale(1.3).next_to(n327, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(n327, DOWN, buff=0.2)

        # Satırlar
        res1 = MathTex('3', '2', '0', '6', color='#FFFFFF').scale(1.5).next_to(line1, DOWN, buff=0.4).align_to(n458[2], RIGHT)
        res2 = MathTex('9', '1', '6', color='#FFFFFF').scale(1.5).next_to(res1, DOWN, buff=0.4).align_to(n458[1], RIGHT)
        res3 = MathTex('1', '3', '7', '4', color='#FFFFFF').scale(1.5).next_to(res2, DOWN, buff=0.4).align_to(n458[0], RIGHT)

        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(2.0).next_to(res3, DOWN, buff=0.2).align_to(line1, RIGHT)
        sign_add = MathTex('+', color='#FFFFFF').scale(1.5).next_to(line2, LEFT, buff=0.3).shift(UP * 0.4)

        # Final Sonuç (V43 Kuralı: scale(1.8))
        final_res = MathTex('1', '4', '9', '7', '6', '6', color='#FFFF00').scale(1.8).next_to(line2, DOWN, buff=0.4).align_to(res1, RIGHT)

        # Eldeler (V43 Kuralı: scale(0.8))
        c5 = MathTex('+5', color='#FFFF00').scale(0.8).next_to(n458[1], UP, buff=0.1)
        c4 = MathTex('+4', color='#FFFF00').scale(0.8).next_to(n458[0], UP, buff=0.1)
        
        c1_1 = MathTex('+1', color='#00FFFF').scale(0.8).next_to(n458[1], UP, buff=0.1)
        c1_2 = MathTex('+1', color='#00FFFF').scale(0.8).next_to(n458[0], UP, buff=0.1)
        
        c2 = MathTex('+2', color='#FFFF00').scale(0.8).next_to(n458[1], UP, buff=0.1)
        c1_3 = MathTex('+1', color='#FFFF00').scale(0.8).next_to(n458[0], UP, buff=0.1)

        self.play(Write(header))
        self.play(Write(n458), Write(n327), Write(sign_mult))
        self.play(Create(line1))

        # --- 1. BLOK: YEDİ İLE ÇARPMA ---
        self.play(n327[2].animate.set_color('#FFFF00'))
        self.wait(3.5)
        self.play(Write(res1[3]), Write(c5), run_time=0.8)
        self.wait(3.5)
        self.play(Write(res1[2]), FadeOut(c5), Write(c4), run_time=0.8)
        self.wait(3.5)
        self.play(Write(res1[1]), Write(res1[0]), run_time=0.8)
        self.play(FadeOut(c4))
        self.wait(3.5)

        # --- 2. BLOK: İKİ İLE ÇARPMA ---
        self.play(n327[2].animate.set_color('#FFFFFF'), n327[1].animate.set_color('#00FFFF'))
        self.wait(3.5)
        self.play(Write(res2[2]), Write(c1_1), run_time=0.8)
        self.wait(3.5)
        self.play(Write(res2[1]), FadeOut(c1_1), Write(c1_2), run_time=0.8)
        self.wait(3.5)
        self.play(Write(res2[0]), FadeOut(c1_2), run_time=0.8)
        self.wait(3.5)

        # --- 3. BLOK: ÜÇ İLE ÇARPMA ---
        self.play(n327[1].animate.set_color('#FFFFFF'), n327[0].animate.set_color('#FFFF00'))
        self.wait(3.5)
        self.play(Write(res3[3]), Write(c2), run_time=0.8)
        self.wait(3.5)
        self.play(Write(res3[2]), FadeOut(c2), Write(c1_3), run_time=0.8)
        self.wait(3.5)
        self.play(Write(res3[1]), Write(res3[0]), FadeOut(c1_3), run_time=0.8)
        self.wait(3.5)
        self.play(n327[0].animate.set_color('#FFFFFF'))

        # --- TOPLAMA AŞAMASI ---
        self.play(Create(line2), Write(sign_add))
        self.wait(3.5)
        for i in range(5, -1, -1):
            self.play(Write(final_res[i]), run_time=0.8)
            self.wait(3.5)
        
        self.wait(8.0)