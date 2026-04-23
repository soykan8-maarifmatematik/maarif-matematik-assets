from manim import *

class BirimKesirler(Scene):
    def construct(self):
        config.pixel_height = 1920
        config.pixel_width = 1080
        config.frame_height = 14.22
        config.frame_width = 8.0

        hook_text = Text("2 kişi mi 8 kişi mi", font="sans-serif", font_size=48).to_edge(UP, buff=1)
        self.play(Write(hook_text))
        self.wait(6.0)
        self.play(FadeOut(hook_text))

        pizza1 = Circle(radius=2, color=WHITE).shift(UP*2.5)
        pizza2 = Circle(radius=2, color=WHITE).shift(DOWN*2.5)
        self.play(Create(pizza1), Create(pizza2))
        self.wait(5.0)

        line1 = Line(pizza1.get_top(), pizza1.get_bottom(), color=WHITE)
        lines2 = VGroup(*[Line(pizza2.get_center(), pizza2.get_center() + 2*UP).rotate(i*PI/4, about_point=pizza2.get_center()) for i in range(8)])
        self.play(Create(line1), Create(lines2))
        self.wait(5.8)

        label1 = MathTex(r"\frac{1}{2}", font_size=96).next_to(pizza1, LEFT, buff=0.5)
        slice1 = Sector(outer_radius=2, angle=PI, color=ORANGE, fill_opacity=0.8, arc_center=pizza1.get_center())
        self.play(Write(label1), Create(slice1))
        self.wait(4.0)

        label2 = MathTex(r"\frac{1}{8}", font_size=96).next_to(pizza2, LEFT, buff=0.5)
        slice2 = Sector(outer_radius=2, angle=PI/4, color=ORANGE, fill_opacity=0.8, arc_center=pizza2.get_center())
        self.play(Write(label2), Create(slice2))
        self.wait(6.4)

        rule_text = Text("Payda büyüdükçe dilim küçülür", font="sans-serif", font_size=45, color=YELLOW).move_to(ORIGIN)
        self.play(Write(rule_text))
        self.wait(2.0)

        result_text = MathTex(r"\frac{1}{2} > \frac{1}{8}", font_size=96, color=GREEN).move_to(ORIGIN)
        self.play(ReplacementTransform(rule_text, result_text))
        self.wait(4.0)

        self.play(FadeOut(pizza1), FadeOut(pizza2), FadeOut(line1), FadeOut(lines2), FadeOut(label1), FadeOut(label2), FadeOut(slice1), FadeOut(slice2), FadeOut(result_text))

        outro_text = Text("Daha fazlası için Sen Maarif Matematik", font="sans-serif", font_size=40).move_to(ORIGIN)
        self.play(Write(outro_text))
        self.wait(4.4)