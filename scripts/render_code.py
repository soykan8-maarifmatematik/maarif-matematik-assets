from manim import *

class MaarifScene(Scene):
    def construct(self):
        # 1. MARKA KİMLİĞİ VE ESTETİK
        self.camera.background_color = "#FFFFFF"
        c_text = "#333333"
        c_navy = "#002B4D"
        c_red = "#D32F2F"

        # PARAGRAF 1 (10.0 saniye)
        title = Text("Sen Maarif Matematik", color=c_navy, font_size=40).shift(UP)
        subtitle = Text("Kesirlerin Mantığı", color=c_red, font_size=48)
        
        self.play(Write(title), run_time=1.5)
        self.play(Write(subtitle), run_time=1.5)
        self.wait(6.0)
        self.play(FadeOut(title, subtitle), run_time=1.0)

        # PARAGRAF 2 (10.4 saniye)
        # Görsel Zenginlik: Pasta Dilimi (Sector). outer_radius YASAK, radius KULLANILDI.
        sector1 = Sector(radius=2, angle=PI/2, start_angle=0, color=c_navy, fill_opacity=0.8, stroke_width=3, stroke_color="#FFFFFF")
        sector2 = Sector(radius=2, angle=PI/2, start_angle=PI/2, color=c_navy, fill_opacity=0.8, stroke_width=3, stroke_color="#FFFFFF")
        sector3 = Sector(radius=2, angle=PI/2, start_angle=PI, color=c_navy, fill_opacity=0.8, stroke_width=3, stroke_color="#FFFFFF")
        sector4 = Sector(radius=2, angle=PI/2, start_angle=3*PI/2, color=c_red, fill_opacity=0.9, stroke_width=3, stroke_color="#FFFFFF")
        
        pie = VGroup(sector1, sector2, sector3, sector4).shift(LEFT * 3)
        
        self.play(FadeIn(pie), run_time=2.0)
        self.play(sector4.animate.shift(RIGHT * 0.5 + DOWN * 0.5), run_time=1.5)
        self.wait(6.9)

        # PARAGRAF 3 (14.8 saniye)
        frac_line = Line(LEFT, RIGHT, color=c_text).scale(0.6).shift(RIGHT * 3)
        num = MathTex("1", color=c_red, font_size=60).next_to(frac_line, UP)
        den = MathTex("4", color=c_navy, font_size=60).next_to(frac_line, DOWN)
        fraction = VGroup(num, frac_line, den)

        self.play(Write(fraction), run_time=2.0)

        # Profesyonel Oklar (Arrow)
        arrow_den = Arrow(start=RIGHT * 5.5 + DOWN * 1.5, end=den.get_right(), color=c_navy, buff=0.1)
        label_den = Text("Payda (Bütün)", color=c_navy, font_size=24).next_to(arrow_den, RIGHT)

        arrow_num = Arrow(start=RIGHT * 5.5 + UP * 1.5, end=num.get_right(), color=c_red, buff=0.1)
        label_num = Text("Pay (Alınan)", color=c_red, font_size=24).next_to(arrow_num, RIGHT)

        self.play(GrowArrow(arrow_den), Write(label_den), run_time=2.0)
        self.play(GrowArrow(arrow_num), Write(label_num), run_time=2.0)
        self.wait(6.8)
        
        self.play(
            FadeOut(pie, arrow_num, label_num, arrow_den, label_den), 
            fraction.animate.move_to(ORIGIN).scale(1.5), 
            run_time=2.0
        )

        # PARAGRAF 4 (12.4 saniye)
        arrow_down = Arrow(start=LEFT * 2 + UP * 1.5, end=LEFT * 2 + DOWN * 1.5, color=c_text)
        read_down = Text("Bir bölü dört", color=c_text, font_size=32).next_to(arrow_down, LEFT)

        arrow_up = Arrow(start=RIGHT * 2 + DOWN * 1.5, end=RIGHT * 2 + UP * 1.5, color=c_text)
        read_up = Text("Dörtte bir", color=c_text, font_size=32).next_to(arrow_up, RIGHT)

        self.play(GrowArrow(arrow_down), Write(read_down), run_time=2.0)
        self.play(GrowArrow(arrow_up), Write(read_up), run_time=2.0)
        self.wait(6.4)
        
        self.play(FadeOut(fraction, arrow_down, read_down, arrow_up, read_up), run_time=2.0)

        # PARAGRAF 5 (11.6 saniye)
        # Görsel Zenginlik: Sayı Doğrusu (NumberLine)
        nl = NumberLine(
            x_range=[0, 1, 0.25],
            length=10,
            color=c_text,
            include_numbers=False,
            label_direction=DOWN
        )
        labels = VGroup(
            MathTex("0", color=c_text).next_to(nl.n2p(0), DOWN),
            MathTex("1", color=c_text).next_to(nl.n2p(1), DOWN)
        )

        self.play(Create(nl), Write(labels), run_time=2.0)

        dot = Dot(nl.n2p(0.25), color=c_red, radius=0.12)
        dot_label = MathTex("\\frac{1}{4}", color=c_red, font_size=48).next_to(dot, UP * 1.5)
        arrow_nl = Arrow(start=dot_label.get_bottom(), end=dot.get_top(), color=c_navy, buff=0.1)

        self.play(Create(dot), Write(dot_label), GrowArrow(arrow_nl), run_time=2.0)
        self.wait(7.6)
