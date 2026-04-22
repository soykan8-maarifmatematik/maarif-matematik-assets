from manim import *

class MaarifScene(Scene):
    def construct(self):
        config.pixel_height = 1920
        config.pixel_width = 1080
        config.frame_height = 14.22
        config.frame_width = 8.0
        self.camera.background_color = "#002B4D"

        # Title
        title = Text("BİRİM KESİRLER", font_size=60, color="#FFD700", weight=BOLD).move_to(UP * 6)

        # Pizza 1 (1/2)
        pizza1_outline = Circle(radius=1.5, color=WHITE, stroke_width=4)
        pizza1_lines = Line(pizza1_outline.get_top(), pizza1_outline.get_bottom(), color=WHITE)
        pizza1_sector = Sector(radius=1.5, angle=PI, start_angle=PI/2, color="#D32F2F", fill_opacity=0.8)
        pizza1_group = VGroup(pizza1_outline, pizza1_lines, pizza1_sector).move_to(UP * 2.5 + LEFT * 1.5)
        
        label1 = MathTex(r"\frac{1}{2}", font_size=90, color=WHITE).next_to(pizza1_group, RIGHT, buff=1)

        # Pizza 2 (1/8)
        pizza2_outline = Circle(radius=1.5, color=WHITE, stroke_width=4)
        pizza2_lines = VGroup(
            Line(pizza2_outline.get_top(), pizza2_outline.get_bottom(), color=WHITE),
            Line(pizza2_outline.get_left(), pizza2_outline.get_right(), color=WHITE),
            Line(pizza2_outline.point_at_angle(PI/4), pizza2_outline.point_at_angle(5*PI/4), color=WHITE),
            Line(pizza2_outline.point_at_angle(3*PI/4), pizza2_outline.point_at_angle(7*PI/4), color=WHITE)
        )
        pizza2_sector = Sector(radius=1.5, angle=PI/4, start_angle=PI/2, color="#FFD700", fill_opacity=0.8)
        pizza2_group = VGroup(pizza2_outline, pizza2_lines, pizza2_sector).move_to(DOWN * 1.5 + LEFT * 1.5)
        
        label2 = MathTex(r"\frac{1}{8}", font_size=90, color=WHITE).next_to(pizza2_group, RIGHT, buff=1)

        # Comparison & Rule
        comparison = MathTex(r"\frac{1}{2} > \frac{1}{8}", font_size=90, color="#FFD700").move_to(DOWN * 4.5)
        rule = Text("Payda Büyürse, Değer Küçülür!", font_size=40, color=WHITE).next_to(comparison, DOWN, buff=0.5)

        # CTA
        cta = Text("Maarif Matematik ile Mantığını Kavra!", font_size=35, color="#D32F2F", weight=BOLD).move_to(DOWN * 6.5)

        # --- ANIMATIONS ---
        # Hook (7.2s)
        self.play(Write(title), run_time=1)
        self.wait(6.2)

        # Body 1 (10.4s)
        self.play(Create(pizza1_outline), run_time=1)
        self.play(Create(pizza1_lines), run_time=1)
        self.play(FadeIn(pizza1_sector), run_time=1)
        self.play(Write(label1), run_time=1)
        self.wait(6.4)

        # Body 2 (7.6s)
        self.play(Create(pizza2_outline), run_time=1)
        self.play(Create(pizza2_lines), run_time=1)
        self.play(FadeIn(pizza2_sector), run_time=1)
        self.play(Write(label2), run_time=1)
        self.wait(3.6)

        # Body 3 (10.0s)
        self.play(Indicate(label1, color="#FFD700", scale_factor=1.2), run_time=1)
        self.play(Indicate(label2, color="#FFD700", scale_factor=1.2), run_time=1)
        self.wait(8.0)

        # Body 4 (10.4s)
        self.play(Write(comparison), run_time=1)
        self.play(Write(rule), run_time=1)
        self.wait(8.4)

        # CTA (7.6s)
        self.play(Write(cta), run_time=1)
        self.wait(6.6)