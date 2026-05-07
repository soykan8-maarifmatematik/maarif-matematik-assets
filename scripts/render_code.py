from manim import *
import numpy as np

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#000000"
        
        # V33 - Başlık Kuralı
        header = Paragraph(
            "İKİ BASAMAKLI SAYILARLA\nÇARPMA İŞLEMİ",
            alignment="center",
            line_spacing=0.8,
            color="#FFFFFF",
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=0.9)

        # V33 - Ölçeklendirme Kuralı (Ana sayılar 1.6)
        n67 = MathTex("6", "7", color="#FFFFFF").scale(1.6)
        n89 = MathTex("8", "9", color="#FFFFFF").scale(1.6)
        sign = MathTex("\\times", color="#FFFFFF").scale(1.6)
        line1 = Line(LEFT, RIGHT, color="#FFFFFF").scale(1.6)

        n89.next_to(n67, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign.next_to(n89, LEFT, buff=0.8)
        line1.next_to(n89, DOWN, buff=0.2)
        
        res1 = MathTex("6", "0", "3", color="#FFFFFF").scale(1.6).next_to(line1, DOWN, aligned_edge=RIGHT, buff=0.3)
        res2 = MathTex("5", "3", "6", color="#FFFFFF").scale(1.6).next_to(res1, DOWN, aligned_edge=RIGHT, buff=0.3).shift(LEFT * 0.75)
        
        line2 = Line(LEFT, RIGHT, color="#FFFFFF").scale(1.6).next_to(res2, DOWN, buff=0.2)
        final_res = MathTex("5", "9", "6", "3", color="#FFFF00").scale(1.6).next_to(line2, DOWN, aligned_edge=RIGHT, buff=0.3)

        # V33 - Merkezleme Kuralı (İşlem grubunu merkezin biraz üstüne alma)
        math_group = VGroup(n67, n89, sign, line1, res1, res2, line2, final_res)
        math_group.move_to(ORIGIN + UP * 0.5)

        # V33 - Eldeler Kuralı (Merkezlemeden sonra, scale 0.8 ve buff 0.1)
        carry_6 = MathTex("+6", color="#FFFF00").scale(0.8).next_to(n67[0], UP, buff=0.1)
        carry_5 = MathTex("+5", color="#00FFFF").scale(0.8).next_to(n67[0], UP, buff=0.1)

        # V33 - Açıklama Metni Kuralı
        desc = Paragraph(
            "Eldeleri eklemeyi ve ikinci satırı\nsola kaydırmayı unutma!",
            alignment="center",
            color="#FFFFFF"
        ).to_edge(DOWN, buff=1.5)

        self.play(Write(header))
        self.play(Write(n67), Write(n89), Write(sign))
        self.play(Create(line1))
        
        # --- 1. SATIR ÇARPIMI (Blok Senkron ve Hızlı Rakamlar) ---
        self.play(n89[1].animate.set_color("#FFFF00"), run_time=0.3)
        self.play(Write(res1[2]), run_time=0.3)
        self.play(Write(carry_6), run_time=0.3)
        self.play(Write(res1[0:2]), run_time=0.3)
        self.play(FadeOut(carry_6), n89[1].animate.set_color("#FFFFFF"), run_time=0.3)
        self.wait(1.5) # V33: Birinci satır bittikten sonra bekleme

        # --- 2. SATIR ÇARPIMI (Blok Senkron ve Hızlı Rakamlar) ---
        self.play(n89[0].animate.set_color("#00FFFF"), run_time=0.3)
        self.play(Write(res2[2]), run_time=0.3)
        self.play(Write(carry_5), run_time=0.3)
        self.play(Write(res2[0:2]), run_time=0.3)
        self.play(FadeOut(carry_5), n89[0].animate.set_color("#FFFFFF"), run_time=0.3)
        self.wait(1.5) # V33: İkinci satır bittikten sonra bekleme

        # --- TOPLAMA İŞLEMİ (Blok Senkron) ---
        self.wait(1.0) # V33: Toplama işlemi başlamadan önce bekleme
        self.play(Create(line2), run_time=0.3)
        self.play(Write(final_res), run_time=0.3)

        self.play(Write(desc))
        self.wait(3)