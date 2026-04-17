from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        # Title
        title = Text("Kesir Nedir?", color=BLACK, font_size=48).to_edge(UP)
        self.play(Write(title))

        # Fraction 3/4
        fraction = MathTex(r"\frac{3}{4}", color=BLACK, font_size=120).move_to(main_center)
        self.play(Write(fraction))
        self.wait(1)

        # Labels for Pay and Payda
        pay_label = Text("Pay (Alınan Parça)", color=BLUE, font_size=28).next_to(fraction, UP, buff=0.5)
        payda_label = Text("Payda (Bölünen Eş Parça Sayısı)", color=RED, font_size=28).next_to(fraction, DOWN, buff=0.5)
        
        # Show Payda first to emphasize the base
        self.play(FadeIn(payda_label, shift=UP))
        self.wait(1.5)
        
        # Show Pay
        self.play(FadeIn(pay_label, shift=DOWN))
        self.wait(2)

        self.play(FadeOut(pay_label), FadeOut(payda_label))

        # Readings
        read1 = Text('1. Okunuş: "Üç bölü dört"', color=DARK_GRAY, font_size=32).next_to(fraction, DOWN, buff=1)
        self.play(Write(read1))
        self.wait(2)

        read2 = Text('2. Okunuş: "Dörtte üç"', color=DARK_GRAY, font_size=32).next_to(read1, DOWN, buff=0.4)
        self.play(Write(read2))
        self.wait(3)

        # Clear scene
        self.play(FadeOut(fraction), FadeOut(read1), FadeOut(read2), FadeOut(title))
        self.wait(1)
