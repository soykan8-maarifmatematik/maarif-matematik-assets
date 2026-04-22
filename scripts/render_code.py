from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi
        self.camera.background_color = "#FFFFFF"

        # --- PARAGRAF 1 ---
        # Kelime sayısı: 37. Süre: 37 / 2.0 = 18.5 saniye.
        # Animasyon süresi: 9 saniye. Bekleme süresi: 9.5 saniye.
        title = Text("Kesirler", color="#002B4D", font_size=72)
        self.play(Write(title), run_time=2)
        self.wait(2)
        self.play(title.animate.to_edge(UP), run_time=1)
        
        circle = Circle(radius=1.5, color="#333333", stroke_width=4)
        self.play(Create(circle), run_time=1)
        
        lines = VGroup(
            Line(circle.get_top(), circle.get_bottom(), color="#333333"),
            Line(circle.get_left(), circle.get_right(), color="#333333")
        )
        self.play(Create(lines), run_time=2)
        
        colored_part = Sector(radius=1.5, angle=PI/2, start_angle=0, color="#002B4D", fill_opacity=0.8)
        self.play(FadeIn(colored_part), run_time=1)
        
        self.wait(9.5)

        # --- PARAGRAF 2 ---
        # Kelime sayısı: 36. Süre: 36 / 2.0 = 18.0 saniye.
        # Animasyon süresi: 6 saniye. Bekleme süresi: 12.0 saniye.
        self.play(FadeOut(title), FadeOut(circle), FadeOut(lines), FadeOut(colored_part), run_time=1)
        
        line = Line(LEFT, RIGHT, color="#333333", stroke_width=6).scale(1.5)
        self.play(Create(line), run_time=1)
        
        payda_text = Text("Payda", color="#002B4D", font_size=48).next_to(line, DOWN, buff=0.5)
        payda_desc = Text("(Bütünün kaç eşit parçaya bölündüğü)", color="#333333", font_size=24).next_to(payda_text, DOWN)
        self.play(Write(payda_text), run_time=1)
        self.play(FadeIn(payda_desc), run_time=1)
        
        pay_text = Text("Pay", color="#002B4D", font_size=48).next_to(line, UP, buff=0.5)
        pay_desc = Text("(Kaç parçanın alındığı)", color="#333333", font_size=24).next_to(pay_text, UP)
        self.play(Write(pay_text), run_time=1)
        self.play(FadeIn(pay_desc), run_time=1)
        
        self.wait(12.0)

        # --- PARAGRAF 3 ---
        # Kelime sayısı: 49. Süre: 49 / 2.0 = 24.5 saniye.
        # Animasyon süresi: 7 saniye. Bekleme süresi: 17.5 saniye.
        self.play(
            FadeOut(line), FadeOut(payda_text), FadeOut(payda_desc),
            FadeOut(pay_text), FadeOut(pay_desc), run_time=1
        )
        
        frac_line = Line(LEFT, RIGHT, color="#333333", stroke_width=6).scale(0.5)
        num_3 = Text("3", color="#002B4D", font_size=64).next_to(frac_line, UP, buff=0.3)
        den_4 = Text("4", color="#002B4D", font_size=64).next_to(frac_line, DOWN, buff=0.3)
        
        frac_group = VGroup(num_3, frac_line, den_4).shift(LEFT * 3)
        self.play(Write(frac_group), run_time=2)
        
        arrow1 = Arrow(start=num_3.get_right() + RIGHT*0.5, end=den_4.get_right() + RIGHT*0.5 + DOWN*0.5, color="#333333", path_arc=-1.5)
        read1 = Text("Üç bölü dört", color="#333333", font_size=36).next_to(arrow1, RIGHT)
        self.play(Create(arrow1), Write(read1), run_time=2)
        
        arrow2 = Arrow(start=den_4.get_left() + LEFT*0.5, end=num_3.get_left() + LEFT*0.5 + UP*0.5, color="#002B4D", path_arc=-1.5)
        read2 = Text("Dörtte üç", color="#002B4D", font_size=36).next_to(arrow2, LEFT)
        self.play(Create(arrow2), Write(read2), run_time=2)
        
        self.wait(17.5)

        # --- PARAGRAF 4 ---
        # Kelime sayısı: 28. Süre: 28 / 2.0 = 14.0 saniye.
        # Animasyon süresi: 3 saniye. Bekleme süresi: 11.0 saniye.
        self.play(
            FadeOut(frac_group), FadeOut(arrow1), FadeOut(read1),
            FadeOut(arrow2), FadeOut(read2), run_time=1
        )
        
        outro_text = Text("Maarif Matematik", color="#002B4D", font_size=60)
        self.play(Write(outro_text), run_time=2)
        
        self.wait(11.0)
