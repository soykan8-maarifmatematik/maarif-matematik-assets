from manim import *

config.pixel_height, config.pixel_width = 1920, 1080

class BirimKesirler(Scene):
    def construct(self):
        # ARKA PLAN & RENK
        self.camera.background_color = WHITE
        text_color = "#212121"

        # BAŞLIK
        header = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", color=text_color, font_size=48, weight=BOLD)
        header.to_edge(UP, buff=1.0).scale_to_fit_width(8.0)
        self.play(Write(header))

        # MODELLEME FONKSİYONU
        def create_fraction_circle(denominator, color):
            circle_group = VGroup()
            angle = TAU / denominator
            for i in range(denominator):
                # Sadece payı temsil eden 1 birim dilim %60 opak, diğerleri şeffaf
                fill_op = 0.6 if i == 0 else 0.0
                slice_color = color if i == 0 else WHITE
                
                # SECTOR FIX: Sadece radius=1.0 kullanıldı
                sector = Sector(
                    radius=1.0,
                    angle=angle,
                    start_angle=i * angle,
                    color=BLACK,
                    fill_color=slice_color,
                    fill_opacity=fill_op,
                    stroke_width=3,
                    stroke_color=BLACK
                )
                circle_group.add(sector)
            return circle_group

        # MODELLERİ OLUŞTURMA
        circle_1_3 = create_fraction_circle(3, ORANGE)
        circle_1_6 = create_fraction_circle(6, BLUE)

        label_1_3 = MathTex(r"\frac{1}{3}", color=text_color, font_size=96).next_to(circle_1_3, DOWN, buff=0.5)
        label_1_6 = MathTex(r"\frac{1}{6}", color=text_color, font_size=96).next_to(circle_1_6, DOWN, buff=0.5)

        group_1_3 = VGroup(circle_1_3, label_1_3)
        group_1_6 = VGroup(circle_1_6, label_1_6)

        gt_symbol = MathTex(">", color=text_color, font_size=120)

        # MODELLERİ YERLEŞTİRME (Orta - Üst Yarı)
        models_group = VGroup(group_1_3, gt_symbol, group_1_6).arrange(RIGHT, buff=1.0)
        models_group.move_to(UP * 2.8)

        # AÇIKLAMA (Alt - Butonların üstü)
        explanation = Paragraph(
            "Payda büyüdükçe,",
            "bütün daha fazla parçaya bölünür.",
            "Bu yüzden dilimler KÜÇÜLÜR!",
            alignment="center",
            color=text_color,
            font_size=42,
            weight=BOLD,
            line_spacing=1.2
        )
        explanation.move_to(DOWN * 3.5)

        # ANİMASYON SIRALAMASI
        self.play(FadeIn(group_1_3, shift=UP), FadeIn(group_1_6, shift=UP), run_time=1.5)
        self.wait(0.5)
        self.play(Write(gt_symbol), run_time=1)
        self.wait(0.5)
        self.play(Write(explanation), run_time=2)
        self.wait(2)
