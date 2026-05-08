from manim import *
import numpy as np

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # Başlık Yerleşimi
        header = Paragraph(
            'ADIM ADIM\nÇARPMA İŞLEMİ',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # Ana Sayılar
        n74 = MathTex('7', '4', color='#FFFFFF').scale(1.7).move_to(UP * 1.5 + LEFT * 0.5)
        n53 = MathTex('5', '3', color='#FFFFFF').scale(1.7).next_to(n74, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign_mult = MathTex('\\times', color='#FFFFFF').scale(1.3).next_to(n53, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(n53, DOWN, buff=0.2)

        # 1. Satır (222)
        res1 = MathTex('2', '2', '2', color='#FFFFFF').scale(1.7).next_to(line1, DOWN, aligned_edge=RIGHT, buff=0.4)

        # 2. Satır (370) - Basamak kaydırma milimetrik fix
        res2 = MathTex('3', '7', '0', color='#FFFFFF').scale(1.7).next_to(res1, DOWN, buff=0.45)
        res2.align_to(res1[1], RIGHT) 

        # Toplama Çizgisi ve Artı İşareti (+)
        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.8).next_to(res2, DOWN, buff=0.2)
        # Artı işareti toplama çizgisinin sol üstünde olacak şekilde dikey hizalandı
        sign_add = MathTex('+', color='#FFFFFF').scale(1.5).next_to(line2, LEFT, buff=0.3)
        sign_add.shift(UP * 0.15)

        # Final Sonuç Rakamları - KİLİTLİ
        final_res = VGroup(
            MathTex('3', color='#FFFF00').scale(2.1), # Binler
            MathTex('9', color='#FFFF00').scale(2.1), # Yüzler
            MathTex('2', color='#FFFF00').scale(2.1), # Onlar
            MathTex('2', color='#FFFF00').scale(2.1)  # Birler
        )
        
        # Sonuç basamaklarının milimetrik hizalaması
        final_res[3].next_to(line2, DOWN, buff=0.4).align_to(res1, RIGHT)
        final_res[2].next_to(final_res[3], LEFT, buff=0.6)
        final_res[1].next_to(final_res[2], LEFT, buff=0.6)
        final_res[0].next_to(final_res[1], LEFT, buff=0.6)

        # Eldeler
        carry_1 = MathTex('+1', color='#FFFF00').scale(0.8).next_to(n74[0], UP, buff=0.1)
        carry_2 = MathTex('+2', color='#00FFFF').scale(0.8).next_to(n74[0], UP, buff=0.1)

        # --- ANİMASYON AKIŞI ---
        self.play(Write(header))
        self.play(Write(n74), Write(n53), Write(sign_mult))
        self.play(Create(line1))
        
        # Çarpma 1
        self.play(n53[1].animate.set_color('#FFFF00'))
        self.wait(1.5)
        self.play(Write(res1[2]), run_time=0.8)
        self.play(Write(carry_1))
        self.wait(2.5)
        self.play(Write(res1[0]), Write(res1[1]), run_time=1.5)
        self.wait(3.5)
        self.play(FadeOut(carry_1), n53[1].animate.set_color('#FFFFFF'))

        # Çarpma 2
        self.play(n53[0].animate.set_color('#00FFFF'))
        self.wait(1.5)
        self.play(Write(res2[2]), run_time=0.9) 
        self.play(Write(carry_2))
        self.wait(2.5)
        self.play(Write(res2[0]), Write(res2[1]), run_time=1.5)
        self.wait(3.5)
        self.play(FadeOut(carry_2), n53[0].animate.set_color('#FFFFFF'))

        # Toplama ve Kapanış
        self.play(Create(line2), Write(sign_add))
        self.wait(1.0)
        self.play(Write(final_res[3]), run_time=0.8)
        self.wait(1.5)
        self.play(Write(final_res[2]), run_time=0.8)
        self.wait(1.5)
        self.play(Write(final_res[1]), run_time=0.8)
        self.wait(1.5)
        self.play(Write(final_res[0]), run_time=0.8)
        self.wait(8.0)