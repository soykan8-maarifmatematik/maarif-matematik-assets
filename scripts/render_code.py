from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        title = Text("Birim Kesirlerin Büyüklüğü", color=BLACK, weight=BOLD)
        title.to_edge(np.array([0,1,0]), buff=1.2)
        title.scale_to_fit_width(6.0)
        
        c1 = Circle(radius=0.9, color=BLACK)
        s1 = Sector(radius=0.9, angle=PI, color=BLUE, fill_opacity=0.8)
        t1 = MathTex("\\frac{1}{2}", color=BLACK).shift(np.array([0,-1.5,0]))
        g1 = VGroup(c1, s1, t1)
        
        c2 = Circle(radius=0.9, color=BLACK)
        s2 = Sector(radius=0.9, angle=2*PI/3, color=RED, fill_opacity=0.8)
        t2 = MathTex("\\frac{1}{3}", color=BLACK).shift(np.array([0,-1.5,0]))
        g2 = VGroup(c2, s2, t2)
        
        c3 = Circle(radius=0.9, color=BLACK)
        s3 = Sector(radius=0.9, angle=PI/2, color=GREEN, fill_opacity=0.8)
        t3 = MathTex("\\frac{1}{4}", color=BLACK).shift(np.array([0,-1.5,0]))
        g3 = VGroup(c3, s3, t3)
        
        models = VGroup(g1, g2, g3)
        models.arrange(np.array([1,0,0]), buff=0.8)
        models.scale(0.8)
        models.shift(np.array([0,1.5,0]))
        
        result_text = Text("Payda büyüdükçe parça küçülür!", color=BLACK)
        result_text.to_edge(np.array([0,-1,0]), buff=4.8)
        result_text.scale_to_fit_width(6.0)
        
        self.play(Write(title))
        self.play(Create(g1))
        self.play(Create(g2))
        self.play(Create(g3))
        self.play(Write(result_text))
        self.wait(2)