from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi
        self.camera.background_color = "#FFFFFF"
        
        # --- PARAGRAF 1 ---
        # Kelime sayısı: 33. Süre: 16.5 sn. Animasyon: 2 sn. Bekleme: 14.5 sn.
        title = Tex("Kesir Nedir?", color="#002B4D", font_size=72)
        self.play(Write(title), run_time=2)
        self.wait(14.5)
        
        # --- PARAGRAF 2 ---
        # Kelime sayısı: 38. Süre: 19.0 sn. Animasyon: 4 sn. Bekleme: 15.0 sn.
        self.play(FadeOut(title), run_time=1)
        
        line = Line(LEFT, RIGHT, color="#002B4D").scale(1.5)
        line_label = Tex("Kesir Çizgisi", color="#333333", font_size=36).next_to(line, RIGHT, buff=0.5)
        self.play(Create(line), Write(line_label), run_time=1)
        
        den_text = Tex("Payda", color="#333333", font_size=48).next_to(line, DOWN, buff=0.5)
        den_desc = Tex("(Bütünün bölündüğü parça sayısı)", color="#333333", font_size=24).next_to(den_text, DOWN)
        self.play(Write(den_text), Write(den_desc), run_time=1)
        
        num_text = Tex("Pay", color="#333333", font_size=48).next_to(line, UP, buff=0.5)
        num_desc = Tex("(Alınan parça sayısı)", color="#333333", font_size=24).next_to(num_text, UP)
        self.play(Write(num_text), Write(num_desc), run_time=1)
        
        self.wait(15.0)
        
        # --- PARAGRAF 3 ---
        # Kelime sayısı: 42. Süre: 21.0 sn. Animasyon: 7 sn. Bekleme: 14.0 sn.
        self.play(FadeOut(VGroup(line, line_label, den_text, den_desc, num_text, num_desc)), run_time=1)
        
        frac_line = Line(LEFT, RIGHT, color="#002B4D").scale(0.5)
        num_3 = Tex("3", color="#333333", font_size=60).next_to(frac_line, UP, buff=0.3)
        den_4 = Tex("4", color="#333333", font_size=60).next_to(frac_line, DOWN, buff=0.3)
        fraction = VGroup(num_3, frac_line, den_4).shift(LEFT * 3)
        
        self.play(Write(fraction), run_time=2)
        
        read_1 = Tex("3 bölü 4", color="#002B4D", font_size=40).next_to(fraction, RIGHT, buff=2).shift(UP*0.5)
        arrow_down = Arrow(start=UP, end=DOWN, color="#002B4D").next_to(read_1, LEFT).scale(0.5)
        
        read_2 = Tex("4'te 3", color="#002B4D", font_size=40).next_to(fraction, RIGHT, buff=2).shift(DOWN*0.5)
        arrow_up = Arrow(start=DOWN, end=UP, color="#002B4D").next_to(read_2, LEFT).scale(0.5)
        
        self.play(Create(arrow_down), Write(read_1), run_time=1)
        self.play(Create(arrow_up), Write(read_2), run_time=1)
        
        rects = VGroup(*[Rectangle(height=1, width=1, color="#333333") for _ in range(4)]).arrange(RIGHT, buff=0).shift(RIGHT * 2 + DOWN * 2)
        fills = VGroup(*[Rectangle(height=1, width=1, color="#002B4D", fill_opacity=0.8, stroke_width=0) for _ in range(3)]).arrange(RIGHT, buff=0).move_to(rects[0:3].get_center())
        
        self.play(Create(rects), run_time=1)
        self.play(FadeIn(fills), run_time=1)
        
        self.wait(14.0)
        
        # --- PARAGRAF 4 ---
        # Kelime sayısı: 14. Süre: 7.0 sn. Animasyon: 2 sn. Bekleme: 5.0 sn.
        self.play(FadeOut(VGroup(fraction, read_1, read_2, arrow_down, arrow_up, rects, fills)), run_time=1)
        
        outro_text = Tex("Maarif Matematik", color="#002B4D", font_size=60)
        self.play(Write(outro_text), run_time=1)
        
        self.wait(5.0)
