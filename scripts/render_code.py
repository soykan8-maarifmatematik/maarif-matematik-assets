from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class BirimKesirler(Scene):
    def construct(self):
        intro_text = Text("Maarif Matematik", color=YELLOW)
        intro_text.scale_to_fit_width(7.0)
        self.play(Write(intro_text))
        self.wait(2.0)

        self.play(FadeOut(intro_text))

        title = Text("Birim Kesirler")
        title.scale_to_fit_width(7.0)
        title.to_edge(UP, buff=1.0)
        self.play(FadeIn(title))
        self.wait(3.6)
        self.wait(2.6)

        circle1_outline = Circle(radius=2, color=WHITE)
        slice1 = Sector(radius=2, angle=PI, color=BLUE, fill_opacity=0.7)
        pasta1 = VGroup(circle1_outline, slice1)
        
        label1 = Text("Bir Bolu Iki")
        label1.scale_to_fit_width(7.0)
        
        circle2_outline = Circle(radius=2, color=WHITE)
        slice2 = Sector(radius=2, angle=PI/2, color=RED, fill_opacity=0.7)
        pasta2 = VGroup(circle2_outline, slice2)
        
        label2 = Text("Bir Bolu Dort")
        label2.scale_to_fit_width(7.0)

        g1 = VGroup(pasta1, label1).arrange(DOWN, buff=0.5)
        g2 = VGroup(pasta2, label2).arrange(DOWN, buff=0.5)

        main_group = VGroup(g1, g2).arrange(DOWN, buff=1.2)

        self.play(Create(circle1_outline), Create(circle2_outline))
        self.wait(2.3)

        self.play(Create(slice1), Write(label1))
        self.wait(2.3)
        self.wait(3.0)

        self.play(Create(slice2), Write(label2))
        self.wait(2.6)
        self.wait(4.3)

        rule_text = Text("Payda Buyurse Dilim Kuculur", color=YELLOW)
        rule_text.scale_to_fit_width(7.0)
        rule_text.to_edge(DOWN, buff=1.0)
        self.play(Write(rule_text))
        self.wait(3.3)

        comp = MathTex(r"\frac{1}{2} > \frac{1}{4}", color=GREEN)
        comp.scale_to_fit_width(7.0)
        comp.move_to(rule_text.get_center())
        self.play(Transform(rule_text, comp))
        self.wait(4.0)

        self.play(FadeOut(main_group), FadeOut(title), FadeOut(rule_text))
        outro_text = Text("Maarif Matematik", color=YELLOW)
        outro_text.scale_to_fit_width(7.0)
        self.play(Write(outro_text))
        self.wait(2.3)

        self.wait(5)
