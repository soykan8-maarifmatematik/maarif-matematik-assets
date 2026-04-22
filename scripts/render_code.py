from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Renk Paleti
        self.camera.background_color = "#FFFFFF"
        DARK_GRAY = "#333333"
        MAARIF_NAVY = "#002B4D"
        MAARIF_RED = "#D32F2F"

        # 1. Paragraf: Giriş (24 kelime / 2.5 = 9.6 saniye)
        title = Text("Kesir Nedir?", color=MAARIF_NAVY, font_size=48).to_edge(UP)
        self.play(Write(title), run_time=2)
        self.wait(7.6)

        # 2. Paragraf: Pay ve Payda (30 kelime / 2.5 = 12.0 saniye)
        line = Line(LEFT*0.5, RIGHT*0.5, color=DARK_GRAY).shift(UP*1.5 + LEFT*3)
        num = Text("3", color=MAARIF_RED, font_size=48).next_to(line, UP)
        den = Text("4", color=MAARIF_NAVY, font_size=48).next_to(line, DOWN)
        fraction = VGroup(num, line, den)

        pay_text = Text("Pay", color=MAARIF_RED, font_size=36).next_to(num, LEFT, buff=1.5)
        payda_text = Text("Payda", color=MAARIF_NAVY, font_size=36).next_to(den, LEFT, buff=1.5)

        arrow_pay = Arrow(pay_text.get_right(), num.get_left(), color=MAARIF_RED, buff=0.1)
        arrow_payda = Arrow(payda_text.get_right(), den.get_left(), color=MAARIF_NAVY, buff=0.1)

        self.play(Write(fraction), run_time=2)
        self.play(Write(pay_text), Write(payda_text), Create(arrow_pay), Create(arrow_payda), run_time=2)
        self.wait(8.0)

        # 3. Paragraf: Model Üzerinde Gösterim (23 kelime / 2.5 = 9.2 saniye)
        pie = VGroup()
        colors = [MAARIF_RED, MAARIF_RED, MAARIF_RED, "#E0E0E0"]
        for i in range(4):
            # Kural 3: outer_radius ASLA kullanılmaz, sadece radius kullanılır.
            slice_sector = Sector(start_angle=i*PI/2, angle=PI/2, radius=1.5, color=colors[i], fill_opacity=0.9, stroke_color=DARK_GRAY, stroke_width=2)
            pie.add(slice_sector)
        pie.shift(UP*1.5 + RIGHT*3)

        self.play(Create(pie), run_time=2)
        self.wait(7.2)

        # 4. Paragraf: Kesrin Okunuşu (27 kelime / 2.5 = 10.8 saniye)
        read_down = Text("Üç bölü dört", color=DARK_GRAY, font_size=36).shift(DOWN*1 + LEFT*2)
        arrow_down = Arrow(UP, DOWN, color=MAARIF_RED).next_to(read_down, LEFT)

        read_up = Text("Dörtte üç", color=DARK_GRAY, font_size=36).shift(DOWN*2.5 + LEFT*2)
        arrow_up = Arrow(DOWN, UP, color=MAARIF_NAVY).next_to(read_up, LEFT)

        self.play(Write(read_down), Create(arrow_down), run_time=2)
        self.play(Write(read_up), Create(arrow_up), run_time=2)
        self.wait(6.8)

        # 5. Paragraf: Sayı Doğrusu (24 kelime / 2.5 = 9.6 saniye)
        nl = NumberLine(
            x_range=[0, 1, 0.25],
            length=6,
            color=DARK_GRAY,
            include_numbers=False
        ).shift(DOWN*1.5 + RIGHT*3)

        tick_0 = Text("0", color=DARK_GRAY, font_size=24).next_to(nl.number_to_point(0), DOWN)
        tick_1 = Text("1", color=DARK_GRAY, font_size=24).next_to(nl.number_to_point(1), DOWN)

        dot = Dot(nl.number_to_point(0.75), color=MAARIF_RED, radius=0.1)
        dot_label = Text("3/4", color=MAARIF_RED, font_size=24).next_to(dot, UP)

        self.play(Create(nl), Write(tick_0), Write(tick_1), run_time=2)
        self.play(Create(dot), Write(dot_label), run_time=1)
        self.wait(6.6)
