from manim import *

config.background_color = "#FFFFFF"

class MaarifScene(Scene):
    def construct(self):
        # Başlık (Kural 1 ve 2)
        title = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", color="#212121", weight=BOLD)
        title.scale_to_fit_width(7.0).to_edge(UP, buff=1.0)
        self.play(Write(title))

        # Kesir Modelleri Oluşturma Fonksiyonu (Kural 3, 4 ve 6)
        def create_fraction_pie(denominator, color):
            pie = VGroup()
            angle = TAU / denominator
            for i in range(denominator):
                # Sadece 1 adet birim dilimi renkli ve fill_opacity=0.5
                fill_color = color if i == 0 else "#FFFFFF"
                fill_op = 0.5 if i == 0 else 0.0
                
                # outer_radius kullanılmıyor, sadece radius=0.9
                slice_sector = Sector(
                    radius=0.9,
                    angle=angle,
                    start_angle=i * angle,
                    color="#212121",
                    stroke_width=2,
                    fill_color=fill_color,
                    fill_opacity=fill_op
                )
                pie.add(slice_sector)
            return pie

        # 1/3 ve 1/6 Modelleri (Kural 1 ve 2 - Paylar daima 1, Modeller UP * 1.5 kaydırıldı)
        pie_1_3 = create_fraction_pie(3, BLUE).shift(LEFT * 2 + UP * 1.5)
        pie_1_6 = create_fraction_pie(6, RED).shift(RIGHT * 2 + UP * 1.5)

        # Kesir Yazıları
        label_1_3 = MathTex(r"\frac{1}{3}", color="#212121").next_to(pie_1_3, DOWN, buff=0.5)
        label_1_6 = MathTex(r"\frac{1}{6}", color="#212121").next_to(pie_1_6, DOWN, buff=0.5)

        # Karşılaştırma İşareti
        greater_than = MathTex(">", color="#212121").scale(1.5).shift(UP * 1.5)

        # Animasyonlar (Kural 3 - Create ile oluşturma)
        self.play(Create(pie_1_3), Create(pie_1_6), run_time=2)
        self.play(Write(label_1_3), Write(label_1_6))
        self.wait(1)
        
        self.play(Write(greater_than))
        self.wait(1)

        # Otomatik Alt Satır ve Güvenli Genişlik (Kural 2 - Paragraph kullanımı)
        rule_text = Paragraph(
            "Payda büyüdükçe birim",
            "kesrin değeri küçülür.",
            line_spacing=0.8,
            alignment="center",
            color="#212121"
        )
        rule_text.scale_to_fit_width(6.5).to_edge(DOWN, buff=3.5)
        
        self.play(Write(rule_text))
        self.wait(3)
