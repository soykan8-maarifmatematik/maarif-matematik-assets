from manim import *
import numpy as np

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        title = Text("Birim Kesirlerin Büyüklüğü").to_edge(np.array([0,1,0]), buff=1.2).scale_to_fit_width(6.0)
        self.play(Write(title))

        sector_half = Sector(outer_radius=0.9, angle=PI, color=BLUE, fill_opacity=0.7)
        circle_half = Circle(radius=0.9, color=WHITE)
        line_half = Line(np.array([-0.9, 0, 0]), np.array([0.9, 0, 0]), color=WHITE)
        group_half = VGroup(sector_half, circle_half, line_half)

        sector_quarter = Sector(outer_radius=0.9, angle=PI/2, color=RED, fill_opacity=0.7)
        circle_quarter = Circle(radius=0.9, color=WHITE)
        line_q1 = Line(np.array([-0.9, 0, 0]), np.array([0.9, 0, 0]), color=WHITE)
        line_q2 = Line(np.array([0, -0.9, 0]), np.array([0, 0.9, 0]), color=WHITE)
        group_quarter = VGroup(sector_quarter, circle_quarter, line_q1, line_q2)

        models = VGroup(group_half, group_quarter).arrange(np.array([1,0,0]), buff=1.5)
        models.scale(0.8).shift(np.array([0,1.5,0]))

        self.play(Create(sector_half))
        self.play(Create(circle_half))
        self.play(Create(line_half))

        self.play(Create(sector_quarter))
        self.play(Create(circle_quarter))
        self.play(Create(line_q1), Create(line_q2))

        result_text = Text("Payda büyüdükçe parça küçülür!").to_edge(np.array([0,-1,0]), buff=4.8).scale_to_fit_width(6.0)
        self.play(Write(result_text))

        math_result = MathTex(r"\frac{1}{2} > \frac{1}{4}").next_to(result_text, np.array([0,-1,0]), buff=1.0).scale_to_fit_width(6.0)
        self.play(Write(math_result))
        
        self.wait(2)