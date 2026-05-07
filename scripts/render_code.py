from manim import *
import numpy as np

class MultiplicationShorts(Scene):
    def construct(self):
        # 1. ARKA PLAN (SİYAH TEMA ZORUNLULUĞU)
        self.camera.background_color = BLACK

        # 2. BAŞLIK (MİLİMETRİK YERLEŞİM)
        header = Text("İKİ BASAMAKLI ÇARPMA İŞLEMİ", weight=BOLD, color=WHITE)
        header.to_edge(UP, buff=1.1).scale_to_fit_width(8.5)
        self.play(Write(header))

        # 3. İÇERİK (İŞLEM GRUBU VE MATEMATİKSEL NESNELER)
        # Sayılar ve işaretler
        n67_6 = MathTex("6", color=WHITE)
        n67_7 = MathTex("7", color=WHITE)
        n89_8 = MathTex("8", color=WHITE)
        n89_9 = MathTex("9", color=WHITE)
        times = MathTex("\\times", color=WHITE)
        line1 = Line(LEFT, RIGHT, color=WHITE).set_length(2.5)

        # İlk Çarpan (67) ve İkinci Çarpan (89) Pozisyonları
        n67_7.move_to(ORIGIN)
        n67_6.next_to(n67_7, LEFT, buff=0.5)
        n89_9.next_to(n67_7, DOWN, buff=0.5)
        n89_8.next_to(n67_6, DOWN, buff=0.5)
        times.next_to(n89_8, LEFT, buff=0.5)
        line1.next_to(n89_9, DOWN, buff=0.3).align_to(n67_7, RIGHT).shift(RIGHT * 0.2)

        # Eldeler (Vurgu Renkleri)
        carry_1 = MathTex("+6", color=YELLOW).scale(0.6).next_to(n67_6, UP, buff=0.3)
        carry_2 = MathTex("+5", color=CYAN).scale(0.6).next_to(n67_6, UP, buff=0.3)

        # 1. Adım Sonucu (603)
        r3_3 = MathTex("3", color=WHITE).next_to(line1, DOWN, buff=0.3).align_to(n67_7, RIGHT)
        r3_0 = MathTex("0", color=WHITE).next_to(r3_3, LEFT, buff=0.5)
        r3_6 = MathTex("6", color=WHITE).next_to(r3_0, LEFT, buff=0.5)

        # 2. Adım Sonucu (536 - Sola Kaydırılmış)
        r4_6 = MathTex("6", color=WHITE).next_to(r3_0, DOWN, buff=0.5)
        r4_3 = MathTex("3", color=WHITE).next_to(r4_6, LEFT, buff=0.5)
        r4_5 = MathTex("5", color=WHITE).next_to(r4_3, LEFT, buff=0.5)

        # Toplama İşlemi ve Çizgisi
        plus = MathTex("+", color=WHITE).next_to(r4_5, LEFT, buff=0.5)
        line2 = Line(LEFT, RIGHT, color=WHITE).set_length(3.5).next_to(r4_6, DOWN, buff=0.3).align_to(r3_3, RIGHT).shift(RIGHT * 0.2)

        # Final Sonucu (5963 - Vurgulu Renk)
        r5_3 = MathTex("3", color=YELLOW).next_to(line2, DOWN, buff=0.3).align_to(r3_3, RIGHT)
        r5_6 = MathTex("6", color=YELLOW).next_to(r5_3, LEFT, buff=0.5)
        r5_9 = MathTex("9", color=YELLOW).next_to(r5_6, LEFT, buff=0.5)
        r5_5 = MathTex("5", color=YELLOW).next_to(r5_9, LEFT, buff=0.5)

        # Tüm matematiksel nesneleri VGroup içine alıp boyutlandır/konumlandır
        math_group = VGroup(
            n67_6, n67_7, n89_8, n89_9, times, line1,
            carry_1, carry_2,
            r3_3, r3_0, r3_6,
            r4_6, r4_3, r4_5,
            plus, line2,
            r5_3, r5_6, r5_9, r5_5
        )
        math_group.scale(1.5).move_to(UP * 1.2)

        # 4. AÇIKLAMA (ALT KISIM - PARAGRAPH KULLANIMI)
        desc_text = Paragraph(
            "1) 9 ile 67'yi çarp. (Eldelere dikkat!)",
            "2) 8 ile 67'yi çarp, bir basamak sola kaydır.",
            "3) Çıkan sonuçları topla.",
            color=WHITE
        ).move_to(DOWN * 3.5).scale_to_fit_width(7.5)

        # 5. ANİMASYONLAR (AKICI VE KESİNTİSİZ)
        # Başlangıç kurulumu
        self.play(
            Write(n67_6), Write(n67_7), 
            Write(n89_8), Write(n89_9), 
            Write(times), Create(line1)
        )
        self.play(Write(desc_text))
        self.wait(0.5)

        # Adım 1: 9 x 7 = 63
        self.play(Indicate(n89_9, color=YELLOW), Indicate(n67_7, color=YELLOW))
        self.play(Write(r3_3), Write(carry_1))
        self.wait(0.5)

        # Adım 1: 9 x 6 = 54, +6 = 60
        self.play(Indicate(n89_9, color=YELLOW), Indicate(n67_6, color=YELLOW))
        self.play(Indicate(carry_1, color=WHITE))
        self.play(Write(r3_0), Write(r3_6))
        self.play(FadeOut(carry_1))
        self.wait(0.5)

        # Adım 2: 8 x 7 = 56
        self.play(Indicate(n89_8, color=CYAN), Indicate(n67_7, color=CYAN))
        self.play(Write(r4_6), Write(carry_2))
        self.wait(0.5)

        # Adım 2: 8 x 6 = 48, +5 = 53
        self.play(Indicate(n89_8, color=CYAN), Indicate(n67_6, color=CYAN))
        self.play(Indicate(carry_2, color=WHITE))
        self.play(Write(r4_3), Write(r4_5))
        self.play(FadeOut(carry_2))
        self.wait(0.5)

        # Adım 3: Toplama
        self.play(Write(plus), Create(line2))
        self.wait(0.5)

        self.play(Write(r5_3))
        self.play(Write(r5_6))
        self.play(Write(r5_9))
        self.play(Write(r5_5))
        
        # FİNAL BEKLEME (ZORUNLU)
        self.wait(3)
