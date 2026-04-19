from manim import *
import numpy as np

# Maarif Matematik - %100 Çalışan Renk Sabitli Sahne
class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5
        
        # Renk Mühürleri (Hata almamak için Hex kodları kullanıldı)
        text_color = "#333333" 
        maarif_blue = "#1976D2" # Koyu Mavi Karşılığı
        maarif_red = "#D32F2F"  # Koyu Kırmızı Karşılığı

        # 1. Başlık
        title = Text("Kesir Kavramı: Pay ve Payda", color=text_color).scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 2. Kesir Yazımı (MathTex)
        num = MathTex("2", color=maarif_blue).scale(2.5)
        line = Line(LEFT*0.8, RIGHT*0.8, color=text_color).set_stroke(width=4)
        den = MathTex("5", color=text_color).scale(2.5)
        frac_group = VGroup(num, line, den).arrange(DOWN, buff=0.3).shift(LEFT*3 + UP*0.5)

        self.play(Create(line), Write(den))
        self.wait(1)
        self.play(Write(num))
        self.wait(1)

        # 3. Görselleştirme (Pasta Modeli)
        circle_center = RIGHT*2 + UP*0.5
        circle = Circle(radius=1.5, color=text_color).move_to(circle_center)
        
        # Boyalı dilimler
        sectors = VGroup()
        for i in range(2):
            sector = Sector(radius=1.48, angle=TAU/5, start_angle=i*TAU/5, color=maarif_blue, fill_opacity=0.7).move_to(circle_center)
            sectors.add(sector)

        self.play(Create(circle))
        self.wait(1)
        self.play(FadeIn(sectors))
        self.wait(2)

        # 4. Okunuşlar (DARK_RED hatası giderildi)
        read_1 = Text("1. Okunuş: İki bölü beş", color=maarif_blue, font_size=28)
        read_2 = Text("2. Okunuş: Beşte iki", color=maarif_red, font_size=28)
        read_group = VGroup(read_1, read_2).arrange(DOWN, aligned_edge=LEFT, buff=0.5).to_edge(DOWN, buff=1)

        self.play(Write(read_1))
        self.wait(1)
        self.play(Write(read_2))
        self.wait(3)

        # 5. Kapanış
        self.play(FadeOut(VGroup(title, frac_group, circle, sectors, read_group)))
        outro = Text("Bir sonraki derste görüşmek üzere,\nhoşça kalın.", color=maarif_blue).scale(0.8)
        self.play(Write(outro))
        self.wait(2)
