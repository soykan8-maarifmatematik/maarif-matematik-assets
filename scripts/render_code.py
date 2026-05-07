from manim import *
import numpy as np

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#000000"
        
        header = Paragraph(
            "İKİ BASAMAKLI SAYILARLA\nÇARPMA İŞLEMİ",
            alignment="center",
            line_spacing=0.8,
            color="#FFFFFF",
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.0)

        # Ana Sayılar ve İşlem Elemanları (V34 Ölçeklendirme)
        n83 = MathTex("8", "3", color="#FFFFFF").scale(1.7)
        n47 = MathTex("4", "7", color="#FFFFFF").scale(1.7)
        sign = MathTex("\\times", color="#FFFFFF").scale(1.3)
        line1 = Line(LEFT, RIGHT, color="#FFFFFF").scale(1.5)

        # Yerleşim: V34 El Yazısı Düzeni (Hafif sola/merkeze çekilmiş)
        n83.move_to(UP * 1.5 + LEFT * 0.2)
        n47.next_to(n83, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign.next_to(n47, LEFT, buff=0.8)
        line1.next_to(n47, DOWN, buff=0.2)

        # Eldeler (V34 - Ana rakamın hemen üzerinde, scale 0.8)
        carry_2 = MathTex("+2", color="#FFFF00").scale(0.8).next_to(n83[0], UP, buff=0.1)
        carry_1 = MathTex("+1", color="#00FFFF").scale(0.8).next_to(n83[0], UP, buff=0.1)

        # Adım Sonuçları
        res1 = MathTex("5", "8", "1", color="#FFFFFF").scale(1.7).next_to(line1, DOWN, aligned_edge=RIGHT, buff=0.4)
        res2 = MathTex("3", "3", "2", color="#FFFFFF").scale(1.7).next_to(res1, DOWN, aligned_edge=RIGHT, buff=0.4)
        res2.shift(LEFT * 0.7) # V34 Zorunlu Basamak Kaydırma
        
        line2 = Line(LEFT, RIGHT, color="#FFFFFF").scale(1.8).next_to(res2, DOWN, buff=0.2)
        final_res = MathTex("3", "9", "0", "1", color="#FFFF00").scale(2.0).next_to(line2, DOWN, aligned_edge=RIGHT, buff=0.4)

        desc = Paragraph(
            "Eldeleri eklemeyi ve ikinci satırı\nsola kaydırmayı unutma!",
            alignment="center",
            color="#FFFFFF"
        ).scale_to_fit_width(7.0).to_edge(DOWN, buff=1.2)

        # ANİMASYON (V34 Senkron ve Bekleme Kuralları)
        self.play(Write(header))
        self.play(Write(n83, run_time=0.5), Write(n47, run_time=0.5), Write(sign, run_time=0.5))
        self.play(Create(line1))
        self.wait(1.0)
        
        # 1. Adım
        self.play(n47[1].animate.set_color("#FFFF00"))
        self.play(Write(carry_2, run_time=0.5))
        self.play(Write(res1, run_time=0.8))
        self.wait(3.0) # V34: 3 Saniye Kuralı
        self.play(FadeOut(carry_2), n47[1].animate.set_color("#FFFFFF"))

        # 2. Adım
        self.play(n47[0].animate.set_color("#00FFFF"))
        self.play(Write(carry_1, run_time=0.5))
        self.play(Write(res2, run_time=0.8))
        self.wait(3.0) # V34: 3 Saniye Kuralı
        self.play(FadeOut(carry_1), n47[0].animate.set_color("#FFFFFF"))

        # Final
        self.play(Create(line2))
        self.play(Write(final_res, run_time=0.8))
        self.play(Write(desc))
        self.wait(4.0) # V34: Kapanış öncesi 4 saniye bekleme