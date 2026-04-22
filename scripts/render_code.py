from manim import *

config.pixel_height = 1920; config.pixel_width = 1080; config.frame_height = 14.22; config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi (Maarif Laciverti)
        self.camera.background_color = "#002B4D"

        # 1. KANCA (HOOK)
        hook_text = MarkupText(
            '<span fgcolor="#FFFFFF">Payda büyüdükçe</span>\n<span fgcolor="#FFD700">kesir küçülür mü?</span>',
            text_align="center",
            font_size=60
        ).scale(0.8).shift(UP*2)
        
        self.play(Write(hook_text), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(hook_text))

        # 2. GÖVDE - 1/2 PİZZA
        pizza_radius = 2.0
        pizza_base = Circle(radius=pizza_radius, color=WHITE, stroke_width=4).shift(UP*1)
        
        half_slice = Sector(radius=pizza_radius, angle=PI, start_angle=PI/2, color="#FFD700", fill_opacity=0.8).shift(UP*1)
        half_line = Line(pizza_base.get_top(), pizza_base.get_bottom(), color=WHITE, stroke_width=4)
        
        half_tex = MathTex(r"\frac{1}{2}", color=WHITE).scale(2).shift(DOWN*2)

        self.play(Create(pizza_base), Create(half_line), run_time=1)
        self.play(FadeIn(half_slice), Write(half_tex), run_time=1.5)
        self.wait(3)

        # 3. GÖVDE - 1/4 PİZZA
        quarter_line = Line(pizza_base.get_left(), pizza_base.get_right(), color=WHITE, stroke_width=4)
        quarter_slice = Sector(radius=pizza_radius, angle=PI/2, start_angle=PI/2, color="#FFD700", fill_opacity=0.8).shift(UP*1)
        quarter_tex = MathTex(r"\frac{1}{4}", color=WHITE).scale(2).shift(DOWN*2)

        self.play(Create(quarter_line), run_time=1)
        self.play(
            Transform(half_slice, quarter_slice),
            Transform(half_tex, quarter_tex),
            run_time=1.5
        )
        self.wait(3)

        # 4. KARŞILAŞTIRMA (COMPARISON)
        self.play(
            FadeOut(pizza_base), FadeOut(half_line), FadeOut(quarter_line), FadeOut(half_tex), FadeOut(half_slice)
        )

        comp_half = Sector(radius=1.5, angle=PI, start_angle=PI/2, color="#FFD700", fill_opacity=0.8).shift(UP*1.5 + LEFT*2)
        comp_quarter = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color="#FFD700", fill_opacity=0.8).shift(UP*1.5 + RIGHT*2)
        
        self.play(FadeIn(comp_half), FadeIn(comp_quarter), run_time=1)
        
        final_eq = MathTex(r"\frac{1}{2}", ">", r"\frac{1}{4}").scale(2).shift(DOWN*1.5)
        final_eq[0].set_color(WHITE)
        final_eq[1].set_color("#FFD700")
        final_eq[2].set_color(WHITE)

        self.play(Write(final_eq), run_time=1.5)
        self.wait(3)

        # 5. KAPANIŞ (CTA)
        cta_text = MarkupText(
            '<span fgcolor="#FFFFFF">Maarif Matematik ile</span>\n<span fgcolor="#FFD700">mantığını kavra!</span>',
            text_align="center",
            font_size=50
        ).scale(0.8).shift(DOWN*3.5)

        self.play(Write(cta_text), run_time=1.5)
        self.wait(2)
