from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # BASLIK (TITLE) - Kesinlikle to_edge(UP, buff=1.0)
        title = Text("Birim Kesirlerde Büyüklük", color=BLACK, weight=BOLD).to_edge(UP, buff=1.0)
        self.play(Write(title))

        # 1/2 KESRI VE GORSELI
        frac_half = MathTex(r"\frac{1}{2}", color=BLACK).scale(2.5).move_to(UP * 3 + LEFT * 2)
        circle_half = Circle(radius=1.2, color=BLACK)
        sector_half = Sector(radius=1.2, angle=PI, color=RED, fill_opacity=0.8)
        circle_half.shift(UP * 3 + RIGHT * 1.5)
        sector_half.shift(UP * 3 + RIGHT * 1.5)
        
        self.play(Write(frac_half))
        self.play(Create(circle_half), FadeIn(sector_half))

        # 1/3 KESRI VE GORSELI
        frac_third = MathTex(r"\frac{1}{3}", color=BLACK).scale(2.5).move_to(ORIGIN + LEFT * 2)
        circle_third = Circle(radius=1.2, color=BLACK)
        sector_third = Sector(radius=1.2, angle=TAU/3, color=BLUE, fill_opacity=0.8)
        circle_third.shift(ORIGIN + RIGHT * 1.5)
        sector_third.shift(ORIGIN + RIGHT * 1.5)

        self.play(Write(frac_third))
        self.play(Create(circle_third), FadeIn(sector_third))

        # 1/4 KESRI VE GORSELI
        frac_quarter = MathTex(r"\frac{1}{4}", color=BLACK).scale(2.5).move_to(DOWN * 3 + LEFT * 2)
        circle_quarter = Circle(radius=1.2, color=BLACK)
        sector_quarter = Sector(radius=1.2, angle=TAU/4, color=GREEN, fill_opacity=0.8)
        circle_quarter.shift(DOWN * 3 + RIGHT * 1.5)
        sector_quarter.shift(DOWN * 3 + RIGHT * 1.5)

        self.play(Write(frac_quarter))
        self.play(Create(circle_quarter), FadeIn(sector_quarter))

        # KARSILASTIRMA ISARETLERI
        gt1 = MathTex(">", color=BLACK).scale(2).move_to(UP * 1.5 + LEFT * 2)
        gt2 = MathTex(">", color=BLACK).scale(2).move_to(DOWN * 1.5 + LEFT * 2)
        self.play(Write(gt1), Write(gt2))

        # ALT METIN (RESULT) - Kesinlikle to_edge(DOWN, buff=2.0)
        result = Text("Payda Büyüdükçe Kesir KÜÇÜLÜR!", color=RED, weight=BOLD).scale(0.8).to_edge(DOWN, buff=2.0)
        self.play(Write(result))
        self.wait(2)
