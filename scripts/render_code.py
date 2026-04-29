from manim import *
config.pixel_height = 1920
config.pixel_width = 1080

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # Title
        title = Text("Birim Kesirler", color=BLACK, weight=BOLD, font_size=60)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(11 / 3.0)
        
        # Pizzas
        pizza1_outline = Circle(radius=1.5, color=BLACK, stroke_width=4).move_to(UP * 2.0 + LEFT * 1.5)
        pizza2_outline = Circle(radius=1.5, color=BLACK, stroke_width=4).move_to(DOWN * 1.5 + LEFT * 1.5)
        
        self.play(Create(pizza1_outline), Create(pizza2_outline))
        self.wait(6 / 3.0)
        
        # Pizza 1 slices
        slice1 = Sector(radius=1.5, angle=PI, color=ORANGE, fill_opacity=0.8)
        slice1.shift(pizza1_outline.get_center())
        label1 = MathTex(r"\frac{1}{2}", color=BLACK, font_size=80).next_to(pizza1_outline, RIGHT, buff=1.0)
        
        self.play(Create(slice1), Write(label1))
        self.wait(8 / 3.0)
        
        # Pizza 2 slices
        slice2 = Sector(radius=1.5, angle=PI/2, color=RED, fill_opacity=0.8)
        slice2.shift(pizza2_outline.get_center())
        label2 = MathTex(r"\frac{1}{4}", color=BLACK, font_size=80).next_to(pizza2_outline, RIGHT, buff=1.0)
        
        self.play(Create(slice2), Write(label2))
        self.wait(9 / 3.0)
        
        # Comparison
        self.play(Indicate(slice1, color=YELLOW, scale_factor=1.1))
        self.wait(10 / 3.0)
        
        # Bottom Text
        result_text = Text("Payda Büyüdükçe\nDeğer Küçülür!", color=RED, weight=BOLD, font_size=50, text_align="CENTER")
        result_text.to_edge(DOWN, buff=2.0)
        
        self.play(Write(result_text))
        self.wait(8 / 3.0)
        
        # Outro
        outro = Text("Maarif Matematik", color=BLUE, weight=BOLD, font_size=40).next_to(result_text, DOWN, buff=0.5)
        self.play(FadeIn(outro))
        self.wait(8 / 3.0)
