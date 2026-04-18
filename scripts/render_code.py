from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        # Başlık
        title = Text("Kesirler: Pay ve Payda", color=BLACK, font_size=40).to_edge(UP)
        self.play(Write(title))

        # Kesir İfadesi
        fraction = MathTex(r"\frac{3}{4}", color=BLACK, font_size=96)
        
        pay_text = Text("Pay (Kendi Payımıza Düşen)", color=BLUE, font_size=24).next_to(fraction, UP, buff=0.5)
        payda_text = Text("Payda (Bütünün Parçaları)", color=RED, font_size=24).next_to(fraction, DOWN, buff=0.5)
        
        frac_group = VGroup(fraction, pay_text, payda_text)

        # Görsel Temsil (Pizza/Daire)
        circle = Circle(radius=1.5, color=BLACK)
        sectors = VGroup()
        colors = [BLUE, BLUE, BLUE, LIGHT_GREY]
        for i in range(4):
            sector = Sector(outer_radius=1.5, angle=PI/2, start_angle=i*PI/2, color=colors[i], fill_opacity=0.8, stroke_color=BLACK, stroke_width=2)
            sectors.add(sector)
        
        pizza_group = VGroup(circle, sectors)

        # Grupları yan yana dizip main_center'a sabitleme
        content_group = VGroup(frac_group, pizza_group).arrange(RIGHT, buff=2).move_to(main_center)

        # Animasyonlar
        self.play(Write(fraction))
        self.play(FadeIn(payda_text, shift=UP))
        self.play(Create(circle))
        self.play(FadeIn(sectors[3])) # Alınmayan parça
        self.wait(1)
        
        self.play(FadeIn(pay_text, shift=DOWN))
        self.play(FadeIn(VGroup(sectors[0], sectors[1], sectors[2]))) # Alınan paylar
        self.wait(2)

        self.play(FadeOut(content_group))

        # Okunuşlar
        read_1 = Text("1. Okunuş: 3 bölü 4", color=BLACK, font_size=40)
        read_2 = Text("2. Okunuş: 4'te 3", color=BLACK, font_size=40).next_to(read_1, DOWN, buff=1)
        read_group = VGroup(read_1, read_2).move_to(main_center)

        self.play(Write(read_1))
        self.wait(1)
        self.play(Write(read_2))
        self.wait(2)

        self.play(FadeOut(read_group), FadeOut(title))
