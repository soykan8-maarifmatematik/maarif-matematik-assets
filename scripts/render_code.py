from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        # Title
        title = Text("Kesir Nedir?", color=BLACK, font_size=48, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Fraction components
        num = Text("3", color=BLACK, font_size=96)
        line = Line(LEFT, RIGHT, color=BLACK).scale(0.8)
        den = Text("4", color=BLACK, font_size=96)
        
        fraction = VGroup(num, line, den).arrange(DOWN, buff=0.3)
        fraction.move_to(main_center)
        
        self.play(FadeIn(fraction, shift=UP))
        self.wait(1)

        # Denominator (Payda)
        payda_label = Text("Payda\n(Eş Parça Sayısı)", color=RED, font_size=24, alignment="CENTER")
        payda_label.next_to(fraction, DOWN, buff=1)
        arrow_payda = Arrow(payda_label.get_top(), den.get_bottom(), color=RED, buff=0.1)
        
        self.play(den.animate.set_color(RED), Write(payda_label), GrowArrow(arrow_payda))
        self.wait(1)

        # Numerator (Pay)
        pay_label = Text("Pay\n(Alınan Parça)", color=BLUE, font_size=24, alignment="CENTER")
        pay_label.next_to(fraction, UP, buff=1)
        arrow_pay = Arrow(pay_label.get_bottom(), num.get_top(), color=BLUE, buff=0.1)

        self.play(num.animate.set_color(BLUE), Write(pay_label), GrowArrow(arrow_pay))
        self.wait(1)

        # Readings
        reading1 = Text("1. Okunuş: Üç bölü dört", color=DARK_GRAY, font_size=28)
        reading1.next_to(fraction, LEFT, buff=1.5)
        
        reading2 = Text("2. Okunuş: Dörtte üç", color=DARK_GRAY, font_size=28)
        reading2.next_to(fraction, RIGHT, buff=1.5)

        self.play(Write(reading1))
        self.wait(1)
        self.play(Write(reading2))
        self.wait(2)

        # Clear screen
        self.play(FadeOut(VGroup(title, fraction, pay_label, payda_label, arrow_pay, arrow_payda, reading1, reading2)))
        self.wait(1)