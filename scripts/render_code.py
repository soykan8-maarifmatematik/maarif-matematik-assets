from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi
        self.camera.background_color = "#FFFFFF"
        
        # 1. Paragraf (31 kelime / 1.8 = ~17.2 sn. Animasyon: 2 sn, Bekleme: 15.2 sn)
        title = Text("Maarif Matematik", color="#002B4D", font_size=48, weight=BOLD)
        subtitle = Text("Kesirlerin Mantığı", color="#D32F2F", font_size=36).next_to(title, DOWN)
        self.play(Write(title), Write(subtitle), run_time=2)
        self.wait(15.2)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.5)

        # 2. Paragraf (37 kelime / 1.8 = ~20.5 sn. Animasyon: 2 sn, Bekleme: 18.5 sn)
        circle = Circle(radius=2, color="#333333", stroke_width=4)
        line_v = Line(circle.get_top(), circle.get_bottom(), color="#333333", stroke_width=4)
        line_h = Line(circle.get_left(), circle.get_right(), color="#333333", stroke_width=4)
        pizza_group = VGroup(circle, line_v, line_h).shift(LEFT*3)
        
        self.play(Create(circle), run_time=1)
        self.play(Create(line_v), Create(line_h), run_time=1)
        self.wait(18.5)

        # 3. Paragraf (29 kelime / 1.8 = ~16.1 sn. Animasyon: 3 sn, Bekleme: 13.1 sn)
        frac_line = Line(LEFT, RIGHT, color="#333333", stroke_width=4).shift(RIGHT*3)
        denom = MathTex("4", color="#002B4D", font_size=72).next_to(frac_line, DOWN, buff=0.3)
        denom_label = Text("Payda (Bütün)", color="#002B4D", font_size=24).next_to(denom, RIGHT, buff=0.5)
        
        self.play(Create(frac_line), run_time=1)
        self.play(Write(denom), run_time=1)
        self.play(Write(denom_label), run_time=1)
        self.wait(13.1)

        # 4. Paragraf (29 kelime / 1.8 = ~16.1 sn. Animasyon: 4 sn, Bekleme: 12.1 sn)
        slice1 = Sector(radius=2, angle=PI/2, start_angle=0, color="#D32F2F", fill_opacity=0.7).shift(LEFT*3)
        slice2 = Sector(radius=2, angle=PI/2, start_angle=PI/2, color="#D32F2F", fill_opacity=0.7).shift(LEFT*3)
        slice3 = Sector(radius=2, angle=PI/2, start_angle=PI, color="#D32F2F", fill_opacity=0.7).shift(LEFT*3)
        
        num = MathTex("3", color="#D32F2F", font_size=72).next_to(frac_line, UP, buff=0.3)
        num_label = Text("Pay (Alınan)", color="#D32F2F", font_size=24).next_to(num, RIGHT, buff=0.5)

        self.play(FadeIn(slice1), FadeIn(slice2), FadeIn(slice3), run_time=2)
        self.play(Write(num), run_time=1)
        self.play(Write(num_label), run_time=1)
        self.wait(12.1)

        # 5. Paragraf (34 kelime / 1.8 = ~18.8 sn. Animasyon: 3 sn, Bekleme: 15.8 sn)
        read1 = Text("Okunuş 1: Üç bölü dört", color="#333333", font_size=30).to_edge(DOWN).shift(UP*1)
        read2 = Text("Okunuş 2: Dörtte üç", color="#333333", font_size=30).next_to(read1, DOWN, buff=0.2)

        self.play(Write(read1), run_time=1.5)
        self.play(Write(read2), run_time=1.5)
        self.wait(15.8)

        # 6. Paragraf (19 kelime / 1.8 = ~10.5 sn. Animasyon: 2.5 sn, Bekleme: 8 sn)
        self.play(
            FadeOut(pizza_group), FadeOut(slice1), FadeOut(slice2), FadeOut(slice3),
            FadeOut(frac_line), FadeOut(denom), FadeOut(denom_label),
            FadeOut(num), FadeOut(num_label), FadeOut(read1), FadeOut(read2),
            run_time=1
        )
        outro = Text("Maarif Matematik", color="#002B4D", font_size=48, weight=BOLD)
        self.play(Write(outro), run_time=1.5)
        self.wait(8)
