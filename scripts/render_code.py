from manim import *

class UnitFractions(Scene):
    def construct(self):
        # Ekran ayarlari
        config.pixel_height = 1920
        config.pixel_width = 1080
        config.frame_height = 16.0
        config.frame_width = 9.0
        self.camera.background_color = "#FFFFFF"

        # Baslik
        title = Text("Birim Kesirler", font="DejaVu Sans", weight=BOLD, color="#333333").scale(1.2).to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(4.6) # 14 kelime / 3.0

        # Model 1/2
        circle_half = Circle(radius=1.5, color="#333333", stroke_width=4)
        slice_half = Sector(radius=1.5, angle=PI, start_angle=0, color="#007BFF", fill_opacity=0.8)
        model_half = VGroup(circle_half, slice_half).shift(UP * 2.0 + LEFT * 2.0)
        
        frac_half = MathTex(r"\frac{1}{2}", color="#007BFF").scale(2).next_to(model_half, DOWN, buff=0.8)
        
        self.play(Create(circle_half), FadeIn(slice_half), Write(frac_half))
        self.wait(5.0) # 15 kelime / 3.0

        # Model 1/4
        circle_quarter = Circle(radius=1.5, color="#333333", stroke_width=4)
        slice_quarter = Sector(radius=1.5, angle=PI/2, start_angle=0, color="#FF0000", fill_opacity=0.8)
        model_quarter = VGroup(circle_quarter, slice_quarter).shift(UP * 2.0 + RIGHT * 2.0)
        
        frac_quarter = MathTex(r"\frac{1}{4}", color="#FF0000").scale(2).next_to(model_quarter, DOWN, buff=0.8)
        
        self.play(Create(circle_quarter), FadeIn(slice_quarter), Write(frac_quarter))
        self.wait(4.3) # 13 kelime / 3.0

        # Karsilastirma Isareti
        greater_sign = MathTex(">", color="#333333").scale(2.5).move_to((frac_half.get_center() + frac_quarter.get_center()) / 2)
        self.play(Write(greater_sign))
        self.wait(3.3) # 10 kelime / 3.0

        # Alt Sonuc Metni
        bottom_text = Text("Payda buyudukce dilim kuculur!", font="DejaVu Sans", weight=BOLD, color="#333333").scale(0.8).to_edge(DOWN, buff=3.5)
        self.play(Write(bottom_text))
        self.wait(3.6) # 5 kelime / 3.0 + 2.0s bitis payi
