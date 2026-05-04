from manim import *
import numpy as np

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        # Başlık
        title = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", color=BLACK, font_size=48).scale_to_fit_width(6.0)
        title.to_edge(np.array([0, 1, 0]), buff=1.2)
        self.play(Write(title))

        # 1/2 Modeli
        circle1 = Circle(radius=0.9, color=BLACK, stroke_width=4)
        sector1 = Sector(radius=0.9, angle=PI, start_angle=0, color=BLUE, fill_opacity=0.7)
        line1_1 = Line(start=np.array([-0.9, 0, 0]), end=np.array([0.9, 0, 0]), color=BLACK, stroke_width=4)
        
        frac1_group = VGroup(circle1, sector1, line1_1)
        frac1_group.shift(np.array([-2.5, 0, 0]))
        label1 = MathTex(r"\frac{1}{2}", color=BLACK).scale(1.5)
        label1.next_to(frac1_group, np.array([0, -1, 0]), buff=0.5)

        # 1/4 Modeli
        circle2 = Circle(radius=0.9, color=BLACK, stroke_width=4)
        sector2 = Sector(radius=0.9, angle=PI/2, start_angle=0, color=RED, fill_opacity=0.7)
        line2_1 = Line(start=np.array([-0.9, 0, 0]), end=np.array([0.9, 0, 0]), color=BLACK, stroke_width=4)
        line2_2 = Line(start=np.array([0, -0.9, 0]), end=np.array([0, 0.9, 0]), color=BLACK, stroke_width=4)
        
        frac2_group = VGroup(circle2, sector2, line2_1, line2_2)
        frac2_group.shift(np.array([2.5, 0, 0]))
        label2 = MathTex(r"\frac{1}{4}", color=BLACK).scale(1.5)
        label2.next_to(frac2_group, np.array([0, -1, 0]), buff=0.5)

        # Karşılaştırma Sembolü
        symbol = MathTex(">", color=BLACK).scale(2.5)
        symbol.move_to(np.array([0, 0, 0]))

        # Modelleri Gruplama ve Konumlandırma
        models_group = VGroup(frac1_group, label1, frac2_group, label2, symbol)
        models_group.scale(0.8).shift(np.array([0, 1.5, 0]))

        # Animasyonlar
        self.play(Create(circle1), Create(circle2))
        self.play(Create(line1_1), Create(line2_1), Create(line2_2))
        self.play(Create(sector1), Create(sector2))
        self.play(Write(label1), Write(label2))
        self.play(Write(symbol))

        # Sonuç Metni
        result_text = Text("Payda büyüdükçe dilim küçülür!", color=BLACK, font_size=40).scale_to_fit_width(6.0)
        result_text.to_edge(np.array([0, -1, 0]), buff=4.8)
        self.play(Write(result_text))
        
        self.wait(2)
