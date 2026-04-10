from manim import *
import numpy as np

class BirimKesirHapDersi(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # 0-5. sn: Giriş, İsimsiz Selamlama ve Başlık (Ekranın Üstüne Sabit)
        title = Text('Birim Kesir: En Sade Anlatım', color=DARK_GRAY, font_size=40).to_edge(UP)
        self.play(Write(title), run_time=2)
        self.wait(3)

        # 5-15. sn: Bütünün Merkezlenerek Tanımı ve Bölünme
        whole = Circle(radius=2, color=DARK_GRAY).move_to(ORIGIN)
        lines = VGroup(*[Line(ORIGIN, [2*np.cos(i*TAU/4), 2*np.sin(i*TAU/4), 0], color=DARK_GRAY) for i in range(4)]).move_to(ORIGIN)
        self.play(Create(whole), Create(lines), run_time=3)
        self.wait(7)

        # 15-25. sn: Birim Parçanın (1/4) Vurgulanması (Daire İçinde)
        unit_slice = AnnularSector(inner_radius=0, outer_radius=2, angle=TAU/4, start_angle=0, color=BLUE, fill_opacity=0.6).move_to(ORIGIN)
        self.play(FadeIn(unit_slice), run_time=2)
        self.wait(8)

        # 25-35. sn: Matematiksel Gösterim (1/4) - Dairenin Hemen Sağına Merkezli
        frac = MathTex(r'\frac{1}{4}', color=BLUE, font_size=100).next_to(whole, RIGHT, buff=1)
        self.play(Write(frac), run_time=2)
        self.wait(8)

        # 35-50. sn: 'Payda büyüdükçe kesir küçülür' mantığı (Özet)
        # Bu önemli vurguda görsel ekranda SABİT KALIR, öğrenci incelemeye devam eder
        self.wait(15)

        # 50-55. sn: Kapanış (ADSZ)
        self.play(FadeOut(whole), FadeOut(lines), FadeOut(unit_slice), FadeOut(frac), FadeOut(title))
        outro = Text('Bir sonraki derste görüşmek üzere, hoşça kalın.', color=BLUE, font_size=40)
        self.play(Write(outro))
        self.wait(2)