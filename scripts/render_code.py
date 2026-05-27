from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # Intro
        title = Text("Kesir Dönüşümleri", color="#002B4D", font_size=48)
        subtitle = Text("Bileşik ve Tam Sayılı Kesirler", color="#333333", font_size=36).next_to(title, DOWN)
        intro_group = VGroup(title, subtitle)
        
        self.play(Write(intro_group), run_time=2)
        self.wait(18)
        self.play(FadeOut(intro_group))
        
        # 7/3 Visuals
        frac_7_3 = MathTex(r"\frac{7}{3}", color="#333333", font_size=64).to_edge(UP)
        self.play(Write(frac_7_3), run_time=1)
        
        c1 = VGroup(*[Sector(radius=1.2, angle=TAU/3, start_angle=i*TAU/3, color="#007BFF", fill_opacity=0.6, stroke_width=2, stroke_color="#333333") for i in range(3)]).move_to(LEFT*3)
        c2 = VGroup(*[Sector(radius=1.2, angle=TAU/3, start_angle=i*TAU/3, color="#007BFF", fill_opacity=0.6, stroke_width=2, stroke_color="#333333") for i in range(3)]).move_to(ORIGIN)
        c3 = Sector(radius=1.2, angle=TAU/3, start_angle=0, color="#007BFF", fill_opacity=0.6, stroke_width=2, stroke_color="#333333").move_to(RIGHT*3)
        
        self.play(FadeIn(c1, shift=UP), FadeIn(c2, shift=UP), FadeIn(c3, shift=UP), run_time=2)
        self.wait(20)
        
        mixed_7_3 = MathTex(r"= 2 \frac{1}{3}", color="#002B4D", font_size=64).next_to(frac_7_3, RIGHT)
        self.play(Write(mixed_7_3), run_time=3)
        self.wait(20)
        
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(frac_7_3), FadeOut(mixed_7_3))
        
        # Division House (Bölme Evi)
        div_text = Text("Bölme Evi Algoritması", color="#002B4D", font_size=40).to_edge(UP)
        self.play(Write(div_text), run_time=1)
        
        dividend = MathTex("7", color="#333333", font_size=64).move_to(LEFT*0.5 + UP*0.5)
        divisor = MathTex("3", color="#333333", font_size=64).move_to(RIGHT*0.5 + UP*0.5)
        v_line = Line(UP*1, DOWN*0.2, color="#333333").move_to(ORIGIN + UP*0.4)
        h_line = Line(LEFT*0.4, RIGHT*0.4, color="#333333").next_to(divisor, DOWN, buff=0.1)
        
        div_house = VGroup(dividend, divisor, v_line, h_line)
        self.play(Create(div_house), run_time=2)
        self.wait(20)
        
        quotient = MathTex("2", color="#007BFF", font_size=64).next_to(h_line, DOWN, buff=0.2)
        minus_six = MathTex("-6", color="#333333", font_size=64).next_to(dividend, DOWN, buff=0.2)
        h_line_sub = Line(LEFT*0.4, RIGHT*0.4, color="#333333").next_to(minus_six, DOWN, buff=0.1)
        remainder = MathTex("1", color="#002B4D", font_size=64).next_to(h_line_sub, DOWN, buff=0.2)
        
        self.play(Write(quotient), Write(minus_six), Create(h_line_sub), Write(remainder), run_time=3)
        self.wait(20)
        
        box_quotient = SurroundingRectangle(quotient, color="#007BFF", buff=0.1)
        box_remainder = SurroundingRectangle(remainder, color="#002B4D", buff=0.1)
        
        q_label = Text("Tam Kısım", color="#007BFF", font_size=24).next_to(box_quotient, RIGHT)
        r_label = Text("Pay", color="#002B4D", font_size=24).next_to(box_remainder, LEFT)
        
        self.play(Create(box_quotient), Write(q_label), Create(box_remainder), Write(r_label), run_time=2)
        self.wait(15)
        
        self.play(FadeOut(div_house), FadeOut(quotient), FadeOut(minus_six), FadeOut(h_line_sub), FadeOut(remainder), FadeOut(box_quotient), FadeOut(box_remainder), FadeOut(q_label), FadeOut(r_label), FadeOut(div_text))
        
        # 2 1/4 Visuals
        mixed_2_1_4 = MathTex(r"2 \frac{1}{4}", color="#333333", font_size=64).to_edge(UP)
        self.play(Write(mixed_2_1_4), run_time=1)
        
        q1 = VGroup(*[Sector(radius=1.2, angle=TAU/4, start_angle=i*TAU/4, color="#002B4D", fill_opacity=0.6, stroke_width=2, stroke_color="#333333") for i in range(4)]).move_to(LEFT*3)
        q2 = VGroup(*[Sector(radius=1.2, angle=TAU/4, start_angle=i*TAU/4, color="#002B4D", fill_opacity=0.6, stroke_width=2, stroke_color="#333333") for i in range(4)]).move_to(ORIGIN)
        q3 = Sector(radius=1.2, angle=TAU/4, start_angle=0, color="#002B4D", fill_opacity=0.6, stroke_width=2, stroke_color="#333333").move_to(RIGHT*3)
        
        self.play(FadeIn(q1, shift=UP), FadeIn(q2, shift=UP), FadeIn(q3, shift=UP), run_time=2)
        self.wait(20)
        
        math_calc = MathTex(r"\frac{(2 \times 4) + 1}{4} = \frac{9}{4}", color="#007BFF", font_size=56).next_to(mixed_2_1_4, DOWN)
        self.play(Write(math_calc), run_time=3)
        self.wait(20)
        
        # Break wholes into quarters visually
        self.play(q1.animate.arrange_in_grid(rows=2, cols=2, buff=0.1), q2.animate.arrange_in_grid(rows=2, cols=2, buff=0.1), run_time=3)
        self.wait(20)
        
        self.play(FadeOut(q1), FadeOut(q2), FadeOut(q3), FadeOut(mixed_2_1_4), FadeOut(math_calc))
        
        # Conclusion
        conc_text = Text("Mantığı Anla Ezberleme", color="#002B4D", font_size=48)
        self.play(Write(conc_text), run_time=2)
        self.wait(28)
        self.play(FadeOut(conc_text), run_time=1)
        self.wait(1)
