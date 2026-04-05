from manim import *

class KesirlerinMantigi(Scene):
    def construct(self):
        # Arka plan rengini beyaz yapiyoruz
        self.camera.background_color = WHITE
        
        # Baslik (Ana metin - Koyu Gri)
        title = Text("Kesirlerin Mantığı", font="Montserrat", color=DARK_GRAY, weight=BOLD).scale(0.9).to_edge(UP)
        self.play(Write(title, run_time=2))
        self.wait(1)

        # Cikolata (Butun - Koyu Gri)
        whole = Rectangle(width=8, height=2, color=DARK_GRAY, stroke_width=4)
        self.play(Create(whole, run_time=2))
        self.wait(1)

        # 4 parcaya bolme (Payda - Kirmizi vurgu eklenecek)
        lines = VGroup(
            Line(whole.get_top() + LEFT*2, whole.get_bottom() + LEFT*2, color=DARK_GRAY, stroke_width=4),
            Line(whole.get_top(), whole.get_bottom(), color=DARK_GRAY, stroke_width=4),
            Line(whole.get_top() + RIGHT*2, whole.get_bottom() + RIGHT*2, color=DARK_GRAY, stroke_width=4)
        )
        self.play(Create(lines, run_time=2))
        
        # Payda aciklamasi (Dikkat/Kural - Kirmizi)
        payda_text = Text("Payda = 4", font="Montserrat", color=RED, weight=BOLD).scale(0.7).next_to(whole, DOWN, buff=0.8)
        payda_desc = Text("Bütünün kaç eşit parçaya bölündüğünü gösterir.", font="Montserrat", color=DARK_GRAY).scale(0.5).next_to(payda_text, DOWN)
        self.play(Write(payda_text, run_time=1.5), Write(payda_desc, run_time=1.5))
        self.wait(2)

        # 3 parcasini boyama (Pay - Mavi vurgu)
        part1 = Rectangle(width=1.95, height=1.95, color=BLUE, fill_color=BLUE, fill_opacity=0.6, stroke_width=0).move_to(whole.get_center() + LEFT*3)
        part2 = Rectangle(width=1.95, height=1.95, color=BLUE, fill_color=BLUE, fill_opacity=0.6, stroke_width=0).move_to(whole.get_center() + LEFT*1)
        part3 = Rectangle(width=1.95, height=1.95, color=BLUE, fill_color=BLUE, fill_opacity=0.6, stroke_width=0).move_to(whole.get_center() + RIGHT*1)
        
        self.play(FadeIn(part1), FadeIn(part2), FadeIn(part3), run_time=2)
        
        # Pay aciklamasi (Mavi)
        pay_text = Text("Pay = 3", font="Montserrat", color=BLUE, weight=BOLD).scale(0.7).next_to(whole, UP, buff=0.8)
        pay_desc = Text("Bu parçalardan kaç tanesinin alındığını gösterir.", font="Montserrat", color=DARK_GRAY).scale(0.5).next_to(pay_text, UP)
        self.play(Write(pay_text, run_time=1.5), Write(pay_desc, run_time=1.5))
        self.wait(2)

        # Kesir olarak gosterme (Dogru/Sonuc - Yesil vurgu)
        graphics_group = VGroup(whole, lines, part1, part2, part3)
        self.play(
            FadeOut(pay_desc), FadeOut(payda_desc), FadeOut(pay_text), FadeOut(payda_text),
            graphics_group.animate.scale(0.7).shift(LEFT * 3),
            run_time=2
        )
        
        # Kesir cizimi
        fraction = MathTex(r"\frac{3}{4}", color=GREEN).scale(2.5).move_to(RIGHT * 3)
        sonuc_text = Text("Dörtte Üç", font="Montserrat", color=GREEN, weight=BOLD).scale(0.7).next_to(fraction, DOWN, buff=0.7)
        
        self.play(Write(fraction, run_time=1.5))
        self.play(Write(sonuc_text, run_time=1.5))
        self.wait(3)
