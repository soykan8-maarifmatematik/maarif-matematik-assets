from manim import *

class MaarifScene(Scene):
    def construct(self):
        config.pixel_height = 1920
        config.pixel_width = 1080
        config.frame_height = 14.22
        config.frame_width = 8.0
        self.camera.background_color = "#002B4D"

        # KANCA (HOOK)
        hook_text1 = Text("Payda Büyüdükçe", font_size=60, color="#FFFFFF").scale(0.8).shift(UP*2)
        hook_text2 = Text("Kesir Küçülür mü?", font_size=70, color="#FFD700").scale(0.8).next_to(hook_text1, DOWN)
        
        self.play(Write(hook_text1))
        self.play(FadeIn(hook_text2, shift=UP))
        self.wait(3.5)
        self.play(FadeOut(hook_text1), FadeOut(hook_text2))

        # GÖVDE (BODY) - Kesirler
        frac_half = MathTex(r"\frac{1}{2}", font_size=120, color="#FFFFFF").scale(0.8).shift(UP*3 + LEFT*2)
        frac_third = MathTex(r"\frac{1}{3}", font_size=120, color="#FFFFFF").scale(0.8).shift(UP*3)
        frac_fourth = MathTex(r"\frac{1}{4}", font_size=120, color="#FFFFFF").scale(0.8).shift(UP*3 + RIGHT*2)

        self.play(Write(frac_half), Write(frac_third), Write(frac_fourth))
        self.wait(3.5)

        # Pizza Mantığı
        pizza_text = Text("1 Pizzayı...", font_size=50, color="#FFD700").scale(0.8).shift(UP*1)
        self.play(Write(pizza_text))

        # 1/2 Pizza
        circle_half_bg = Circle(radius=1.5, color="#FFFFFF", stroke_width=2).shift(DOWN*1.5 + LEFT*2.2)
        slice_half = Sector(radius=1.5, angle=PI, start_angle=PI/2, color="#FFD700", fill_opacity=0.8).shift(DOWN*1.5 + LEFT*2.2)
        label_half = MathTex(r"\frac{1}{2}", font_size=70, color="#FFFFFF").next_to(circle_half_bg, DOWN)

        # 1/10 Pizza
        circle_ten_bg = Circle(radius=1.5, color="#FFFFFF", stroke_width=2).shift(DOWN*1.5 + RIGHT*2.2)
        slice_ten = Sector(radius=1.5, angle=TAU/10, start_angle=PI/2, color="#FFD700", fill_opacity=0.8).shift(DOWN*1.5 + RIGHT*2.2)
        label_ten = MathTex(r"\frac{1}{10}", font_size=70, color="#FFFFFF").next_to(circle_ten_bg, DOWN)

        self.play(Create(circle_half_bg), Create(circle_ten_bg))
        self.wait(2)
        self.play(Create(slice_half), Write(label_half))
        self.wait(2)
        self.play(Create(slice_ten), Write(label_ten))
        self.wait(3.5)

        # Karşılaştırma
        greater_sign = MathTex(">", font_size=120, color="#FFD700").shift(DOWN*1.5)
        self.play(Write(greater_sign))
        
        rule_text = Text("Parça Sayısı Artarsa\nDilim Küçülür!", font_size=50, color="#FFFFFF", text_align="CENTER").scale(0.8).shift(DOWN*4)
        self.play(Write(rule_text))
        self.wait(5.5)

        self.play(
            FadeOut(frac_half), FadeOut(frac_third), FadeOut(frac_fourth),
            FadeOut(pizza_text), FadeOut(circle_half_bg), FadeOut(slice_half),
            FadeOut(label_half), FadeOut(circle_ten_bg), FadeOut(slice_ten),
            FadeOut(label_ten), FadeOut(greater_sign), FadeOut(rule_text)
        )

        # KAPANIŞ (CTA)
        cta_text1 = Text("Maarif Matematik ile", font_size=60, color="#FFFFFF").scale(0.8).shift(UP*0.5)
        cta_text2 = Text("Mantığını Kavra!", font_size=70, color="#FFD700").scale(0.8).next_to(cta_text1, DOWN)
        self.play(Write(cta_text1))
        self.play(FadeIn(cta_text2, shift=UP))
        self.wait(3)
