from manim import *
import numpy as np

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        dark_gray = "#333333"
        maarif_blue = "#87CEEB"
        main_center = DOWN * 0.5

        title = Text("Kesir Nedir?", color=dark_gray, font_size=48, weight=BOLD)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title))

        num = Text("3", color=dark_gray, font_size=64)
        line = Line(LEFT, RIGHT, color=dark_gray).set_length(1.2)
        den = Text("4", color=dark_gray, font_size=64)
        fraction = VGroup(num, line, den).arrange(DOWN, buff=0.3)
        fraction.move_to(main_center + LEFT * 3)

        pay_label = Text("Pay", color=maarif_blue, font_size=28).next_to(num, UP, buff=0.6)
        pay_arrow = Arrow(pay_label.get_bottom(), num.get_top(), color=dark_gray, buff=0.1)

        payda_label = Text("Payda", color=maarif_blue, font_size=28).next_to(den, DOWN, buff=0.6)
        payda_arrow = Arrow(payda_label.get_top(), den.get_bottom(), color=dark_gray, buff=0.1)

        self.play(Write(fraction))
        self.wait(1)

        self.play(FadeIn(payda_label), GrowArrow(payda_arrow))
        self.wait(1)

        self.play(FadeIn(pay_label), GrowArrow(pay_arrow))
        self.wait(1)

        sectors = VGroup()
        for i in range(4):
            sector = Sector(outer_radius=1.5, angle=PI/2, start_angle=i*PI/2, color=dark_gray, fill_opacity=0, stroke_width=3)
            sectors.add(sector)
        sectors.move_to(main_center + RIGHT * 3)

        self.play(Create(sectors))
        self.wait(1)

        filled_sectors = VGroup()
        for i in range(3):
            filled_sector = Sector(outer_radius=1.5, angle=PI/2, start_angle=i*PI/2, color=maarif_blue, fill_opacity=0.8, stroke_width=3)
            filled_sectors.add(filled_sector)
        filled_sectors.move_to(main_center + RIGHT * 3)

        self.play(FadeIn(filled_sectors))
        self.wait(1)

        reading1 = Text("1. Okunuş: Dörtte Üç", color=maarif_blue, font_size=32)
        reading2 = Text("2. Okunuş: Üç Bölü Dört", color=dark_gray, font_size=32)
        readings = VGroup(reading1, reading2).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        readings.move_to(main_center + DOWN * 2.5)

        self.play(Write(reading1))
        self.wait(1)
        self.play(Write(reading2))
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)