from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class MaarifScene(Scene):
    def construct(self):
        title = Text("BİRİM KESİRLER", weight=BOLD, font_size=60).to_edge(UP, buff=1.0)
        self.play(Write(title), run_time=1.6)

        q_text = Text("Payda büyüdükçe\nkesir neden küçülür?", font_size=48).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(q_text), run_time=3.6)
        self.wait(1.3)

        self.play(FadeOut(q_text))

        pizza1 = Circle(radius=2.0, color=ORANGE, fill_opacity=0.2).shift(UP * 1.5)
        self.play(Create(pizza1), run_time=1.6)

        half_pizza = Sector(radius=2.0, angle=PI, start_angle=0, color=ORANGE, fill_opacity=0.8).shift(UP * 1.5)
        line1 = Line(pizza1.get_top(), pizza1.get_bottom(), color=WHITE)
        label_half = MathTex(r"\frac{1}{2}", font_size=72).move_to(pizza1.get_center() + RIGHT * 1.0)

        self.play(Create(line1), FadeIn(half_pizza), Write(label_half), run_time=4.0)

        self.play(
            pizza1.animate.shift(LEFT * 2.5 + UP * 1.0).scale(0.6),
            half_pizza.animate.shift(LEFT * 2.5 + UP * 1.0).scale(0.6),
            line1.animate.shift(LEFT * 2.5 + UP * 1.0).scale(0.6),
            label_half.animate.shift(LEFT * 2.5 + UP * 1.0).scale(0.6),
            run_time=1.5
        )

        pizza2 = Circle(radius=1.2, color=BLUE, fill_opacity=0.2).shift(RIGHT * 2.5 + UP * 2.5)
        self.play(Create(pizza2), run_time=1.5)

        quarter_pizza = Sector(radius=1.2, angle=PI/2, start_angle=0, color=BLUE, fill_opacity=0.8).shift(RIGHT * 2.5 + UP * 2.5)
        line2_v = Line(pizza2.get_top(), pizza2.get_bottom(), color=WHITE)
        line2_h = Line(pizza2.get_left(), pizza2.get_right(), color=WHITE)
        label_quarter = MathTex(r"\frac{1}{4}", font_size=60).move_to(pizza2.get_center() + RIGHT * 0.5 + UP * 0.5)

        self.play(Create(line2_v), Create(line2_h), FadeIn(quarter_pizza), Write(label_quarter), run_time=2.0)

        exp_text1 = Text("Parça sayısı artıyor", font_size=40, color=YELLOW).next_to(pizza2, DOWN, buff=1.0)
        exp_text2 = Text("Dilim küçülüyor", font_size=40, color=RED).next_to(exp_text1, DOWN, buff=0.5)

        self.play(Write(exp_text1), run_time=1.6)
        self.play(Write(exp_text2), run_time=1.7)

        self.wait(2.6)
        self.wait(2.3)

        result = MathTex(r"\frac{1}{2} > \frac{1}{4}", font_size=96, color=GREEN).to_edge(DOWN, buff=2.0)
        self.play(Write(result), run_time=3.0)

        self.wait(1.0)
        self.wait(3.8)
