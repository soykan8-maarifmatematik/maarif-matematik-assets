from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class BirimKesirler(Scene):
    def construct(self):
        # Arka plan rengi (Kural 2)
        self.camera.background_color = "#FFFFFF"
        
        # Başlık (Kural 2: UP, buff=2.0, scale(1.2))
        title = Tex("Birim Kesirlerde Siralama", color=BLACK)
        title.scale(1.2)
        title.to_edge(UP, buff=2.0)
        self.play(Write(title))
        
        # 1/2 Kesri Görseli (Kural 1: SADECE radius)
        circle1_bg = Circle(radius=1.5, color=GRAY, fill_opacity=0.2)
        sector1 = Sector(radius=1.5, angle=PI, color=BLUE, fill_opacity=0.8)
        frac1 = MathTex(r"\frac{1}{2}", color=BLACK).scale(1.5)
        group1 = VGroup(VGroup(circle1_bg, sector1), frac1).arrange(DOWN, buff=0.5)
        
        # 1/4 Kesri Görseli (Kural 1: SADECE radius)
        circle2_bg = Circle(radius=1.5, color=GRAY, fill_opacity=0.2)
        sector2 = Sector(radius=1.5, angle=PI/2, color=RED, fill_opacity=0.8)
        frac2 = MathTex(r"\frac{1}{4}", color=BLACK).scale(1.5)
        group2 = VGroup(VGroup(circle2_bg, sector2), frac2).arrange(DOWN, buff=0.5)
        
        # Kesirleri yan yana dizme
        fractions_group = VGroup(group1, group2).arrange(RIGHT, buff=1.0)
        
        # Sonuç Metni (Kural 4: Ok ve LaTeX formatı)
        conclusion = Tex(r"Payda Büyüdükçe $\rightarrow$ Değer Küçülür", color=BLACK).scale(1.1)
        
        # Merkezi Yerleşim (Kural 2: arrange(DOWN, buff=2.5) ve y ekseni sınırları)
        main_content = VGroup(fractions_group, conclusion).arrange(DOWN, buff=2.5)
        main_content.move_to(ORIGIN) # [-4.5, 3.5] aralığında kalmasını garantiler
        
        # Animasyonlar
        self.play(FadeIn(circle1_bg), FadeIn(circle2_bg))
        self.wait(0.5)
        self.play(Create(sector1), Write(frac1))
        self.wait(0.5)
        self.play(Create(sector2), Write(frac2))
        self.wait(0.5)
        
        # Büyüktür işareti
        greater_sign = MathTex(">", color=BLACK).scale(2.5)
        greater_sign.move_to(fractions_group.get_center() + UP*0.7)
        self.play(Write(greater_sign))
        self.wait(1)
        
        # Sonuç yazısı animasyonu
        self.play(Write(conclusion))
        self.wait(2)
