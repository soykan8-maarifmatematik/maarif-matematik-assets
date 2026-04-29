from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        # BAŞLIK
        title = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", color=BLACK, weight=BOLD)
        title.scale(1.2).to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(2.0) # 6 kelime

        # MODELLER
        circle_3 = Circle(radius=1.5, color=BLACK, stroke_width=4)
        sector_3 = Sector(radius=1.5, angle=TAU/3, start_angle=0, color=BLUE, fill_opacity=0.8)
        lines_3 = VGroup(*[Line(ORIGIN, [1.5*np.cos(i*TAU/3), 1.5*np.sin(i*TAU/3), 0], color=BLACK, stroke_width=4) for i in range(3)])
        model_1_3 = VGroup(circle_3, sector_3, lines_3).shift(UP * 2.0 + LEFT * 2.5)

        circle_5 = Circle(radius=1.5, color=BLACK, stroke_width=4)
        sector_5 = Sector(radius=1.5, angle=TAU/5, start_angle=0, color=RED, fill_opacity=0.8)
        lines_5 = VGroup(*[Line(ORIGIN, [1.5*np.cos(i*TAU/5), 1.5*np.sin(i*TAU/5), 0], color=BLACK, stroke_width=4) for i in range(5)])
        model_1_5 = VGroup(circle_5, sector_5, lines_5).shift(UP * 2.0 + RIGHT * 2.5)

        # KESİR SAYILARI
        frac_1_3 = MathTex(r"\frac{1}{3}", color=BLACK).scale(2.5).next_to(model_1_3, DOWN, buff=0.8)
        frac_1_5 = MathTex(r"\frac{1}{5}", color=BLACK).scale(2.5).next_to(model_1_5, DOWN, buff=0.8)

        self.play(FadeIn(frac_1_3), FadeIn(frac_1_5))
        self.wait(4.0) # 12 kelime

        self.play(Create(circle_3), Create(circle_5))
        self.wait(1.33) # 4 kelime

        self.play(Create(lines_3))
        self.play(FadeIn(sector_3))
        self.wait(1.33) # 10 kelime (animasyon süreleri düşüldü)

        self.play(Create(lines_5))
        self.play(FadeIn(sector_5))
        self.wait(2.0) # 12 kelime (animasyon süreleri düşüldü)

        # KARŞILAŞTIRMA SEMBOLÜ
        comp_sym = Text(">", color=BLACK, weight=BOLD).scale(3.0).move_to(UP * 2.0)
        self.play(Write(comp_sym))
        self.wait(2.33) # 7 kelime

        # SONUÇ METNİ
        result_text = Text("Payda Büyüdükçe\nKesir Küçülür!", color=BLACK, weight=BOLD, text_alignment="CENTER")
        result_text.scale(1.5).to_edge(DOWN, buff=3.0)
        self.play(Write(result_text))
        self.wait(5.33) # 10 kelime + 2.0s bitiş payı
