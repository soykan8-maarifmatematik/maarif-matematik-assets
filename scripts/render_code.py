from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class BirimKesir(Scene):
    def construct(self):
        baslik = Text("Birim Kesirler", color=YELLOW)
        baslik.scale_to_fit_width(6.8)
        baslik.to_edge(UP, buff=1)
        self.play(Write(baslik))
        self.wait(3.33)

        alt_yazi = Text("Pizza Mantigi", color=WHITE)
        alt_yazi.scale_to_fit_width(6.8)
        alt_yazi.next_to(baslik, DOWN, buff=0.5)
        self.play(FadeIn(alt_yazi))
        self.wait(4.58)

        daire = Circle(radius=3, color=WHITE, fill_opacity=0.1)
        self.play(Create(daire))
        self.wait(3.33)

        dilim_iki = Sector(arc_center=daire.get_center(), radius=3, angle=PI, start_angle=0, color=ORANGE, fill_opacity=0.8)
        self.play(Create(dilim_iki))
        self.wait(7.5)

        yazi_iki = Text("1 / 2", color=WHITE)
        yazi_iki.scale_to_fit_width(6.8)
        yazi_iki.move_to(UP * 1.5)
        self.play(Write(yazi_iki))
        self.wait(1.25)

        self.play(FadeOut(dilim_iki), FadeOut(yazi_iki))

        dilim_sekiz = Sector(arc_center=daire.get_center(), radius=3, angle=PI/4, start_angle=0, color=RED, fill_opacity=0.8)
        self.play(Create(dilim_sekiz))
        self.wait(7.5)

        yazi_sekiz = Text("1 / 8", color=WHITE)
        yazi_sekiz.scale_to_fit_width(6.8)
        yazi_sekiz.move_to(RIGHT * 1.5 + UP * 0.6)
        self.play(Write(yazi_sekiz))
        self.wait(5.0)

        kural = Text("Payda Buyudukce Deger Kuculur", color=GREEN)
        kural.scale_to_fit_width(6.8)
        kural.to_edge(DOWN, buff=2)
        self.play(Write(kural))
        self.wait(5.83)

        veda = Text("Maarif Matematik", color=BLUE)
        veda.scale_to_fit_width(6.8)
        self.play(FadeOut(daire), FadeOut(dilim_sekiz), FadeOut(yazi_sekiz), FadeOut(baslik), FadeOut(alt_yazi), FadeOut(kural))
        self.play(FadeIn(veda))
        self.wait(2.91)