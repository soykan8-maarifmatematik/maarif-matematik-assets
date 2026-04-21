from manim import *

class KesirMantigi(Scene):
    def construct(self):
        # Sabitler ve Renkler
        main_center = DOWN * 0.5
        BLUE_C = "#1976D2"
        RED_C = "#D32F2F"
        GRAY_C = "#333333"

        # 1. Sahne: Giriş (Toplam 8 saniye)
        title = Tex("Kesirlerin Mantığı", color=BLUE_C, font_size=48).move_to(UP * 2.5)
        self.play(Write(title)) # 1 sn
        self.wait(7)

        # 2. Sahne: Pay ve Payda Mantığı (Toplam 14 saniye)
        fraction = MathTex(r"\frac{3}{4}", font_size=120, color=GRAY_C).move_to(main_center + LEFT * 3)
        fraction[0][0].set_color(RED_C)  # Pay (3)
        fraction[0][2].set_color(BLUE_C) # Payda (4)

        pay_text = Tex("Pay: Alınan Parça", color=RED_C, font_size=32).next_to(fraction, UP, buff=0.5)
        payda_text = Tex("Payda: Toplam Eş Parça", color=BLUE_C, font_size=32).next_to(fraction, DOWN, buff=0.5)

        # Pasta/Bütün Modeli
        pie_group = VGroup()
        circle = Circle(radius=1.5, color=BLUE_C, stroke_width=4)
        lines = VGroup(
            Line(circle.get_top(), circle.get_bottom(), color=BLUE_C),
            Line(circle.get_left(), circle.get_right(), color=BLUE_C)
        )
        sectors = VGroup(
            Sector(radius=1.5, angle=PI/2, start_angle=0, color=RED_C, fill_opacity=0.6),
            Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color=RED_C, fill_opacity=0.6),
            Sector(radius=1.5, angle=PI/2, start_angle=PI, color=RED_C, fill_opacity=0.6)
        )
        pie_group.add(circle, lines, sectors).move_to(main_center + RIGHT * 3)

        self.play(Write(fraction)) # 1 sn
        self.play(Create(pie_group[0]), Create(pie_group[1])) # 1 sn
        self.play(Write(payda_text)) # 1 sn
        self.play(FadeIn(pie_group[2])) # 1 sn
        self.play(Write(pay_text)) # 1 sn
        self.wait(9)

        # 3. Sahne: Yukarıdan Aşağıya Okunuş (Toplam 10 saniye)
        arrow_down = Arrow(start=UP, end=DOWN, color=GRAY_C).next_to(fraction, LEFT, buff=0.5)
        read_down = Tex("3 bölü 4", color=GRAY_C, font_size=36).next_to(arrow_down, LEFT)

        self.play(GrowArrow(arrow_down)) # 1 sn
        self.play(Write(read_down)) # 1 sn
        self.wait(8)

        # 4. Sahne: Aşağıdan Yukarıya Okunuş (Toplam 10 saniye)
        arrow_up = Arrow(start=DOWN, end=UP, color=GRAY_C).next_to(fraction, RIGHT, buff=0.5)
        read_up = Tex("4'te 3", color=GRAY_C, font_size=36).next_to(arrow_up, RIGHT)

        self.play(GrowArrow(arrow_up)) # 1 sn
        self.play(Write(read_up)) # 1 sn
        self.wait(8)

        # 5. Sahne: Kapanış (Toplam 8 saniye)
        all_objects = Group(title, fraction, pay_text, payda_text, pie_group, arrow_down, read_down, arrow_up, read_up)
        self.play(FadeOut(all_objects)) # 1 sn
        
        outro_text = Tex("Maarif Matematik", color=BLUE_C, font_size=60).move_to(main_center)
        self.play(Write(outro_text)) # 1 sn
        self.wait(6)
