from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class BirimKesirler(Scene):
    def construct(self):
        # Giriş (8 kelime -> 3.33s)
        title = Text("Maarif Matematik", font_size=85).move_to(UP * 4.5)
        title.scale_to_fit_width(7.0)
        self.play(Write(title))
        self.wait(3.33)

        # Soru ve Kanca (12 kelime -> 5.0s)
        q_text = Text("Birim Kesirler Neden Küçülür?", font_size=85).move_to(DOWN * 4.5)
        q_text.scale_to_fit_width(7.0)
        self.play(Write(q_text))
        self.wait(5.0)

        # Pizzaların ortaya çıkışı (12 kelime -> 5.0s)
        self.play(FadeOut(title), FadeOut(q_text))
        circle1 = Circle(radius=1.8, color=WHITE)
        circle2 = Circle(radius=1.8, color=WHITE)
        pizzas = VGroup(circle1, circle2).arrange(DOWN, buff=1.2)
        self.play(Create(pizzas))
        self.wait(5.0)

        # İlk Pizza 1/2 (15 kelime -> 6.25s)
        slice1 = Sector(radius=1.8, angle=PI, color=YELLOW, fill_opacity=0.8, arc_center=circle1.get_center())
        frac1 = MathTex(r"\frac{1}{2}").next_to(circle1, LEFT, buff=0.5).scale(2)
        self.play(Create(slice1), Write(frac1))
        self.wait(6.25)

        # İkinci Pizza 1/10 (19 kelime -> 7.91s)
        slice2 = Sector(radius=1.8, angle=TAU/10, color=ORANGE, fill_opacity=0.8, arc_center=circle2.get_center())
        frac2 = MathTex(r"\frac{1}{10}").next_to(circle2, LEFT, buff=0.5).scale(2)
        self.play(Create(slice2), Write(frac2))
        self.wait(7.91)

        # Mantık Açıklaması (20 kelime -> 8.33s)
        exp_text = Text("Payda Büyüdükçe Dilim Küçülür", font_size=85).move_to(UP * 4.5)
        exp_text.scale_to_fit_width(7.0)
        self.play(Write(exp_text))
        self.wait(8.33)

        # Sonuç (17 kelime -> 7.08s)
        comp_text = MathTex(r"\frac{1}{2} > \frac{1}{10}").move_to(DOWN * 4.5).scale(2.5)
        self.play(Write(comp_text))
        self.wait(7.08)

        # Kapanış (7 kelime -> 2.91s)
        self.play(FadeOut(comp_text))
        outro_text = Text("Görüşmek Üzere!", font_size=85).move_to(DOWN * 4.5)
        outro_text.scale_to_fit_width(7.0)
        self.play(Write(outro_text))
        self.wait(2.91)