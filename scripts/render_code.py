from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Renk Paleti
        self.camera.background_color = "#FFFFFF"
        dark_gray = "#333333"
        navy_blue = "#002B4D"
        maarif_red = "#D32F2F"

        # BÖLÜM 1: Birim Kesir Nedir? (52 kelime / 1.8 = 28.8 saniye)
        title = Text("Birim Kesirler", color=navy_blue, font_size=48).to_edge(UP)
        self.play(Write(title), run_time=2)
        
        circle = Circle(radius=2, color=dark_gray, stroke_width=4)
        self.play(Create(circle), run_time=2)
        
        lines = VGroup(
            Line(circle.get_top(), circle.get_bottom(), color=dark_gray),
            Line(circle.get_left(), circle.get_right(), color=dark_gray)
        )
        self.play(Create(lines), run_time=2)
        
        slice1 = Sector(radius=2, angle=PI/2, start_angle=0, color=maarif_red, fill_opacity=0.7)
        self.play(FadeIn(slice1), run_time=2)
        
        frac_1_4 = MathTex(r"\frac{1}{4}", color=navy_blue, font_size=64).next_to(circle, RIGHT, buff=1)
        self.play(Write(frac_1_4), run_time=2)
        
        # Animasyonlar 10 saniye sürdü. Kalan süre: 28.8 - 10 = 18.8 -> 19 saniye bekleme.
        self.wait(19)

        # BÖLÜM 2: Sayı Doğrusunda Gösterme (49 kelime / 1.8 = 27.2 saniye)
        self.play(FadeOut(circle), FadeOut(lines), FadeOut(slice1), FadeOut(frac_1_4), run_time=1)
        
        nl = NumberLine(x_range=[0, 1, 0.25], length=8, color=dark_gray, include_numbers=False)
        nl.add_labels({0: MathTex("0", color=navy_blue), 1: MathTex("1", color=navy_blue)})
        self.play(Create(nl), run_time=2)
        
        ticks = VGroup(*[Line(UP*0.2, DOWN*0.2, color=dark_gray).move_to(nl.n2p(i*0.25)) for i in range(1,4)])
        self.play(Create(ticks), run_time=2)
        
        dot = Dot(nl.n2p(0.25), color=maarif_red, radius=0.15)
        label_1_4 = MathTex(r"\frac{1}{4}", color=maarif_red).next_to(dot, UP)
        self.play(FadeIn(dot), Write(label_1_4), run_time=2)
        
        # Animasyonlar 7 saniye sürdü. Kalan süre: 27.2 - 7 = 20.2 -> 20 saniye bekleme.
        self.wait(20)

        # BÖLÜM 3: Karşılaştırma (54 kelime / 1.8 = 30 saniye)
        self.play(FadeOut(nl), FadeOut(ticks), FadeOut(dot), FadeOut(label_1_4), run_time=1)
        
        circle_half = Circle(radius=1.5, color=dark_gray).shift(LEFT*3)
        slice_half = Sector(radius=1.5, angle=PI, start_angle=0, color=maarif_red, fill_opacity=0.7).shift(LEFT*3)
        frac_half = MathTex(r"\frac{1}{2}", color=navy_blue, font_size=48).next_to(circle_half, DOWN)
        
        circle_ten = Circle(radius=1.5, color=dark_gray).shift(RIGHT*3)
        slice_ten = Sector(radius=1.5, angle=TAU/10, start_angle=0, color=maarif_red, fill_opacity=0.7).shift(RIGHT*3)
        frac_ten = MathTex(r"\frac{1}{10}", color=navy_blue, font_size=48).next_to(circle_ten, DOWN)
        
        self.play(Create(circle_half), FadeIn(slice_half), Write(frac_half), run_time=2)
        self.play(Create(circle_ten), FadeIn(slice_ten), Write(frac_ten), run_time=2)
        
        gt_sign = MathTex(">", color=dark_gray, font_size=64).move_to(ORIGIN)
        self.play(Write(gt_sign), run_time=2)
        
        # Animasyonlar 7 saniye sürdü. Kalan süre: 30 - 7 = 23 saniye bekleme.
        self.wait(23)

        # BÖLÜM 4: Çıkış (7 kelime / 1.8 = 3.8 saniye)
        self.play(
            FadeOut(circle_half), FadeOut(slice_half), FadeOut(frac_half),
            FadeOut(circle_ten), FadeOut(slice_ten), FadeOut(frac_ten),
            FadeOut(gt_sign), FadeOut(title),
            run_time=1
        )
        
        outro_text = Text("Maarif Matematik", color=navy_blue, font_size=48)
        self.play(Write(outro_text), run_time=1)
        
        # Animasyonlar 2 saniye sürdü. Kalan süre: 3.8 - 2 = 1.8 -> 2 saniye bekleme.
        self.wait(2)
