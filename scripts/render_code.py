from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # Title
        title = Text("BİRİM KESİRLER", color=BLACK, weight=BOLD).to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(2)
        
        # Circle 1 (1/2)
        circle1 = Circle(radius=1.5, color=BLUE).shift(UP * 3.5)
        slice1 = Sector(radius=1.5, angle=PI, color=BLUE, fill_opacity=0.8).shift(UP * 3.5)
        label1 = MathTex(r"\frac{1}{2}", color=BLACK).scale(2.5).next_to(circle1, RIGHT, buff=0.8)
        
        self.play(Create(circle1))
        self.wait(1)
        self.play(Create(slice1), Write(label1))
        self.wait(2)
        
        # Circle 2 (1/4)
        circle2 = Circle(radius=1.5, color=RED).shift(ORIGIN)
        slice2 = Sector(radius=1.5, angle=PI/2, color=RED, fill_opacity=0.8).shift(ORIGIN)
        label2 = MathTex(r"\frac{1}{4}", color=BLACK).scale(2.5).next_to(circle2, RIGHT, buff=0.8)
        
        self.play(Create(circle2))
        self.wait(1)
        self.play(Create(slice2), Write(label2))
        self.wait(2)
        
        # Comparison
        comp = MathTex(r"\frac{1}{2} > \frac{1}{4}", color=BLACK).scale(2.5).shift(DOWN * 3.0)
        self.play(Write(comp))
        self.wait(2)
        
        # Bottom Text
        result = Text("Payda Büyüdükçe Değer Küçülür!", color=BLACK, weight=BOLD).to_edge(DOWN, buff=2.0)
        self.play(Write(result))
        self.wait(3)
