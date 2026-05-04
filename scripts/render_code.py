from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0
config.background_color = "#FFFFFF"

class MaarifScene(Scene):
    def construct(self):
        title = Text("Birim Kesirleri Karsilastirma", color=BLACK).to_edge(np.array([0,1,0]), buff=1.5).scale_to_fit_width(6.5)
        self.play(Write(title))
        
        sector_half = Sector(radius=1.0, angle=PI, color=BLUE, fill_opacity=0.8)
        circle_half = Circle(radius=1.0, color=BLACK)
        line_half = Line(np.array([-1,0,0]), np.array([1,0,0]), color=BLACK)
        group_half = VGroup(sector_half, circle_half, line_half)
        label_half = MathTex(r"\frac{1}{2}", color=BLACK).next_to(group_half, np.array([0,-1,0]), buff=0.5)
        model_1 = VGroup(group_half, label_half)
        
        sector_quarter = Sector(radius=1.0, angle=PI/2, color=RED, fill_opacity=0.8)
        circle_quarter = Circle(radius=1.0, color=BLACK)
        line_q1 = Line(np.array([-1,0,0]), np.array([1,0,0]), color=BLACK)
        line_q2 = Line(np.array([0,-1,0]), np.array([0,1,0]), color=BLACK)
        group_quarter = VGroup(sector_quarter, circle_quarter, line_q1, line_q2)
        label_quarter = MathTex(r"\frac{1}{4}", color=BLACK).next_to(group_quarter, np.array([0,-1,0]), buff=0.5)
        model_2 = VGroup(group_quarter, label_quarter)
        
        models = VGroup(model_1, model_2).arrange(np.array([1,0,0]), buff=1.5)
        models.scale(0.8).shift(np.array([0,1.8,0]))
        
        self.play(FadeIn(models))
        self.wait(1)
        
        sign = MathTex(">", color=BLACK).scale(2).move_to(models.get_center())
        self.play(Write(sign))
        self.wait(1)
        
        result = Text("Payda buyudukce parca kuculur!", color=BLACK).to_edge(np.array([0,-1,0]), buff=4.8).scale_to_fit_width(6.5)
        self.play(Write(result))
        self.wait(2)