from manim import *
config.pixel_height=1920
config.pixel_width=1080
config.frame_height=14.22
config.frame_width=8.0

class MaarifScene(Scene):
    def construct(self):
        # GİRİŞ (5 kelime -> 1.66 saniye)
        intro_text = Text("Merhaba, Maarif Matematik'e\nhoş geldiniz.", font="DejaVu Sans", color=YELLOW).scale_to_fit_width(6.2)
        self.play(Write(intro_text), run_time=0.66)
        self.wait(1.0)
        self.play(FadeOut(intro_text), run_time=0.2)

        # KANCA (7 kelime -> 2.33 saniye)
        hook_text = Text("Birim kesirlerde payda büyüdükçe\nkesir neden küçülür?", font="DejaVu Sans", color=WHITE).scale_to_fit_width(6.2)
        self.play(Write(hook_text), run_time=1.0)
        self.wait(1.33)
        self.play(FadeOut(hook_text), run_time=0.2)

        # GÖRSEL İSPAT HAZIRLIĞI
        # 1/2 Kesri Modeli
        circle1 = Circle(radius=2, color=WHITE)
        line1 = Line(circle1.get_top(), circle1.get_bottom(), color=WHITE)
        sector1 = Sector(radius=2, angle=PI, start_angle=PI/2, color=ORANGE, fill_opacity=0.7)
        frac1 = MathTex(r"\frac{1}{2}").scale(2)
        group1_pizza = VGroup(circle1, line1, sector1)
        group1 = VGroup(group1_pizza, frac1).arrange(DOWN, buff=0.5)

        # 1/8 Kesri Modeli
        circle2 = Circle(radius=2, color=WHITE)
        line2_1 = Line(circle2.get_left(), circle2.get_right(), color=WHITE)
        line2_2 = Line(circle2.get_top(), circle2.get_bottom(), color=WHITE)
        line2_3 = Line(circle2.point_at_angle(PI/4), circle2.point_at_angle(5*PI/4), color=WHITE)
        line2_4 = Line(circle2.point_at_angle(3*PI/4), circle2.point_at_angle(7*PI/4), color=WHITE)
        lines2 = VGroup(line2_1, line2_2, line2_3, line2_4)
        sector2 = Sector(radius=2, angle=PI/4, start_angle=PI/2, color=RED, fill_opacity=0.7)
        frac2 = MathTex(r"\frac{1}{8}").scale(2)
        group2_pizza = VGroup(circle2, lines2, sector2)
        group2 = VGroup(group2_pizza, frac2).arrange(DOWN, buff=0.5)

        # Dikey Hizalama ve Ekrana Sığdırma
        main_group = VGroup(group1, group2).arrange(DOWN, buff=1.8)
        main_group.scale_to_fit_width(6.2)

        # AÇIKLAMA 1 (10 kelime -> 3.33 saniye)
        self.play(Create(circle1), Create(line1), run_time=1.0)
        self.play(FadeIn(sector1), Write(frac1), run_time=1.0)
        self.wait(1.33)

        # AÇIKLAMA 2 (13 kelime -> 4.33 saniye)
        self.play(Create(circle2), Create(lines2), run_time=1.0)
        self.play(FadeIn(sector2), Write(frac2), run_time=1.0)
        self.wait(2.33)

        # SONUÇ (9 kelime -> 3.0 saniye)
        self.play(FadeOut(main_group), run_time=0.5)
        conc_text = Text("Payda büyüdükçe\nparça sayısı artar\nve dilimler küçülür.", font="DejaVu Sans", color=YELLOW).scale_to_fit_width(6.2)
        self.play(Write(conc_text), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(conc_text), run_time=0.5)

        # ÇIKIŞ (7 kelime -> 2.33 saniye)
        outro_text = Text("Bir sonraki derste\ngörüşmek üzere,\nhoşça kalın.", font="DejaVu Sans", color=WHITE).scale_to_fit_width(6.2)
        self.play(Write(outro_text), run_time=1.0)
        self.wait(1.33)
        
        # Kapanış Sabitleme
        self.wait(5)