from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class BirimKesirler(Scene):
    def construct(self):
        # Arka plan rengi
        self.camera.background_color = "#FFFFFF"

        # Başlık ve Güvenli Alan
        title = Text("Birim Kesirler", color="#333333", font_size=70, weight=BOLD)
        title.to_edge(UP, buff=2.0)

        # 1/2 Modeli (Modern İnşa)
        circle1 = Circle(radius=1.8, color="#333333", stroke_width=4)
        line1 = Line(circle1.get_top(), circle1.get_bottom(), color="#333333", stroke_width=4)
        sector1 = Sector(radius=1.8, angle=PI, start_angle=PI/2, color="#007BFF", fill_opacity=0.8)
        model1 = VGroup(circle1, line1, sector1)
        text1 = MathTex(r"\frac{1}{2}", color="#333333", font_size=120)
        part1 = VGroup(model1, text1).arrange(DOWN, buff=0.8)

        # 1/4 Modeli (Modern İnşa)
        circle2 = Circle(radius=1.8, color="#333333", stroke_width=4)
        line2_v = Line(circle2.get_top(), circle2.get_bottom(), color="#333333", stroke_width=4)
        line2_h = Line(circle2.get_left(), circle2.get_right(), color="#333333", stroke_width=4)
        sector2 = Sector(radius=1.8, angle=PI/2, start_angle=PI/2, color="#FF0000", fill_opacity=0.8)
        model2 = VGroup(circle2, line2_v, line2_h, sector2)
        text2 = MathTex(r"\frac{1}{4}", color="#333333", font_size=120)
        part2 = VGroup(model2, text2).arrange(DOWN, buff=0.8)

        # Sembol (Büyüktür)
        symbol = MathTex(">", color="#333333", font_size=150)

        # Matematiksel İfade Grubu
        math_group = VGroup(part1, symbol, part2).arrange(RIGHT, buff=1.0)

        # Sonuç Metni
        conc_line1 = Text("Payda Büyüdükçe", color="#007BFF", font_size=55, weight=BOLD)
        conc_line2 = Text("Değer Küçülür", color="#007BFF", font_size=55, weight=BOLD)
        conclusion = VGroup(conc_line1, conc_line2).arrange(DOWN, buff=0.3)

        # Dikey Hizalama ve Merkezleme
        main_layout = VGroup(math_group, conclusion).arrange(DOWN, buff=1.8)
        main_layout.move_to(ORIGIN)

        # Animasyonlar
        self.play(Write(title), run_time=1)
        
        # Önce bütünü gri çizgilerle böl
        self.play(
            Create(circle1), Create(line1),
            Create(circle2), Create(line2_v), Create(line2_h),
            run_time=1.5
        )
        
        # Sonra renkli dilimleri ekle
        self.play(
            FadeIn(sector1),
            FadeIn(sector2),
            run_time=1.5
        )
        
        # Kesirleri yaz
        self.play(
            Write(text1),
            Write(text2),
            run_time=1
        )
        
        # Sembolü ekle
        self.play(Write(symbol), run_time=1)
        
        # Sonuç metnini göster
        self.play(Write(conclusion), run_time=1)

        # Bekleme Süresi (Kelime sayısı: 37 -> 12.3 sn ses. Animasyon: ~7 sn. Kalan: ~5.3 sn + 2 sn = 7.3 sn)
        self.wait(8)
