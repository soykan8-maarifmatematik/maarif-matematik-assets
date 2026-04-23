from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class BirimKesir(Scene):
    def construct(self):
        hook_text = Text("1/2 mi büyük 1/10 mu", color=WHITE).move_to(UP * 5)
        hook_text.scale_to_fit_width(6.5)
        self.play(Write(hook_text))
        self.wait(5.2)

        c1 = Circle(radius=1.5, color=WHITE).move_to(UP * 1.5)
        l1 = VGroup(*[Line(c1.get_center(), c1.get_boundary_point(i * TAU / 2), color=WHITE) for i in range(2)])
        s1 = Sector(radius=1.5, angle=TAU/2, start_angle=0, color=BLUE, fill_opacity=0.8, arc_center=c1.get_center())
        label1 = MathTex("1 / 2", font_size=72, color=BLUE).next_to(c1, RIGHT, buff=0.5)
        
        self.play(Create(c1))
        self.play(Create(l1))
        self.play(FadeIn(s1), Write(label1))
        self.wait(2.0)

        c2 = Circle(radius=1.5, color=WHITE).move_to(DOWN * 2)
        l2 = VGroup(*[Line(c2.get_center(), c2.get_boundary_point(i * TAU / 10), color=WHITE) for i in range(10)])
        s2 = Sector(radius=1.5, angle=TAU/10, start_angle=0, color=RED, fill_opacity=0.8, arc_center=c2.get_center())
        label2 = MathTex("1 / 10", font_size=72, color=RED).next_to(c2, RIGHT, buff=0.5)

        self.play(Create(c2))
        self.play(Create(l2))
        self.play(FadeIn(s2), Write(label2))
        self.wait(2.8)

        exp_text = Text("Payda Büyüdükçe Parça Küçülür", color=YELLOW).move_to(DOWN * 4.5)
        exp_text.scale_to_fit_width(6.5)
        self.play(Write(exp_text))
        self.wait(2.4)

        self.play(FadeOut(exp_text))
        cta_text = Text("Daha fazlası için takip et", color=GREEN).move_to(DOWN * 4.5)
        cta_text.scale_to_fit_width(6.5)
        self.play(Write(cta_text))
        self.wait(4.0)
