from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        title = Text("BİRİM KESİRLER", color="#333333", weight=BOLD).scale(1.2).to_edge(UP, buff=1.0)
        
        left_center = UP * 1.5 + LEFT * 1.8
        right_center = UP * 1.5 + RIGHT * 1.8

        left_circle = Circle(radius=1.5, color="#333333", stroke_width=2).move_to(left_center)
        left_line = Line(left_center + LEFT*1.5, left_center + RIGHT*1.5, color="#333333", stroke_width=2)
        left_sector = Sector(outer_radius=1.5, angle=PI, color="#007BFF", fill_opacity=0.8, stroke_width=2).shift(left_center)

        right_circle = Circle(radius=1.5, color="#333333", stroke_width=2).move_to(right_center)
        right_line1 = Line(right_center + LEFT*1.5, right_center + RIGHT*1.5, color="#333333", stroke_width=2)
        right_line2 = Line(right_center + UP*1.5, right_center + DOWN*1.5, color="#333333", stroke_width=2)
        right_sector = Sector(outer_radius=1.5, angle=PI/2, color="#FF5733", fill_opacity=0.8, stroke_width=2).shift(right_center)

        frac_left = MathTex(r"\frac{1}{2}", color="#333333").scale(1.5).next_to(left_circle, DOWN, buff=0.8)
        frac_right = MathTex(r"\frac{1}{4}", color="#333333").scale(1.5).next_to(right_circle, DOWN, buff=0.8)

        comp_sign = Text(">", color="#333333", weight=BOLD).scale(2).move_to((frac_left.get_center() + frac_right.get_center()) / 2)

        bottom_text = Text("Payda Büyüdükçe\nDilim Küçülür!", color="#333333", weight=BOLD, text_align="CENTER").scale(0.9).to_edge(DOWN, buff=4.5)

        self.play(Write(title))
        self.wait(2.5)

        self.play(Create(left_circle), Create(right_circle))
        self.wait(1.7)

        self.play(Create(left_line))
        self.wait(1.5)

        self.play(FadeIn(left_sector), Write(frac_left))
        self.wait(1.5)

        self.play(Create(right_line1), Create(right_line2))
        self.wait(1.7)

        self.play(FadeIn(right_sector), Write(frac_right))
        self.wait(1.7)

        self.play(Write(comp_sign))
        self.wait(3.5)

        self.play(Write(bottom_text))
        self.wait(3.5)