from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class BirimKesirler(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        title = Text("BIRIM KESIRLER", color="#333333", font_size=60).to_edge(UP, buff=1.5)
        self.play(Write(title))
        self.wait(3.6)

        circle1 = Circle(radius=1.0, color="#333333", stroke_width=4)
        circle2 = Circle(radius=1.0, color="#333333", stroke_width=4)
        circle3 = Circle(radius=1.0, color="#333333", stroke_width=4)
        circles = VGroup(circle1, circle2, circle3).arrange(RIGHT, buff=0.5).shift(UP * 1.5)

        self.play(Create(circles))
        self.wait(2.0)

        slice1 = Sector(outer_radius=1.0, angle=PI, color="#007BFF", fill_opacity=0.8).move_to(circle1)
        frac1 = MathTex(r"\frac{1}{2}", color="#333333", font_size=72).next_to(circle1, DOWN, buff=0.5)
        self.play(Create(slice1), Write(frac1))
        self.wait(4.6)

        slice2 = Sector(outer_radius=1.0, angle=2*PI/3, color="#007BFF", fill_opacity=0.8).move_to(circle2)
        frac2 = MathTex(r"\frac{1}{3}", color="#333333", font_size=72).next_to(circle2, DOWN, buff=0.5)
        self.play(Create(slice2), Write(frac2))
        self.wait(4.6)

        slice3 = Sector(outer_radius=1.0, angle=PI/2, color="#007BFF", fill_opacity=0.8).move_to(circle3)
        frac3 = MathTex(r"\frac{1}{4}", color="#333333", font_size=72).next_to(circle3, DOWN, buff=0.5)
        self.play(Create(slice3), Write(frac3))
        self.wait(3.6)

        self.play(Indicate(slice1, color=RED, scale_factor=1.1))
        self.wait(3.6)

        final_text = MarkupText(
            "<span fgcolor='#007BFF'>Payda</span> büyüdükçe,\n<span fgcolor='RED'>dilim</span> küçülür!",
            color="#333333", font_size=55, justify=True
        ).to_edge(DOWN, buff=3.0)

        self.play(Write(final_text))
        self.wait(5.6)

        self.play(Circumscribe(frac1, color=RED, time_width=2))
        self.wait(7.3)