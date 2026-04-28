from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class BirimKesirler(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        title = Text("Birim Kesirler", color=BLACK, weight=BOLD).scale(1.2).to_edge(UP, buff=2.0)
        
        c1_outline = Circle(radius=1.0, color=BLACK)
        c1_fill = Sector(radius=1.0, angle=PI, color=RED, fill_opacity=0.8)
        c1_group = VGroup(c1_outline, c1_fill)
        t1 = MathTex("\\frac{1}{2}", color=BLACK).scale(2.0)
        g1 = VGroup(c1_group, t1).arrange(DOWN, buff=1.0)

        c2_outline = Circle(radius=1.0, color=BLACK)
        c2_fill = Sector(radius=1.0, angle=TAU/3, color=BLUE, fill_opacity=0.8)
        c2_group = VGroup(c2_outline, c2_fill)
        t2 = MathTex("\\frac{1}{3}", color=BLACK).scale(2.0)
        g2 = VGroup(c2_group, t2).arrange(DOWN, buff=1.0)

        c3_outline = Circle(radius=1.0, color=BLACK)
        c3_fill = Sector(radius=1.0, angle=PI/2, color=GREEN, fill_opacity=0.8)
        c3_group = VGroup(c3_outline, c3_fill)
        t3 = MathTex("\\frac{1}{4}", color=BLACK).scale(2.0)
        g3 = VGroup(c3_group, t3).arrange(DOWN, buff=1.0)

        content = VGroup(g1, g2, g3).arrange(RIGHT, buff=0.8)
        
        main_layout = VGroup(title, content).arrange(DOWN, buff=2.5)
        title.to_edge(UP, buff=2.0)
        content.next_to(title, DOWN, buff=2.5)

        sym1 = MathTex(">", color=BLACK).scale(2.0).move_to(VGroup(t1, t2).get_center())
        sym2 = MathTex(">", color=BLACK).scale(2.0).move_to(VGroup(t2, t3).get_center())

        self.play(Write(title))
        self.wait(2.66)

        self.play(Create(c1_outline), Create(c2_outline), Create(c3_outline))
        self.wait(1.0)

        self.play(Create(c1_fill))
        self.play(Write(t1))
        self.wait(3.66)

        self.play(Create(c2_fill))
        self.play(Write(t2))
        self.wait(2.66)

        self.play(Create(c3_fill))
        self.play(Write(t3))
        self.wait(1.66)

        self.play(Indicate(t1, color=RED, scale_factor=1.5), Indicate(t2, color=RED, scale_factor=1.5), Indicate(t3, color=RED, scale_factor=1.5))
        self.wait(4.0)

        self.play(GrowFromCenter(sym1), GrowFromCenter(sym2))
        self.wait(2.33)

        self.play(Circumscribe(VGroup(t1, sym1, t2, sym2, t3), color=RED, time_width=2))
        self.wait(1.66)

        self.play(FadeOut(*self.mobjects))
        self.wait(2.33)