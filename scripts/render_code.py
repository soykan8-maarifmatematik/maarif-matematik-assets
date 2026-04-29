from manim import *
config.pixel_height = 1920
config.pixel_width = 1080

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        title = Text("BİRİM KESİRLER", font_size=72, color=BLACK, weight=BOLD).to_edge(UP, buff=1.5)
        self.play(Write(title))
        self.wait(2.0)
        
        question = Text("Payda büyüdükçe\nkesir neden küçülür?", font_size=56, color=BLUE, weight=BOLD).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(question))
        self.wait(4.0)
        
        pizza_base = Circle(radius=2.0, color=ORANGE, fill_opacity=0.2).shift(UP * 1.0)
        self.play(Create(pizza_base))
        self.wait(1.0)
        
        slice1 = Sector(radius=2.0, angle=PI, color=ORANGE, fill_opacity=0.8).shift(UP * 1.0)
        label1 = MathTex(r"\frac{1}{2}", color=BLACK, font_size=120).next_to(pizza_base, DOWN, buff=0.5)
        self.play(Create(slice1), Write(label1))
        self.wait(5.0)
        
        self.play(FadeOut(slice1), FadeOut(label1))
        slice2 = Sector(radius=2.0, angle=PI/2, color=RED, fill_opacity=0.8).shift(UP * 1.0)
        label2 = MathTex(r"\frac{1}{4}", color=BLACK, font_size=120).next_to(pizza_base, DOWN, buff=0.5)
        self.play(Create(slice2), Write(label2))
        self.wait(4.5)
        
        self.play(FadeOut(slice2), FadeOut(label2))
        slice3 = Sector(radius=2.0, angle=PI/4, color=PURPLE, fill_opacity=0.8).shift(UP * 1.0)
        label3 = MathTex(r"\frac{1}{8}", color=BLACK, font_size=120).next_to(pizza_base, DOWN, buff=0.5)
        self.play(Create(slice3), Write(label3))
        self.wait(4.5)
        
        self.wait(6.0)
        
        result = MathTex(r"\frac{1}{2} > \frac{1}{8}", color=GREEN, font_size=144).to_edge(DOWN, buff=3.0)
        self.play(Write(result))
        self.wait(4.0)
        
        outro = Text("Maarif Matematik", font_size=56, color=BLACK, weight=BOLD).next_to(result, DOWN, buff=1.0)
        self.play(FadeIn(outro))
        self.wait(2.5)