from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0

class MaarifScene(Scene):
    def construct(self):
        # GİRİŞ (5 kelime / 3.0 = 1.67s)
        logo = Text("Maarif Matematik", font_size=50, color=YELLOW).move_to(UP * 6.5)
        self.play(Write(logo))
        self.wait(1.67)

        # GÖVDE 1: Soru (11 kelime / 3.0 = 3.67s)
        title = Text("Birim Kesirlerin Büyüklüğü", font_size=40).next_to(logo, DOWN, buff=0.3)
        self.play(Write(title))
        self.wait(3.67)

        # GÖVDE 2: Pizzaların Çizimi (14 kelime / 3.0 = 4.67s)
        pizza1 = Circle(radius=1.5, color=WHITE).move_to(UP * 2.5)
        pizza2 = Circle(radius=1.5, color=WHITE).move_to(DOWN * 2)
        line1 = Line(pizza1.get_top(), pizza1.get_bottom())
        line2_v = Line(pizza2.get_top(), pizza2.get_bottom())
        line2_h = Line(pizza2.get_left(), pizza2.get_right())
        self.play(Create(pizza1), Create(pizza2), Create(line1), Create(line2_v), Create(line2_h))
        self.wait(4.67)

        # GÖVDE 3: 1/2 Gösterimi (14 kelime / 3.0 = 4.67s)
        slice1 = Sector(arc_center=pizza1.get_center(), outer_radius=1.5, angle=PI, start_angle=-PI/2, color=ORANGE, fill_opacity=0.7)
        frac1 = MathTex(r"\frac{1}{2}", font_size=72).next_to(pizza1, RIGHT, buff=0.8)
        self.play(Create(slice1), Write(frac1))
        self.wait(4.67)

        # GÖVDE 4: 1/4 Gösterimi (14 kelime / 3.0 = 4.67s)
        slice2 = Sector(arc_center=pizza2.get_center(), outer_radius=1.5, angle=PI/2, start_angle=0, color=ORANGE, fill_opacity=0.7)
        frac2 = MathTex(r"\frac{1}{4}", font_size=72).next_to(pizza2, RIGHT, buff=0.8)
        self.play(Create(slice2), Write(frac2))
        self.wait(4.67)

        # GÖVDE 5: Karşılaştırma ve Kural (19 kelime / 3.0 = 6.33s)
        self.play(FadeOut(pizza1, pizza2, line1, line2_v, line2_h, slice1, slice2, frac1, frac2))
        comp_text = MathTex(r"\frac{1}{2} > \frac{1}{4}", font_size=120, color=YELLOW).move_to(UP * 1)
        rule_text = VGroup(
            Text("Payda büyüdükçe", font_size=45, color=GREEN),
            Text("parça küçülür!", font_size=45, color=GREEN)
        ).arrange(DOWN).next_to(comp_text, DOWN, buff=1)
        self.play(Write(comp_text), Write(rule_text))
        self.wait(6.33)

        # ÇIKIŞ (MÜHÜR) (7 kelime / 3.0 = 2.33s)
        outro = VGroup(
            Text("Maarif Matematik ile mantığını kavra,", font_size=35, color=BLUE),
            Text("takipte kal!", font_size=35, color=BLUE)
        ).arrange(DOWN).move_to(DOWN * 5.5)
        self.play(Write(outro))
        self.wait(2.33)

        # FİNAL SABİTLEME
        self.wait(4)
