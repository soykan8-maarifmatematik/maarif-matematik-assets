from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # BÖLÜM 1: Basit Kesir (Süre: 24.1s)
        title1 = Text("Basit Kesir: 3/4", color=BLACK, font_size=40).to_edge(UP)
        
        circle1 = Circle(radius=1.5, color=BLACK).move_to(DOWN * 0.5)
        sector1_1 = Sector(radius=1.5, angle=PI/2, start_angle=0, color=BLUE, fill_opacity=0.7).move_to(DOWN * 0.5)
        sector1_2 = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color=BLUE, fill_opacity=0.7).move_to(DOWN * 0.5)
        sector1_3 = Sector(radius=1.5, angle=PI/2, start_angle=PI, color=BLUE, fill_opacity=0.7).move_to(DOWN * 0.5)
        
        lines1 = VGroup(
            Line(DOWN * 0.5, DOWN * 0.5 + RIGHT * 1.5, color=BLACK),
            Line(DOWN * 0.5, DOWN * 0.5 + UP * 1.5, color=BLACK),
            Line(DOWN * 0.5, DOWN * 0.5 + LEFT * 1.5, color=BLACK),
            Line(DOWN * 0.5, DOWN * 0.5 + DOWN * 1.5, color=BLACK)
        )

        self.play(Write(title1), run_time=2.0)
        self.play(Create(circle1), Create(lines1), run_time=2.0)
        self.play(Create(sector1_1), Create(sector1_2), Create(sector1_3), run_time=3.0)
        self.wait(17.1)

        # BÖLÜM 2: Bileşik Kesir (Süre: 27.6s)
        self.play(FadeOut(*self.mobjects), run_time=1.0)
        
        title2 = Text("Bileşik Kesir: 5/4", color=BLACK, font_size=40).to_edge(UP)
        
        circle2_1 = Circle(radius=1.5, color=BLACK).move_to(LEFT * 2 + DOWN * 0.5)
        circle2_2 = Circle(radius=1.5, color=BLACK).move_to(RIGHT * 2 + DOWN * 0.5)
        
        lines2_1 = VGroup(
            Line(circle2_1.get_center(), circle2_1.get_center() + RIGHT * 1.5, color=BLACK),
            Line(circle2_1.get_center(), circle2_1.get_center() + UP * 1.5, color=BLACK),
            Line(circle2_1.get_center(), circle2_1.get_center() + LEFT * 1.5, color=BLACK),
            Line(circle2_1.get_center(), circle2_1.get_center() + DOWN * 1.5, color=BLACK)
        )
        
        lines2_2 = VGroup(
            Line(circle2_2.get_center(), circle2_2.get_center() + RIGHT * 1.5, color=BLACK),
            Line(circle2_2.get_center(), circle2_2.get_center() + UP * 1.5, color=BLACK),
            Line(circle2_2.get_center(), circle2_2.get_center() + LEFT * 1.5, color=BLACK),
            Line(circle2_2.get_center(), circle2_2.get_center() + DOWN * 1.5, color=BLACK)
        )

        full_sector = Sector(radius=1.5, angle=TAU, start_angle=0, color=RED, fill_opacity=0.7).move_to(circle2_1.get_center())
        extra_sector = Sector(radius=1.5, angle=PI/2, start_angle=0, color=RED, fill_opacity=0.7).move_to(circle2_2.get_center())

        self.play(Write(title2), run_time=2.0)
        self.play(Create(circle2_1), Create(lines2_1), Create(circle2_2), Create(lines2_2), run_time=2.0)
        self.play(Create(full_sector), run_time=2.0)
        self.play(Create(extra_sector), run_time=2.0)
        self.wait(18.6)

        # BÖLÜM 3: Tam Sayılı Kesir ve Bölme Evi (Süre: 27.1s)
        self.play(FadeOut(*self.mobjects), run_time=1.0)
        
        title3 = Text("Tam Sayılı Kesire Çevirme", color=BLACK, font_size=40).to_edge(UP)
        
        dividend = MathTex("5", color=BLACK, font_size=60).move_to(LEFT * 0.8 + UP * 0.5)
        divisor = MathTex("4", color=BLACK, font_size=60).move_to(RIGHT * 0.8 + UP * 0.5)
        
        vert_line = Line(UP * 1.2, DOWN * 0.2, color=BLACK).move_to(ORIGIN + UP * 0.5)
        horiz_line = Line(RIGHT * 0.2, RIGHT * 1.4, color=BLACK).next_to(divisor, DOWN, buff=0.1)
        
        quotient = MathTex("1", color=BLACK, font_size=60).next_to(horiz_line, DOWN, buff=0.2)
        
        sub_val = MathTex("4", color=BLACK, font_size=60).next_to(dividend, DOWN, buff=0.5)
        minus_sign = MathTex("-", color=BLACK, font_size=60).next_to(sub_val, LEFT, buff=0.1)
        sub_line = Line(LEFT * 1.4, LEFT * 0.2, color=BLACK).next_to(sub_val, DOWN, buff=0.1)
        
        remainder = MathTex("1", color=BLACK, font_size=60).next_to(sub_line, DOWN, buff=0.2)
        
        eq_text = MathTex(r"\frac{5}{4} = 1 \frac{1}{4}", color=BLACK, font_size=60).move_to(DOWN * 2)

        self.play(Write(title3), run_time=2.0)
        self.play(Write(dividend), Write(divisor), run_time=2.0)
        self.play(Create(vert_line), Create(horiz_line), run_time=2.0)
        self.play(Write(quotient), run_time=2.0)
        self.play(Write(sub_val), Write(minus_sign), run_time=2.0)
        self.play(Create(sub_line), Write(remainder), run_time=2.0)
        self.play(Write(eq_text), run_time=3.0)
        self.wait(11.1)

        # BÖLÜM 4: Kapanış (Süre: 10.0s)
        self.play(FadeOut(*self.mobjects), run_time=1.0)
        outro_text = Text("Maarif Matematik", color=BLACK, font_size=50)
        self.play(Write(outro_text), run_time=2.0)
        self.wait(6.0)
        self.wait(1.0) # Hoşça kalın dedikten sonra tam 1 saniye bekleme
