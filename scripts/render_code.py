from manim import *
import numpy as np

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        # Başlık
        title = Text("Kesirler: Pay ve Payda", color="#333333", font_size=48, weight=BOLD)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title))

        # Kesir: 3/4
        numerator = Text("3", color="#87CEEB", font_size=72, weight=BOLD)
        line = Line(LEFT, RIGHT, color="#333333").scale(0.8)
        denominator = Text("4", color="#333333", font_size=72, weight=BOLD)

        fraction_group = VGroup(numerator, line, denominator).arrange(DOWN, buff=0.3)
        fraction_group.move_to(main_center)

        self.play(FadeIn(fraction_group))
        self.wait(1)

        # Etiketler
        payda_label = Text("Payda (Tüm Eş Parçalar)", color="#333333", font_size=32).next_to(denominator, RIGHT, buff=1)
        pay_label = Text("Pay (Alınan Parça)", color="#87CEEB", font_size=32).next_to(numerator, RIGHT, buff=1)

        self.play(Write(payda_label))
        self.wait(2)
        self.play(Write(pay_label))
        self.wait(2)

        # Okunuş 1: Yukarıdan Aşağıya (3 bölü 4)
        arrow_down = Arrow(start=numerator.get_left() + LEFT*0.3, end=denominator.get_left() + LEFT*0.3, color="#87CEEB", buff=0.1)
        read1 = Text("Üç bölü dört", color="#333333", font_size=36).next_to(arrow_down, LEFT, buff=0.5)

        self.play(GrowArrow(arrow_down), Write(read1))
        self.wait(3)

        # Okunuş 2: Aşağıdan Yukarıya (4'te 3)
        self.play(FadeOut(arrow_down), FadeOut(read1))

        arrow_up = Arrow(start=denominator.get_left() + LEFT*0.3, end=numerator.get_left() + LEFT*0.3, color="#333333", buff=0.1)
        read2 = Text("Dörtte üç", color="#87CEEB", font_size=36).next_to(arrow_up, LEFT, buff=0.5)

        self.play(GrowArrow(arrow_up), Write(read2))
        self.wait(3)

        self.play(FadeOut(arrow_up), FadeOut(read2), FadeOut(pay_label), FadeOut(payda_label))

        # Görselleştirme (Parça - Bütün)
        circle = Circle(radius=1.5, color="#333333", stroke_width=4)
        lines = VGroup(
            Line(circle.get_top(), circle.get_bottom(), color="#333333"),
            Line(circle.get_left(), circle.get_right(), color="#333333")
        )
        pie_chart = VGroup(circle, lines)

        sector1 = Sector(outer_radius=1.5, angle=PI/2, start_angle=0, color="#87CEEB", fill_opacity=0.7)
        sector2 = Sector(outer_radius=1.5, angle=PI/2, start_angle=PI/2, color="#87CEEB", fill_opacity=0.7)
        sector3 = Sector(outer_radius=1.5, angle=PI/2, start_angle=PI, color="#87CEEB", fill_opacity=0.7)
        sectors = VGroup(sector1, sector2, sector3)

        visual_group = VGroup(pie_chart, sectors)

        # Kesri ve görseli yan yana koyup main_center'a hizalama
        target_group = VGroup(fraction_group.copy(), visual_group).arrange(RIGHT, buff=2).move_to(main_center)
        
        self.play(fraction_group.animate.move_to(target_group[0].get_center()))
        visual_group.move_to(target_group[1].get_center())

        self.play(Create(pie_chart))
        self.wait(1)
        self.play(FadeIn(sectors))
        self.wait(3)

        # Kapanış
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)