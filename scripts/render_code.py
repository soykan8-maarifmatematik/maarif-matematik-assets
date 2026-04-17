from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        text_color = BLACK
        num_color = BLUE
        den_color = RED

        # Kesir oluşturma
        fraction = MathTex(r"\frac{3}{4}", color=text_color).scale(3)
        fraction[0][0].set_color(num_color)  # Pay (3)
        fraction[0][2].set_color(den_color)  # Payda (4)
        
        # Konumlandırma kuralı
        fraction.move_to(main_center)

        self.play(Write(fraction))
        self.wait(1)

        # Etiketler
        pay_label = Text("Pay (Alınan Parça)", color=num_color, font_size=24).next_to(fraction, UP, buff=0.5)
        payda_label = Text("Payda (Toplam Eş Parça)", color=den_color, font_size=24).next_to(fraction, DOWN, buff=0.5)
        cizgi_label = Text("Kesir Çizgisi", color=text_color, font_size=24).next_to(fraction, RIGHT, buff=1)

        self.play(Write(payda_label))
        self.wait(1)
        self.play(Write(pay_label))
        self.wait(1)
        self.play(Write(cizgi_label))
        self.wait(1)

        # Okunuşlar
        read1 = Text("1. Okunuş: 3 bölü 4", color=text_color, font_size=24)
        read2 = Text("2. Okunuş: 4'te 3", color=text_color, font_size=24)
        read_group = VGroup(read1, read2).arrange(DOWN, aligned_edge=LEFT).next_to(fraction, LEFT, buff=1)

        self.play(Write(read_group[0]))
        self.wait(1)
        self.play(Write(read_group[1]))
        self.wait(2)

        # Kapanış
        self.play(FadeOut(VGroup(fraction, pay_label, payda_label, cizgi_label, read_group)))
        self.wait(1)