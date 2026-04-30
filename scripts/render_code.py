from manim import *

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        title = Text("BİRİM KESİRLER", font="DejaVu Sans", weight=BOLD, color="#333333").scale(1.2)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(3.0)
        
        subtitle = Text("Payda Büyüdükçe Ne Olur?", font="DejaVu Sans", color="#007BFF").scale(0.8)
        subtitle.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(subtitle))
        self.wait(2.0)
        
        pizza1_base = Circle(radius=1.2, color="#333333", stroke_width=4, fill_color="#EEEEEE", fill_opacity=1)
        pizza2_base = Circle(radius=1.2, color="#333333", stroke_width=4, fill_color="#EEEEEE", fill_opacity=1)
        pizzas = VGroup(pizza1_base, pizza2_base).arrange(RIGHT, buff=0.8).shift(UP * 2.0)
        
        self.play(FadeIn(pizzas))
        self.wait(1.7)
        
        line1 = Line(pizza1_base.get_top(), pizza1_base.get_bottom(), color="#333333", stroke_width=4)
        line2_v = Line(pizza2_base.get_top(), pizza2_base.get_bottom(), color="#333333", stroke_width=4)
        line2_h = Line(pizza2_base.get_left(), pizza2_base.get_right(), color="#333333", stroke_width=4)
        
        self.play(Create(line1), Create(line2_v), Create(line2_h))
        self.wait(3.0)
        
        slice1 = Sector(radius=1.2, angle=PI, start_angle=PI/2, color="#FF0000", fill_opacity=0.8).move_to(pizza1_base.get_center())
        slice2 = Sector(radius=1.2, angle=PI/2, start_angle=PI/2, color="#007BFF", fill_opacity=0.8).move_to(pizza2_base.get_center())
        
        self.play(FadeIn(slice1), FadeIn(slice2))
        self.wait(3.3)
        
        frac1 = MathTex(r"\frac{1}{2}", color="#FF0000").scale(1.5)
        frac2 = MathTex(r"\frac{1}{4}", color="#007BFF").scale(1.5)
        frac1.next_to(pizza1_base, DOWN, buff=0.8)
        frac2.next_to(pizza2_base, DOWN, buff=0.8)
        
        self.play(Write(frac1), Write(frac2))
        self.wait(3.0)
        
        result_text = Text("1/2 > 1/4", font="DejaVu Sans", weight=BOLD, color="#333333").scale(1.5)
        result_text.to_edge(DOWN, buff=3.5)
        
        self.play(Write(result_text))
        self.wait(4.7)