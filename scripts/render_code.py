from manim import *
import numpy as np

class MaarifScene(Scene):
    def construct(self):
        # 1. TEMİZ TASARIM
        self.camera.background_color = "#FFFFFF"
        dark_grey = "#333333"
        maarif_blue = "#87CEEB"
        main_center = DOWN * 0.5 

        # 2. Başlık (Üste Sabit)
        title = Text("Birim Kesir Mantığı", color=dark_grey).scale(0.9)
        title.to_edge(UP, buff=0.7)

        # 3. Ana Bütün (Daire)
        whole = Circle(radius=2.0, color=dark_grey, stroke_width=3).move_to(main_center)
        
        # 4 Parçalı Bölme Çizgileri
        lines = VGroup(
            Line(whole.get_left(), whole.get_right(), color=dark_grey),
            Line(whole.get_top(), whole.get_bottom(), color=dark_grey)
        ).move_to(main_center)

        # 4. Birim Parça (Sector - Parametreler Sadeleşti)
        # Hata ihtimaline karşı AnnularSector yerine en güvenli Sector'u kullanıyoruz
        unit_slice = Sector(
            radius=2.0,
            angle=90*DEGREES,
            start_angle=90*DEGREES,
            color=maarif_blue,
            fill_opacity=0.7,
            stroke_width=1,
            stroke_color=dark_grey
        ).move_to(main_center)

        # 5. Kesir Yazısı
        frac = MathTex(r"\frac{1}{4}", color=maarif_blue).scale(2.5)
        frac.next_to(whole, RIGHT, buff=1.0)

        # --- AKIŞ ---
        self.play(Write(title))
        self.play(Create(whole), Create(lines))
        self.wait(1)
        self.play(FadeIn(unit_slice))
        self.play(Write(frac))
        self.wait(3)
        self.play(FadeOut(VGroup(whole, lines, unit_slice, frac, title)))
        self.wait(1)
