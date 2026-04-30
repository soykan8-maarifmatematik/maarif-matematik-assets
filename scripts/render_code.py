from manim import *

class UnitFractions(Scene):
    def construct(self):
        config.pixel_width = 1080
        config.pixel_height = 1920
        config.frame_width = 1080 / 100
        config.frame_height = 1920 / 100
        
        self.camera.background_color = "#FFFFFF"
        
        title = Text("BİRİM KESİRLER", font="DejaVu Sans", weight=BOLD, color="#333333").scale(1.2)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(2.0)
        
        circle1 = Circle(radius=1.5, color="#333333")
        slice1 = Sector(radius=1.5, angle=PI, color="#007BFF", fill_opacity=0.8)
        model1 = VGroup(circle1, slice1).shift(UP * 2.0 + LEFT * 2.5)
        
        circle2 = Circle(radius=1.5, color="#333333")
        slice2 = Sector(radius=1.5, angle=PI/2, color="#FF0000", fill_opacity=0.8)
        model2 = VGroup(circle2, slice2).shift(UP * 2.0 + RIGHT * 2.5)
        
        self.play(Create(circle1), Create(circle2))
        self.wait(1.3)
        
        frac1 = MathTex(r"\frac{1}{2}", color="#333333").scale(2.0)
        frac1.next_to(model1, DOWN, buff=0.8)
        self.play(FadeIn(slice1), Write(frac1))
        self.wait(4.0)
        
        frac2 = MathTex(r"\frac{1}{4}", color="#333333").scale(2.0)
        frac2.next_to(model2, DOWN, buff=0.8)
        self.play(FadeIn(slice2), Write(frac2))
        self.wait(3.6)
        
        comp_sign = MathTex(">", color="#333333").scale(2.5)
        comp_sign.move_to((frac1.get_center() + frac2.get_center()) / 2)
        
        bottom_text = Text("Payda büyüdükçe\ndilim küçülür!", font="DejaVu Sans", weight=BOLD, color="#007BFF").scale(0.9)
        bottom_text.to_edge(DOWN, buff=3.5)
        
        self.play(Write(comp_sign), Write(bottom_text))
        self.wait(4.0)
        
        self.play(bottom_text.animate.scale(1.1).set_color("#FF0000"))
        self.wait(4.0)
