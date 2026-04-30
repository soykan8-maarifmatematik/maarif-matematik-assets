from manim import *
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        # BASLIK
        title = Text("Birim Kesirleri\nKarşılaştırma", color=BLACK, weight=BOLD).to_edge(UP, buff=1.0).scale_to_fit_width(7.0)
        self.play(Write(title))
        self.wait(0.5)

        # MODEL 1: 1/2
        sector_half = Sector(radius=1.5, angle=PI, color=BLUE, fill_opacity=0.8).shift(UP * 2.0 + LEFT * 2.2)
        circle_half = Circle(radius=1.5, color=BLACK, stroke_width=5).shift(UP * 2.0 + LEFT * 2.2)
        line_half = Line(start=LEFT*1.5, end=RIGHT*1.5, color=BLACK, stroke_width=5).shift(UP * 2.0 + LEFT * 2.2)
        label_half = MathTex(r"\frac{1}{2}", color=BLACK).scale(1.8).next_to(circle_half, DOWN, buff=0.5)

        self.play(FadeIn(sector_half))
        self.play(Create(circle_half))
        self.play(Create(line_half))
        self.play(Write(label_half))
        self.wait(0.5)

        # MODEL 2: 1/4
        sector_quarter = Sector(radius=1.5, angle=PI/2, color=RED, fill_opacity=0.8).shift(UP * 2.0 + RIGHT * 2.2)
        circle_quarter = Circle(radius=1.5, color=BLACK, stroke_width=5).shift(UP * 2.0 + RIGHT * 2.2)
        line_quarter_1 = Line(start=LEFT*1.5, end=RIGHT*1.5, color=BLACK, stroke_width=5).shift(UP * 2.0 + RIGHT * 2.2)
        line_quarter_2 = Line(start=DOWN*1.5, end=UP*1.5, color=BLACK, stroke_width=5).shift(UP * 2.0 + RIGHT * 2.2)
        label_quarter = MathTex(r"\frac{1}{4}", color=BLACK).scale(1.8).next_to(circle_quarter, DOWN, buff=0.5)

        self.play(FadeIn(sector_quarter))
        self.play(Create(circle_quarter))
        self.play(Create(line_quarter_1), Create(line_quarter_2))
        self.play(Write(label_quarter))
        self.wait(0.5)

        # KARSILASTIRMA ISARETI
        greater_sign = MathTex(">", color=BLACK).scale(2.5).shift(UP * 2.0)
        self.play(Write(greater_sign))
        self.wait(1)

        # SONUC METNI
        result = Text("Payda büyüdükçe\ndilim küçülür!", color=BLACK, weight=BOLD).to_edge(DOWN, buff=4.5).scale_to_fit_width(7.0)
        self.play(Write(result))
        self.wait(2)