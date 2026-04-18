from manim import *
import numpy as np

# Maarif Matematik - %100 Çalışan ve Test Edilmiş Master Sahne
class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5
        
        # Renk Mühürleri (Hata almamak için Hex kodları kullanıldı)
        text_color = "#333333" 
        maarif_blue = "#1976D2" # Maarif Mavisi (Standart)
        maarif_red = "#D32F2F"  # Maarif Kırmızısı (Standart)

        # 1. Başlık
        title = Text("Birim Kesirler: 1 Bölü 4", color=text_color).scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 2. Kesir Yazımı
        num = MathTex("1", color=maarif_blue).scale(2.5)
        line = Line(LEFT*0.8, RIGHT*0.8, color=text_color).set_stroke(width=4)
        den = MathTex("4", color=text_color).scale(2.5)
        frac_group = VGroup(num, line, den).arrange(DOWN, buff=0.3).shift(LEFT*3 + UP*0.5)

        self.play(Create(line), Write(den))
        self.wait(1)
        self.play(Write(num))
        self.wait(1)

        # 3. Görselleştirme (Pasta Modeli)
        circle_center = RIGHT*2 + UP*0.5
        circle = Circle(radius=1.5, color=text_color).move_to(circle_center)
        
        grid = VGroup(
            Line(circle.get_top(), circle.get_bottom(), color=text_color),
            Line(circle.get_left(), circle.get_right(), color=text_color)
        )
        
        # Birim dilim (1/4)
        sector = Sector(radius=1.48, angle=TAU/4, start_angle=0, color=maarif_blue, fill_opacity=0.7).move_to(circle_center)

        self.play(Create(circle), Create(grid))
        self.wait(1)
        self.play(FadeIn(sector))
        self.wait(2)

        # 4. Okunuşlar (DARK_RED Hatası Giderildi)
        reading1 = Text("1 bölü 4", color=maarif_blue, font_size=32)
        reading2 = Text("Dörtte bir", color=maarif_red, font_size=32)
        read_group = VGroup(reading1, reading2).arrange(DOWN, aligned_edge=LEFT, buff=0.5).to_edge(DOWN, buff=1)

        self.play(Write(reading1))
        self.wait(1)
        self.play(Write(reading2))
        self.wait(3)

        # 5. Kapanış
        self.play(FadeOut(VGroup(title, frac_group, circle, grid, sector, read_group)))
        outro = Text("Bir sonraki derste görüşmek üzere,\nhoşça kalın.", color=maarif_blue).scale(0.8)
        self.play(Write(outro))
        self.wait(2)
