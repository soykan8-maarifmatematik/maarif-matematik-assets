from manim import *
import numpy as np

class MultiplicationShorts(Scene):
    def construct(self):
        # ARKA PLAN KİLİDİ
        self.camera.background_color = "#000000"
        
        # BAŞLIK
        header = Text("İKİ BASAMAKLI ÇARPMA", color="#FFFF00", weight=BOLD)
        header.to_edge(UP, buff=1.1).scale_to_fit_width(8.5)
        self.play(Write(header))
        self.wait(0.5)
        
        # MATEMATİKSEL İZLEK (GRID) KURULUMU
        dx = 0.7
        dy = 0.9
        
        def get_digit(char, col, row, color="#FFFFFF"):
            d = Text(char, color=color, weight=BOLD).scale(1.3)
            d.move_to(RIGHT * col * dx + DOWN * row * dy)
            return d
            
        # Üst Sayı (67)
        t_6 = get_digit("6", 1, 0)
        t_7 = get_digit("7", 2, 0)
        
        # Alt Sayı (89)
        b_8 = get_digit("8", 1, 1)
        b_9 = get_digit("9", 2, 1)
        sym_mul = get_digit("\u00d7", 0, 1)
        
        # Çizgi 1
        line1 = Line(LEFT * 0.5, RIGHT * 2.5 * dx, color="#FFFFFF")
        line1.move_to(DOWN * 1.5 * dy + RIGHT * dx)
        
        # Sonuç 1 (603)
        r1_6 = get_digit("6", 0, 2)
        r1_0 = get_digit("0", 1, 2)
        r1_3 = get_digit("3", 2, 2)
        
        # Sonuç 2 (536)
        r2_5 = get_digit("5", -1, 3)
        r2_3 = get_digit("3", 0, 3)
        r2_6 = get_digit("6", 1, 3)
        sym_add = get_digit("+", -2, 3)
        
        # Çizgi 2
        line2 = Line(LEFT * 1.5, RIGHT * 2.5 * dx, color="#FFFFFF")
        line2.move_to(DOWN * 3.5 * dy + RIGHT * dx * 0.5)
        
        # Final (5963)
        f_5 = get_digit("5", -1, 4)
        f_9 = get_digit("9", 0, 4)
        f_6 = get_digit("6", 1, 4)
        f_3 = get_digit("3", 2, 4)
        
        # Eldeler
        c9_6 = Text("+6", color="#FFFF00", weight=BOLD).scale(0.6)
        c9_6.move_to(t_6.get_center() + UP * 0.6 + RIGHT * 0.3)
        
        c8_5 = Text("+5", color="#00FFFF", weight=BOLD).scale(0.6)
        c8_5.move_to(t_6.get_center() + UP * 1.0 + LEFT * 0.3)
        
        # GRUPLAMA VE MERKEZİ HİZALAMA
        math_group = VGroup(
            t_6, t_7, b_8, b_9, sym_mul, line1,
            r1_6, r1_0, r1_3,
            r2_5, r2_3, r2_6, sym_add, line2,
            f_5, f_9, f_6, f_3,
            c9_6, c8_5
        )
        math_group.move_to(UP * 1.2)
        
        # ANİMASYON SÜRECİ
        self.play(Write(VGroup(t_6, t_7)))
        self.wait(0.5)
        self.play(Write(VGroup(sym_mul, b_8, b_9)))
        self.wait(0.5)
        self.play(Create(line1))
        self.wait(0.5)
        
        # Adım 1: 9 x 67
        self.play(b_9.animate.set_color("#FFFF00"), t_7.animate.set_color("#FFFF00"))
        self.wait(0.5)
        self.play(Write(r1_3), Write(c9_6))
        self.wait(0.5)
        
        self.play(t_7.animate.set_color("#FFFFFF"), t_6.animate.set_color("#FFFF00"))
        self.wait(0.5)
        self.play(Indicate(c9_6, color="#FFFF00"))
        self.play(Write(r1_0), Write(r1_6))
        self.wait(0.5)
        
        self.play(b_9.animate.set_color("#FFFFFF"), t_6.animate.set_color("#FFFFFF"))
        self.wait(0.5)
        
        # Adım 2: 8 x 67
        self.play(b_8.animate.set_color("#00FFFF"), t_7.animate.set_color("#00FFFF"))
        self.wait(0.5)
        self.play(Write(r2_6), Write(c8_5))
        self.wait(0.5)
        
        self.play(t_7.animate.set_color("#FFFFFF"), t_6.animate.set_color("#00FFFF"))
        self.wait(0.5)
        self.play(Indicate(c8_5, color="#00FFFF"))
        self.play(Write(r2_3), Write(r2_5))
        self.wait(0.5)
        
        self.play(b_8.animate.set_color("#FFFFFF"), t_6.animate.set_color("#FFFFFF"))
        self.wait(0.5)
        
        # Adım 3: Toplama
        self.play(Write(sym_add), Create(line2))
        self.wait(0.5)
        
        self.play(Write(f_3))
        self.wait(0.5)
        self.play(Write(f_6))
        self.wait(0.5)
        self.play(Write(f_9))
        self.wait(0.5)
        self.play(Write(f_5))
        self.wait(0.5)
        
        # AÇIKLAMA METNİ
        desc = Paragraph("Adım Adım Çarpma", "Eldelere Dikkat!", alignment="center", color="#FFFFFF", weight=BOLD)
        desc.move_to(DOWN * 3.5)
        self.play(Write(desc))
        
        # VİDEO SONU BEKLEMESİ
        self.wait(3)
