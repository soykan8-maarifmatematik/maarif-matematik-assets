from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        Text.set_default(color="#333333")
        MathTex.set_default(color="#333333")
        
        # Chunk 1: Intro
        title_basit = Text("Basit Kesir", font_size=36).shift(LEFT*4)
        title_bilesik = Text("Bileşik Kesir", font_size=36)
        title_tam = Text("Tam Sayılı Kesir", font_size=36).shift(RIGHT*4)
        
        self.play(Write(title_basit), Write(title_bilesik), Write(title_tam))
        self.wait(11.5)
        
        # Chunk 2 & 3: Basit Kesir
        self.play(FadeOut(title_bilesik), FadeOut(title_tam), title_basit.animate.shift(UP*3 + RIGHT*4))
        self.wait(6.2)
        
        circle = Circle(radius=1.5, color="#333333")
        l1 = Line(circle.point_at_angle(PI/2), circle.point_at_angle(3*PI/2), color="#333333")
        l2 = Line(circle.point_at_angle(0), circle.point_at_angle(PI), color="#333333")
        lines = VGroup(l1, l2)
        
        slice1 = Sector(outer_radius=1.5, angle=PI/2, start_angle=0, color="#FF9999", fill_opacity=0.8)
        
        frac_1_4 = MathTex("\\frac{1}{4}", font_size=72).shift(RIGHT*3)
        
        self.play(Create(circle), Create(lines))
        self.play(FadeIn(slice1))
        self.play(Write(frac_1_4))
        self.wait(11.3)
        
        # Chunk 4 & 5: Bileşik Kesir
        self.play(FadeOut(Group(title_basit, circle, lines, slice1, frac_1_4)))
        
        title_bilesik_center = Text("Bileşik Kesir", font_size=48)
        self.play(Write(title_bilesik_center))
        self.play(title_bilesik_center.animate.shift(UP*3))
        self.wait(8.8)
        
        frac_7_3 = MathTex("\\frac{7}{3}", font_size=72).shift(UP*1.5)
        self.play(Write(frac_7_3))
        
        c1 = Circle(radius=1, color="#333333").shift(LEFT*2.5 + DOWN*1)
        c2 = Circle(radius=1, color="#333333").shift(DOWN*1)
        c3 = Circle(radius=1, color="#333333").shift(RIGHT*2.5 + DOWN*1)
        
        def get_thirds(c):
            return VGroup(
                Line(c.get_center(), c.point_at_angle(PI/2), color="#333333"),
                Line(c.get_center(), c.point_at_angle(PI/2 + 2*PI/3), color="#333333"),
                Line(c.get_center(), c.point_at_angle(PI/2 + 4*PI/3), color="#333333")
            )
        
        t1 = get_thirds(c1)
        t2 = get_thirds(c2)
        t3 = get_thirds(c3)
        
        s1 = Sector(arc_center=c1.get_center(), outer_radius=1, angle=2*PI, color="#99CCFF", fill_opacity=0.8)
        s2 = Sector(arc_center=c2.get_center(), outer_radius=1, angle=2*PI, color="#99CCFF", fill_opacity=0.8)
        s3 = Sector(arc_center=c3.get_center(), outer_radius=1, angle=2*PI/3, start_angle=PI/2, color="#99CCFF", fill_opacity=0.8)
        
        self.play(Create(VGroup(c1, c2, c3, t1, t2, t3)))
        self.play(FadeIn(VGroup(s1, s2, s3)))
        self.wait(6.2)
        
        # Chunk 6 & 7: Division Setup
        self.play(FadeOut(Group(title_bilesik_center, c1, c2, c3, t1, t2, t3, s1, s2, s3, frac_7_3)))
        self.wait(11.9)
        
        dividend = MathTex("7", font_size=60).shift(LEFT*1 + UP*1)
        divisor = MathTex("3", font_size=60).shift(RIGHT*0.5 + UP*1)
        v_line = Line(UP*1.5, DOWN*1, color="#333333").shift(LEFT*0.25)
        h_line = Line(LEFT*0.25, RIGHT*1.25, color="#333333").shift(UP*0.5)
        
        self.play(Write(dividend), Write(divisor), Create(v_line), Create(h_line))
        self.wait(5.4)
        
        quotient = MathTex("2", font_size=60).shift(RIGHT*0.5 + DOWN*0.2)
        self.play(Write(quotient))
        self.wait(1)
        
        # Chunk 8: Subtraction
        self.wait(2)
        subtrahend = MathTex("6", font_size=60).shift(LEFT*1 + UP*0.2)
        minus = MathTex("-", font_size=60).next_to(subtrahend, LEFT, buff=0.2)
        sub_line = Line(LEFT*1.8, LEFT*0.2, color="#333333").shift(DOWN*0.3)
        
        self.play(Write(subtrahend), Write(minus), Create(sub_line))
        self.wait(3.8)
        
        remainder = MathTex("1", font_size=60).shift(LEFT*1 + DOWN*0.8)
        self.play(Write(remainder))
        
        # Chunk 9: Arrows and Mixed Fraction
        mixed_tam = MathTex("2", font_size=72).shift(RIGHT*3)
        mixed_line = Line(RIGHT*3.5, RIGHT*4.3, color="#333333").shift(UP*0.1)
        mixed_pay = MathTex("1", font_size=60).shift(RIGHT*3.9 + UP*0.6)
        mixed_payda = MathTex("3", font_size=60).shift(RIGHT*3.9 + DOWN*0.4)
        
        arrow_tam = CurvedArrow(quotient.get_bottom(), mixed_tam.get_bottom() + DOWN*0.5, angle=PI/4, color="#FF9900")
        self.play(Write(mixed_tam), GrowArrow(arrow_tam))
        self.wait(2)
        
        arrow_pay = CurvedArrow(remainder.get_bottom(), mixed_pay.get_top() + UP*0.5, angle=-PI/2, color="#00CC66")
        self.play(Write(mixed_line), Write(mixed_pay), GrowArrow(arrow_pay))
        self.wait(2)
        
        arrow_payda = CurvedArrow(divisor.get_top(), mixed_payda.get_bottom() + DOWN*0.5, angle=PI/3, color="#CC00CC")
        self.play(Write(mixed_payda), GrowArrow(arrow_payda))
        self.wait(4.1)
        
        # Chunk 10: Mixed to Improper
        self.play(FadeOut(Group(dividend, divisor, v_line, h_line, quotient, subtrahend, minus, sub_line, remainder, arrow_tam, arrow_pay, arrow_payda)))
        
        mixed_group = VGroup(mixed_tam, mixed_line, mixed_pay, mixed_payda)
        self.play(mixed_group.animate.move_to(LEFT*2))
        self.wait(8.4)
        
        # Chunk 11: Multiplication and Addition Arcs
        arc_mul = CurvedArrow(mixed_payda.get_bottom(), mixed_tam.get_bottom(), angle=PI/2, color="#FF3333")
        mul_sign = MathTex("\\times", font_size=36, color="#FF3333").next_to(arc_mul, DOWN, buff=0.1)
        
        self.play(Create(arc_mul), Write(mul_sign))
        self.wait(2)
        
        arc_add = CurvedArrow(mixed_tam.get_top(), mixed_pay.get_top(), angle=PI/2, color="#33CC33")
        add_sign = MathTex("+", font_size=36, color="#33CC33").next_to(arc_add, UP, buff=0.1)
        
        self.play(Create(arc_add), Write(add_sign))
        self.wait(2)
        
        eq_sign = MathTex("=", font_size=60).next_to(mixed_group, RIGHT, buff=0.5)
        final_frac = MathTex("\\frac{7}{3}", font_size=72).next_to(eq_sign, RIGHT, buff=0.5)
        
        self.play(Write(eq_sign), Write(final_frac))
        self.wait(3.2)
        
        # Chunk 12: Outro
        self.wait(11.8)
