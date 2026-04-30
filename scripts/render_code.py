from manim import *

class UnitFractions(Scene):
    def construct(self):
        # 9:16 Dikey Format Ayarları
        self.camera.frame_width = 9
        self.camera.frame_height = 16
        self.camera.background_color = "#FFFFFF"

        # 1. BAŞLIK (TITLE) - En tepeye mıhlanmış
        title = Text("BİRİM KESİRLER", font="DejaVu Sans", weight=BOLD, color=BLACK).scale(1.2)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(2.3) # Merhaba arkadaşlar! Birim kesirleri karşılaştırmayı öğrenelim.
        self.wait(2.0) # Birim kesir, payı bir olan kesirdir.

        # 2. MODELLER (MODELS) - Merkezin üstüne (UP * 2.0) yerleştirilmiş
        # 1/2 Modeli
        circle_half = Circle(radius=1.5, color=BLACK, stroke_width=4)
        slice_half = Sector(radius=1.5, angle=PI, start_angle=PI/2, color=ORANGE, fill_opacity=0.8)
        line_half = Line(circle_half.get_top(), circle_half.get_bottom(), color=BLACK)
        model_half = VGroup(circle_half, slice_half, line_half).shift(LEFT * 2.2 + UP * 2.0)

        # 1/4 Modeli
        circle_quarter = Circle(radius=1.5, color=BLACK, stroke_width=4)
        slice_quarter = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color=BLUE, fill_opacity=0.8)
        line1 = Line(circle_quarter.get_top(), circle_quarter.get_bottom(), color=BLACK)
        line2 = Line(circle_quarter.get_left(), circle_quarter.get_right(), color=BLACK)
        model_quarter = VGroup(circle_quarter, slice_quarter, line1, line2).shift(RIGHT * 2.2 + UP * 2.0)

        self.play(Create(circle_half), Create(circle_quarter))
        self.wait(1.7) # Elimizde iki eş pizza olsun.

        self.play(FadeIn(slice_half), Create(line_half))
        self.wait(4.0) # İlk pizzayı iki parçaya bölelim ve birini alalım. Bu bir bölü ikidir.

        self.play(FadeIn(slice_quarter), Create(line1), Create(line2))
        self.wait(4.0) # İkinci pizzayı dört parçaya bölelim ve birini alalım. Bu bir bölü dörttür.

        # 3. KESİR SAYILARI - Modellerin hemen altına (DOWN, buff=0.8)
        frac_half = MathTex(r"\frac{1}{2}", color=BLACK).scale(2.0)
        frac_half.next_to(model_half, DOWN, buff=0.8)

        frac_quarter = MathTex(r"\frac{1}{4}", color=BLACK).scale(2.0)
        frac_quarter.next_to(model_quarter, DOWN, buff=0.8)

        self.play(Write(frac_half), Write(frac_quarter))
        self.wait(2.3) # Gördüğünüz gibi, parça sayısı arttıkça dilim küçülüyor!

        greater_sign = MathTex(">", color=RED).scale(2.5)
        greater_sign.move_to((frac_half.get_center() + frac_quarter.get_center()) / 2)
        self.play(Write(greater_sign))
        self.wait(2.3) # Yani payda büyüdükçe, birim kesrin değeri küçülür.

        # 4. ALT SONUÇ/CTA METNİ - En alta, butonlardan kaçarak (DOWN, buff=3.5)
        cta = Text("Abone Ol: Maarif Matematik", font="DejaVu Sans", weight=BOLD, color=RED).scale(0.8)
        cta.to_edge(DOWN, buff=3.5)
        self.play(Write(cta))
        
        # Bitiş bekleme süresi (Kelime hesabı + 2.0 saniye güvenlik)
        self.wait(5.0)
