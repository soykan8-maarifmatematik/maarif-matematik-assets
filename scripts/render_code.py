from manim import *
config.pixel_height = 1920
config.pixel_width = 1080

class BirimKesirler(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        # Baslik
        title = Text("BİRİM KESİRLER", color=BLACK, weight=BOLD, font_size=60)
        title.to_edge(UP, buff=1.0)

        # Intro (11 kelime)
        self.play(Write(title))
        self.wait(11 / 3.0)

        # Modeller
        circle1 = Circle(radius=1.5, color=BLACK)
        sector1 = Sector(radius=1.5, angle=PI, color=RED, fill_opacity=0.8).rotate(-PI/2)
        frac1 = MathTex(r"\frac{1}{2}", color=BLACK, font_size=80).next_to(circle1, DOWN, buff=0.5)
        group1 = VGroup(circle1, sector1, frac1)

        circle2 = Circle(radius=1.5, color=BLACK)
        sector2 = Sector(radius=1.5, angle=PI/2, color=BLUE, fill_opacity=0.8).rotate(-PI/2)
        frac2 = MathTex(r"\frac{1}{4}", color=BLACK, font_size=80).next_to(circle2, DOWN, buff=0.5)
        group2 = VGroup(circle2, sector2, frac2)

        models = VGroup(group1, group2).arrange(RIGHT, buff=1.0).move_to(ORIGIN)

        # 1/2 kismi (14 kelime)
        self.play(Create(circle1), FadeIn(sector1), Write(frac1))
        self.wait(14 / 3.0)

        # 1/4 kismi (11 kelime)
        self.play(Create(circle2), FadeIn(sector2), Write(frac2))
        self.wait(11 / 3.0)

        # Karsilastirma (17 kelime)
        greater_sign = MathTex(">", color=BLACK, font_size=100).move_to(ORIGIN).shift(UP*0.5)
        self.play(Write(greater_sign))
        self.wait(17 / 3.0)

        # Alt Metin
        result_text = Text("Payda büyüdükçe kesir KÜÇÜLÜR!", color=RED, weight=BOLD, font_size=50)
        result_text.to_edge(DOWN, buff=2.0)

        # Sonuc (8 kelime)
        self.play(Write(result_text))
        self.wait(8 / 3.0)
