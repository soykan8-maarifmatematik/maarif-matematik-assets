from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.background_color = "#FFFFFF"

class BirimKesirler(Scene):
    def construct(self):
        # 1. Başlık (Güvenli Alan: UP, buff=2.0)
        title = Tex("BİRİM KESİRLER", color="#333333", font_size=70).to_edge(UP, buff=2.0)
        self.play(Write(title))
        self.wait(3.3) # "Bir pizzayı ikiye mi bölersen dilimin büyük olur, dörde mi?" (10 kelime)
        self.wait(2.0) # "Gelin birim kesirlerin sırrını görselle ispatlayalım." (6 kelime)

        # 2. Modellerin İnşası
        # Model 1: 1/2
        circle1 = Circle(radius=1.8, color="#333333", stroke_width=5)
        line1 = Line(circle1.get_top(), circle1.get_bottom(), color="#333333", stroke_width=5)
        group1_base = VGroup(circle1, line1)
        sector1 = Sector(outer_radius=1.8, angle=PI, start_angle=PI/2, color="#007BFF", fill_opacity=0.9)
        model1 = VGroup(group1_base, sector1)

        # Model 2: 1/4
        circle2 = Circle(radius=1.8, color="#333333", stroke_width=5)
        line2_v = Line(circle2.get_top(), circle2.get_bottom(), color="#333333", stroke_width=5)
        line2_h = Line(circle2.get_left(), circle2.get_right(), color="#333333", stroke_width=5)
        group2_base = VGroup(circle2, line2_v, line2_h)
        sector2 = Sector(outer_radius=1.8, angle=PI/2, start_angle=PI/2, color="#FF0000", fill_opacity=0.9)
        model2 = VGroup(group2_base, sector2)

        models = VGroup(model1, model2).arrange(RIGHT, buff=1.2)

        # 3. Etiketler ve Sembol
        label1 = MathTex(r"\frac{1}{2}", color="#007BFF", font_size=110)
        label2 = MathTex(r"\frac{1}{4}", color="#FF0000", font_size=110)
        symbol = MathTex(">", color="#333333", font_size=120)
        
        equation = VGroup(label1, symbol, label2).arrange(RIGHT, buff=1.5)

        # 4. Dikey Hizalama (Kural: VGroup(...).arrange(DOWN, buff=1.8))
        main_group = VGroup(models, equation).arrange(DOWN, buff=1.8)
        main_group.set_y(-0.5) # Güvenli alan içinde ortalama (Alt sınır y=-4.5'e çok uzak)

        # Animasyonlar
        # "İşte bir tam! Önce iki eş parçaya bölelim." (8 kelime -> 2.6s)
        self.play(Create(group1_base), run_time=1.0)
        self.wait(1.6)

        # "Bu dilim, ikide birdir." (4 kelime -> 1.3s)
        self.play(FadeIn(sector1), Write(label1), run_time=1.0)
        self.wait(0.3)

        # "Şimdi aynı bütünü dört eş parçaya bölelim." (7 kelime -> 2.3s)
        self.play(Create(group2_base), run_time=1.0)
        self.wait(1.3)

        # "Bu dilim ise dörtte birdir." (5 kelime -> 1.6s)
        self.play(FadeIn(sector2), Write(label2), run_time=1.0)
        self.wait(0.6)

        # "Gördüğünüz gibi, parça sayısı arttıkça dilim küçülüyor!" (7 kelime -> 2.3s)
        self.play(Indicate(sector1, color="#007BFF", scale_factor=1.1), Indicate(sector2, color="#FF0000", scale_factor=1.1), run_time=1.5)
        self.wait(0.8)

        # "Yani ikide bir, büyüktür dörtte birden." (6 kelime -> 2.0s)
        self.play(Write(symbol), run_time=0.5)
        self.play(Circumscribe(symbol, color="#333333", time_width=2), run_time=1.0)
        self.wait(0.5)

        # "Payda büyüdükçe, birim kesir küçülür. Unutma!" (6 kelime -> 2.0s)
        self.play(Circumscribe(equation, color="#007BFF", time_width=2), run_time=1.0)
        
        # Bitiş Kuralı: Son kelime sayısı (6) / 3.0 = 2.0s + 2s = 4.0s bekleme. Ekran temizlenmez.
        self.wait(4.0)
