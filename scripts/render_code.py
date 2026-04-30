from manim import *

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # BAŞLIK
        title = Text("Birim Kesirler", font="DejaVu Sans", weight=BOLD, color="#333333").scale(1.2)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(1.5)
        
        # MODELLER
        circle_half = Circle(radius=1.5, color="#333333", stroke_width=4)
        slice_half = Sector(radius=1.5, angle=PI, start_angle=PI/2, color="#007BFF", fill_opacity=0.8)
        line_half = Line(circle_half.get_top(), circle_half.get_bottom(), color="#333333", stroke_width=4)
        model_half = VGroup(circle_half, slice_half, line_half)
        
        circle_quarter = Circle(radius=1.5, color="#333333", stroke_width=4)
        slice_quarter = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color="#FF0000", fill_opacity=0.8)
        line_q1 = Line(circle_quarter.get_top(), circle_quarter.get_bottom(), color="#333333", stroke_width=4)
        line_q2 = Line(circle_quarter.get_left(), circle_quarter.get_right(), color="#333333", stroke_width=4)
        model_quarter = VGroup(circle_quarter, slice_quarter, line_q1, line_q2)
        
        models = VGroup(model_half, model_quarter).arrange(RIGHT, buff=1.0)
        models.shift(UP * 2.0)
        
        self.play(FadeIn(models))
        self.wait(3.5)
        
        # KESİR SAYILARI
        frac_half = MathTex(r"\frac{1}{2}", color="#007BFF").scale(2.5)
        frac_quarter = MathTex(r"\frac{1}{4}", color="#FF0000").scale(2.5)
        
        frac_half.next_to(model_half, DOWN, buff=0.8)
        frac_quarter.next_to(model_quarter, DOWN, buff=0.8)
        
        self.play(Write(frac_half), Write(frac_quarter))
        self.wait(3.0)
        
        # BÜYÜKTÜR İŞARETİ
        greater_sign = MathTex(">", color="#333333").scale(2.5)
        greater_sign.move_to(VGroup(frac_half, frac_quarter).get_center())
        self.play(Write(greater_sign))
        self.wait(3.5)
        
        # ALT SONUÇ METNİ
        result_text = Text("Payda büyüdükçe kesir KÜÇÜLÜR!", font="DejaVu Sans", weight=BOLD, color="#333333").scale(0.7)
        result_text.to_edge(DOWN, buff=3.5)
        
        self.play(Write(result_text))
        self.wait(4.5)
