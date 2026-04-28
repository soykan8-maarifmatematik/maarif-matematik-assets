from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        text_color = BLACK
        highlight_color = RED
        pizza_color = ORANGE

        title = Text("BİRİM KESİRLER", color=text_color, weight=BOLD).to_edge(UP, buff=2.8)
        self.play(Write(title))
        self.wait(4.0)

        definition = Text("Payı 1 olan kesir", color=BLUE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(definition))
        self.wait(2.0)

        frac_1_2 = MathTex(r"\frac{1}{2}", color=text_color).scale(2).shift(LEFT*2 + UP*1)
        frac_1_4 = MathTex(r"\frac{1}{4}", color=text_color).scale(2).shift(RIGHT*2 + UP*1)
        self.play(Write(frac_1_2), Write(frac_1_4))
        self.wait(3.3)

        pizza1 = Circle(radius=1.5, color=pizza_color, fill_opacity=0.2).next_to(frac_1_2, DOWN, buff=1)
        pizza2 = Circle(radius=1.5, color=pizza_color, fill_opacity=0.2).next_to(frac_1_4, DOWN, buff=1)
        self.play(Create(pizza1), Create(pizza2))
        self.wait(2.3)

        line1 = Line(pizza1.get_top(), pizza1.get_bottom(), color=text_color)
        line2_v = Line(pizza2.get_top(), pizza2.get_bottom(), color=text_color)
        line2_h = Line(pizza2.get_left(), pizza2.get_right(), color=text_color)
        self.play(Create(line1), Create(line2_v), Create(line2_h))
        self.wait(3.0)

        slice1 = Sector(radius=1.5, angle=PI, start_angle=-PI/2, color=highlight_color, fill_opacity=0.6).move_to(pizza1.get_center())
        slice2 = Sector(radius=1.5, angle=PI/2, start_angle=0, color=highlight_color, fill_opacity=0.6).move_to(pizza2.get_center())
        self.play(FadeIn(slice1), FadeIn(slice2))
        self.wait(4.0)

        rule = Text("Payda büyürse dilim küçülür", color=text_color, weight=BOLD).scale(0.8).shift(DOWN*3.0)
        self.play(Write(rule))
        self.wait(1.6)

        greater_sign = MathTex(">", color=RED).scale(2).move_to(UP*1)
        self.play(Write(greater_sign))
        self.wait(3.3)

        arrow = Tex(r"$\rightarrow$", color=BLACK).scale(1.5).next_to(rule, DOWN, buff=0.2)
        advice = Text("Kişi artarsa pay azalır", color=BLUE).scale(0.7).next_to(arrow, DOWN, buff=0.2)
        self.play(Write(arrow), Write(advice))
        self.wait(7.2)

        self.wait(1.5)
        self.play(FadeOut(Group(*self.mobjects)))