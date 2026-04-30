from manim import *

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        title = Text("BİRİM KESİRLER", font="DejaVu Sans", weight=BOLD, color="#333333")
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(2.7)

        pizza1 = Circle(radius=1.5, color="#333333", stroke_width=4)
        pizza2 = Circle(radius=1.5, color="#333333", stroke_width=4)

        line1 = Line(pizza1.get_top(), pizza1.get_bottom(), color="#333333")
        line2_v = Line(pizza2.get_top(), pizza2.get_bottom(), color="#333333")
        line2_h = Line(pizza2.get_left(), pizza2.get_right(), color="#333333")

        p1_group = VGroup(pizza1, line1)
        p2_group = VGroup(pizza2, line2_v, line2_h)

        pizzas = VGroup(p1_group, p2_group).arrange(RIGHT, buff=1.0)
        pizzas.shift(UP * 2.0)

        self.play(Create(pizzas))
        self.wait(1.3)

        slice1 = Sector(radius=1.5, angle=PI, start_angle=PI/2, color="#007BFF", fill_opacity=0.8)
        slice1.shift(pizza1.get_center())

        slice2 = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color="#FF0000", fill_opacity=0.8)
        slice2.shift(pizza2.get_center())

        self.play(FadeIn(slice1), FadeIn(slice2))
        self.wait(4.7)

        self.play(Indicate(slice1, color="#007BFF", scale_factor=1.1))
        self.wait(1.3)

        frac1 = MathTex(r"\frac{1}{2}", color="#007BFF").scale(1.5)
        frac1.next_to(p1_group, DOWN, buff=0.8)

        frac2 = MathTex(r"\frac{1}{4}", color="#FF0000").scale(1.5)
        frac2.next_to(p2_group, DOWN, buff=0.8)

        greater_sign = MathTex(">", color="#333333").scale(2)
        greater_sign.move_to((frac1.get_center() + frac2.get_center()) / 2)

        self.play(Write(frac1), Write(frac2))
        self.play(Write(greater_sign))
        self.wait(2.3)

        bottom_text = Text("Payda büyüdükçe\ndilim küçülür!", font="DejaVu Sans", weight=BOLD, color="#333333")
        bottom_text.to_edge(DOWN, buff=3.5)

        self.play(Write(bottom_text))
        self.wait(3.3)
