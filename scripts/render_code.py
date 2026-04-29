from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # TITLE
        title = Text("BIRIM KESIRLER", color=BLACK, weight=BOLD).scale(1.1)
        title.to_edge(UP, buff=1.5)
        self.play(Write(title))
        self.wait(2.0)
        
        # MODELS
        pizza1 = VGroup()
        circle1 = Circle(radius=1.5, color=BLACK, stroke_width=4)
        pizza1.add(circle1)
        for i in range(3):
            line = Line(ORIGIN, [1.5*np.cos(i*2*PI/3), 1.5*np.sin(i*2*PI/3), 0], color=BLACK)
            pizza1.add(line)
        pizza1.move_to(LEFT * 2.5)
        
        pizza2 = VGroup()
        circle2 = Circle(radius=1.5, color=BLACK, stroke_width=4)
        pizza2.add(circle2)
        for i in range(6):
            line = Line(ORIGIN, [1.5*np.cos(i*2*PI/6), 1.5*np.sin(i*2*PI/6), 0], color=BLACK)
            pizza2.add(line)
        pizza2.move_to(RIGHT * 2.5)
        
        pizzas = VGroup(pizza1, pizza2).shift(UP * 1.5)
        
        self.play(Create(pizza1), Create(pizza2))
        self.wait(3.0)
        
        # SLICE 1 AND FRACTION 1
        slice1 = Sector(radius=1.5, angle=2*PI/3, start_angle=0, color=ORANGE, fill_opacity=0.8)
        slice1.shift(pizza1.get_center())
        
        frac1 = MathTex(r"\frac{1}{3}", color=BLACK).scale(2.5)
        frac1.next_to(pizza1, DOWN, buff=0.8)
        
        self.play(FadeIn(slice1), Write(frac1))
        self.wait(4.3)
        
        # SLICE 2 AND FRACTION 2
        slice2 = Sector(radius=1.5, angle=2*PI/6, start_angle=0, color=ORANGE, fill_opacity=0.8)
        slice2.shift(pizza2.get_center())
        
        frac2 = MathTex(r"\frac{1}{6}", color=BLACK).scale(2.5)
        frac2.next_to(pizza2, DOWN, buff=0.8)
        
        self.play(FadeIn(slice2), Write(frac2))
        self.wait(5.3)
        
        # COMPARISON SYMBOL
        comp_symbol = Text(">", color=RED, weight=BOLD).scale(2.5)
        comp_symbol.move_to(pizzas.get_center())
        
        self.play(Write(comp_symbol))
        self.wait(2.6)
        
        # BOTTOM TEXT
        bottom_text = VGroup(
            Text("Payda Buyudukce", color=BLUE, weight=BOLD),
            Text("Deger Kuculur", color=RED, weight=BOLD)
        ).arrange(DOWN, buff=0.5).scale(1.2)
        bottom_text.to_edge(DOWN, buff=3.5)
        
        self.play(Write(bottom_text[0]))
        self.wait(3.3)
        
        self.play(Write(bottom_text[1]))
        self.wait(5.3)
