from manim import *
config.pixel_height = 1920
config.pixel_width = 1080

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        title = Text("BIRIM KESIRLER", color=BLACK, weight=BOLD).scale(1.1).to_edge(UP, buff=1.2)
        self.play(Write(title))
        self.wait(1.7)
        
        c1_outline = Circle(radius=1.5, color=BLACK, stroke_width=4)
        c1_line = Line(c1_outline.get_top(), c1_outline.get_bottom(), color=BLACK)
        c1_sector = Sector(radius=1.5, angle=PI, start_angle=PI/2, color=BLUE, fill_opacity=0.8)
        model1 = VGroup(c1_outline, c1_line, c1_sector)
        
        c2_outline = Circle(radius=1.5, color=BLACK, stroke_width=4)
        c2_line1 = Line(c2_outline.get_top(), c2_outline.get_bottom(), color=BLACK)
        c2_line2 = Line(c2_outline.get_left(), c2_outline.get_right(), color=BLACK)
        c2_sector = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color=RED, fill_opacity=0.8)
        model2 = VGroup(c2_outline, c2_line1, c2_line2, c2_sector)
        
        models = VGroup(model1, model2).arrange(RIGHT, buff=1.5).shift(UP * 1.0)
        
        frac1 = MathTex(r"\frac{1}{2}", color=BLACK).scale(2.5).next_to(model1, DOWN, buff=0.5)
        frac2 = MathTex(r"\frac{1}{4}", color=BLACK).scale(2.5).next_to(model2, DOWN, buff=0.5)
        
        bottom_text1 = Text("Payda buyudukce kesir kuculur", color=BLACK, weight=BOLD).scale(0.85).to_edge(DOWN, buff=3.5)
        bottom_text2 = MathTex(r"\frac{1}{2} > \frac{1}{4}", color=BLACK).scale(2.5).to_edge(DOWN, buff=3.5)
        
        self.play(Create(c1_outline), Create(c1_line))
        self.play(FadeIn(c1_sector), Write(frac1))
        self.wait(2.3)
        
        self.play(Create(c2_outline), Create(c2_line1), Create(c2_line2))
        self.play(FadeIn(c2_sector), Write(frac2))
        self.wait(1.7)
        
        self.play(Write(bottom_text1))
        self.wait(2.0)
        
        self.play(ReplacementTransform(bottom_text1, bottom_text2))
        self.wait(5.0)