from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        text_color = BLACK
        num_color = BLUE
        den_color = RED

        title = Text("Kesirler: Pay ve Payda", color=text_color, font_size=40).to_edge(UP)
        self.play(Write(title))

        fraction = MathTex(r"\frac{3}{4}", color=text_color, font_size=120)
        fraction.move_to(main_center)
        
        fraction[0][0].set_color(num_color)
        fraction[0][2].set_color(den_color)

        self.play(Write(fraction))
        self.wait(1)

        payda_label = Text("Payda: Toplam Eş Parça", color=den_color, font_size=24).next_to(fraction, DOWN, buff=0.8)
        self.play(Write(payda_label))
        self.wait(1)

        pay_label = Text("Pay: Alınan Parça", color=num_color, font_size=24).next_to(fraction, UP, buff=0.8)
        self.play(Write(pay_label))
        self.wait(1)

        reading1 = Text("Okunuş 1: Üç bölü dört", color=text_color, font_size=28).next_to(fraction, LEFT, buff=1.2)
        self.play(Write(reading1))
        self.wait(1)

        reading2 = Text("Okunuş 2: Dörtte üç", color=text_color, font_size=28).next_to(fraction, RIGHT, buff=1.2)
        self.play(Write(reading2))
        self.wait(2)

        all_mobjects = VGroup(title, fraction, pay_label, payda_label, reading1, reading2)
        self.play(FadeOut(all_mobjects))
        self.wait(1)