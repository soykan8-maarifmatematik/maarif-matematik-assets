from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0
config.background_color = "#FFFFFF"

class MaarifScene(Scene):
    def construct(self):
        title = Text("Birim Kesirlerin Büyüklüğü", color=BLACK).scale_to_fit_width(6.5)
        title.to_edge(np.array([0,1,0]), buff=1.5)
        self.play(Write(title))
        
        c1_group = VGroup()
        sector1 = Sector(radius=1.0, angle=PI, start_angle=0, color="#3498db", fill_opacity=0.8)
        circle1 = Circle(radius=1.0, color=BLACK, stroke_width=4)
        line1 = Line(np.array([-1.0, 0, 0]), np.array([1.0, 0, 0]), color=BLACK, stroke_width=4)
        label1 = MathTex(r"\frac{1}{2}", color=BLACK).scale(1.5).next_to(circle1, np.array([0,-1,0]), buff=0.5)
        c1_group.add(sector1, circle1, line1, label1)
        
        c2_group = VGroup()
        sector2 = Sector(radius=1.0, angle=PI/2, start_angle=0, color="#e74c3c", fill_opacity=0.8)
        circle2 = Circle(radius=1.0, color=BLACK, stroke_width=4)
        lines2 = VGroup(
            Line(np.array([-1.0, 0, 0]), np.array([1.0, 0, 0]), color=BLACK, stroke_width=4),
            Line(np.array([0, -1.0, 0]), np.array([0, 1.0, 0]), color=BLACK, stroke_width=4)
        )
        label2 = MathTex(r"\frac{1}{4}", color=BLACK).scale(1.5).next_to(circle2, np.array([0,-1,0]), buff=0.5)
        c2_group.add(sector2, circle2, lines2, label2)
        
        models = VGroup(c1_group, c2_group).arrange(np.array([1,0,0]), buff=1.5)
        models.scale(0.8).shift(np.array([0,1.8,0]))
        
        self.play(FadeIn(models))
        
        gt_sign = MathTex(">", color=BLACK).scale(2.5).move_to(np.array([0, 1.8, 0]))
        self.play(Write(gt_sign))
        
        result = Text("Payda büyüdükçe kesir küçülür!", color=BLACK, weight=BOLD).scale_to_fit_width(6.5)
        result.to_edge(np.array([0,-1,0]), buff=4.8)
        self.play(Write(result))
        
        self.wait(2)