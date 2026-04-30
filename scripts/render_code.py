from manim import *
import numpy as np

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        title = Text("Birim Kesirleri Karşılaştırma", color=BLACK).scale_to_fit_width(7.5)
        title.to_edge(np.array([0,1,0]), buff=1.2)
        
        sector1 = Sector(start_angle=0, angle=PI, radius=1.1, color=BLUE, fill_opacity=0.8)
        circle1 = Circle(radius=1.1, color=BLACK)
        line1 = Line(np.array([-1.1,0,0]), np.array([1.1,0,0]), color=BLACK)
        label1 = MathTex("\\frac{1}{2}", color=BLACK).next_to(circle1, np.array([0,-1,0]))
        model1 = VGroup(sector1, circle1, line1, label1).shift(np.array([-2.5,0,0]))
        
        sector2 = Sector(start_angle=0, angle=PI/2, radius=1.1, color=RED, fill_opacity=0.8)
        circle2 = Circle(radius=1.1, color=BLACK)
        line2_1 = Line(np.array([-1.1,0,0]), np.array([1.1,0,0]), color=BLACK)
        line2_2 = Line(np.array([0,-1.1,0]), np.array([0,1.1,0]), color=BLACK)
        label2 = MathTex("\\frac{1}{4}", color=BLACK).next_to(circle2, np.array([0,-1,0]))
        model2 = VGroup(sector2, circle2, line2_1, line2_2, label2).shift(np.array([2.5,0,0]))
        
        comp_sign = MathTex(">", color=BLACK).scale(2)
        
        models = VGroup(model1, comp_sign, model2)
        models.scale(0.85).shift(np.array([0,1.5,0]))
        
        result = Text("Payda büyüdükçe değer küçülür!", color=BLACK).scale_to_fit_width(7.5)
        result.to_edge(np.array([0,-1,0]), buff=4.5)
        
        self.play(Write(title))
        self.play(FadeIn(sector1), Create(circle1), Create(line1), Write(label1))
        self.play(FadeIn(sector2), Create(circle2), Create(line2_1), Create(line2_2), Write(label2))
        self.play(Write(comp_sign))
        self.play(Write(result))
        self.wait(2)
