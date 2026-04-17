from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        # Renkler
        text_color = BLACK
        pay_color = "#D32F2F"  # Kırmızı
        payda_color = "#1976D2"  # Mavi

        # Kesir Bileşenleri
        num = MathTex("3", color=text_color).scale(2.5)
        line = Line(LEFT*0.8, RIGHT*0.8, color=text_color).set_stroke(width=4)
        den = MathTex("4", color=text_color).scale(2.5)

        frac_group = VGroup(num, line, den).arrange(DOWN, buff=0.3)
        frac_group.move_to(main_center + UP * 1.5)

        # Etiketler
        pay_label = Text("Pay (Alınan Parça)", color=pay_color, font_size=24)
        pay_label.next_to(num, RIGHT, buff=1.5)
        
        payda_label = Text("Payda (Eş Parçalar)", color=payda_color, font_size=24)
        payda_label.next_to(den, RIGHT, buff=1.5)

        # Oklar
        arrow_pay = Arrow(pay_label.get_left(), num.get_right(), color=pay_color, buff=0.2)
        arrow_payda = Arrow(payda_label.get_left(), den.get_right(), color=payda_color, buff=0.2)

        # Animasyon: Payda ve Kesir Çizgisi
        self.play(Create(line))
        self.play(Write(den))
        self.play(Write(payda_label), GrowArrow(arrow_payda))
        self.wait(1)
        
        # Animasyon: Pay
        self.play(Write(num))
        self.play(Write(pay_label), GrowArrow(arrow_pay))
        self.wait(1)

        # Görsel Temsil (Pasta Grafiği)
        circle_center = main_center + DOWN * 1.5 + LEFT * 2.5
        circle = Circle(radius=1.2, color=text_color, stroke_width=4)
        circle.move_to(circle_center)

        lines = VGroup(
            Line(circle.get_top(), circle.get_bottom(), color=text_color, stroke_width=4),
            Line(circle.get_left(), circle.get_right(), color=text_color, stroke_width=4)
        )

        sectors = VGroup()
        for i in range(3):
            sectors.add(Sector(arc_center=circle_center, outer_radius=1.18, start_angle=i*PI/2, angle=PI/2, color=pay_color, fill_opacity=0.7))

        self.play(Create(circle), Create(lines))
        self.wait(1)
        self.play(FadeIn(sectors))
        self.wait(1)

        # Okunuşlar
        read_1 = Text("1. Okunuş: Üç bölü dört", color=text_color, font_size=28)
        read_2 = Text("2. Okunuş: Dörtte üç", color=text_color, font_size=28)
        read_group = VGroup(read_1, read_2).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        read_group.move_to(main_center + DOWN * 1.5 + RIGHT * 2.5)

        self.play(Write(read_1))
        self.wait(1)
        self.play(Write(read_2))
        self.wait(2)

        # Kapanış
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)