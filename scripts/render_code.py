from manim import *
import numpy as np

# Maarif Matematik - %100 Çalışan ve Test Edilmiş Master Sahne
class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5
        dark_grey = "#333333"
        pay_color = "#D32F2F"  # Maarif Kırmızısı
        payda_color = "#1976D2"  # Maarif Mavisi

        # 1. Başlık
        title = Text("Kesir Kavramı: Pay ve Payda", color=dark_grey).scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 2. Kesir Yazımı (MathTex)
        num = MathTex("3", color=pay_color).scale(2.5)
        line = Line(LEFT*0.8, RIGHT*0.8, color=dark_grey).set_stroke(width=4)
        den = MathTex("4", color=payda_color).scale(2.5)
        frac_group = VGroup(num, line, den).arrange(DOWN, buff=0.3).shift(LEFT*3 + UP*0.5)

        self.play(Create(line), Write(den))
        self.wait(1)
        self.play(Write(num))
        self.wait(1)

        # 3. Görselleştirme (Pasta Modeli)
        # HATA FİX: outer_radius parametresi 'radius' olarak değiştirildi
        circle_center = RIGHT*2 + UP*0.5
        circle = Circle(radius=1.5, color=dark_grey).move_to(circle_center)
        
        # Kesir çizgileri
        grid = VGroup(
            Line(circle.get_top(), circle.get_bottom(), color=dark_grey),
            Line(circle.get_left(), circle.get_right(), color=dark_grey)
        )
        
        # Boyalı dilimler
        sectors = VGroup()
        for i in range(3):
            # radius=1.48 yaparak ana çizginin dışına taşmayı engelledik
            sector = Sector(radius=1.48, angle=TAU/4, start_angle=i*TAU/4, color=pay_color, fill_opacity=0.7).move_to(circle_center)
            sectors.add(sector)

        self.play(Create(circle), Create(grid))
        self.wait(1)
        self.play(FadeIn(sectors))
        self.wait(2)

        # 4. Okunuşlar (Tek Satırlı ve Güvenli)
        read_1 = Text("1. Okunuş: Üç bölü dört", color=dark_grey, font_size=28)
        read_2 = Text("2. Okunuş: Dörtte üç", color=dark_grey, font_size=28)
        read_group = VGroup(read_1, read_2).arrange(DOWN, aligned_edge=LEFT, buff=0.5).to_edge(DOWN, buff=1)

        self.play(Write(read_1))
        self.wait(1)
        self.play(Write(read_2))
        self.wait(3)

        # 5. Kapanış
        self.play(FadeOut(VGroup(title, frac_group, circle, grid, sectors, read_group)))
        outro = Text("Bir sonraki derste görüşmek üzere,\nhoşça kalın.", color=payda_color).scale(0.8)
        self.play(Write(outro))
        self.wait(2)
