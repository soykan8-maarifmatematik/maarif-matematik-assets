from manim import *
config.pixel_height = 1920
config.pixel_width = 1080

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        title = Text("BİRİM KESİRLER", color=BLACK, weight=BOLD).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        circle1 = Circle(radius=1.2, color=BLACK).shift(UP * 3.5 + LEFT * 1.5)
        slice1 = Sector(radius=1.2, angle=PI, color=RED, fill_opacity=0.8).shift(UP * 3.5 + LEFT * 1.5)
        text1 = MathTex(r"\frac{1}{2}", color=BLACK, font_size=96).next_to(circle1, RIGHT, buff=1.0)
        
        self.play(Create(circle1), FadeIn(slice1))
        self.play(Write(text1))
        self.wait(1)
        
        circle2 = Circle(radius=1.2, color=BLACK).shift(LEFT * 1.5)
        slice2 = Sector(radius=1.2, angle=PI/2, color=BLUE, fill_opacity=0.8).shift(LEFT * 1.5)
        text2 = MathTex(r"\frac{1}{4}", color=BLACK, font_size=96).next_to(circle2, RIGHT, buff=1.0)
        
        self.play(Create(circle2), FadeIn(slice2))
        self.play(Write(text2))
        self.wait(1)
        
        circle3 = Circle(radius=1.2, color=BLACK).shift(DOWN * 3.5 + LEFT * 1.5)
        slice3 = Sector(radius=1.2, angle=PI/4, color=GREEN, fill_opacity=0.8).shift(DOWN * 3.5 + LEFT * 1.5)
        text3 = MathTex(r"\frac{1}{8}", color=BLACK, font_size=96).next_to(circle3, RIGHT, buff=1.0)
        
        self.play(Create(circle3), FadeIn(slice3))
        self.play(Write(text3))
        self.wait(1)
        
        result = Text("Payda büyüdükçe kesir küçülür!", color=RED, weight=BOLD, font_size=48).to_edge(DOWN, buff=2.0)
        self.play(Write(result))
        self.wait(2)