from manim import *
config.pixel_height = 1920
config.pixel_width = 1080

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        title = Text("Birim Kesirler", color=BLACK, weight=BOLD).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        c1 = Circle(radius=1.2, color=BLACK).shift(UP * 3.5 + LEFT * 1.5)
        s1 = Sector(radius=1.2, angle=TAU/2, color=BLUE, fill_opacity=0.7).move_to(c1.get_center())
        t1 = MathTex(r"\frac{1}{2}", color=BLACK, font_size=72).next_to(c1, RIGHT, buff=1.0)
        
        c2 = Circle(radius=1.2, color=BLACK).shift(UP * 0.5 + LEFT * 1.5)
        s2 = Sector(radius=1.2, angle=TAU/3, color=RED, fill_opacity=0.7).move_to(c2.get_center())
        t2 = MathTex(r"\frac{1}{3}", color=BLACK, font_size=72).next_to(c2, RIGHT, buff=1.0)
        
        c3 = Circle(radius=1.2, color=BLACK).shift(DOWN * 2.5 + LEFT * 1.5)
        s3 = Sector(radius=1.2, angle=TAU/4, color=GREEN, fill_opacity=0.7).move_to(c3.get_center())
        t3 = MathTex(r"\frac{1}{4}", color=BLACK, font_size=72).next_to(c3, RIGHT, buff=1.0)
        
        self.play(Create(c1), Create(c2), Create(c3))
        self.wait(0.5)
        
        self.play(Create(s1), Write(t1))
        self.wait(0.5)
        
        self.play(Create(s2), Write(t2))
        self.wait(0.5)
        
        self.play(Create(s3), Write(t3))
        self.wait(0.5)
        
        result_text = Text("Payda Büyüdükçe Değer Küçülür!", color=RED, weight=BOLD, font_size=48).to_edge(DOWN, buff=2.0)
        comp_text = MathTex(r"\frac{1}{2} > \frac{1}{3} > \frac{1}{4}", color=BLACK, font_size=72).next_to(result_text, UP, buff=0.8)
        
        self.play(Write(result_text))
        self.play(Write(comp_text))
        self.wait(2)