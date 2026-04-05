from manim import *

class KesirlerinMantigi(Scene):
    def construct(self):
        # Arka plan ayarı
        self.camera.background_color = WHITE
        
        # Varsayılan metin rengi ve font
        Text.set_default(color=DARK_GRAY, font="sans-serif")
        
        # Başlık (Ana Metin: Koyu Gri)
        title = Text("Kesirlerin Mantığı", font_size=48, weight=BOLD).to_edge(UP)
        self.play(Write(title), run_time=1.5)
        self.wait(1)

        # Bütün Çikolata (4 parçalı dikdörtgen)
        choc_bar = VGroup(*[
            Rectangle(width=2, height=2, color=DARK_GRAY) for _ in range(4)
        ]).arrange(RIGHT, buff=0)
        self.play(Create(choc_bar), run_time=2)
        self.wait(1)

        # Payda Açıklaması (Dikkat/Vurgu: Kırmızı)
        payda_text = Text("4 Eşit Parça = Payda", font_size=32, color=RED).next_to(choc_bar, DOWN, buff=0.5)
        self.play(Write(payda_text), run_time=1.5)
        self.wait(2)

        # Pay Açıklaması (Vurgu: Mavi)
        fills = VGroup(*[
            Rectangle(width=2, height=2, fill_color=BLUE, fill_opacity=0.7, stroke_color=DARK_GRAY) for _ in range(3)
        ]).arrange(RIGHT, buff=0).move_to(choc_bar[:3].get_center())

        self.play(Create(fills), run_time=2)
        pay_text = Text("3 Alınan Parça = Pay", font_size=32, color=BLUE).next_to(choc_bar, UP, buff=0.5)
        self.play(Write(pay_text), run_time=1.5)
        self.wait(2)

        # Geçiş (Animasyonların pürüzsüzlüğü)
        self.play(FadeOut(choc_bar), FadeOut(fills), FadeOut(payda_text), FadeOut(pay_text))

        # Kesir Gösterimi
        fraction = MathTex(r"\frac{3}{4}", font_size=144)
        fraction[0][0].set_color(BLUE)      # Pay (3) - Mavi
        fraction[0][1].set_color(DARK_GRAY) # Kesir Çizgisi - Koyu Gri
        fraction[0][2].set_color(RED)       # Payda (4) - Kırmızı

        self.play(Write(fraction), run_time=2)
        self.wait(1)

        # Kesir Etiketleri
        pay_label = Text("Pay (Alınan)", color=BLUE, font_size=36).next_to(fraction, LEFT, buff=1).shift(UP*0.8)
        payda_label = Text("Payda (Bütün)", color=RED, font_size=36).next_to(fraction, LEFT, buff=1).shift(DOWN*0.8)
        cizgi_label = Text("Kesir Çizgisi", color=DARK_GRAY, font_size=30).next_to(fraction, RIGHT, buff=1)

        self.play(Write(pay_label), Write(payda_label), Write(cizgi_label), run_time=2)
        self.wait(1)

        # Sonuç/Doğru Gösterimi (Yeşil)
        result_text = Text("3/4 (Dörtte Üç)", color=GREEN, font_size=42, weight=BOLD).next_to(fraction, DOWN, buff=1.2)
        self.play(Write(result_text), run_time=1.5)
        self.wait(3)

        # Kapanış
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)