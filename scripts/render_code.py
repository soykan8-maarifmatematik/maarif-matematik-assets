from manim import *

config.pixel_height, config.pixel_width = 1920, 1080
config.background_color = "#FFFFFF"

class MaarifScene(Scene):
    def construct(self):
        self.camera.frame_width = 9
        self.camera.frame_height = 16

        # 1. BAŞLIK (Üst Bölge)
        title = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", color="#212121", font_size=48, weight=BOLD)
        title.to_edge(UP, buff=1.0)
        title.scale_to_fit_width(8.0)

        # 2. MODELLER (Orta-Üst Bölge)
        # 1/2 Modeli
        m1_slice1 = Sector(radius=1.0, angle=PI, start_angle=0, color="#FF6B6B", fill_opacity=0.8, stroke_color="#212121", stroke_width=3)
        m1_slice2 = Sector(radius=1.0, angle=PI, start_angle=PI, color="#FFFFFF", fill_opacity=0, stroke_color="#212121", stroke_width=3)
        m1_pie = VGroup(m1_slice1, m1_slice2)
        m1_label = MathTex(r"\frac{1}{2}", color="#212121", font_size=72).next_to(m1_pie, DOWN, buff=0.5)
        model1 = VGroup(m1_pie, m1_label)

        # 1/4 Modeli
        m2_slice1 = Sector(radius=1.0, angle=PI/2, start_angle=0, color="#FF6B6B", fill_opacity=0.8, stroke_color="#212121", stroke_width=3)
        m2_slice2 = Sector(radius=1.0, angle=PI/2, start_angle=PI/2, color="#FFFFFF", fill_opacity=0, stroke_color="#212121", stroke_width=3)
        m2_slice3 = Sector(radius=1.0, angle=PI/2, start_angle=PI, color="#FFFFFF", fill_opacity=0, stroke_color="#212121", stroke_width=3)
        m2_slice4 = Sector(radius=1.0, angle=PI/2, start_angle=3*PI/2, color="#FFFFFF", fill_opacity=0, stroke_color="#212121", stroke_width=3)
        m2_pie = VGroup(m2_slice1, m2_slice2, m2_slice3, m2_slice4)
        m2_label = MathTex(r"\frac{1}{4}", color="#212121", font_size=72).next_to(m2_pie, DOWN, buff=0.5)
        model2 = VGroup(m2_pie, m2_label)

        # Karşılaştırma Sembolü
        symbol = MathTex(">", color="#212121", font_size=96)

        # Modelleri Gruplama ve Konumlandırma
        all_models = VGroup(model1, symbol, model2).arrange(RIGHT, buff=0.8)
        all_models.shift(UP * 3.5)

        # 3. PARAGRAF (Alt-Orta Bölge)
        paragraph = Paragraph(
            "Payda büyüdükçe",
            "dilimler küçülür,",
            "kesrin değeri azalır!",
            alignment="center",
            color="#212121",
            font_size=42,
            weight=BOLD,
            line_spacing=1.2
        )
        paragraph.to_edge(DOWN, buff=4.5)

        # --- ANİMASYONLAR ---
        self.play(Write(title))
        self.wait(0.5)

        # 1/2 Çizimi
        self.play(Create(m1_slice2), Create(m1_slice1), run_time=1.5)
        self.play(Write(m1_label))
        self.wait(0.5)

        # 1/4 Çizimi
        self.play(Create(m2_slice2), Create(m2_slice3), Create(m2_slice4), Create(m2_slice1), run_time=1.5)
        self.play(Write(m2_label))
        self.wait(0.5)

        # Sembolün Gelmesi
        self.play(Write(symbol), run_time=1)
        self.wait(1)

        # Paragrafın Gelmesi
        self.play(Write(paragraph), run_time=2)
        self.wait(2)
