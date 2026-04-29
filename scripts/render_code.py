from manim import *
config.pixel_height = 1920
config.pixel_width = 1080

class BirimKesirler(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # BAŞLIK
        title = Text("Birim Kesirler", font_size=90, color=BLACK, weight=BOLD).to_edge(UP, buff=1.0)
        
        # GÖRSELLER (Pizzalar)
        pizza1_group = VGroup()
        circle1 = Circle(radius=1.5, color=BLACK, stroke_width=6)
        slice1 = Sector(radius=1.5, angle=PI, color="#FF5733", fill_opacity=0.9)
        label1 = MathTex(r"\frac{1}{2}", font_size=110, color=BLACK).next_to(circle1, DOWN, buff=0.5)
        pizza1_group.add(circle1, slice1, label1).shift(LEFT * 2.5 + UP * 0.5)
        
        pizza2_group = VGroup()
        circle2 = Circle(radius=1.5, color=BLACK, stroke_width=6)
        slice2 = Sector(radius=1.5, angle=PI/2, color="#33A1FF", fill_opacity=0.9)
        line1 = Line(circle2.get_top(), circle2.get_bottom(), color=BLACK, stroke_width=4)
        line2 = Line(circle2.get_left(), circle2.get_right(), color=BLACK, stroke_width=4)
        label2 = MathTex(r"\frac{1}{4}", font_size=110, color=BLACK).next_to(circle2, DOWN, buff=0.5)
        pizza2_group.add(circle2, slice2, line1, line2, label2).shift(RIGHT * 2.5 + UP * 0.5)
        
        greater_than = MathTex(">", font_size=150, color=BLACK).move_to(UP * 0.5)
        
        # ALT METİN
        result = Text("Payda büyüdükçe\nkesir KÜÇÜLÜR!", font_size=80, color=BLACK, weight=BOLD, t2c={"KÜÇÜLÜR!": RED}, text_align="CENTER").to_edge(DOWN, buff=2.0)
        
        # ANİMASYONLAR
        self.play(Write(title), run_time=1.5)
        self.wait(2)
        
        self.play(Create(circle1), Create(circle2), run_time=1.5)
        self.play(Create(line1), Create(line2), run_time=1)
        self.wait(2)
        
        self.play(FadeIn(slice1), Write(label1), run_time=1.5)
        self.wait(2)
        
        self.play(FadeIn(slice2), Write(label2), run_time=1.5)
        self.wait(2)
        
        self.play(Write(greater_than), run_time=1)
        self.wait(2)
        
        self.play(Write(result), run_time=2)
        self.wait(4)
