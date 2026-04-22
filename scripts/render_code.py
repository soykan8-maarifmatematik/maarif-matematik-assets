from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class BirimKesirler(Scene):
    def construct(self):
        # KANCA [0-5 sn]
        hook_text = Text("1/2 mi büyük 1/8 mi?", font_size=85)
        hook_text.scale_to_fit_width(7)
        hook_text.to_edge(UP, buff=1)
        self.play(Write(hook_text))
        self.wait(2)

        # GÖVDE [5-50 sn]
        circle1 = Circle(radius=1.8, color=WHITE)
        sector1 = Sector(radius=1.8, angle=PI, color=BLUE, fill_opacity=0.7)
        sector1.move_to(circle1.get_center())
        line1 = Line(circle1.get_top(), circle1.get_bottom(), color=WHITE)
        c1_group = VGroup(circle1, sector1, line1)
        frac1 = MathTex(r"\frac{1}{2}", font_size=110)
        group1 = VGroup(frac1, c1_group).arrange(RIGHT, buff=1)

        circle2 = Circle(radius=1.8, color=WHITE)
        sector2 = Sector(radius=1.8, angle=TAU/8, color=RED, fill_opacity=0.7)
        sector2.move_to(circle2.get_center())
        lines2 = VGroup(*[Line(circle2.get_center(), circle2.get_boundary_point(angle), color=WHITE) for angle in [i * TAU/8 for i in range(8)]])
        c2_group = VGroup(circle2, sector2, lines2)
        frac2 = MathTex(r"\frac{1}{8}", font_size=110)
        group2 = VGroup(frac2, c2_group).arrange(RIGHT, buff=1)

        comparison_group = VGroup(group1, group2).arrange(DOWN, buff=1.5)
        comparison_group.next_to(hook_text, DOWN, buff=1)

        self.play(FadeIn(c1_group), FadeIn(c2_group))
        self.wait(3)

        self.play(Write(frac1), Write(frac2))
        self.wait(4)

        self.play(Indicate(sector2, color=YELLOW))
        self.wait(4)

        result = MathTex(r"\frac{1}{2} > \frac{1}{8}", font_size=110, color=GREEN)
        result.next_to(comparison_group, DOWN, buff=1)
        
        self.play(Write(result))
        self.wait(5)

        self.wait(3)

        # KAPANIŞ [50-60 sn]
        self.play(FadeOut(comparison_group), FadeOut(hook_text), FadeOut(result))
        cta_text = Text("Maarif Matematik ile mantığını kavra takipte kal", font_size=85)
        cta_text.scale_to_fit_width(7)
        self.play(Write(cta_text))
        self.wait(3)