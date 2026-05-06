from manim import *

class MaarifScene(Scene):
    def construct(self):
        # 1. DİKEY AYAR (Garanti)
        self.camera.frame_width = 9
        self.camera.frame_height = 16
        self.camera.background_color = "#F0F4F8"

        # 2. ANİMASYON VE MODELLEME (Birim Kesir Fonksiyonu)
        def get_fraction_circle(denominator, color):
            slices = VGroup()
            angle = TAU / denominator
            for i in range(denominator):
                # outer_radius KULLANILMADI, sadece radius=0.9
                slice_sector = Sector(
                    radius=0.9,
                    angle=angle,
                    start_angle=i * angle,
                    stroke_color=BLACK,
                    stroke_width=2,
                    fill_color=color if i == 0 else WHITE,
                    fill_opacity=1
                )
                slices.add(slice_sector)
            return slices

        # Daireleri oluştur (Payı daima 1 olan birim kesirler)
        circle_half = get_fraction_circle(2, "#FF6B6B")
        circle_quarter = get_fraction_circle(4, "#4ECDC4")
        circle_eighth = get_fraction_circle(8, "#45B7D1")

        # Daireleri grupla ve GÜVENLİ ALANA yerleştir
        circles = VGroup(circle_half, circle_quarter, circle_eighth).arrange(RIGHT, buff=0.5)
        circles.shift(UP * 1.5)

        # Matematiksel Etiketler
        label_half = MathTex("\\frac{1}{2}", color=BLACK, font_size=48).next_to(circle_half, DOWN)
        label_quarter = MathTex("\\frac{1}{4}", color=BLACK, font_size=48).next_to(circle_quarter, DOWN)
        label_eighth = MathTex("\\frac{1}{8}", color=BLACK, font_size=48).next_to(circle_eighth, DOWN)

        # 1. EKRAN VE KADRAJ (OTOMATİK ALT SATIR - Paragraph ve Güvenli Alan)
        text1 = Paragraph(
            "Bir bütünü 2'ye böldüğünde",
            "1 dilim oldukça büyüktür.",
            alignment="center",
            color=BLACK
        ).scale_to_fit_width(6.5).to_edge(DOWN, buff=3.5)

        text2 = Paragraph(
            "Ama 4'e veya 8'e böldüğünde",
            "birim kesir giderek küçülür.",
            alignment="center",
            color=BLACK
        ).scale_to_fit_width(6.5).to_edge(DOWN, buff=3.5)

        text3 = Paragraph(
            "Kural basit:",
            "Payda büyüdükçe,",
            "birim kesir KÜÇÜLÜR!",
            alignment="center",
            color=BLACK
        ).scale_to_fit_width(6.5).to_edge(DOWN, buff=3.5)

        # Animasyon Akışı
        self.play(Write(text1))
        self.play(
            Create(circle_half),
            Write(label_half)
        )
        self.wait(1.5)

        self.play(ReplacementTransform(text1, text2))
        self.play(
            Create(circle_quarter),
            Write(label_quarter)
        )
        self.wait(0.5)
        self.play(
            Create(circle_eighth),
            Write(label_eighth)
        )
        self.wait(1.5)

        self.play(ReplacementTransform(text2, text3))
        
        # Son vurgu
        self.play(
            Indicate(circle_half[0], color="#FF6B6B"),
            Indicate(circle_quarter[0], color="#4ECDC4"),
            Indicate(circle_eighth[0], color="#45B7D1")
        )
        self.wait(2)
