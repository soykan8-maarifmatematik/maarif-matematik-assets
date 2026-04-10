from manim import *
import numpy as np

class BirimKesirSenkronize(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # 0-5. saniyeler: Giriş ve Selamlama
        title = Text('Birim Kesir: Bir Tek Parça', color=DARK_GRAY, font_size=40).to_edge(UP)
        self.play(Write(title), run_time=2)
        self.wait(3)
        
        # 5-15. saniyeler: Bütünün Tanımı ve Bölünme
        whole = Circle(radius=2, color=DARK_GRAY)
        lines = VGroup(*[Line(ORIGIN, [2*np.cos(i*TAU/4), 2*np.sin(i*TAU/4), 0], color=DARK_GRAY) for i in range(4)])
        self.play(Create(whole), Create(lines), run_time=3)
        self.wait(7) # Tanım yapılırken görsel sabit kalır
        
        # 15-25. saniyeler: Birim Parçanın Vurgulanması
        unit_slice = AnnularSector(inner_radius=0, outer_radius=2, angle=TAU/4, start_angle=0, color=BLUE, fill_opacity=0.6)
        self.play(FadeIn(unit_slice), run_time=2)
        self.wait(8)
        
        # 25-35. saniyeler: Matematiksel Gösterim (1/4)
        frac = MathTex(r'\frac{1}{4}', color=BLUE, font_size=100).move_to(RIGHT*4)
        self.play(Write(frac), run_time=2)
        self.wait(8)
        
        # 35-50. saniyeler: 'Payda büyüdükçe kesir küçülür' mantığı (Özet)
        # Burada görsel sabit kalır, dersin en önemli vurgusu yapılır
        self.wait(15)
        
        # 50-55. saniyeler: Kapanış
        self.play(FadeOut(whole), FadeOut(lines), FadeOut(unit_slice), FadeOut(frac), FadeOut(title))
        outro = Text('Hoşça kalın...', color=BLUE, font_size=45)
        self.play(Write(outro))
        self.wait(2)