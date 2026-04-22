from manim import *

class BirimKesirler(Scene):
    def construct(self):
        config.pixel_height = 1920
        config.pixel_width = 1080
        config.frame_height = 14.22
        config.frame_width = 8.0

        # Hook (19 kelime -> 7.6 sn)
        hook_text = Text("PAYDA BUYUDUKCE\nKESIR KUCULUR MU?", font_size=60, color=YELLOW).scale(0.8).shift(UP * 2)
        hook_sub = Text("5 Saniyede Ogren!", font_size=50, color=WHITE).scale(0.8).next_to(hook_text, DOWN)
        self.play(Write(hook_text), FadeIn(hook_sub), run_time=1.5)
        self.wait(6.1)
        self.play(FadeOut(hook_text), FadeOut(hook_sub), run_time=0.5)

        # Body 1: 1/2 (32 kelime -> 12.8 sn)
        pizza_base = Circle(radius=2.5, color=WHITE, stroke_width=4).shift(UP * 1)
        slice_1_2 = Sector(radius=2.5, angle=PI, start_angle=0, color=ORANGE, fill_opacity=0.8).shift(UP * 1)
        
        frac_1_2 = MathTex(r"\frac{1}{2}", font_size=120).scale(0.8).shift(DOWN * 2.5)
        text_1_2 = Text("2 KISI", font_size=60, color=RED).scale(0.8).next_to(frac_1_2, RIGHT, buff=1)
        
        self.play(Create(pizza_base), FadeIn(slice_1_2), run_time=1.5)
        self.play(Write(frac_1_2), Write(text_1_2), run_time=1)
        self.wait(10.3)

        # Body 2: 1/4 (24 kelime -> 9.6 sn)
        slice_1_4 = Sector(radius=2.5, angle=PI/2, start_angle=0, color=ORANGE, fill_opacity=0.8).shift(UP * 1)
        frac_1_4 = MathTex(r"\frac{1}{4}", font_size=120).scale(0.8).shift(DOWN * 2.5)
        text_1_4 = Text("4 KISI", font_size=60, color=RED).scale(0.8).next_to(frac_1_4, RIGHT, buff=1)

        self.play(Transform(slice_1_2, slice_1_4), run_time=1)
        self.play(Transform(frac_1_2, frac_1_4), Transform(text_1_2, text_1_4), run_time=1)
        self.wait(7.6)

        # Body 3: 1/8 (34 kelime -> 13.6 sn)
        slice_1_8 = Sector(radius=2.5, angle=PI/4, start_angle=0, color=ORANGE, fill_opacity=0.8).shift(UP * 1)
        frac_1_8 = MathTex(r"\frac{1}{8}", font_size=120).scale(0.8).shift(DOWN * 2.5)
        text_1_8 = Text("8 KISI", font_size=60, color=RED).scale(0.8).next_to(frac_1_8, RIGHT, buff=1)

        self.play(Transform(slice_1_2, slice_1_8), run_time=1)
        self.play(Transform(frac_1_2, frac_1_8), Transform(text_1_2, text_1_8), run_time=1)
        self.wait(11.6)

        # Clear for CTA
        self.play(FadeOut(pizza_base), FadeOut(slice_1_2), FadeOut(frac_1_2), FadeOut(text_1_2), run_time=0.5)

        # CTA (10 kelime -> 4.0 sn)
        cta_text1 = Text("Maarif Matematik ile", font_size=60, color=YELLOW).scale(0.8).shift(UP * 1)
        cta_text2 = Text("Mantigini Kavra,", font_size=70, color=WHITE).scale(0.8).next_to(cta_text1, DOWN)
        cta_text3 = Text("Takipte Kal!", font_size=70, color=RED).scale(0.8).next_to(cta_text2, DOWN)

        self.play(Write(cta_text1), Write(cta_text2), Write(cta_text3), run_time=1.5)
        self.wait(2.5)