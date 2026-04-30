from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = '#FFFFFF'
        
        title = Text('BİRİM KESİRLER', font='DejaVu Sans', weight=BOLD, color='#333333').scale(1.2)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(3.6)
        
        pizza1 = Circle(radius=1.5, color='#333333', stroke_width=4)
        pizza2 = Circle(radius=1.5, color='#333333', stroke_width=4)
        pizzas = VGroup(pizza1, pizza2).arrange(RIGHT, buff=0.8).shift(UP * 2.0)
        
        self.play(Create(pizzas))
        self.wait(2.3)
        
        slice1 = Sector(radius=1.5, angle=PI, start_angle=PI/2, color='#007BFF', fill_opacity=0.8)
        slice1.move_to(pizza1.get_center())
        line1 = Line(pizza1.get_top(), pizza1.get_bottom(), color='#333333', stroke_width=4)
        
        frac1 = MathTex(r'\frac{1}{2}', color='#333333').scale(1.5)
        frac1.next_to(pizza1, DOWN, buff=0.8)
        
        self.play(Create(line1))
        self.play(FadeIn(slice1), Write(frac1))
        self.wait(4.6)
        
        slice2 = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color='#FF0000', fill_opacity=0.8)
        slice2.move_to(pizza2.get_center())
        line2_v = Line(pizza2.get_top(), pizza2.get_bottom(), color='#333333', stroke_width=4)
        line2_h = Line(pizza2.get_left(), pizza2.get_right(), color='#333333', stroke_width=4)
        
        frac2 = MathTex(r'\frac{1}{4}', color='#333333').scale(1.5)
        frac2.next_to(pizza2, DOWN, buff=0.8)
        
        self.play(Create(line2_v), Create(line2_h))
        self.play(FadeIn(slice2), Write(frac2))
        self.wait(5.6)
        
        greater_sign = MathTex('>', color='#333333').scale(2.0)
        greater_sign.move_to(VGroup(frac1, frac2).get_center())
        
        bottom_text1 = Text('Payda büyüdükçe', font='DejaVu Sans', weight=BOLD, color='#333333').scale(0.8)
        bottom_text2 = Text('kesir KÜÇÜLÜR!', font='DejaVu Sans', weight=BOLD, color='#007BFF').scale(0.9)
        bottom_group = VGroup(bottom_text1, bottom_text2).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=3.5)
        
        self.play(Write(greater_sign))
        self.play(Write(bottom_group))
        self.wait(5.0)
        
        self.wait(5.0)
