from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        title = Text("Kesir Nedir?", color=BLACK, font_size=48)
        title.to_edge(UP)
        self.play(Write(title))

        # Kesir
        fraction = MathTex(r"\frac{2}{5}", color=BLACK, font_size=96)
        
        # Etiketler
        pay_label = Text("Pay (Alınan)", color=BLUE, font_size=28)
        pay_label.next_to(fraction, RIGHT, buff=1).shift(UP*0.6)
        payda_label = Text("Payda (Bütün)", color=RED, font_size=28)
        payda_label.next_to(fraction, RIGHT, buff=1).shift(DOWN*0.6)
        
        arrow_pay = Arrow(pay_label.get_left(), fraction[0][0].get_right(), color=BLUE, buff=0.1)
        arrow_payda = Arrow(payda_label.get_left(), fraction[0][2].get_right(), color=RED, buff=0.1)

        frac_group = VGroup(fraction, pay_label, payda_label, arrow_pay, arrow_payda)

        # Görselleştirme (5 parçalı dikdörtgen)
        rect_group = VGroup()
        for i in range(5):
            rect = Rectangle(height=1, width=1, color=BLACK, fill_opacity=0.6 if i < 2 else 0, fill_color=BLUE)
            rect_group.add(rect)
        rect_group.arrange(RIGHT, buff=0)
        
        # Okunuşlar
        read_1 = Text("1. Okunuş: İki bölü beş", color=DARK_BLUE, font_size=32)
        read_2 = Text("2. Okunuş: Beşte iki", color=DARK_RED, font_size=32)
        read_group = VGroup(read_1, read_2).arrange(DOWN, buff=0.4)

        # Tüm elemanları gruplayıp merkeze hizalama
        master_group = VGroup(frac_group, rect_group, read_group).arrange(DOWN, buff=1)
        master_group.move_to(main_center)

        # Animasyonlar
        self.play(Write(fraction))
        self.wait(1)
        
        self.play(Write(payda_label), GrowArrow(arrow_payda))
        self.wait(1)
        
        self.play(Write(pay_label), GrowArrow(arrow_pay))
        self.wait(1)

        self.play(Create(rect_group))
        self.wait(2)

        self.play(Write(read_1))
        self.wait(1)
        self.play(Write(read_2))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(master_group))
        self.wait(1)