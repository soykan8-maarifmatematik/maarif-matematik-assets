from manim import *

class UnitFractions(Scene):
    def construct(self):
        # Arka plan rengi beyaz (Kural 2)
        self.camera.background_color = "#FFFFFF"

        # BAŞLIK (Kural 1: to_edge(UP, buff=1.0), scale(1.2))
        title = Text("Birim Kesirler", font="DejaVu Sans", weight=BOLD, color=BLACK).scale(1.2).to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(3.0) # 9 kelime / 3.0 = 3.0 sn

        # MODELLER (Kural 1: shift(UP * 2.0) ve Kural 2: outer_radius yasak, radius kullan)
        left_circle = Circle(radius=1.5, color=BLACK)
        left_slice = Sector(radius=1.5, angle=PI, color=BLUE, fill_opacity=0.8)
        left_model = VGroup(left_circle, left_slice)

        right_circle = Circle(radius=1.5, color=BLACK)
        right_slice = Sector(radius=1.5, angle=PI/2, color=RED, fill_opacity=0.8)
        right_model = VGroup(right_circle, right_slice)

        # Modelleri yan yana dizip yukarı kaydırma
        models = VGroup(left_model, right_model).arrange(RIGHT, buff=1.5).shift(UP * 2.0)

        self.play(Create(left_model))
        
        # KESİR SAYILARI (Kural 1: next_to(model, DOWN, buff=0.8))
        frac_1_2 = MathTex(r"\frac{1}{2}", color=BLACK).scale(2.5).next_to(left_model, DOWN, buff=0.8)
        self.play(Write(frac_1_2))
        self.wait(3.0) # 9 kelime / 3.0 = 3.0 sn

        self.play(Create(right_model))
        frac_1_4 = MathTex(r"\frac{1}{4}", color=BLACK).scale(2.5).next_to(right_model, DOWN, buff=0.8)
        self.play(Write(frac_1_4))
        self.wait(5.0) # 15 kelime / 3.0 = 5.0 sn

        # Karşılaştırma işareti
        greater_than = MathTex(">", color=BLACK).scale(3.0).move_to((frac_1_2.get_center() + frac_1_4.get_center()) / 2)
        self.play(Write(greater_than))

        # ALT SONUÇ / CTA METNİ (Kural 1: to_edge(DOWN, buff=3.5))
        cta = Text("Payda büyüdükçe\ndeğer küçülür!", font="DejaVu Sans", weight=BOLD, color=BLACK).to_edge(DOWN, buff=3.5)
        self.play(Write(cta))
        self.wait(4.0) # 12 kelime / 3.0 = 4.0 sn

        # BİTİŞ (Kural 3: Ses bitmeden ekran beyaza düşmez, +2.0 sn ekle)
        self.wait(4.6) # 8 kelime / 3.0 = 2.6 sn + 2.0 sn = 4.6 sn
