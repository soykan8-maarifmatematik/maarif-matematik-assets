from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        title = Text("Birim Kesirlerin Büyüklüğü", color=BLACK, weight=BOLD).to_edge(UP, buff=1.5)
        self.play(Write(title))
        self.wait(5.0)
        
        pizza1 = Circle(radius=2.5, color=BLACK).shift(UP * 1.5 + LEFT * 3)
        pizza2 = Circle(radius=2.5, color=BLACK).shift(UP * 1.5 + RIGHT * 3)
        self.play(Create(pizza1), Create(pizza2))
        self.wait(2.3)
        
        line1 = Line(pizza1.get_top(), pizza1.get_bottom(), color=BLACK)
        line2_v = Line(pizza2.get_top(), pizza2.get_bottom(), color=BLACK)
        line2_h = Line(pizza2.get_left(), pizza2.get_right(), color=BLACK)
        self.play(Create(line1), Create(line2_v), Create(line2_h))
        self.wait(3.0)
        
        slice1 = Sector(radius=2.5, angle=PI, start_angle=PI/2, color=RED, fill_opacity=0.8).shift(UP * 1.5 + LEFT * 3)
        label1 = MathTex(r"\frac{1}{2}", color=BLACK, font_size=72).next_to(pizza1, DOWN, buff=0.5)
        self.play(Create(slice1), Write(label1))
        self.wait(3.3)
        
        slice2 = Sector(radius=2.5, angle=PI/2, start_angle=PI/2, color=BLUE, fill_opacity=0.8).shift(UP * 1.5 + RIGHT * 3)
        label2 = MathTex(r"\frac{1}{4}", color=BLACK, font_size=72).next_to(pizza2, DOWN, buff=0.5)
        self.play(Create(slice2), Write(label2))
        self.wait(3.0)
        
        inequality = MathTex(">", color=BLACK, font_size=96).move_to(UP * 1.5)
        self.play(Write(inequality))
        self.play(Indicate(slice1, color=RED), Indicate(slice2, color=BLUE))
        self.wait(4.3)
        
        result_text = Text("Payda büyüdükçe kesir küçülür!", color=BLACK, weight=BOLD).to_edge(DOWN, buff=3.0)
        self.play(Write(result_text))
        self.wait(6.6)
        
        self.wait(4.3)