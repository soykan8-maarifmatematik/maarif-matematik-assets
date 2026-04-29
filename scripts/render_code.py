from manim import *
config.pixel_height = 1920
config.pixel_width = 1080

class BirimKesirler(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # Başlık
        title = Text("BİRİM KESİRLER", color=BLACK, font_size=72, weight=BOLD).to_edge(UP, buff=1.0)
        self.play(Write(title), run_time=1.5)
        
        # 1/2 Kesri
        c1 = Circle(radius=1.2, color=BLACK).shift(UP * 3)
        s1 = Sector(radius=1.2, angle=PI, color=RED, fill_opacity=0.8).shift(UP * 3)
        t1 = MathTex(r"\frac{1}{2}", color=BLACK, font_size=96).next_to(c1, RIGHT, buff=1.0)
        self.play(Create(c1), run_time=1)
        self.play(FadeIn(s1), Write(t1), run_time=1.5)
        
        # 1/3 Kesri
        c2 = Circle(radius=1.2, color=BLACK).shift(ORIGIN)
        s2 = Sector(radius=1.2, angle=TAU/3, color=BLUE, fill_opacity=0.8).shift(ORIGIN)
        t2 = MathTex(r"\frac{1}{3}", color=BLACK, font_size=96).next_to(c2, RIGHT, buff=1.0)
        self.play(Create(c2), run_time=1)
        self.play(FadeIn(s2), Write(t2), run_time=1.5)
        
        # 1/4 Kesri
        c3 = Circle(radius=1.2, color=BLACK).shift(DOWN * 3)
        s3 = Sector(radius=1.2, angle=TAU/4, color=GREEN, fill_opacity=0.8).shift(DOWN * 3)
        t3 = MathTex(r"\frac{1}{4}", color=BLACK, font_size=96).next_to(c3, RIGHT, buff=1.0)
        self.play(Create(c3), run_time=1)
        self.play(FadeIn(s3), Write(t3), run_time=1.5)
        
        # Alt Metin (Sonuç)
        result = Text("Payda Büyüdükçe Kesir Küçülür!", color=RED, font_size=54, weight=BOLD).to_edge(DOWN, buff=2.0)
        self.play(Write(result), run_time=2)
        
        self.wait(2)