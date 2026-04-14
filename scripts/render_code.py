from manim import *
import numpy as np

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Başlık
        title = Text("Birim Kesir Mantığı", color="#333333").to_edge(UP)
        
        # Bütün (Daire)
        whole = Circle(radius=2, color="#333333").move_to(ORIGIN)
        
        # Bölme Çizgileri
        lines = VGroup(*[Line(ORIGIN, [2*np.cos(i*TAU/4), 2*np.sin(i*TAU/4), 0], color="#333333") for i in range(4)])
        
        # Birim Parça (1/4)
        unit_slice = AnnularSector(inner_radius=0, outer_radius=2, angle=TAU/4, start_angle=0, color="#87CEEB", fill_opacity=0.6).move_to(ORIGIN)
        
        # Animasyon Akışı
        self.play(Write(title))
        self.play(Create(whole), Create(lines))
        self.play(FadeIn(unit_slice))
        self.wait(3)
