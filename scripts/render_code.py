from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # GİRİŞ (5 kelime = 1.67s)
        intro_text = Text("Merhaba,\nMaarif Matematik'e\nhoş geldiniz.", font="DejaVu Sans", font_size=48).move_to(UP*2)
        self.play(Write(intro_text), run_time=0.67)
        self.wait(1.0)
        self.play(FadeOut(intro_text), run_time=0.5)

        # GÖVDE (60 kelime = 20.0s)
        # Kısım 1: 10 kelime = 3.33s
        q_text = Text("Payda büyüdükçe\ndeğer neden küçülür?", font="DejaVu Sans", font_size=40).move_to(UP*3.5)
        self.play(Write(q_text), run_time=1.0)
        self.wait(2.33)

        # Kısım 2: 12 kelime = 4.0s
        circle1 = Circle(radius=1.3, color=WHITE)
        line1 = Line(circle1.get_top(), circle1.get_bottom(), color=WHITE)
        sector1 = Sector(radius=1.3, angle=PI, start_angle=PI/2, color=BLUE, fill_opacity=0.7)
        label1 = MathTex(r"\frac{1}{2}", font_size=72)
        group1 = VGroup(VGroup(circle1, line1, sector1), label1).arrange(RIGHT, buff=1.0)

        # Kısım 3: 11 kelime = 3.67s
        circle2 = Circle(radius=1.3, color=WHITE)
        line2_v = Line(circle2.get_top(), circle2.get_bottom(), color=WHITE)
        line2_h = Line(circle2.get_left(), circle2.get_right(), color=WHITE)
        sector2 = Sector(radius=1.3, angle=PI/2, start_angle=PI/2, color=RED, fill_opacity=0.7)
        label2 = MathTex(r"\frac{1}{4}", font_size=72)
        group2 = VGroup(VGroup(circle2, line2_v, line2_h, sector2), label2).arrange(RIGHT, buff=1.0)

        # Grupları güvenli alana yerleştirme
        main_group = VGroup(group1, group2).arrange(DOWN, buff=1.6).move_to(DOWN * 0.5)

        self.play(Create(circle1), Create(line1), run_time=1.0)
        self.play(FadeIn(sector1), Write(label1), run_time=1.0)
        self.wait(2.0)

        self.play(Create(circle2), Create(line2_v), Create(line2_h), run_time=1.0)
        self.play(FadeIn(sector2), Write(label2), run_time=1.0)
        self.wait(1.67)

        # Kısım 4: 16 kelime = 5.33s
        self.play(FadeOut(main_group), FadeOut(q_text), run_time=0.5)
        exp_text = Text("Parça sayısı artarsa\ndilim küçülür!", font="DejaVu Sans", font_size=42, color=YELLOW).move_to(UP*1)
        self.play(Write(exp_text), run_time=1.0)
        self.wait(3.83)

        # Kısım 5: 11 kelime = 3.67s
        comp_text = MathTex(r"\frac{1}{2} > \frac{1}{4}", font_size=90, color=GREEN).move_to(DOWN*1)
        self.play(Write(comp_text), run_time=1.0)
        self.wait(2.67)

        self.play(FadeOut(exp_text), FadeOut(comp_text), run_time=0.5)

        # ÇIKIŞ (7 kelime = 2.33s)
        outro_text = Text("Maarif Matematik ile\nmantığını kavra,\ntakipte kal!", font="DejaVu Sans", font_size=45, color=ORANGE).move_to(ORIGIN)
        self.play(Write(outro_text), run_time=1.0)
        self.wait(1.33)