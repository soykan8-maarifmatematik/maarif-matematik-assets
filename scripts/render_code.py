from manim import *
import numpy as np

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_width = 9
config.frame_height = 16

class MultiplicationScene(Scene):
    def construct(self):
        # 1. BAŞLIK (Üst - Hassas Yerleşim)
        header = Text("İKİ BASAMAKLI SAYILARLA ÇARPMA", weight=BOLD)
        header.to_edge(UP, buff=1.1)
        header.scale_to_fit_width(8.5)
        self.play(Write(header))

        # 2. MODELLER/İŞLEM (Orta-Üst)
        # Rakamları tek tek tanımlıyoruz (Renklendirme ve animasyon için)
        n6 = MathTex("6")
        n7 = MathTex("7")
        n8 = MathTex("8")
        n9 = MathTex("9")
        
        # Konumlandırma (Bağıl koordinatlar)
        n7.move_to(RIGHT * 0.5)
        n6.move_to(LEFT * 0.5)
        n9.move_to(RIGHT * 0.5 + DOWN * 0.8)
        n8.move_to(LEFT * 0.5 + DOWN * 0.8)
        
        times_sign = MathTex("\\times").move_to(LEFT * 1.5 + DOWN * 0.8)
        line1 = Line(LEFT * 2.0, RIGHT * 1.0, stroke_width=4).move_to(DOWN * 1.3)
        
        # 1. Çarpım (603)
        p1_3 = MathTex("3").move_to(RIGHT * 0.5 + DOWN * 1.8)
        p1_0 = MathTex("0").move_to(LEFT * 0.5 + DOWN * 1.8)
        p1_6 = MathTex("6").move_to(LEFT * 1.5 + DOWN * 1.8)
        
        # 2. Çarpım (536 - Sola Kaydırılmış)
        p2_6 = MathTex("6").move_to(LEFT * 0.5 + DOWN * 2.6)
        p2_3 = MathTex("3").move_to(LEFT * 1.5 + DOWN * 2.6)
        p2_5 = MathTex("5").move_to(LEFT * 2.5 + DOWN * 2.6)
        
        # Toplama İşlemi
        plus_sign = MathTex("+").move_to(LEFT * 3.0 + DOWN * 2.6)
        line2 = Line(LEFT * 3.5, RIGHT * 1.0, stroke_width=4).move_to(DOWN * 3.1)
        
        # Sonuç (5963)
        r_3 = MathTex("3").move_to(RIGHT * 0.5 + DOWN * 3.7)
        r_6 = MathTex("6").move_to(LEFT * 0.5 + DOWN * 3.7)
        r_9 = MathTex("9").move_to(LEFT * 1.5 + DOWN * 3.7)
        r_5 = MathTex("5").move_to(LEFT * 2.5 + DOWN * 3.7)
        
        # Eldeler
        c6 = MathTex("+6", color=YELLOW).scale(0.6).next_to(n6, UP, buff=0.2)
        c5 = MathTex("+5", color=ORANGE).scale(0.6).next_to(n6, UP, buff=0.7)

        # Tüm işlem elemanlarını bir gruba al
        operation_group = VGroup(
            n6, n7, n8, n9, times_sign, line1,
            p1_3, p1_0, p1_6,
            p2_6, p2_3, p2_5,
            plus_sign, line2,
            r_3, r_6, r_9, r_5,
            c6, c5
        )
        
        # Modelleri Ortala ve Yukarı Taşı (V25 Kuralı)
        operation_group.move_to(UP * 1.2)
        
        # Animasyonlar Başlıyor
        self.play(Write(n6), Write(n7))
        self.play(Write(n8), Write(n9), Write(times_sign), Create(line1))
        self.wait(0.5)
        
        # Adım 1: 9 x 67
        self.play(n9.animate.set_color(YELLOW), n7.animate.set_color(YELLOW))
        self.wait(0.3)
        self.play(Write(p1_3))
        self.play(Write(c6)) # Elde 6
        self.wait(0.5)
        
        self.play(n7.animate.set_color(WHITE), n6.animate.set_color(YELLOW))
        self.wait(0.3)
        self.play(Write(p1_0), Write(p1_6))
        self.play(c6.animate.set_opacity(0.3)) # Elde kullanıldı
        self.wait(0.5)
        
        self.play(n9.animate.set_color(WHITE), n6.animate.set_color(WHITE))
        
        # Adım 2: 8 x 67
        self.play(n8.animate.set_color(ORANGE), n7.animate.set_color(ORANGE))
        self.wait(0.3)
        self.play(Write(p2_6))
        self.play(Write(c5)) # Elde 5
        self.wait(0.5)
        
        self.play(n7.animate.set_color(WHITE), n6.animate.set_color(ORANGE))
        self.wait(0.3)
        self.play(Write(p2_3), Write(p2_5))
        self.play(c5.animate.set_opacity(0.3)) # Elde kullanıldı
        self.wait(0.5)
        
        self.play(n8.animate.set_color(WHITE), n6.animate.set_color(WHITE))
        
        # Adım 3: Toplama
        self.play(Write(plus_sign), Create(line2))
        self.wait(0.5)
        
        self.play(Write(r_3))
        self.play(Write(r_6))
        self.play(Write(r_9))
        self.play(Write(r_5))
        self.wait(1)

        # 3. AÇIKLAMA (Alt - Hassas Yerleşim)
        desc = Paragraph(
            "1. Adım: Birler basamağı ile üstteki sayıyı çarp.",
            "2. Adım: Onlar basamağı ile çarp, sola kaydırarak yaz.",
            "3. Adım: Elde edilen sonuçları topla.",
            alignment="center",
            weight=BOLD
        )
        desc.move_to(DOWN * 3.5)
        desc.scale_to_fit_width(7.5)
        self.play(Write(desc))
        self.wait(2)
