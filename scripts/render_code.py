from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # Başlık ve Güvenli Alan Üst Sınırı
        title = Text("Birim Kesirler", color=BLACK, font_size=60, weight=BOLD)
        title.to_edge(UP, buff=2.0).scale(1.2)
        self.play(Write(title))
        self.wait(2.0)

        question = Text("Payda büyüdükçe ne olur?", color=BLACK, font_size=40)
        question.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(question))
        self.wait(3.66)

        # 1/2 Kesri Görseli
        circle2 = Circle(radius=1.0, color=BLACK)
        slice2 = Sector(radius=1.0, angle=TAU/2, color=BLUE, fill_opacity=0.8)
        line2_1 = Line(circle2.get_center() + LEFT*1.0, circle2.get_center() + RIGHT*1.0, color=BLACK)
        label2 = MathTex(r"\frac{1}{2}", color=BLACK, font_size=70)
        group2 = VGroup(VGroup(circle2, slice2, line2_1), label2).arrange(RIGHT, buff=1.0)

        # 1/4 Kesri Görseli
        circle4 = Circle(radius=1.0, color=BLACK)
        slice4 = Sector(radius=1.0, angle=TAU/4, color=GREEN, fill_opacity=0.8)
        line4_1 = Line(circle4.get_center() + LEFT*1.0, circle4.get_center() + RIGHT*1.0, color=BLACK)
        line4_2 = Line(circle4.get_center() + UP*1.0, circle4.get_center() + DOWN*1.0, color=BLACK)
        label4 = MathTex(r"\frac{1}{4}", color=BLACK, font_size=70)
        group4 = VGroup(VGroup(circle4, slice4, line4_1, line4_2), label4).arrange(RIGHT, buff=1.0)

        # Merkezi Yerleşim ve Objelerin Birbirine Binmemesi
        main_group = VGroup(group2, group4).arrange(DOWN, buff=2.5)
        main_group.next_to(question, DOWN, buff=0.5)

        self.play(FadeIn(main_group))
        self.wait(2.0)

        self.play(Indicate(group2, color=BLUE, scale_factor=1.1))
        self.wait(5.0)

        self.play(Indicate(group4, color=GREEN, scale_factor=1.1))
        self.wait(4.0)

        # Sonuç Metni (y = -4.5 sınırının üzerinde kalacak şekilde ayarlandı)
        conclusion = Text("Payda = Kişi Sayısı", color=RED, font_size=45, weight=BOLD)
        conclusion.next_to(main_group, DOWN, buff=0.5)
        self.play(Write(conclusion))
        self.wait(4.66)

        # Kapanış
        self.wait(2.33)
