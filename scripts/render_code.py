from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        # BAŞLIK
        title = Text("Birim Kesirler", color=BLACK, weight=BOLD).to_edge(UP, buff=1.0).scale(1.2)
        self.play(Write(title))
        self.wait(2.66)

        # ALT SONUÇ METNİ
        bottom_text = Text("Payda büyüdükçe değer küçülür!", color=RED, weight=BOLD).to_edge(DOWN, buff=3.5)
        self.play(Write(bottom_text))
        self.wait(1.66)

        # MODELLER
        circle1 = Circle(radius=1.5, color=BLACK)
        sector1 = Sector(radius=1.5, angle=PI, color=BLUE, fill_opacity=0.8)
        pizza1 = VGroup(circle1, sector1)

        circle2 = Circle(radius=1.5, color=BLACK)
        sector2 = Sector(radius=1.5, angle=PI/2, color=ORANGE, fill_opacity=0.8)
        pizza2 = VGroup(circle2, sector2)

        models = VGroup(pizza1, pizza2).arrange(RIGHT, buff=1.5).shift(UP * 2.0)

        self.play(Create(circle1), FadeIn(sector1))
        self.wait(4.66)

        self.play(Create(circle2), FadeIn(sector2))
        self.wait(4.66)

        # KESİR SAYILARI
        frac1 = MathTex(r"\frac{1}{2}", color=BLACK).scale(2.0).next_to(pizza1, DOWN, buff=0.8)
        frac2 = MathTex(r"\frac{1}{4}", color=BLACK).scale(2.0).next_to(pizza2, DOWN, buff=0.8)
        
        self.play(Write(frac1), Write(frac2))
        self.wait(1.0)

        gt_sign = MathTex(">", color=BLACK).scale(2.5).move_to((frac1.get_center() + frac2.get_center()) / 2)
        self.play(Write(gt_sign))
        self.wait(2.33)

        # Kapanış
        self.wait(5.0)
