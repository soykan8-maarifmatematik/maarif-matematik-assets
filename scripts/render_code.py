from manim import *

class BirimKesirler(Scene):
    def construct(self):
        config.pixel_height = 1920
        config.pixel_width = 1080
        config.frame_height = 14.22
        config.frame_width = 8.0

        # Hook (21 kelime -> 8.4 saniye)
        hook_text = Text("Payda Buyurse\nKesir Buyur mu?", font_size=60).scale(0.8).shift(UP * 2)
        cross = Cross(hook_text, stroke_color=RED, stroke_width=8)
        self.play(Write(hook_text), run_time=1)
        self.play(Create(cross), run_time=1)
        self.wait(6.4)
        self.play(FadeOut(hook_text), FadeOut(cross))

        # Body 1 (37 kelime -> 14.8 saniye)
        pizza_text = Text("1 Butun Pizza", font_size=50, color=YELLOW).scale(0.8).shift(UP * 3)
        pizza = Circle(radius=2.5, color=ORANGE, fill_opacity=0.5).scale(0.8)
        self.play(Write(pizza_text), run_time=1)
        self.play(Create(pizza), run_time=1)
        self.wait(12.8)

        # Body 2 (29 kelime -> 11.6 saniye)
        half_pizza = Sector(radius=2.0, angle=PI, color=RED, fill_opacity=0.8)
        half_text = MathTex(r"\frac{1}{2}", font_size=80).scale(0.8).shift(UP * 1.5 + LEFT * 1)
        
        eighth_pizza = Sector(radius=2.0, angle=PI/4, color=BLUE, fill_opacity=0.8)
        eighth_text = MathTex(r"\frac{1}{8}", font_size=80).scale(0.8).shift(UP * 1.5 + RIGHT * 1)

        self.play(Transform(pizza, half_pizza), Write(half_text), run_time=1)
        self.wait(4.8)
        self.play(Transform(pizza, eighth_pizza), Transform(half_text, eighth_text), run_time=1)
        self.wait(4.8)
        self.play(FadeOut(pizza), FadeOut(half_text), FadeOut(pizza_text))

        # Body 3 (31 kelime -> 12.4 saniye)
        rule_text1 = Text("Payda Buyurse", font_size=60, color=GREEN).scale(0.8).shift(UP * 1)
        rule_text2 = Text("Dilim Kuculur!", font_size=60, color=RED).scale(0.8).shift(DOWN * 1)
        tiny_text = MathTex(r"\frac{1}{100} = \text{Tek Lokma!}", font_size=50).scale(0.8).shift(DOWN * 3)

        self.play(Write(rule_text1), Write(rule_text2), run_time=1)
        self.play(Write(tiny_text), run_time=1)
        self.wait(10.4)
        self.play(FadeOut(rule_text1), FadeOut(rule_text2), FadeOut(tiny_text))

        # CTA (7 kelime -> 2.8 saniye)
        cta_text = Text("Maarif Matematik ile\nmantigini kavra!", font_size=60, color=YELLOW).scale(0.8)
        self.play(Write(cta_text), run_time=1)
        self.wait(1.8)