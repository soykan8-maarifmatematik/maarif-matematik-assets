from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class BirimKesirler(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        title = Text("BİRİM KESİRLER", color=BLACK, weight=BOLD, font_size=65)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(13 / 3.0)

        pizza1 = Circle(radius=1.5, color=ORANGE, fill_opacity=0.3).shift(UP * 2.5)
        line1 = Line(pizza1.get_top(), pizza1.get_bottom(), color=BLACK)
        slice1 = Sector(radius=1.5, angle=PI, start_angle=PI/2, color=RED, fill_opacity=0.8).shift(UP * 2.5)
        label1 = MathTex(r"\frac{1}{2}", color=BLACK, font_size=90).next_to(pizza1, LEFT, buff=0.8)

        pizza2 = Circle(radius=1.5, color=ORANGE, fill_opacity=0.3).shift(DOWN * 0.8)
        line2_v = Line(pizza2.get_top(), pizza2.get_bottom(), color=BLACK)
        line2_h = Line(pizza2.get_left(), pizza2.get_right(), color=BLACK)
        slice2 = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color=RED, fill_opacity=0.8).shift(DOWN * 0.8)
        label2 = MathTex(r"\frac{1}{4}", color=BLACK, font_size=90).next_to(pizza2, LEFT, buff=0.8)

        self.play(Create(pizza1), Create(pizza2))
        self.play(Create(line1), Create(line2_v), Create(line2_h))
        self.wait(14 / 3.0)

        self.play(Create(slice1), Write(label1))
        self.wait(12 / 3.0)

        self.play(Create(slice2), Write(label2))
        self.wait(14 / 3.0)

        result_text = Text("Payda büyüdükçe kesir küçülür!", color=BLACK, weight=BOLD, font_size=45)
        result_text.to_edge(DOWN, buff=2.0)

        compare_text = MathTex(r"\frac{1}{2} > \frac{1}{4}", color=RED, font_size=90)
        compare_text.next_to(result_text, UP, buff=1.0)

        self.play(Write(compare_text))
        self.wait(10 / 3.0)

        self.play(Write(result_text))
        self.wait(11 / 3.0)