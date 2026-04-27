from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Part 1: Basit Kesir (Target: 45s)
        title1 = Text("Basit Kesir", font_size=48, color=BLUE).to_edge(UP)
        self.play(Write(title1), run_time=3)
        self.wait(5)
        
        pizza_circle = Circle(radius=1.5, color=WHITE).shift(LEFT*2)
        self.play(Create(pizza_circle), run_time=4)
        self.wait(5)
        
        slice1 = Sector(radius=1.5, angle=PI/2, start_angle=0, color=ORANGE, fill_opacity=0.8).shift(LEFT*2)
        slice2 = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color=ORANGE, fill_opacity=0.8).shift(LEFT*2)
        slice3 = Sector(radius=1.5, angle=PI/2, start_angle=PI, color=ORANGE, fill_opacity=0.8).shift(LEFT*2)
        slices_group = VGroup(slice1, slice2, slice3)
        
        self.play(FadeIn(slices_group), run_time=4)
        self.wait(5)
        
        fraction1 = MathTex(r"\frac{3}{4}", font_size=72).shift(RIGHT*2)
        self.play(Write(fraction1), run_time=3)
        self.wait(6)
        
        self.play(Indicate(fraction1[0][0], color=YELLOW, scale_factor=1.5), run_time=2)
        self.wait(4)
        
        group1 = VGroup(title1, pizza_circle, slices_group, fraction1)
        self.play(FadeOut(group1), run_time=4)
        
        # Part 2: Bileşik Kesir (Target: 45s)
        title2 = Text("Bileşik Kesir", font_size=48, color=RED).to_edge(UP)
        self.play(Write(title2), run_time=3)
        self.wait(5)
        
        pizza1 = Circle(radius=1.2, color=WHITE).shift(LEFT*3)
        pizza2 = Circle(radius=1.2, color=WHITE).shift(LEFT*0)
        self.play(Create(pizza1), Create(pizza2), run_time=4)
        self.wait(5)
        
        p1_s1 = Sector(radius=1.2, angle=PI/2, start_angle=0, color=ORANGE, fill_opacity=0.8).shift(LEFT*3)
        p1_s2 = Sector(radius=1.2, angle=PI/2, start_angle=PI/2, color=ORANGE, fill_opacity=0.8).shift(LEFT*3)
        p1_s3 = Sector(radius=1.2, angle=PI/2, start_angle=PI, color=ORANGE, fill_opacity=0.8).shift(LEFT*3)
        p1_s4 = Sector(radius=1.2, angle=PI/2, start_angle=3*PI/2, color=ORANGE, fill_opacity=0.8).shift(LEFT*3)
        p1_slices = VGroup(p1_s1, p1_s2, p1_s3, p1_s4)
        
        p2_s1 = Sector(radius=1.2, angle=PI/2, start_angle=0, color=ORANGE, fill_opacity=0.8).shift(LEFT*0)
        p2_slices = VGroup(p2_s1)
        
        self.play(FadeIn(p1_slices), run_time=3)
        self.play(FadeIn(p2_slices), run_time=3)
        self.wait(5)
        
        fraction2 = MathTex(r"\frac{5}{4}", font_size=72).shift(RIGHT*3)
        self.play(Write(fraction2), run_time=3)
        self.wait(5)
        
        self.play(Indicate(fraction2[0][0], color=YELLOW, scale_factor=1.5), run_time=2)
        self.wait(4)
        
        group2 = VGroup(title2, pizza1, pizza2, p1_slices, p2_slices, fraction2)
        self.play(FadeOut(group2), run_time=3)
        
        # Part 3: Tam Sayılı Kesir (Target: 40s)
        title3 = Text("Tam Sayılı Kesir", font_size=48, color=GREEN).to_edge(UP)
        self.play(Write(title3), run_time=3)
        self.wait(4)
        
        pizza1_copy = pizza1.copy()
        pizza2_copy = pizza2.copy()
        p1_slices_copy = p1_slices.copy()
        p2_slices_copy = p2_slices.copy()
        group3_visuals = VGroup(pizza1_copy, pizza2_copy, p1_slices_copy, p2_slices_copy)
        
        self.play(FadeIn(group3_visuals), run_time=4)
        self.wait(5)
        
        one_whole = MathTex("1 \text{ Tam}", font_size=48).shift(LEFT*3 + DOWN*2)
        self.play(Transform(p1_slices_copy, one_whole), Transform(pizza1_copy, one_whole), run_time=4)
        self.wait(5)
        
        mixed_fraction = MathTex(r"1 \frac{1}{4}", font_size=72).shift(RIGHT*3)
        self.play(Write(mixed_fraction), run_time=4)
        self.wait(6)
        
        group3 = VGroup(title3, group3_visuals, one_whole, mixed_fraction, p2_slices_copy, pizza2_copy)
        self.play(FadeOut(group3), run_time=5)
        
        # Part 4: Bölme Evi (Target: 55s)
        title4 = Text("Bileşik Kesri Tam Sayılı Kesre Çevirme", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(title4), run_time=3)
        self.wait(4)
        
        div_eq = MathTex(r"\frac{5}{4}", font_size=60).shift(LEFT*4 + UP*1)
        self.play(Write(div_eq), run_time=3)
        self.wait(4)
        
        dividend = MathTex("5", font_size=60).shift(LEFT*0.5 + UP*1)
        divisor = MathTex("4", font_size=60).shift(RIGHT*0.5 + UP*1)
        v_line = Line(dividend.get_right() + RIGHT*0.2 + UP*0.3, dividend.get_right() + RIGHT*0.2 + DOWN*1.5)
        h_line = Line(divisor.get_left() + DOWN*0.3, divisor.get_right() + DOWN*0.3)
        
        self.play(Create(v_line), Create(h_line), Write(dividend), Write(divisor), run_time=5)
        self.wait(4)
        
        quotient = MathTex("1", font_size=60).next_to(h_line, DOWN, buff=0.3)
        self.play(Write(quotient), run_time=3)
        self.wait(3)
        
        mult_result = MathTex("4", font_size=60).next_to(dividend, DOWN, buff=0.5)
        sub_line = Line(mult_result.get_left() + DOWN*0.2 + LEFT*0.2, mult_result.get_right() + DOWN*0.2 + RIGHT*0.2)
        minus = MathTex("-", font_size=60).next_to(mult_result, LEFT, buff=0.2)
        
        self.play(Write(mult_result), Write(minus), Create(sub_line), run_time=4)
        self.wait(3)
        
        remainder = MathTex("1", font_size=60).next_to(sub_line, DOWN, buff=0.3)
        self.play(Write(remainder), run_time=3)
        self.wait(3)
        
        box_q = SurroundingRectangle(quotient, color=GREEN, buff=0.1)
        box_r = SurroundingRectangle(remainder, color=YELLOW, buff=0.1)
        self.play(Create(box_q), Create(box_r), run_time=4)
        self.wait(4)
        
        final_mixed = MathTex(r"1 \frac{1}{4}", font_size=72).shift(RIGHT*4 + UP*0)
        self.play(Write(final_mixed), run_time=3)
        self.wait(2)
        
        group4 = VGroup(title4, div_eq, dividend, divisor, v_line, h_line, quotient, mult_result, sub_line, minus, remainder, box_q, box_r, final_mixed)
        
        # Part 5: Tam -> Bileşik (Target: 49s)
        self.play(FadeOut(group4), run_time=3)
        
        title5 = Text("Tam Sayılı Kesri Bileşik Kesre Çevirme", font_size=36, color=PURPLE).to_edge(UP)
        self.play(Write(title5), run_time=3)
        self.wait(4)
        
        start_mixed = MathTex(r"2 \frac{3}{4}", font_size=72).shift(LEFT*3)
        self.play(Write(start_mixed), run_time=3)
        self.wait(4)
        
        calc_text1 = Text("2 tam pizza x 4 dilim = 8 dilim", font_size=32).shift(RIGHT*2 + UP*1)
        self.play(Write(calc_text1), run_time=4)
        self.wait(4)
        
        calc_text2 = Text("8 dilim + 3 dilim = 11 dilim", font_size=32).shift(RIGHT*2 + DOWN*0.5)
        self.play(Write(calc_text2), run_time=4)
        self.wait(4)
        
        final_improper = MathTex(r"\frac{11}{4}", font_size=72).shift(RIGHT*2 + DOWN*2)
        self.play(Write(final_improper), run_time=3)
        self.wait(4)
        
        arrow1 = CurvedArrow(start_mixed[0][2].get_bottom(), start_mixed[0][0].get_bottom(), angle=PI/2, color=YELLOW)
        arrow2 = CurvedArrow(start_mixed[0][0].get_top(), start_mixed[0][1].get_top(), angle=PI/2, color=GREEN)
        self.play(Create(arrow1), Create(arrow2), run_time=4)
        self.wait(4)
        
        group5 = VGroup(title5, start_mixed, calc_text1, calc_text2, final_improper, arrow1, arrow2)
        self.play(FadeOut(group5), run_time=1)
