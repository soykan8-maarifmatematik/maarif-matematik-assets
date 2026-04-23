from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class BirimKesirler(Scene):
    def construct(self):
        hook_text = Text("Pastayı 2'ye mi bölsen", font="sans-serif", font_size=80).scale_to_fit_width(7.2).to_edge(UP, buff=1.0)
        hook_text2 = Text("daha büyük dilim yersin 8'e mi?", font="sans-serif", font_size=80).scale_to_fit_width(7.2).next_to(hook_text, DOWN, buff=0.5)
        
        self.play(Write(hook_text), Write(hook_text2))
        self.wait(1)
        self.play(FadeOut(hook_text), FadeOut(hook_text2))

        circle_half = Circle(radius=1.5, color=WHITE)
        frac_half = MathTex(r"\frac{1}{2}", font_size=120)
        group_half = VGroup(circle_half, frac_half).arrange(DOWN, buff=0.5)

        circle_eighth = Circle(radius=1.5, color=WHITE)
        frac_eighth = MathTex(r"\frac{1}{8}", font_size=120)
        group_eighth = VGroup(circle_eighth, frac_eighth).arrange(DOWN, buff=0.5)

        comparison_group = VGroup(group_half, group_eighth).arrange(DOWN, buff=1.5).move_to(ORIGIN)

        sector_half = Sector(radius=1.5, angle=TAU/2, arc_center=circle_half.get_center(), color=YELLOW, fill_opacity=0.8)
        sector_eighth = Sector(radius=1.5, angle=TAU/8, arc_center=circle_eighth.get_center(), color=RED, fill_opacity=0.8)

        self.play(FadeIn(circle_half), Write(frac_half))
        self.play(Create(sector_half))
        self.wait(1)

        self.play(FadeIn(circle_eighth), Write(frac_eighth))
        self.play(Create(sector_eighth))
        self.wait(1)

        rule_text = Text("Payda büyüdükçe dilim küçülür!", font="sans-serif", font_size=80).scale_to_fit_width(7.2).to_edge(DOWN, buff=2.0)
        self.play(Write(rule_text))
        self.play(Indicate(sector_half), Indicate(sector_eighth))
        self.wait(2)

        self.play(FadeOut(comparison_group), FadeOut(sector_half), FadeOut(sector_eighth), FadeOut(rule_text))

        cta_text = Text("Maarif Matematik ile mantığını kavra", font="sans-serif", font_size=80).scale_to_fit_width(7.2).to_edge(UP, buff=5.0)
        cta_text2 = Text("takipte kal!", font="sans-serif", font_size=80).scale_to_fit_width(7.2).next_to(cta_text, DOWN, buff=0.5)
        self.play(Write(cta_text), Write(cta_text2))
        self.play(Wiggle(cta_text2))
        self.wait(1)