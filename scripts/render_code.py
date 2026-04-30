from manim import *

class UnitFractions(Scene):
    def construct(self):
        config.pixel_height = 1920
        config.pixel_width = 1080
        config.frame_height = 16.0
        config.frame_width = 9.0
        self.camera.background_color = "#FFFFFF"

        title = Text("Birim Kesirler", font="DejaVu Sans", weight=BOLD, color="#333333").scale(1.2)
        title.to_edge(UP, buff=1.0)
        
        self.play(Write(title))
        self.wait(2.0)

        pizza1 = Circle(radius=1.5, color="#333333", fill_opacity=0.1)
        slice1 = Sector(radius=1.5, angle=PI, start_angle=0, color="#007BFF", fill_opacity=0.8)
        line1 = Line(pizza1.get_top(), pizza1.get_bottom(), color="#333333")
        group1 = VGroup(pizza1, slice1, line1)

        pizza2 = Circle(radius=1.5, color="#333333", fill_opacity=0.1)
        slice2 = Sector(radius=1.5, angle=PI/2, start_angle=0, color="#FF0000", fill_opacity=0.8)
        line2_1 = Line(pizza2.get_top(), pizza2.get_bottom(), color="#333333")
        line2_2 = Line(pizza2.get_left(), pizza2.get_right(), color="#333333")
        group2 = VGroup(pizza2, slice2, line2_1, line2_2)

        models = VGroup(group1, group2).arrange(RIGHT, buff=0.8).shift(UP * 2.0)
        
        self.play(FadeIn(pizza1), FadeIn(pizza2))
        self.wait(1.3)

        self.play(Create(line1), Create(line2_1), Create(line2_2))
        self.wait(4.0)

        self.play(FadeIn(slice1), FadeIn(slice2))
        self.wait(2.3)

        frac1 = MathTex(r"\frac{1}{2}", color="#007BFF").scale(2.5)
        frac2 = MathTex(r"\frac{1}{4}", color="#FF0000").scale(2.5)
        
        frac1.set_x(group1.get_x())
        frac2.set_x(group2.get_x())
        fractions = VGroup(frac1, frac2)
        fractions.next_to(models, DOWN, buff=0.8)

        self.play(Write(frac1), Write(frac2))
        self.wait(1.3)

        bottom_text = Text("Payda büyüdükçe\ndeğer küçülür!", font="DejaVu Sans", weight=BOLD, color="#333333").scale(1.0)
        bottom_text.to_edge(DOWN, buff=3.5)
        
        greater_sign = MathTex(">", color="#333333").scale(3.0)
        greater_sign.move_to(fractions.get_center())

        self.play(Write(bottom_text), Write(greater_sign))
        self.wait(3.0)
        self.wait(2.0)