from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # B1: Intro
        title = Text("Doğal Sayılar ve Kesirler", color="#002B4D", font_size=48).shift(UP*2)
        nat_num = MathTex("4", color="#333333", font_size=72).shift(LEFT*2)
        frac_num = MathTex(r"\frac{17}{5}", color="#333333", font_size=72).shift(RIGHT*2)
        
        self.play(Write(title), run_time=2)
        self.wait(5)
        self.play(FadeIn(nat_num), FadeIn(frac_num), run_time=2)
        self.wait(8.9)
        self.play(FadeOut(title), FadeOut(nat_num), FadeOut(frac_num), run_time=2)
        self.wait(2)
        
        # B2: Method 1 Setup
        method1_text = Text("Yöntem 1: Bölme Evi", color="#007BFF", font_size=40).shift(UP*3)
        comp1 = MathTex(r"4 \quad ? \quad \frac{17}{5}", color="#333333", font_size=60).shift(UP*1.5)
        
        self.play(Write(method1_text), run_time=2)
        self.wait(5)
        self.play(Write(comp1), run_time=2)
        self.wait(6)
        
        # B3: Division House (Bölme Evi)
        dividend = MathTex("17", color="#333333", font_size=60).shift(LEFT*1)
        divisor = MathTex("5", color="#333333", font_size=60).shift(RIGHT*1)
        line_v = Line(UP*0.5, DOWN*0.5, color="#333333").shift(ORIGIN)
        line_h = Line(ORIGIN, RIGHT*2, color="#333333").shift(DOWN*0.5)
        
        self.play(Create(line_v), Create(line_h), run_time=2)
        self.wait(6)
        self.play(Write(dividend), Write(divisor), run_time=2)
        self.wait(8)
        
        quotient = MathTex("3", color="#333333", font_size=60).shift(DOWN*1 + RIGHT*1)
        self.play(Write(quotient), run_time=2)
        self.wait(5)
        
        product = MathTex("15", color="#333333", font_size=60).shift(DOWN*1 + LEFT*1)
        self.play(Write(product), run_time=2)
        self.wait(5)
        
        minus_sign = MathTex("-", color="#333333", font_size=60).next_to(product, LEFT, buff=0.2)
        line_sub = Line(LEFT*2, ORIGIN, color="#333333").shift(DOWN*1.5)
        self.play(Write(minus_sign), Create(line_sub), run_time=2)
        self.wait(2)
        
        remainder = MathTex("2", color="#333333", font_size=60).shift(DOWN*2 + LEFT*1)
        self.play(Write(remainder), run_time=2)
        self.wait(6)
        
        rect_q = SurroundingRectangle(quotient, color="#007BFF")
        self.play(Create(rect_q), run_time=2)
        self.wait(3)
        
        rect_r = SurroundingRectangle(remainder, color="#002B4D")
        self.play(Create(rect_r), run_time=2)
        self.wait(3)
        
        # B4: Method 1 Result
        mixed_frac = MathTex(r"\frac{17}{5} = 3 \frac{2}{5}", color="#002B4D", font_size=50).shift(RIGHT*4 + UP*0.5)
        self.play(Write(mixed_frac), run_time=2)
        self.wait(9)
        
        final_comp1 = MathTex(r"4 > 3 \frac{2}{5}", color="#007BFF", font_size=50).shift(RIGHT*4 + DOWN*0.5)
        self.play(Write(final_comp1), run_time=2)
        self.wait(4)
        
        final_comp1_res = MathTex(r"4 > \frac{17}{5}", color="#007BFF", font_size=50).shift(RIGHT*4 + DOWN*1.5)
        self.play(Write(final_comp1_res), run_time=2)
        self.wait(4)
        
        Group_all_method1 = VGroup(method1_text, comp1, dividend, divisor, line_v, line_h, quotient, product, minus_sign, line_sub, remainder, rect_q, rect_r, mixed_frac, final_comp1, final_comp1_res)
        self.play(FadeOut(Group_all_method1), run_time=2)
        self.wait(2)
        
        # B5: Method 2 Setup
        method2_text = Text("Yöntem 2: Genişletme", color="#007BFF", font_size=40).shift(UP*3)
        comp2 = MathTex(r"5 \quad ? \quad \frac{23}{4}", color="#333333", font_size=60).shift(UP*1.5)
        
        self.play(Write(method2_text), run_time=2)
        self.wait(5)
        self.play(Write(comp2), run_time=2)
        self.wait(6)
        
        # B6: Method 2 Expansion
        five_as_frac = MathTex(r"5 = \frac{5}{1}", color="#333333", font_size=60).shift(LEFT*2)
        self.play(Write(five_as_frac), run_time=2)
        self.wait(8)
        
        expand_text = MathTex(r"(\times 4)", color="#007BFF", font_size=40).next_to(five_as_frac, DOWN)
        self.play(Write(expand_text), run_time=2)
        self.wait(9)
        
        twenty_fourths = MathTex(r"5 = \frac{20}{4}", color="#002B4D", font_size=60).shift(LEFT*2)
        self.play(Transform(five_as_frac, twenty_fourths), run_time=2)
        self.wait(7)
        
        # B7: Method 2 Result
        final_comp2 = MathTex(r"\frac{23}{4} > \frac{20}{4}", color="#333333", font_size=60).shift(RIGHT*2)
        self.play(Write(final_comp2), run_time=2)
        self.wait(10)
        
        conclusion2 = MathTex(r"\frac{23}{4} > 5", color="#007BFF", font_size=60).shift(RIGHT*2 + DOWN*1.5)
        self.play(Write(conclusion2), run_time=2)
        self.wait(11)
        
        Group_all_method2 = VGroup(method2_text, comp2, five_as_frac, expand_text, final_comp2, conclusion2)
        self.play(FadeOut(Group_all_method2), run_time=2)
        self.wait(2)
        
        # B8: Conclusion & Outro
        summary_text1 = Text("1. Bölme Evi ile Tamları Bul", color="#002B4D", font_size=40).shift(UP*1)
        self.play(Write(summary_text1), run_time=2)
        self.wait(10)
        
        summary_text2 = Text("2. Genişletme ile Paydaları Eşitle", color="#007BFF", font_size=40).shift(DOWN*1)
        self.play(Write(summary_text2), run_time=2)
        self.wait(10)
        
        summary_text3 = Text("Maarif Modeli: Mantığı Gör!", color="#333333", font_size=48).shift(DOWN*3)
        self.play(Write(summary_text3), run_time=2)
        self.wait(15)
        
        Group_summary = VGroup(summary_text1, summary_text2, summary_text3)
        self.play(FadeOut(Group_summary), run_time=2)
        self.wait(5)
        
        outro_text = Text("Maarif Matematik", color="#002B4D", font_size=60)
        self.play(Write(outro_text), run_time=2)
        self.wait(1)
