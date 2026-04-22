from manim import *

class MaarifScene(Scene):
    def construct(self):
        config.pixel_height = 1920
        config.pixel_width = 1080
        config.frame_height = 14.22
        config.frame_width = 8.0
        self.camera.background_color = "#002B4D"

        # KANCA (19 kelime -> 7.6 saniye)
        hook_text = Text("Payda Büyüdükçe\nKesir Büyür mü?", font_size=56, color=WHITE).move_to(UP*2)
        cross = Line(hook_text.get_corner(UL), hook_text.get_corner(DR), color="#D32F2F", stroke_width=12)
        no_text = Text("HAYIR!", font_size=80, color="#D32F2F", weight=BOLD).next_to(hook_text, DOWN, buff=1)

        self.play(Write(hook_text), run_time=2)
        self.play(Create(cross), run_time=1)
        self.play(Write(no_text), run_time=1)
        self.wait(3.6)

        # GÖVDE 1 (29 kelime -> 11.6 saniye)
        self.play(FadeOut(hook_text, cross, no_text), run_time=1)

        pizza1_center = UP * 3.5
        pizza2_center = DOWN * 1.5

        pizza1 = Circle(radius=1.8, color=WHITE).move_to(pizza1_center)
        pizza2 = Circle(radius=1.8, color=WHITE).move_to(pizza2_center)

        line1 = Line(pizza1.get_top(), pizza1.get_bottom(), color=WHITE)
        
        lines2 = VGroup(*[
            Line(pizza2_center + 1.8 * np.array([np.cos(a), np.sin(a), 0]),
                 pizza2_center - 1.8 * np.array([np.cos(a), np.sin(a), 0]), color=WHITE)
            for a in [0, PI/4, PI/2, 3*PI/4]
        ])

        self.play(Create(pizza1), Create(pizza2), run_time=2)
        self.play(Create(line1), Create(lines2), run_time=2)
        self.wait(6.6)

        # GÖVDE 2 (26 kelime -> 10.4 saniye)
        slice1 = Sector(arc_center=pizza1_center, radius=1.8, angle=PI, start_angle=PI/2, color="#FFD700", fill_opacity=0.9)
        slice2 = Sector(arc_center=pizza2_center, radius=1.8, angle=PI/4, start_angle=PI/2, color="#FFD700", fill_opacity=0.9)

        self.play(FadeIn(slice1), FadeIn(slice2), run_time=2)
        self.wait(8.4)

        # GÖVDE 3 (26 kelime -> 10.4 saniye)
        frac1 = MathTex(r"\frac{1}{2}", font_size=80, color=WHITE).next_to(pizza1, LEFT, buff=0.8)
        frac2 = MathTex(r"\frac{1}{8}", font_size=80, color=WHITE).next_to(pizza2, LEFT, buff=0.8)
        
        self.play(Write(frac1), Write(frac2), run_time=2)
        
        comparison = MathTex(r"\frac{1}{2} > \frac{1}{8}", font_size=100, color="#FFD700").move_to(DOWN*5.5)
        self.play(Write(comparison), run_time=2)
        self.wait(6.4)

        # GÖVDE 4 (17 kelime -> 6.8 saniye)
        self.play(
            FadeOut(pizza1, pizza2, line1, lines2, slice1, slice2, frac1, frac2, comparison),
            run_time=1
        )
        rule_text1 = Text("PAYDA BÜYÜDÜKÇE", font_size=64, color=WHITE).move_to(UP*1)
        rule_text2 = Text("DEĞER KÜÇÜLÜR!", font_size=80, color="#FFD700", weight=BOLD).next_to(rule_text1, DOWN, buff=0.5)
        
        self.play(Write(rule_text1), run_time=1)
        self.play(Write(rule_text2), run_time=1)
        self.wait(3.8)

        # KAPANIŞ (14 kelime -> 5.6 saniye)
        self.play(FadeOut(rule_text1, rule_text2), run_time=1)
        cta1 = Text("Mantığını Kavra!", font_size=72, color="#FFD700", weight=BOLD).move_to(UP*0.5)
        cta2 = Text("Maarif Matematik", font_size=56, color=WHITE).next_to(cta1, DOWN, buff=0.5)
        
        self.play(Write(cta1), Write(cta2), run_time=2)
        self.wait(2.6)