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

        n85 = MathTex('8', '5', color='#FFFFFF').scale(1.7).move_to(UP * 1.5 + LEFT * 0.5)
        n34 = MathTex('3', '4', color='#FFFFFF').scale(1.7).next_to(n85, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign = MathTex('\\times', color='#FFFFFF').scale(1.3).next_to(n34, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(n34, DOWN, buff=0.2)

        # 1. Satır: 340
        res1_0 = MathTex('0', color='#FFFFFF').scale(1.7).next_to(line1, DOWN, aligned_edge=RIGHT, buff=0.4)
        res1_4 = MathTex('4', color='#FFFFFF').scale(1.7).next_to(res1_0, LEFT, buff=0.5)
        res1_3 = MathTex('3', color='#FFFFFF').scale(1.7).next_to(res1_4, LEFT, buff=0.5)

        # 2. Satır: 255 (İlk rakam res1_4'ün tam altına hizalanır)
        res2_5_1 = MathTex('5', color='#FFFFFF').scale(1.7).next_to(res1_4, DOWN, buff=0.45)
        res2_5_2 = MathTex('5', color='#FFFFFF').scale(1.7).next_to(res2_5_1, LEFT, buff=0.5)
        res2_2 = MathTex('2', color='#FFFFFF').scale(1.7).next_to(res2_5_2, LEFT, buff=0.5)

        # Toplam Çizgisi ve Sonuç: 2890
        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.8).next_to(res2_5_1, DOWN, buff=0.2).align_to(res1_0, RIGHT)
        final_res = MathTex('2', '8', '9', '0', color='#FFFF00').scale(2.1).next_to(line2, DOWN, buff=0.4).align_to(res1_0, RIGHT)

        # Eldeler
        carry_1 = MathTex('+2', color='#FFFF00').scale(0.8).next_to(n85[0], UP, buff=0.1)
        carry_2 = MathTex('+1', color='#00FFFF').scale(0.8).next_to(n85[0], UP, buff=0.1)

        # --- ANİMASYON BAŞLANGICI ---
        self.play(Write(header))
        self.play(Write(n85), Write(n34), Write(sign))
        self.play(Create(line1))
        
        # 1. Satır İşlemleri
        self.play(n34[1].animate.set_color('#FFFF00'))
        self.wait(2.0) # 'Dört ile başlıyoruz' beklemesi
        self.play(Write(res1_0), run_time=0.9) 
        self.play(Write(carry_1), run_time=0.8)
        self.wait(3.5) # 'Dört kere sekiz otuz iki' beklemesi
        self.play(Write(res1_4, run_time=0.9), Write(res1_3, run_time=0.9))
        self.wait(3.5) # 'İlk satırımız bitti' beklemesi
        self.play(FadeOut(carry_1), n34[1].animate.set_color('#FFFFFF'))

        # 2. Satır İşlemleri
        self.play(n34[0].animate.set_color('#00FFFF'))
        self.wait(2.0)
        self.play(Write(res2_5_1), run_time=0.9)
        self.play(Write(carry_2), run_time=0.8)
        self.wait(3.5) # 'Üç kere sekiz yirmi dört' beklemesi
        self.play(Write(res2_5_2, run_time=0.9), Write(res2_2, run_time=0.9))
        self.wait(3.5) # 'İkinci satırımız da hazır' beklemesi
        self.play(FadeOut(carry_2), n34[0].animate.set_color('#FFFFFF'))

        # Toplama ve Kapanış
        self.play(Create(line2))
        self.play(Write(final_res, run_time=2.5))
        self.wait(5.0)