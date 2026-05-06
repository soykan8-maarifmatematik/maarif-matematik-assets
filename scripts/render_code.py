from manim import *

config.pixel_height, config.pixel_width = 1920, 1080

class UnitFractions(Scene):
    def construct(self):
        # 4. KAMERA VE ARKA PLAN AYARLARI
        self.camera.background_color = WHITE
        self.camera.frame_width = 9
        self.camera.frame_height = 16

        # 2. BAŞLIK (Üst)
        header = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", color=BLACK, font_size=48, weight=BOLD)
        header.to_edge(UP, buff=1.0).scale_to_fit_width(8.0)
        
        # 1/2 Modeli
        half_group = VGroup()
        for i in range(2):
            color = ORANGE if i == 0 else WHITE
            fill_op = 0.8 if i == 0 else 0.0
            # 1. SECTOR KISITLARI VE ÇİZGİSEL NETLİK
            slice_sector = Sector(
                radius=1.5,
                angle=TAU/2,
                start_angle=i*TAU/2,
                color=color,
                fill_opacity=fill_op,
                stroke_width=3,
                stroke_color=BLACK
            )
            half_group.add(slice_sector)
        
        label_half = MathTex(r"\frac{1}{2}", color=BLACK, font_size=80).next_to(half_group, DOWN, buff=0.6)
        model_half = VGroup(half_group, label_half)

        # 1/4 Modeli
        quarter_group = VGroup()
        for i in range(4):
            color = GREEN if i == 0 else WHITE
            fill_op = 0.8 if i == 0 else 0.0
            # 1. SECTOR KISITLARI VE ÇİZGİSEL NETLİK
            slice_sector = Sector(
                radius=1.5,
                angle=TAU/4,
                start_angle=i*TAU/4,
                color=color,
                fill_opacity=fill_op,
                stroke_width=3,
                stroke_color=BLACK
            )
            quarter_group.add(slice_sector)
        
        label_quarter = MathTex(r"\frac{1}{4}", color=BLACK, font_size=80).next_to(quarter_group, DOWN, buff=0.6)
        model_quarter = VGroup(quarter_group, label_quarter)

        # Karşılaştırma Sembolü
        gt_symbol = MathTex(">", color=RED, font_size=120)

        # 2. MODELLER (Orta-Üst Hiyerarşik Kilit)
        all_models = VGroup(model_half, gt_symbol, model_quarter).arrange(RIGHT, buff=0.8)
        all_models.move_to(UP * 2.8)

        # 2. AÇIKLAMA (Alt Hiyerarşik Kilit ve Paragraph Kullanımı)
        desc_text = Paragraph(
            "Payda büyüdükçe,",
            "bütün daha çok parçaya bölünür,",
            "bu yüzden birim kesrin değeri küçülür.",
            alignment="center",
            color=BLACK,
            font_size=42
        ).move_to(DOWN * 3.5)

        # Animasyon Sekansı
        self.play(Write(header))
        self.wait(0.5)
        
        self.play(FadeIn(model_half, shift=UP))
        self.wait(0.5)
        
        self.play(FadeIn(model_quarter, shift=UP))
        self.wait(1)
        
        self.play(Write(gt_symbol))
        self.play(Indicate(gt_symbol, color=RED, scale_factor=1.3))
        self.wait(1)
        
        self.play(Write(desc_text))
        self.wait(2)
