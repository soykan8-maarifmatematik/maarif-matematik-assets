from manim import *
import numpy as np

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # Başlık 3mm aşağı kaydırıldı (buff=1.1) ve taşma engellendi
        header = Paragraph(
            'ADIM ADIM\nÇARPMA İŞLEMİ',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # Dikey İşlem Kuralı: Merkeze/sola çek (LEFT * 0.5)
        n68 = MathTex('6', '8', color='#FFFFFF').scale(1.7).move_to(UP * 1.5 + LEFT * 0.5)
        n35 = MathTex('3', '5', color='#FFFFFF').scale(1.7).next_to(n68, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign = MathTex('\\times', color='#FFFFFF').scale(1.3).next_to(n35, LEFT, buff=0.6)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(n35, DOWN, buff=0.2)

        # 1. Satır (340)
        res1_0 = MathTex('0', color='#FFFFFF').scale(1.7).next_to(line1, DOWN, aligned_edge=RIGHT, buff=0.4)
        res1_4 = MathTex('4', color='#FFFFFF').scale(1.7).next_to(res1_0, LEFT, buff=0.5)
        res1_3 = MathTex('3', color='#FFFFFF').scale(1.7).next_to(res1_4, LEFT, buff=0.5)

        # 2. Satır (204) - Milimetrik Hizalama: 1. satırın onlar basamağının tam altı
        res2_4 = MathTex('4', color='#FFFFFF').scale(1.7).next_to(res1_4, DOWN, buff=0.45)
        res2_0 = MathTex('0', color='#FFFFFF').scale(1.7).next_to(res2_4, LEFT, buff=0.5)
        res2_2 = MathTex('2', color='#FFFFFF').scale(1.7).next_to(res2_0, LEFT, buff=0.5)

        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.8).next_to(res2_4, DOWN, aligned_edge=RIGHT, buff=0.2)

        # Toplama Sonucu (2380) - Adım adım gelecek
        final_0 = MathTex('0', color='#FFFF00').scale(2.1).next_to(line2, DOWN, aligned_edge=RIGHT, buff=0.4)
        final_8 = MathTex('8', color='#FFFF00').scale(2.1).next_to(final_0, LEFT, buff=0.6)
        final_3 = MathTex('3', color='#FFFF00').scale(2.1).next_to(final_8, LEFT, buff=0.6)
        final_2 = MathTex('2', color='#FFFF00').scale(2.1).next_to(final_3, LEFT, buff=0.6)

        # Eldeler
        carry_4 = MathTex('+4', color='#FFFF00').scale(0.8).next_to(n68[0], UP, buff=0.1)
        carry_2 = MathTex('+2', color='#00FFFF').scale(0.8).next_to(n68[0], UP, buff=0.1)

        # Animasyon Başlangıcı
        self.play(Write(header))
        self.play(Write(n68), Write(n35), Write(sign))
        self.play(Create(line1))
        
        # 1. Satır Çarpımı (5 ile çarpım)
        self.play(n35[1].animate.set_color('#FFFF00'))
        self.wait(1.5)
        self.play(Write(res1_0), run_time=0.8)
        self.play(Write(carry_4))
        self.wait(2.5)
        self.play(Write(res1_4), Write(res1_3), run_time=1.5)
        self.wait(3.5) # Stratejik Es
        self.play(FadeOut(carry_4), n35[1].animate.set_color('#FFFFFF'))

        # 2. Satır Çarpımı (3 ile çarpım)
        self.play(n35[0].animate.set_color('#00FFFF'))
        self.wait(1.5)
        self.play(Write(res2_4), run_time=0.8)
        self.play(Write(carry_2))
        self.wait(2.5)
        self.play(Write(res2_0), Write(res2_2), run_time=1.5)
        self.wait(3.5) # Stratejik Es
        self.play(FadeOut(carry_2), n35[0].animate.set_color('#FFFFFF'))

        # ADIM ADIM TOPLAMA ANİMASYONU
        self.play(Create(line2))
        self.wait(1.0)
        self.play(Write(final_0), run_time=0.8) # 0 aşağı indi
        self.wait(1.5)
        self.play(Write(final_8), run_time=0.8) # 4+4=8
        self.wait(1.5)
        self.play(Write(final_3), run_time=0.8) # 3+0=3
        self.wait(1.5)
        self.play(Write(final_2), run_time=0.8) # 2 aşağı indi
        
        # INSTAGRAM FIX: Statik Bekleme
        self.wait(8.0)