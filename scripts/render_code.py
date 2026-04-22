from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class BirimKesirler(Scene):
    def construct(self):
        # Kanca (0-5 sn)
        hook_text = Text("Payda Büyüdükçe\nDeğer Neden Küçülür?", font_size=65, color=WHITE)
        self.play(Write(hook_text))
        self.wait(2.4)
        self.play(FadeOut(hook_text))

        # Gövde - Pizza 1 (1/2)
        circle1 = Circle(radius=2, color=YELLOW, fill_opacity=0.2)
        frac1 = MathTex(r"\frac{1}{2}", font_size=120)
        group1 = VGroup(circle1, frac1).arrange(RIGHT, buff=0.6)
        
        sector1 = Sector(radius=2, angle=PI, color=ORANGE, fill_opacity=0.8)
        sector1.move_to(circle1.get_center())
        
        pizza_group1 = VGroup(group1, sector1).scale(0.9)
        pizza_group1.move_to(UP * 2.5)

        self.play(FadeIn(circle1))
        self.wait(1.0)
        self.play(FadeIn(sector1))
        self.wait(2.0)
        self.play(Write(frac1))
        self.wait(2.6)

        # Gövde - Pizza 2 (1/8)
        circle2 = Circle(radius=2, color=YELLOW, fill_opacity=0.2)
        frac2 = MathTex(r"\frac{1}{8}", font_size=120)
        group2 = VGroup(circle2, frac2).arrange(RIGHT, buff=0.6)
        
        sector2 = Sector(radius=2, angle=TAU/8, color=ORANGE, fill_opacity=0.8)
        sector2.move_to(circle2.get_center())
        
        pizza_group2 = VGroup(group2, sector2).scale(0.9)
        pizza_group2.move_to(DOWN * 2.5)

        self.play(FadeIn(circle2))
        self.wait(1.0)
        self.play(FadeIn(sector2))
        self.wait(2.0)
        self.play(Write(frac2))
        self.wait(2.6)

        # Sonuç Vurgusu
        conc_text = Text("Payda = Kişi Sayısı", font_size=65, color=GREEN)
        self.play(Write(conc_text))
        self.wait(4.4)

        self.play(FadeOut(pizza_group1), FadeOut(pizza_group2), FadeOut(conc_text))

        # Kapanış (CTA) (50-60 sn)
        cta_text = Text("Maarif Matematik ile\nmantığını kavra\ntakipte kal", font_size=70, color=YELLOW)
        self.play(Write(cta_text))
        self.wait(2.8)
        self.play(FadeOut(cta_text))
