from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        # Title
        title = Text("BİRİM KESİRLER", color=BLACK, weight=BOLD).to_edge(UP, buff=1.5)
        self.play(Write(title))
        self.wait(4.6) # Intro and question

        # Subtitle
        subtitle = Text("Payı 1 olan kesirlerdir", color=DARK_GRAY, font_size=36).next_to(title, DOWN)
        self.play(FadeIn(subtitle))
        self.wait(2.0) # Definition

        # Pizzas (Circles)
        pizza1_base = Circle(radius=1.5, color=BLACK, stroke_width=4).shift(UP * 1.0 + LEFT * 2.2)
        pizza2_base = Circle(radius=1.5, color=BLACK, stroke_width=4).shift(UP * 1.0 + RIGHT * 2.2)
        
        self.play(Create(pizza1_base), Create(pizza2_base))
        self.wait(2.3) # Two pizzas

        # Pizza 1 (1/2)
        line1 = Line(pizza1_base.get_top(), pizza1_base.get_bottom(), color=BLACK)
        slice1 = Sector(radius=1.5, angle=PI, start_angle=PI/2, color=ORANGE, fill_opacity=0.8).shift(UP * 1.0 + LEFT * 2.2)
        label1 = MathTex(r"\frac{1}{2}", color=BLACK, font_size=70).next_to(pizza1_base, DOWN, buff=0.5)
        
        self.play(Create(line1))
        self.play(FadeIn(slice1), Write(label1))
        self.wait(5.0) # 1/2 explanation

        # Pizza 2 (1/8)
        lines2 = VGroup(*[
            Line(pizza2_base.get_center(), pizza2_base.get_center() + np.array([1.5*np.cos(a), 1.5*np.sin(a), 0]), color=BLACK)
            for a in np.linspace(0, 2*PI, 9)[:-1]
        ])
        slice2 = Sector(radius=1.5, angle=PI/4, start_angle=PI/2, color=BLUE, fill_opacity=0.8).shift(UP * 1.0 + RIGHT * 2.2)
        label2 = MathTex(r"\frac{1}{8}", color=BLACK, font_size=70).next_to(pizza2_base, DOWN, buff=0.5)

        self.play(Create(lines2))
        self.play(FadeIn(slice2), Write(label2))
        self.wait(6.0) # 1/8 explanation

        # Comparison
        self.play(Indicate(slice1, color=RED, scale_factor=1.1))
        self.wait(2.6) # Which is bigger?

        # Rule text
        rule_text = Text("Payda büyüdükçe\ndeğer küçülür!", color=RED, weight=BOLD, text_align="center").to_edge(DOWN, buff=3.0)
        self.play(Write(rule_text))
        self.wait(7.0) # Rule explanation

        # Conclusion
        greater_sign = MathTex(">", color=BLACK, font_size=90).move_to((label1.get_center() + label2.get_center()) / 2)
        self.play(Write(greater_sign))
        self.wait(2.3) # 1/2 > 1/8

        # Outro
        self.wait(2.3) # Outro wait
        
        self.play(FadeOut(Group(*self.mobjects)))