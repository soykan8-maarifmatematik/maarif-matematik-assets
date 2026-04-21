from manim import *
import numpy as np

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5
        text_color = "#333333" # Net Okunur Gri
        pay_color = "#1976D2"  # Maarif Mavisi
        payda_color = "#D32F2F" # Maarif Kırmızısı

        # 1. Başlık
        title = Text("Kesirlerin Okunuş Mantığı", color=text_color).scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # 2. Kesir Yazımı (Büyük ve Net)
        fraction = MathTex(r"\frac{1}{4}", color=text_color).scale(3).move_to(ORIGIN)
        self.play(Write(fraction))
        self.wait(3)

        # 3. Okunuş Okları ve Metinler
        # Aşağı doğru ok (Yukarıdan Aşağıya Okunuş)
        down_arrow = Arrow(start=UP*1.5, end=DOWN*1.5, color=pay_color).next_to(fraction, LEFT, buff=0.8)
        read_1 = Text("Bir bölü dört", color=pay_color, font_size=28).next_to(down_arrow, LEFT)

        # Yukarı doğru ok (Aşağıdan Yukarıya Okunuş)
        up_arrow = Arrow(start=DOWN*1.5, end=UP*1.5, color=payda_color).next_to(fraction, RIGHT, buff=0.8)
        read_2 = Text("Dörtte bir", color=payda_color, font_size=28).next_to(up_arrow, RIGHT)

        # Animasyon Akışı (Sesle uyumlu beklemeler eklendi)
        self.play(GrowArrow(down_arrow))
        self.play(Write(read_1))
        self.wait(15) # Tanım süresi için uzun bekleme

        self.play(GrowArrow(up_arrow))
        self.play(Write(read_2))
        self.wait(15) # Karşılaştırma süresi için uzun bekleme

        # 4. Kapanış
        self.play(FadeOut(Group(*self.mobjects)))
        outro = Text("Hoşça kalın...", color=pay_color).scale(0.8)
        self.play(Write(outro))
        self.wait(2)
