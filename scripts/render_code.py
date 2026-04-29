from manim import *
config.pixel_height = 1920
config.pixel_width = 1080

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        title = Text("BİRİM KESİRLER", color=BLACK, weight=BOLD, font_size=70)
        title.to_edge(UP, buff=1.0)
        
        circle1 = Circle(radius=1.5, color=BLACK)
        slice1 = Sector(radius=1.5, angle=PI, start_angle=0, color=RED, fill_opacity=0.8)
        label1 = MathTex(r"\frac{1}{2}", color=BLACK, font_size=70).next_to(circle1, LEFT, buff=0.8)
        group1 = VGroup(circle1, slice1, label1)
        
        circle2 = Circle(radius=1.5, color=BLACK)
        slice2 = Sector(radius=1.5, angle=PI/2, start_angle=0, color=BLUE, fill_opacity=0.8)
        label2 = MathTex(r"\frac{1}{4}", color=BLACK, font_size=70).next_to(circle2, LEFT, buff=0.8)
        group2 = VGroup(circle2, slice2, label2)
        
        pizzas = VGroup(group1, group2).arrange(DOWN, buff=1.5).move_to(ORIGIN)
        
        result = Text("Payda büyüdükçe kesir küçülür!", color=BLACK, weight=BOLD, font_size=50)
        result.to_edge(DOWN, buff=2.0)
        
        self.play(Write(title))
        self.wait(7 / 3.0)
        
        self.wait(4 / 3.0)
        
        self.play(Create(circle1), Create(circle2))
        self.wait(5 / 3.0)
        
        line1 = Line(circle1.get_top(), circle1.get_bottom(), color=BLACK)
        self.play(Create(line1))
        self.play(FadeIn(slice1), Write(label1))
        self.wait(13 / 3.0)
        
        line2_v = Line(circle2.get_top(), circle2.get_bottom(), color=BLACK)
        line2_h = Line(circle2.get_left(), circle2.get_right(), color=BLACK)
        self.play(Create(line2_v), Create(line2_h))
        self.play(FadeIn(slice2), Write(label2))
        self.wait(15 / 3.0)
        
        self.play(Indicate(slice1, color=RED, scale_factor=1.1), Indicate(slice2, color=BLUE, scale_factor=1.1))
        self.wait(13 / 3.0)
        
        self.play(Write(result))
        self.wait(7 / 3.0)
        
        self.wait(8 / 3.0)