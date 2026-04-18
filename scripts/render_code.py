from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        title = Text("Kesir Nedir?", color=BLACK, font_size=48, weight=BOLD).to_edge(UP)
        
        num = MathTex("3", color=BLUE, font_size=120)
        line = Line(LEFT, RIGHT, color=BLACK).scale(0.8)
        den = MathTex("4", color=RED, font_size=120)
        
        fraction = VGroup(num, line, den).arrange(DOWN, buff=0.3).move_to(main_center)
        
        pay_text = Text("Pay (Bizim payımıza düşen)", color=BLUE, font_size=28).next_to(num, RIGHT, buff=1)
        pay_arrow = Arrow(pay_text.get_left(), num.get_right(), color=BLUE, buff=0.2)
        
        payda_text = Text("Payda (Bütünü pay eden)", color=RED, font_size=28).next_to(den, RIGHT, buff=1)
        payda_arrow = Arrow(payda_text.get_left(), den.get_right(), color=RED, buff=0.2)

        read_1 = Text("1. Okunuş: Üç bölü dört", color=DARK_GRAY, font_size=32).next_to(fraction, LEFT, buff=1.5).shift(UP*0.5)
        read_2 = Text("2. Okunuş: Dörtte üç", color=DARK_GRAY, font_size=32).next_to(fraction, LEFT, buff=1.5).shift(DOWN*0.5)

        self.play(Write(title))
        self.wait(1)
        
        self.play(Create(line))
        self.play(Write(den))
        self.play(Write(payda_text), GrowArrow(payda_arrow))
        self.wait(2)
        
        self.play(Write(num))
        self.play(Write(pay_text), GrowArrow(pay_arrow))
        self.wait(2)
        
        self.play(Write(read_1))
        self.wait(2)
        
        self.play(Write(read_2))
        self.wait(3)
        
        self.play(FadeOut(Group(title, fraction, pay_text, pay_arrow, payda_text, payda_arrow, read_1, read_2)))
        self.wait(1)