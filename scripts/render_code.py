from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan ve genel metin rengi
        self.camera.background_color = "#FFFFFF"
        text_color = "#212121"

        # 1. Başlık (V7 Kuralları)
        title = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", weight=BOLD, color=text_color)
        title.scale_to_fit_width(7.0)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))

        # 2. Daire Modelleri (V7 Kuralları: UP * 1.5, radius=0.9, stroke_width=2)
        left_group = VGroup()
        for i in range(3):
            if i == 0:
                # Sadece 1 adet birim dilim renkli ve fill_opacity=0.5
                slice_sector = Sector(radius=0.9, angle=TAU/3, start_angle=i*TAU/3, color=BLACK, stroke_width=2, fill_color=BLUE, fill_opacity=0.5)
            else:
                # Diğer dilimler şeffaf ama ince siyah çizgili
                slice_sector = Sector(radius=0.9, angle=TAU/3, start_angle=i*TAU/3, color=BLACK, stroke_width=2, fill_opacity=0)
            left_group.add(slice_sector)
        left_group.move_to(LEFT * 2.5 + UP * 1.5)

        right_group = VGroup()
        for i in range(5):
            if i == 0:
                # Sadece 1 adet birim dilim renkli ve fill_opacity=0.5
                slice_sector = Sector(radius=0.9, angle=TAU/5, start_angle=i*TAU/5, color=BLACK, stroke_width=2, fill_color=RED, fill_opacity=0.5)
            else:
                # Diğer dilimler şeffaf ama ince siyah çizgili
                slice_sector = Sector(radius=0.9, angle=TAU/5, start_angle=i*TAU/5, color=BLACK, stroke_width=2, fill_opacity=0)
            right_group.add(slice_sector)
        right_group.move_to(RIGHT * 2.5 + UP * 1.5)

        # Dilimleri Create animasyonu ile çizerek oluşturma
        self.play(Create(left_group), Create(right_group), run_time=2)

        # 3. Kesir İfadeleri ve Karşılaştırma Sembolü (V7 Kuralları: Sembol DAİMA ORIGIN'de)
        frac_left = MathTex(r"\frac{1}{3}", color=text_color, font_size=72).move_to(LEFT * 2.5)
        frac_right = MathTex(r"\frac{1}{5}", color=text_color, font_size=72).move_to(RIGHT * 2.5)
        symbol = MathTex(">", color=text_color, font_size=96).move_to(ORIGIN)

        self.play(Write(frac_left), Write(frac_right))
        self.play(Write(symbol))

        # 4. Otomatik Alt Satır (V7 Kuralları: Paragraph, line_spacing, alignment, scale_to_fit_width, to_edge)
        rule_text = Paragraph(
            "Payda büyüdükçe",
            "kesrin değeri küçülür.",
            line_spacing=0.8,
            alignment="center",
            color=text_color
        )
        rule_text.scale_to_fit_width(6.5)
        rule_text.to_edge(DOWN, buff=3.5)
        
        self.play(Write(rule_text))
        self.wait(2)
