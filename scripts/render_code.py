from manim import *
import numpy as np

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5
        text_color = "#333333"
        pay_color = "#1976D2"
        payda_color = "#D32F2F"

        # Başlık
        title = Text("Kesirlerin Mantığı", color=text_color).scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # Kesir Yazımı
        fraction = MathTex(r"\frac{3}{4}", color=text_color).scale(3).move_to(ORIGIN)
        self.play(Write(fraction))
        self.wait(3)

        # OKLAR (HATA FİX: Katmanlama ve Konumlandırma)
        down_arrow = Arrow(start=UP*1.2, end=DOWN*1.2, color=pay_color).next_to(fraction, LEFT, buff=0.5)
        up_arrow = Arrow(start=DOWN*1.2, end=UP*1.2, color=payda_color).next_to(fraction, RIGHT, buff=0.5)
        
        read_1 = Text("Üç bölü dört", color=pay_color, font_size=24).next_to(down_arrow, LEFT)
        read_2 = Text("Dörtte üç", color=payda_color, font_size=24).next_to(up_arrow, RIGHT)

        self.play(GrowArrow(down_arrow), Write(read_1))
        self.wait(10)
        self.play(GrowArrow(up_arrow), Write(read_2))
        self.wait(10)

        # Kapanış
        self.play(FadeOut(Group(*self.mobjects)))
        self.play(Write(Text("Hoşça kalın...", color=pay_color).scale(0.8)))
        self.wait(2)
