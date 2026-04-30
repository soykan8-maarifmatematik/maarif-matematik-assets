from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class UnitFractions(Scene):
    def construct(self):
        # Arka plan
        self.camera.background_color = "#FFFFFF"
        
        # Baslik
        title = Text("Birim Kesirlerin Büyüklüğü", font="DejaVu Sans", weight=BOLD, color="#333333").scale(1.2)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(2.6)
        
        # Modeller
        circle_half = Circle(radius=1.5, color="#333333", stroke_width=4).shift(UP * 2.0 + LEFT * 2.2)
        sector_half = Sector(radius=1.5, angle=PI, color="#007BFF", fill_opacity=0.8).shift(UP * 2.0 + LEFT * 2.2)
        line_half = Line(circle_half.get_left(), circle_half.get_right(), color="#333333", stroke_width=4)
        
        circle_quarter = Circle(radius=1.5, color="#333333", stroke_width=4).shift(UP * 2.0 + RIGHT * 2.2)
        sector_quarter = Sector(radius=1.5, angle=PI/2, color="#FF0000", fill_opacity=0.8).shift(UP * 2.0 + RIGHT * 2.2)
        line_q1 = Line(circle_quarter.get_left(), circle_quarter.get_right(), color="#333333", stroke_width=4)
        line_q2 = Line(circle_quarter.get_top(), circle_quarter.get_bottom(), color="#333333", stroke_width=4)
        
        self.play(Create(circle_half), Create(circle_quarter))
        self.wait(2.0)
        
        # 1/2 Animasyonu
        self.play(Create(line_half), FadeIn(sector_half))
        frac_half = MathTex(r"\frac{1}{2}", color="#007BFF").scale(2.5).next_to(circle_half, DOWN, buff=0.8)
        self.play(Write(frac_half))
        self.wait(4.0)
        
        # 1/4 Animasyonu
        self.play(Create(line_q1), Create(line_q2), FadeIn(sector_quarter))
        frac_quarter = MathTex(r"\frac{1}{4}", color="#FF0000").scale(2.5).next_to(circle_quarter, DOWN, buff=0.8)
        self.play(Write(frac_quarter))
        self.wait(3.6)
        
        # Alt Metin ve Karsilastirma
        bt1 = Text("Payda büyüdükçe,", font="DejaVu Sans", weight=BOLD, color="#333333")
        bt2 = Text("parçalar küçülür!", font="DejaVu Sans", weight=BOLD, color="#007BFF")
        bottom_group = VGroup(bt1, bt2).arrange(DOWN, buff=0.3).to_edge(DOWN, buff=3.5)
        
        comp_sign = MathTex(">", color="#333333").scale(3.0).move_to((frac_half.get_center() + frac_quarter.get_center()) / 2)
        
        self.play(Write(bottom_group), Write(comp_sign))
        self.wait(5.0)
