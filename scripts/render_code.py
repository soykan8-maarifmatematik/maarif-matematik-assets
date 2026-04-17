from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        title = Text("Kesirler: Pay, Payda ve Okunuş", color=BLACK, font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        numerator = Text("3", color=BLUE, font_size=64)
        line = Line(LEFT, RIGHT, color=BLACK).scale(0.5)
        denominator = Text("4", color=RED, font_size=64)

        numerator.next_to(line, UP, buff=0.2)
        denominator.next_to(line, DOWN, buff=0.2)
        
        fraction = VGroup(numerator, line, denominator)

        pay_label = Text("<- Pay (Alınan Parça)", color=BLUE, font_size=24)
        pay_label.next_to(numerator, RIGHT, buff=0.3)

        payda_label = Text("<- Payda (Toplam Parça)", color=RED, font_size=24)
        payda_label.next_to(denominator, RIGHT, buff=0.3)

        read_1 = Text("Dörtte Üç", color=DARK_GRAY, font_size=32)
        read_2 = Text("Üç Bölü Dört", color=DARK_GRAY, font_size=32)
        
        read_group = VGroup(read_1, read_2).arrange(DOWN, buff=0.5)
        read_group.next_to(fraction, LEFT, buff=1.5)

        content_group = VGroup(fraction, pay_label, payda_label, read_group)
        content_group.move_to(main_center)

        self.play(Write(line))
        self.play(Write(denominator), Write(payda_label))
        self.wait(1)
        self.play(Write(numerator), Write(pay_label))
        self.wait(2)
        
        self.play(Write(read_1))
        self.wait(2)
        self.play(Write(read_2))
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)