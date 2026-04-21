from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Renk Paleti
        bg_color = "#FFFFFF"
        text_color = "#333333"
        maarif_navy = "#002B4D"
        maarif_red = "#D32F2F"

        self.camera.background_color = bg_color

        # --- Paragraf 1: Giriş (23 kelime / 2.5 = 9.2 saniye) ---
        title = Text("Kesir Nedir?", color=maarif_navy, font_size=48, weight=BOLD)
        self.play(Write(title), run_time=2)
        self.wait(7.2) # Toplam 9.2s
        self.play(FadeOut(title))

        # --- Paragraf 2: Sektör / Pizza Modeli (38 kelime / 2.5 = 15.2 saniye) ---
        # 4 eş parça, 1'i kırmızı (alınan), 3'ü lacivert
        sector1 = Sector(radius=2, angle=PI/2, start_angle=0, color=maarif_red, fill_opacity=0.8, stroke_color=bg_color, stroke_width=2)
        sector2 = Sector(radius=2, angle=PI/2, start_angle=PI/2, color=maarif_navy, fill_opacity=0.8, stroke_color=bg_color, stroke_width=2)
        sector3 = Sector(radius=2, angle=PI/2, start_angle=PI, color=maarif_navy, fill_opacity=0.8, stroke_color=bg_color, stroke_width=2)
        sector4 = Sector(radius=2, angle=PI/2, start_angle=3*PI/2, color=maarif_navy, fill_opacity=0.8, stroke_color=bg_color, stroke_width=2)

        pie_chart = VGroup(sector1, sector2, sector3, sector4).shift(LEFT * 3)

        self.play(FadeIn(pie_chart), run_time=2)
        self.wait(13.2) # Toplam 15.2s

        # --- Paragraf 3: Pay ve Payda (37 kelime / 2.5 = 14.8 saniye) ---
        fraction_line = Line(LEFT, RIGHT, color=text_color).set_length(1.5).shift(RIGHT * 3)
        numerator = MathTex("1", color=maarif_red, font_size=64).next_to(fraction_line, UP, buff=0.3)
        denominator = MathTex("4", color=maarif_navy, font_size=64).next_to(fraction_line, DOWN, buff=0.3)

        pay_text = Text("Pay", color=maarif_red, font_size=32).next_to(numerator, RIGHT, buff=1)
        payda_text = Text("Payda", color=maarif_navy, font_size=32).next_to(denominator, RIGHT, buff=1)

        arrow_pay = Arrow(start=pay_text.get_left(), end=numerator.get_right(), color=maarif_red, buff=0.1)
        arrow_payda = Arrow(start=payda_text.get_left(), end=denominator.get_right(), color=maarif_navy, buff=0.1)

        fraction_group = VGroup(fraction_line, numerator, denominator, pay_text, payda_text, arrow_pay, arrow_payda)

        self.play(Write(fraction_line), Write(numerator), Write(denominator), run_time=2)
        self.play(Write(pay_text), GrowArrow(arrow_pay), Write(payda_text), GrowArrow(arrow_payda), run_time=2)
        self.wait(10.8) # Toplam 14.8s
        self.play(FadeOut(pie_chart), FadeOut(fraction_group))

        # --- Paragraf 4: Okunuş (36 kelime / 2.5 = 14.4 saniye) ---
        read_frac_line = Line(LEFT, RIGHT, color=text_color).set_length(1.5)
        read_num = MathTex("1", color=maarif_red, font_size=64).next_to(read_frac_line, UP, buff=0.3)
        read_den = MathTex("4", color=maarif_navy, font_size=64).next_to(read_frac_line, DOWN, buff=0.3)
        read_group = VGroup(read_frac_line, read_num, read_den)

        down_arrow = Arrow(start=UP*1.5, end=DOWN*1.5, color=text_color).next_to(read_group, LEFT, buff=1)
        up_arrow = Arrow(start=DOWN*1.5, end=UP*1.5, color=text_color).next_to(read_group, RIGHT, buff=1)

        read_down_text = Text("Bir bölü dört", color=text_color, font_size=32).next_to(down_arrow, LEFT, buff=0.5)
        read_up_text = Text("Dörtte bir", color=text_color, font_size=32).next_to(up_arrow, RIGHT, buff=0.5)

        self.play(FadeIn(read_group), run_time=1)
        self.play(GrowArrow(down_arrow), Write(read_down_text), run_time=2)
        self.play(GrowArrow(up_arrow), Write(read_up_text), run_time=2)
        self.wait(9.4) # Toplam 14.4s
        self.play(FadeOut(read_group), FadeOut(down_arrow), FadeOut(up_arrow), FadeOut(read_down_text), FadeOut(read_up_text))

        # --- Paragraf 5: Sayı Doğrusu (37 kelime / 2.5 = 14.8 saniye) ---
        number_line = NumberLine(
            x_range=[0, 1, 0.25],
            length=8,
            color=maarif_navy,
            include_numbers=False,
            tick_size=0.15
        )
        nl_0 = MathTex("0", color=text_color).next_to(number_line.n2p(0), DOWN)
        nl_1 = MathTex("1", color=text_color).next_to(number_line.n2p(1), DOWN)

        point_1_4 = Dot(number_line.n2p(0.25), color=maarif_red, radius=0.1)
        label_1_4 = MathTex("\\frac{1}{4}", color=maarif_red).next_to(point_1_4, UP, buff=0.5)
        arrow_1_4 = Arrow(start=label_1_4.get_bottom(), end=point_1_4.get_top(), color=maarif_red, buff=0.1)

        nl_group = VGroup(number_line, nl_0, nl_1)

        self.play(Create(nl_group), run_time=2)
        self.play(FadeIn(point_1_4), GrowArrow(arrow_1_4), Write(label_1_4), run_time=2)
        self.wait(10.8) # Toplam 14.8s
        self.play(FadeOut(nl_group), FadeOut(point_1_4), FadeOut(arrow_1_4), FadeOut(label_1_4))
