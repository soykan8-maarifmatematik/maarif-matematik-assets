from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        # Intro
        title = Text("Kesirler", color=BLACK, font_size=60)
        self.play(Write(title))
        self.wait(10)
        self.play(title.animate.to_edge(UP))

        # Pizza (Bütün ve Eş Parçalar)
        circle = Circle(radius=1.5, color=BLACK)
        lines = VGroup(
            Line(circle.get_top(), circle.get_bottom(), color=BLACK),
            Line(circle.get_left(), circle.get_right(), color=BLACK)
        )
        pizza = VGroup(circle, lines)

        # Sectors (Alınan 3 parça)
        sectors = VGroup(*[
            Sector(outer_radius=1.5, angle=PI/2, start_angle=i*PI/2, color=BLUE, fill_opacity=0.5)
            for i in range(3)
        ])
        pizza_group = VGroup(pizza, sectors).move_to(main_center + LEFT * 3)

        self.play(Create(pizza))
        self.wait(15)
        self.play(FadeIn(sectors))
        self.wait(20)

        # Kesir Yazımı (3/4)
        fraction = MathTex("3", "\\over", "4", color=BLACK, font_size=120).move_to(main_center + RIGHT * 2)
        self.play(Write(fraction))
        self.wait(15)

        # Payda Açıklaması
        payda_text = Text("Payda", color=RED, font_size=30).next_to(fraction[2], DOWN, buff=0.5)
        payda_arrow = Arrow(payda_text.get_top(), fraction[2].get_bottom(), color=RED, buff=0.1)
        self.play(FadeIn(payda_text, payda_arrow))
        self.wait(25)

        # Pay Açıklaması
        pay_text = Text("Pay", color=BLUE, font_size=30).next_to(fraction[0], UP, buff=0.5)
        pay_arrow = Arrow(pay_text.get_bottom(), fraction[0].get_top(), color=BLUE, buff=0.1)
        self.play(FadeIn(pay_text, pay_arrow))
        self.wait(25)

        # Okunuşlar
        readings_group = VGroup(
            Text("1. Okunuş: Üç bölü dört", color=BLACK, font_size=30),
            Text("2. Okunuş: Dörtte üç", color=BLACK, font_size=30)
        ).arrange(DOWN, buff=0.5).move_to(main_center + DOWN * 2.5)

        self.play(Write(readings_group[0]))
        self.wait(25)

        self.play(Write(readings_group[1]))
        self.wait(25)

        # Outro
        self.play(
            FadeOut(pizza_group), FadeOut(pay_text), FadeOut(pay_arrow), 
            FadeOut(payda_text), FadeOut(payda_arrow), FadeOut(readings_group)
        )
        self.play(fraction.animate.move_to(main_center).scale(1.5))
        self.wait(20)