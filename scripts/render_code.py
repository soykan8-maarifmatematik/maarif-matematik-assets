from manim import *

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        title = Text("Birim Kesirler", font="DejaVu Sans", weight=BOLD, color="#333333").scale(1.2)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(3.0)

        self.wait(2.0)

        circle_half = Circle(radius=1.5, color="#333333", stroke_width=4).shift(UP * 2.0)
        slice_half = Sector(radius=1.5, angle=PI, start_angle=0, color="#007BFF", fill_opacity=0.8).shift(UP * 2.0)
        frac_half = MathTex(r"\frac{1}{2}", color="#333333").scale(1.5).next_to(circle_half, DOWN, buff=0.8)

        self.play(Create(circle_half))
        self.play(FadeIn(slice_half))
        self.play(Write(frac_half))
        self.wait(4.0)

        circle_quarter = Circle(radius=1.5, color="#333333", stroke_width=4).shift(UP * 2.0)
        slice_quarter = Sector(radius=1.5, angle=PI/2, start_angle=0, color="#FF0000", fill_opacity=0.8).shift(UP * 2.0)
        frac_quarter = MathTex(r"\frac{1}{4}", color="#333333").scale(1.5).next_to(circle_quarter, DOWN, buff=0.8)

        self.play(
            ReplacementTransform(circle_half, circle_quarter),
            ReplacementTransform(slice_half, slice_quarter),
            ReplacementTransform(frac_half, frac_quarter)
        )
        self.wait(3.6)

        rule_text = Text("Payda Büyürse Kesir Küçülür", font="DejaVu Sans", weight=BOLD, color="#007BFF").scale(0.8)
        rule_text.to_edge(DOWN, buff=3.5)

        self.play(Write(rule_text))
        self.wait(3.0)

        conclusion_text = Text("1/2 > 1/4", font="DejaVu Sans", weight=BOLD, color="#FF0000").scale(1.2)
        conclusion_text.to_edge(DOWN, buff=3.5)

        self.play(ReplacementTransform(rule_text, conclusion_text))
        self.wait(5.3)
