from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0
config.background_color = "#FFFFFF"

class MaarifScene(Scene):
    def construct(self):
        title = Text("Birim Kesirlerin Büyüklüğü", color=BLACK)
        title.scale_to_fit_width(6.5)
        title.to_edge(np.array([0,1,0]), buff=1.5)
        
        sector1 = Sector(radius=1.0, angle=PI, color=BLUE, fill_opacity=0.8)
        circle1 = Circle(radius=1.0, color=BLACK)
        line1 = Line(np.array([-1.0,0,0]), np.array([1.0,0,0]), color=BLACK)
        label1 = MathTex(r"\frac{1}{2}", color=BLACK, font_size=72).shift(np.array([0,-1.8,0]))
        model1 = VGroup(sector1, circle1, line1, label1)
        model1.shift(np.array([-2.5, 0, 0]))
        
        sector2 = Sector(radius=1.0, angle=PI/2, color=RED, fill_opacity=0.8)
        circle2 = Circle(radius=1.0, color=BLACK)
        line2_1 = Line(np.array([-1.0,0,0]), np.array([1.0,0,0]), color=BLACK)
        line2_2 = Line(np.array([0,-1.0,0]), np.array([0,1.0,0]), color=BLACK)
        label2 = MathTex(r"\frac{1}{4}", color=BLACK, font_size=72).shift(np.array([0,-1.8,0]))
        model2 = VGroup(sector2, circle2, line2_1, line2_2, label2)
        model2.shift(np.array([2.5, 0, 0]))
        
        gt_sign = MathTex(">", color=BLACK, font_size=96)
        gt_sign.move_to(ORIGIN)
        
        models = VGroup(model1, gt_sign, model2)
        models.scale(0.8)
        models.shift(np.array([0,1.8,0]))
        
        result_text = Text("Payda büyüdükçe değer küçülür!", color=BLACK)
        result_text.scale_to_fit_width(6.5)
        result_text.to_edge(np.array([0,-1,0]), buff=4.8)
        
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeIn(models[0]))
        self.wait(0.5)
        self.play(FadeIn(models[2]))
        self.wait(0.5)
        self.play(Write(models[1]))
        self.wait(0.5)
        self.play(Write(result_text))
        self.wait(2)
