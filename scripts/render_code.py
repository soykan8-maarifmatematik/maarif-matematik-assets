from manim import *

config.pixel_height, config.pixel_width = 1920, 1080

class BirimKesirler(Scene):
    def construct(self):
        self.camera.frame_width = 9
        self.camera.frame_height = 16
        self.camera.background_color = WHITE
        Mobject.set_default(color="#212121")

        # 1. BAŞLIK (Üst)
        header = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", weight=BOLD)
        header.scale_to_fit_width(6.5)
        header.to_edge(UP, buff=1.0)

        # 2. MODELLER (Orta-Üst)
        def create_fraction_circle(denominator, color):
            circle_group = VGroup()
            angle = TAU / denominator
            for i in range(denominator):
                fill_op = 0.6 if i == 0 else 0.0
                fill_col = color if i == 0 else WHITE
                
                sector = Sector(
                    outer_radius=1.5,
                    angle=angle,
                    start_angle=i * angle + (PI/2), # Üstten başlaması için
                    stroke_width=3,
                    stroke_color=BLACK,
                    fill_color=fill_col,
                    fill_opacity=fill_op
                )
                circle_group.add(sector)
            return circle_group

        circle_1_3 = create_fraction_circle(3, BLUE)
        circle_1_6 = create_fraction_circle(6, RED)

        label_1_3 = MathTex(r"\frac{1}{3}").scale(1.5).next_to(circle_1_3, DOWN, buff=0.5)
        label_1_6 = MathTex(r"\frac{1}{6}").scale(1.5).next_to(circle_1_6, DOWN, buff=0.5)

        group_1_3 = VGroup(circle_1_3, label_1_3)
        group_1_6 = VGroup(circle_1_6, label_1_6)

        greater_than = MathTex(">").scale(2.5)

        models_group = VGroup(group_1_3, greater_than, group_1_6).arrange(RIGHT, buff=0.8)
        models_group.move_to(UP * 2.8)

        # 3. AÇIKLAMA (Alt)
        para = Paragraph(
            "Payda büyüdükçe",
            "dilimler küçülür!",
            "Yani paydası küçük olan",
            "birim kesir daha büyüktür.",
            alignment="center"
        )
        para.scale_to_fit_width(6.5)
        para.move_to(DOWN * 3.5)

        # --- ANİMASYONLAR ---
        self.play(Write(header))
        self.wait(0.5)

        # 1/3 Kesrini Çizme
        for sector in circle_1_3:
            self.play(Create(sector), run_time=0.3)
        self.play(Write(label_1_3))
        self.wait(0.5)

        # 1/6 Kesrini Çizme
        for sector in circle_1_6:
            self.play(Create(sector), run_time=0.2)
        self.play(Write(label_1_6))
        self.wait(0.5)

        # Karşılaştırma Sembolü
        self.play(Write(greater_than))
        self.wait(1)

        # Açıklama Metni
        self.play(Write(para))
        self.wait(2)
