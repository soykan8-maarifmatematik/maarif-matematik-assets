from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi
        self.camera.background_color = "#FFFFFF"

        # 1. Başlık (Kurallara uygun)
        title = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", color="#212121", weight=BOLD)
        title.scale_to_fit_width(7.0).to_edge(UP, buff=1.0)

        # 2. Modeller (1/3 ve 1/6)
        left_group = VGroup()
        for i in range(3):
            if i == 0:
                slice_obj = Sector(radius=0.9, angle=TAU/3, start_angle=i*TAU/3, fill_color=BLUE, fill_opacity=0.5, stroke_color=BLACK, stroke_width=2)
            else:
                slice_obj = Sector(radius=0.9, angle=TAU/3, start_angle=i*TAU/3, fill_opacity=0, stroke_color=BLACK, stroke_width=2)
            left_group.add(slice_obj)
        
        right_group = VGroup()
        for i in range(6):
            if i == 0:
                slice_obj = Sector(radius=0.9, angle=TAU/6, start_angle=i*TAU/6, fill_color=RED, fill_opacity=0.5, stroke_color=BLACK, stroke_width=2)
            else:
                slice_obj = Sector(radius=0.9, angle=TAU/6, start_angle=i*TAU/6, fill_opacity=0, stroke_color=BLACK, stroke_width=2)
            right_group.add(slice_obj)

        # Modelleri yukarı kaydırma (UP * 1.5 kuralı)
        left_group.move_to(LEFT * 2.5 + UP * 1.5)
        right_group.move_to(RIGHT * 2.5 + UP * 1.5)

        # Kesir yazıları
        frac_left = MathTex(r"\frac{1}{3}", color="#212121").scale(1.5).next_to(left_group, DOWN, buff=0.5)
        frac_right = MathTex(r"\frac{1}{6}", color="#212121").scale(1.5).next_to(right_group, DOWN, buff=0.5)

        # 3. Karşılaştırma Sembolü (ORIGIN kuralı)
        comp_sym = MathTex(">", color="#212121").scale(2.5).move_to(ORIGIN)

        # 4. Otomatik Alt Satır (Paragraph kuralı)
        rule_text = Paragraph(
            "Payda büyüdükçe",
            "dilim küçülür,",
            "kesrin değeri azalır!",
            color="#212121",
            line_spacing=0.8,
            alignment="center"
        )
        rule_text.scale_to_fit_width(6.5).to_edge(DOWN, buff=3.5)

        # Animasyonlar
        self.play(Write(title))
        self.play(Create(left_group), Create(right_group), run_time=2)
        self.play(Write(frac_left), Write(frac_right))
        self.wait(0.5)
        self.play(Write(comp_sym))
        self.wait(1)
        self.play(Write(rule_text))
        self.wait(2)