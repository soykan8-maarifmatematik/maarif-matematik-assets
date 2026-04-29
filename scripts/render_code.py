from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        title = Text("BİRİM KESİRLER", color=BLACK, weight=BOLD, font_size=72).to_edge(UP, buff=1.5)
        self.play(Write(title))
        self.wait(1.5)
        self.wait(4.5)
        
        circle1 = Circle(radius=1.5, color=BLACK, stroke_width=4).shift(UP * 1.0 + LEFT * 2.2)
        slice1 = Sector(radius=1.5, angle=PI, color=ORANGE, fill_opacity=0.8).shift(UP * 1.0 + LEFT * 2.2)
        text1 = MathTex(r"\frac{1}{2}", color=BLACK, font_size=72).next_to(circle1, DOWN, buff=0.5)
        
        circle2 = Circle(radius=1.5, color=BLACK, stroke_width=4).shift(UP * 1.0 + RIGHT * 2.2)
        slice2 = Sector(radius=1.5, angle=PI/4, color=BLUE, fill_opacity=0.8).shift(UP * 1.0 + RIGHT * 2.2)
        text2 = MathTex(r"\frac{1}{8}", color=BLACK, font_size=72).next_to(circle2, DOWN, buff=0.5)
        
        self.play(Create(circle1), Create(circle2))
        self.wait(2.5)
        
        self.play(Create(slice1), Write(text1))
        self.wait(4.5)
        
        self.play(Create(slice2), Write(text2))
        self.wait(5.5)
        
        greater_sign = MathTex(">", color=RED, font_size=120).shift(UP * 1.0)
        self.play(Write(greater_sign))
        self.wait(2.5)
        
        result_text = Text("Payda büyüdükçe\nkesir küçülür!", color=BLACK, weight=BOLD, font_size=56, text_alignment="CENTER").to_edge(DOWN, buff=3.0)
        self.play(Write(result_text))
        self.wait(5.5)
        self.wait(2.5)
        self.wait(2.5)
        
        self.play(FadeOut(Group(title, circle1, slice1, text1, circle2, slice2, text2, greater_sign, result_text)))