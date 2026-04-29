from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        # Title
        title = Text("BİRİM KESİRLER", color=BLACK, weight=BOLD).to_edge(UP, buff=1.0)
        self.play(Write(title), run_time=1.5)
        self.wait(3.5)

        # 1/2 Fraction
        c1_outline = Circle(radius=1.2, color=BLACK).shift(UP * 3.8)
        c1_fill = Sector(radius=1.2, angle=TAU/2, color=ORANGE, fill_opacity=0.8).shift(UP * 3.8)
        t1 = MathTex(r"\frac{1}{2}", color=BLACK).next_to(c1_outline, RIGHT, buff=0.8).scale(2)
        
        self.play(Create(c1_outline), run_time=1.0)
        self.play(FadeIn(c1_fill), Write(t1), run_time=1.5)
        self.wait(1.8)

        # 1/4 Fraction
        c2_outline = Circle(radius=1.2, color=BLACK).shift(UP * 0.8)
        c2_fill = Sector(radius=1.2, angle=TAU/4, color=BLUE, fill_opacity=0.8).shift(UP * 0.8)
        t2 = MathTex(r"\frac{1}{4}", color=BLACK).next_to(c2_outline, RIGHT, buff=0.8).scale(2)

        self.play(Create(c2_outline), run_time=1.0)
        self.play(FadeIn(c2_fill), Write(t2), run_time=1.5)
        self.wait(1.8)

        # 1/8 Fraction
        c3_outline = Circle(radius=1.2, color=BLACK).shift(DOWN * 2.2)
        c3_fill = Sector(radius=1.2, angle=TAU/8, color=GREEN, fill_opacity=0.8).shift(DOWN * 2.2)
        t3 = MathTex(r"\frac{1}{8}", color=BLACK).next_to(c3_outline, RIGHT, buff=0.8).scale(2)

        self.play(Create(c3_outline), run_time=1.0)
        self.play(FadeIn(c3_fill), Write(t3), run_time=1.5)
        self.wait(1.1)

        # Result Text
        result = Text("Payda büyüdükçe değer küçülür!", color=RED, weight=BOLD).scale(0.8).to_edge(DOWN, buff=1.5)
        self.play(Write(result), run_time=1.5)
        self.wait(1.5)

        # Comparison Math
        comp = MathTex(r"\frac{1}{2} > \frac{1}{4} > \frac{1}{8}", color=BLACK).scale(1.5).next_to(result, UP, buff=0.8)
        self.play(Write(comp), run_time=1.5)
        self.wait(5.0)
