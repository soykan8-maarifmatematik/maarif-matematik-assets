from manim import *
import numpy as np

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#000000"
        
        # Başlık Yerleşimi (Kural 3)
        header = Paragraph(
            "İKİ BASAMAKLI SAYILARLA\nÇARPMA İŞLEMİ",
            alignment="center",
            line_spacing=0.8,
            color="#FFFFFF",
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=0.8)

        # Alt Metin Yerleşimi (Kural 3)
        subtext = Paragraph(
            "Adım adım çarpma işlemi",
            alignment="center",
            color="#FFFFFF"
        ).to_edge(DOWN, buff=1.2)

        # Sayılar - Sabit Koordinat ve Hizalama (Kural 1)
        n76 = MathTex("7", "6", color="#FFFFFF").scale(1.7).move_to(UP * 1.8 + LEFT * 0.5)
        n48 = MathTex("4", "8", color="#FFFFFF").scale(1.7).next_to(n76, DOWN, buff=0.4)
        sign = MathTex("\\times", color="#FFFFFF").scale(1.3).next_to(n48, LEFT, buff=0.5)
        line1 = Line(LEFT, RIGHT, color="#FFFFFF").scale(1.5).next_to(n48, DOWN, buff=0.2)

        # Adım Sonuçları - Sola Kaydırma (Kural 1)
        res1 = MathTex("6", "0", "8", color="#FFFFFF").scale(1.7).next_to(line1, DOWN, buff=0.3).align_to(n48, RIGHT)
        
        # res2 mutlak sola kaydırma
        res2 = MathTex("3", "0", "4", color="#FFFFFF").scale(1.7).next_to(res1, DOWN, buff=0.4).align_to(res1, RIGHT)
        res2.shift(LEFT * 0.8) 
        
        line2 = Line(LEFT, RIGHT, color="#FFFFFF").scale(1.8).next_to(res2, DOWN, buff=0.2).align_to(line1, RIGHT)
        final_res = MathTex("3", "6", "4", "8", color="#FFFF00").scale(2.1).next_to(line2, DOWN, buff=0.4).align_to(res1, RIGHT)

        # Eldeler (Kural 1 - Ölçek 0.8)
        carry_4 = MathTex("+4", color="#FFFF00").scale(0.8).next_to(n76[0], UP, buff=0.1)
        carry_2 = MathTex("+2", color="#00FFFF").scale(0.8).next_to(n76[0], UP, buff=0.1)

        # Animasyon Akışı - Senkron ve Hız (Kural 2)
        self.play(Write(header), Write(subtext))
        self.play(Write(n76, run_time=0.5), Write(n48, run_time=0.5), Write(sign, run_time=0.4))
        self.play(Create(line1, run_time=0.4))
        
        # 1. Çarpım
        self.play(n48[1].animate.set_color("#FFFF00"), run_time=0.4)
        self.play(Write(carry_4, run_time=0.4))
        self.play(Write(res1, run_time=0.6))
        self.wait(2.2) # Blok beklemesi
        self.play(FadeOut(carry_4), n48[1].animate.set_color("#FFFFFF"), run_time=0.4)

        # 2. Çarpım
        self.play(n48[0].animate.set_color("#00FFFF"), run_time=0.4)
        self.play(Write(carry_2, run_time=0.4))
        self.play(Write(res2, run_time=0.6))
        self.wait(2.2) # Blok beklemesi
        self.play(FadeOut(carry_2), n48[0].animate.set_color("#FFFFFF"), run_time=0.4)

        # Final Toplama
        self.play(Create(line2, run_time=0.4))
        self.play(Write(final_res, run_time=0.6))
        self.wait(4.0) # Final beklemesi
