from manim import *

class FractionsLesson(Scene):
    def construct(self):
        # ARKA PLAN: BEYAZ (HAYATİ KURAL)
        self.camera.background_color = "#FFFFFF"
        
        # RENK STANDARTLARI
        DARK_GRAY = "#333333"
        MAARIF_BLUE = "#007BFF"
        NAVY_BLUE = "#002B4D"

        # ==========================================
        # PARAGRAF 1: Basit Kesir (30.0 Saniye)
        # ==========================================
        title1 = Text("Basit Kesir", color=NAVY_BLUE, font_size=48).to_edge(UP)
        frac1 = MathTex(r"\frac{1}{4}", color=MAARIF_BLUE).scale(2).next_to(title1, DOWN)
        
        self.play(Write(title1), Write(frac1), run_time=2)
        self.wait(3) # Toplam 5s

        # Pizza Modeli (Bütün)
        circle1 = Circle(radius=1.5, color=DARK_GRAY).shift(DOWN*0.5)
        l1 = Line(circle1.get_top(), circle1.get_bottom(), color=DARK_GRAY)
        l2 = Line(circle1.get_left(), circle1.get_right(), color=DARK_GRAY)
        
        self.play(Create(circle1), Create(l1), Create(l2), run_time=3)
        self.wait(2) # Toplam 10s

        # Daire Dilimi (Sector)
        sector1 = Sector(outer_radius=1.5, angle=PI/2, start_angle=0, color=MAARIF_BLUE, fill_opacity=0.7).shift(DOWN*0.5)
        self.play(FadeIn(sector1), run_time=2)
        self.wait(5) # Toplam 17s

        rule1 = MathTex(r"\text{Pay} < \text{Payda}", color=DARK_GRAY).next_to(circle1, DOWN)
        self.play(Write(rule1), run_time=2)
        self.wait(11) # Toplam 30s

        # ==========================================
        # PARAGRAF 2: Bileşik Kesir (30.0 Saniye)
        # ==========================================
        title2 = Text("Bileşik Kesir", color=NAVY_BLUE, font_size=48).to_edge(UP)
        frac2 = MathTex(r"\frac{5}{4}", color=MAARIF_BLUE).scale(2).next_to(title2, DOWN)

        # Akışkan Geçiş (ReplacementTransform)
        self.play(
            ReplacementTransform(title1, title2),
            ReplacementTransform(frac1, frac2),
            FadeOut(rule1),
            run_time=3
        )
        self.wait(2) # Toplam 5s

        # Yeni Pizza Modelleri (2 Adet)
        circle1_new = Circle(radius=1.5, color=DARK_GRAY).shift(LEFT*2 + DOWN*0.5)
        l1_new = Line(circle1_new.get_top(), circle1_new.get_bottom(), color=DARK_GRAY)
        l2_new = Line(circle1_new.get_left(), circle1_new.get_right(), color=DARK_GRAY)
        full_sector = Sector(outer_radius=1.5, angle=2*PI, color=MAARIF_BLUE, fill_opacity=0.7).shift(LEFT*2 + DOWN*0.5)

        circle2 = Circle(radius=1.5, color=DARK_GRAY).shift(RIGHT*2 + DOWN*0.5)
        l3 = Line(circle2.get_top(), circle2.get_bottom(), color=DARK_GRAY)
        l4 = Line(circle2.get_left(), circle2.get_right(), color=DARK_GRAY)

        self.play(
            ReplacementTransform(circle1, circle1_new),
            ReplacementTransform(l1, l1_new),
            ReplacementTransform(l2, l2_new),
            ReplacementTransform(sector1, full_sector),
            Create(circle2), Create(l3), Create(l4),
            run_time=3
        )
        self.wait(2) # Toplam 10s

        sector2 = Sector(outer_radius=1.5, angle=PI/2, start_angle=0, color=MAARIF_BLUE, fill_opacity=0.7).shift(RIGHT*2 + DOWN*0.5)
        self.play(FadeIn(sector2), run_time=3)
        self.wait(5) # Toplam 18s

        rule2 = MathTex(r"\text{Pay} \geq \text{Payda}", color=DARK_GRAY).next_to(circle1_new, DOWN).shift(RIGHT*2)
        self.play(Write(rule2), run_time=2)
        self.wait(10) # Toplam 30s

        # ==========================================
        # PARAGRAF 3: Tam Sayılı Kesir (30.0 Saniye)
        # ==========================================
        title3 = Text("Tam Sayılı Kesir", color=NAVY_BLUE, font_size=48).to_edge(UP)
        frac3 = MathTex(r"1 \frac{1}{4}", color=MAARIF_BLUE).scale(2).next_to(title3, DOWN)

        self.play(
            ReplacementTransform(title2, title3),
            ReplacementTransform(frac2, frac3),
            FadeOut(rule2),
            run_time=3
        )
        self.wait(4) # Toplam 7s

        self.play(Indicate(full_sector, color=NAVY_BLUE), run_time=2)
        self.wait(4) # Toplam 13s

        self.play(Indicate(sector2, color=NAVY_BLUE), run_time=2)
        self.wait(5) # Toplam 20s

        eq = MathTex(r"\frac{5}{4} = 1 \frac{1}{4}", color=DARK_GRAY).scale(1.5).next_to(circle1_new, DOWN).shift(RIGHT*2)
        self.play(Write(eq), run_time=3)
        self.wait(7) # Toplam 30s

        # ==========================================
        # PARAGRAF 4: Kesirleri Çevirme ve Bölme Evi (30.0 Saniye)
        # ==========================================
        div_title = Text("Kesirleri Çevirme", color=NAVY_BLUE, font_size=48).to_edge(UP)
        dividend = MathTex("5", color=DARK_GRAY).scale(1.5).move_to(LEFT*1 + UP*1)
        divisor = MathTex("4", color=DARK_GRAY).scale(1.5).move_to(RIGHT*0.5 + UP*1)

        prev_group = VGroup(title3, frac3, circle1_new, l1_new, l2_new, full_sector, circle2, l3, l4, sector2, eq)

        self.play(
            ReplacementTransform(prev_group, VGroup(div_title, dividend, divisor)),
            run_time=3
        )
        self.wait(2) # Toplam 5s

        # Bölme Evi Geometrik İnşası
        line1 = Line(start=LEFT*0.25 + UP*1.6, end=LEFT*0.25 + UP*0.2, color=DARK_GRAY) # Dikey Çizgi
        line2 = Line(start=LEFT*0.25 + UP*0.5, end=RIGHT*1.25 + UP*0.5, color=DARK_GRAY) # Yatay Çizgi (Bölen Altı)

        self.play(Create(line1), Create(line2), run_time=2)
        self.wait(3) # Toplam 10s

        quotient = MathTex("1", color=MAARIF_BLUE).scale(1.5).move_to(RIGHT*0.5 + DOWN*0.1)
        product = MathTex("4", color=DARK_GRAY).scale(1.5).move_to(LEFT*1 + DOWN*0.1)

        self.play(Write(quotient), Write(product), run_time=2)
        self.wait(3) # Toplam 15s

        # Çıkarma Çizgisi ve Eksi İşareti
        line3 = Line(start=LEFT*1.6, end=LEFT*0.4, color=DARK_GRAY).move_to(LEFT*1 + DOWN*0.6)
        minus = MathTex("-", color=DARK_GRAY).move_to(LEFT*1.8 + DOWN*0.1)

        self.play(Create(line3), Write(minus), run_time=2)
        self.wait(3) # Toplam 20s

        remainder = MathTex("1", color=MAARIF_BLUE).scale(1.5).move_to(LEFT*1 + DOWN*1.3)
        self.play(Write(remainder), run_time=2)
        self.wait(3) # Toplam 25s

        mapping = MathTex(r"1 \frac{1}{4}", color=NAVY_BLUE).scale(2).move_to(RIGHT*3 + DOWN*0.5)
        self.play(Write(mapping), run_time=3)
        self.wait(2) # Toplam 30s
