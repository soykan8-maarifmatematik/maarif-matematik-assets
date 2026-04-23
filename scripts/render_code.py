from manim import *
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        title = Text("Birim Kesirler", font="DejaVu Sans", font_size=60, color=YELLOW)
        title.to_edge(UP, buff=1)
        self.play(Write(title))
        self.wait(2.08)

        desc = Text("Payı 1 olan kesirlerdir.", font="DejaVu Sans", font_size=40)
        desc.next_to(title, DOWN, buff=0.5)
        desc.scale_to_fit_width(6.5)
        self.play(FadeIn(desc))
        self.wait(5.0)

        frac1 = MathTex(r"\frac{1}{2}", font_size=80).shift(LEFT * 2 + UP * 2)
        frac2 = MathTex(r"\frac{1}{4}", font_size=80).shift(RIGHT * 2 + UP * 2)
        self.play(Write(frac1), Write(frac2))
        self.wait(5.83)

        circle1 = Circle(radius=1.5, color=WHITE).next_to(frac1, DOWN, buff=1)
        circle2 = Circle(radius=1.5, color=WHITE).next_to(frac2, DOWN, buff=1)
        self.play(Create(circle1), Create(circle2))
        self.wait(5.0)

        line1 = Line(circle1.get_top(), circle1.get_bottom(), color=WHITE)
        line2_v = Line(circle2.get_top(), circle2.get_bottom(), color=WHITE)
        line2_h = Line(circle2.get_left(), circle2.get_right(), color=WHITE)
        self.play(Create(line1), Create(line2_v), Create(line2_h))

        slice1 = Sector(radius=1.5, angle=PI, start_angle=PI/2, color=BLUE, fill_opacity=0.7, arc_center=circle1.get_center())
        slice2 = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color=RED, fill_opacity=0.7, arc_center=circle2.get_center())
        self.play(FadeIn(slice1), FadeIn(slice2))
        self.wait(5.83)

        greater_sign = MathTex(">", font_size=80).move_to((frac1.get_center() + frac2.get_center()) / 2)
        self.play(Write(greater_sign))
        self.wait(5.83)

        rule = Text("Payda küçüldükçe değer büyür!", font="DejaVu Sans", font_size=45, color=GREEN)
        rule.next_to(circle1, DOWN, buff=1.5)
        rule.scale_to_fit_width(6.5)
        rule.set_x(0)
        self.play(Write(rule))
        self.wait(7.5)

        self.play(FadeOut(Group(title, desc, frac1, frac2, circle1, circle2, line1, line2_v, line2_h, slice1, slice2, greater_sign, rule)))
        self.wait(2.91)