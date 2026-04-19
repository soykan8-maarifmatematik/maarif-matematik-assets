from manim import *
import numpy as np

# Maarif Matematik - %100 Çalışan Master Sahne
class MaarifScene(Scene):
    def construct(self):
        # 1. Sahne Ayarları
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5
        text_color = "#333333"
        maarif_blue = "#1976D2"
        maarif_red = "#D32F2F"

        # 2. Giriş ve Başlık
        title = Text("Kesirlerin Mantığı: Pay ve Payda", color=text_color).scale(0.8)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title))
        self.wait(1)

        # 3. Kesir Yazımı (MathTex)
        # Payda (Bütün) ve Pay (Parça) vurgusu
        num = MathTex("3", color=maarif_blue).scale(2.5)
        line = Line(LEFT*0.8, RIGHT*0.8, color=text_color).set_stroke(width=4)
        den = MathTex("4", color=maarif_red).scale(2.5)
        frac_group = VGroup(num, line, den).arrange(DOWN, buff=0.3).shift(LEFT*3 + UP*0.5)

        self.play(Create(line), Write(den))
        self.wait(1)
        self.play(Write(num))
        self.wait(1)

        # 4. Görselleştirme (Pasta Modeli)
        # HATA FİX: outer_radius yerine sadece radius kullanıldı
        circle_center = RIGHT*2 + UP*0.5
        circle = Circle(radius=1.5, color=text_color).move_to(circle_center)
        
        # Kesir Çizgileri
        grid = VGroup(
            Line(circle.get_top(), circle.get_bottom(), color=text_color),
            Line(circle.get_left(), circle.get_right(), color=text_color)
        ).move_to(circle_center)
        
        # Boyalı dilimler (3 parça)
        sectors = VGroup()
        for i in range(3):
            # radius=1.48 yaparak sınır çizgisinin taşmasını engelledik
            sector = Sector(radius=1.48, angle=TAU/4, start_angle=i*TAU/4, 
                           color=maarif_blue, fill_opacity=0.7).move_to(circle_center)
            sectors.add(sector)

        self.play(Create(circle), Create(grid))
        self.wait(1)
        self.play(FadeIn(sectors))
        self.wait(2)

        # 5. Okunuşlar ve Etiketler
        read_1 = Text("1. Okunuş: Üç bölü dört", color=text_color, font_size=28)
        read_2 = Text("2. Okunuş: Dörtte üç", color=text_color, font_size=28)
        read_group = VGroup(read_1, read_2).arrange(DOWN, aligned_edge=LEFT, buff=0.5).to_edge(DOWN, buff=1)

        self.play(Write(read_1))
        self.wait(1)
        self.play(Write(read_2))
        self.wait(3)

        # 6. Kapanış
        self.play(FadeOut(VGroup(title, frac_group, circle, grid, sectors, read_group)))
        outro = Text("Bir sonraki derste görüşmek üzere,\nhoşça kalın.", color=maarif_blue).scale(0.8)
        self.play(Write(outro))
        self.wait(2)
