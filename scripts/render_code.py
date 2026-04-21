from manim import *

class KesirMantigi(Scene):
    def construct(self):
        # Renk Paleti
        BLUE_C = "#1976D2"
        RED_C = "#D32F2F"
        GRAY_C = "#333333"

        # Merkez Noktasi Kurali
        main_center = DOWN * 0.5

        # Baslik
        title = Text("KESİRLERİN MANTIĞI", font_size=40, color=WHITE).to_edge(UP)
        self.play(Write(title))
        # Paragraf 1 Bekleme Suresi (~34 kelime)
        self.wait(15)

        # Kesir Kurulumu (Sol Taraf)
        frac_center = main_center + LEFT * 3

        line = Line(LEFT, RIGHT, color=GRAY_C).scale(0.8).move_to(frac_center)
        denom = MathTex("4", color=BLUE_C, font_size=72).next_to(line, DOWN, buff=0.3)
        denom_label = Text("Payda (Bütün)", font_size=24, color=BLUE_C).next_to(denom, DOWN)

        self.play(Create(line))
        self.play(Write(denom), Write(denom_label))
        # Paragraf 2 Bekleme Suresi (~75 kelime)
        self.wait(35)

        num = MathTex("3", color=RED_C, font_size=72).next_to(line, UP, buff=0.3)
        num_label = Text("Pay (Alınan)", font_size=24, color=RED_C).next_to(num, UP)

        self.play(Write(num), Write(num_label))
        # Paragraf 3 Bekleme Suresi (~57 kelime)
        self.wait(30)

        # Pasta Dilimi (Sector) Kurulumu (Sag Taraf)
        pie_center = main_center + RIGHT * 3
        sectors = VGroup()
        colors = [RED_C, RED_C, RED_C, GRAY_C]
        angles = [PI/2, PI/2, PI/2, PI/2]
        start_angle = 0

        for i in range(4):
            # KURAL: outer_radius ASLA kullanilmaz, sadece radius.
            sector = Sector(
                arc_center=ORIGIN,
                radius=1.5,
                angle=angles[i],
                start_angle=start_angle,
                color=colors[i],
                fill_opacity=0.8,
                stroke_color=WHITE,
                stroke_width=2
            )
            sectors.add(sector)
            start_angle += angles[i]

        sectors.move_to(pie_center)

        self.play(Create(sectors), run_time=2)
        # Paragraf 4 Bekleme Suresi (~49 kelime)
        self.wait(25)

        # Okunus 1: Yukaridan Asagiya (Kirmizi Ok)
        arrow_down = Arrow(start=num.get_right() + RIGHT*0.2, end=denom.get_right() + RIGHT*0.2, color=RED_C, buff=0.1)
        read_1 = Text("Üç bölü dört", font_size=24, color=RED_C).next_to(arrow_down, RIGHT)

        self.play(GrowArrow(arrow_down))
        self.play(Write(read_1))
        # Paragraf 5 Bekleme Suresi (~59 kelime)
        self.wait(30)

        # Okunus 2: Asagidan Yukariya (Mavi Ok)
        arrow_up = Arrow(start=denom.get_left() + LEFT*0.2, end=num.get_left() + LEFT*0.2, color=BLUE_C, buff=0.1)
        read_2 = Text("Dörtte üç", font_size=24, color=BLUE_C).next_to(arrow_up, LEFT)

        self.play(GrowArrow(arrow_up))
        self.play(Write(read_2))
        # Paragraf 6 Bekleme Suresi (~60 kelime)
        self.wait(30)

        # Kapanis Bekleme Suresi (~33 kelime)
        self.wait(20)
