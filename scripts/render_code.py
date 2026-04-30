from manim import *

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        title = Text("BİRİM KESİRLER", font="DejaVu Sans", weight=BOLD, color=BLACK)
        title.scale(1.2)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(3.3)
        self.wait(1.3)

        pizza1_group = VGroup()
        pizza1_base = Circle(radius=1.5, color=BLACK, stroke_width=4).set_fill(WHITE, opacity=1)
        pizza1_slice = Sector(radius=1.5, angle=PI, start_angle=0, color=ORANGE, stroke_width=2).set_fill(ORANGE, opacity=0.8)
        pizza1_line = Line(start=pizza1_base.get_top(), end=pizza1_base.get_bottom(), color=BLACK, stroke_width=4)
        pizza1_group.add(pizza1_base, pizza1_slice, pizza1_line)
        
        pizza2_group = VGroup()
        pizza2_base = Circle(radius=1.5, color=BLACK, stroke_width=4).set_fill(WHITE, opacity=1)
        pizza2_slice = Sector(radius=1.5, angle=PI/2, start_angle=0, color=BLUE, stroke_width=2).set_fill(BLUE, opacity=0.8)
        pizza2_lines = VGroup(
            Line(start=pizza2_base.get_top(), end=pizza2_base.get_bottom(), color=BLACK, stroke_width=4),
            Line(start=pizza2_base.get_left(), end=pizza2_base.get_right(), color=BLACK, stroke_width=4)
        )
        pizza2_group.add(pizza2_base, pizza2_slice, pizza2_lines)

        pizzas = VGroup(pizza1_group, pizza2_group).arrange(RIGHT, buff=1.0)
        pizzas.shift(UP * 2.0)

        frac1 = MathTex(r"\frac{1}{2}", color=BLACK).scale(1.5)
        frac2 = MathTex(r"\frac{1}{4}", color=BLACK).scale(1.5)
        frac1.next_to(pizza1_group, DOWN, buff=0.8)
        frac2.next_to(pizza2_group, DOWN, buff=0.8)

        self.play(Create(pizza1_base), Create(pizza1_line))
        self.play(FadeIn(pizza1_slice))
        self.play(Write(frac1))
        self.wait(4.3)

        self.play(Create(pizza2_base), Create(pizza2_lines))
        self.play(FadeIn(pizza2_slice))
        self.play(Write(frac2))
        self.wait(5.0)

        self.wait(3.0)

        greater_sign = MathTex(">", color=RED).scale(2.5)
        greater_sign.move_to((frac1.get_center() + frac2.get_center()) / 2)
        self.play(Write(greater_sign))
        self.wait(2.3)

        cta = Text("Abone Ol!", font="DejaVu Sans", weight=BOLD, color=RED)
        cta.to_edge(DOWN, buff=3.5)
        self.play(Write(cta))
        self.wait(5.3)
