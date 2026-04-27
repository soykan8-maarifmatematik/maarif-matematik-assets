from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Intro
        title = Text("Kesirler: Basit, Bileşik ve Tam Sayılı").scale(0.9).set_color(YELLOW)
        self.play(Write(title), run_time=2)
        self.wait(11)
        self.play(FadeOut(title), run_time=1)

        # Basit Kesir
        pizza1_sectors = VGroup()
        colors = [RED, RED, RED, DARK_GRAY]
        for i in range(4):
            sector = Sector(radius=1.5, angle=TAU/4, start_angle=i*TAU/4, color=colors[i], fill_opacity=0.8, stroke_width=2, stroke_color=WHITE)
            pizza1_sectors.add(sector)
        pizza1_sectors.move_to(LEFT*3)
        
        basit_text = Text("Basit Kesir").scale(0.8).move_to(RIGHT*2 + UP*1).set_color(BLUE)
        basit_frac = MathTex(r"\frac{3}{4}").scale(2).next_to(basit_text, DOWN, buff=0.5)

        self.play(Create(pizza1_sectors), run_time=2)
        self.wait(10)
        self.play(Write(basit_text), run_time=2)
        self.wait(10)
        self.play(Write(basit_frac), run_time=2)
        self.wait(15)
        self.play(FadeOut(pizza1_sectors, basit_text, basit_frac), run_time=1)

        # Bileşik Kesir
        self.wait(5)
        pizza2_sectors = VGroup()
        for i in range(4):
            sector = Sector(radius=1.5, angle=TAU/4, start_angle=i*TAU/4, color=RED, fill_opacity=0.8, stroke_width=2, stroke_color=WHITE)
            pizza2_sectors.add(sector)
        pizza2_sectors.move_to(LEFT*3.5)

        pizza3_sectors = VGroup()
        colors3 = [RED, RED, RED, DARK_GRAY]
        for i in range(4):
            sector = Sector(radius=1.5, angle=TAU/4, start_angle=i*TAU/4, color=colors3[i], fill_opacity=0.8, stroke_width=2, stroke_color=WHITE)
            pizza3_sectors.add(sector)
        pizza3_sectors.move_to(ORIGIN)

        bilesik_text = Text("Bileşik Kesir").scale(0.8).move_to(RIGHT*3.5 + UP*1).set_color(ORANGE)
        bilesik_frac = MathTex(r"\frac{7}{4}").scale(2).next_to(bilesik_text, DOWN, buff=0.5)

        self.play(Create(pizza2_sectors), Create(pizza3_sectors), run_time=3)
        self.wait(12)
        self.play(Write(bilesik_text), run_time=2)
        self.wait(12)
        self.play(Write(bilesik_frac), run_time=2)
        self.wait(15)
        self.play(FadeOut(bilesik_text, bilesik_frac), run_time=1)

        # Tam Sayılı Kesir
        self.wait(4)
        tam_text = Text("Tam Sayılı Kesir").scale(0.8).move_to(RIGHT*3.5 + UP*1).set_color(GREEN)
        tam_frac = MathTex(r"1 \frac{3}{4}").scale(2).next_to(tam_text, DOWN, buff=0.5)
        
        self.play(Write(tam_text), run_time=2)
        self.wait(10)
        self.play(Write(tam_frac), run_time=2)
        self.wait(15)
        self.play(FadeOut(pizza2_sectors, pizza3_sectors, tam_text, tam_frac), run_time=1)

        # Bölme Evi (Bileşik -> Tam Sayılı)
        self.wait(5)
        dividend = MathTex("7").scale(1.5).move_to(LEFT * 1 + UP * 1)
        divisor = MathTex("4").scale(1.5).move_to(RIGHT * 1 + UP * 1)
        vert_line = Line(UP * 1.5, DOWN * 0.5).move_to(UP * 0.5)
        horiz_line = Line(RIGHT * 0.2, RIGHT * 1.8).move_to(RIGHT * 1 + UP * 0.5)
        quotient = MathTex("1").scale(1.5).move_to(RIGHT * 1 + ORIGIN)
        sub_val = MathTex("4").scale(1.5).move_to(LEFT * 1 + ORIGIN)
        minus = MathTex("-").scale(1.5).next_to(sub_val, LEFT, buff=0.2)
        sub_line = Line(LEFT * 1.8, LEFT * 0.2).move_to(LEFT * 1 + DOWN * 0.5)
        remainder = MathTex("3").scale(1.5).move_to(LEFT * 1 + DOWN * 1)

        self.play(Write(dividend), Write(divisor), run_time=2)
        self.play(Create(vert_line), Create(horiz_line), run_time=2)
        self.wait(10)
        self.play(Write(quotient), run_time=1)
        self.wait(5)
        self.play(Write(sub_val), Write(minus), Create(sub_line), run_time=2)
        self.wait(5)
        self.play(Write(remainder), run_time=1)
        self.wait(10)

        box_q = SurroundingRectangle(quotient, color=YELLOW, buff=0.1)
        self.play(Create(box_q), run_time=1)
        self.wait(5)
        
        box_r = SurroundingRectangle(remainder, color=GREEN, buff=0.1)
        self.play(Create(box_r), run_time=1)
        self.wait(5)

        box_d = SurroundingRectangle(divisor, color=BLUE, buff=0.1)
        self.play(Create(box_d), run_time=1)
        self.wait(10)

        conversion_eq = MathTex(r"\frac{7}{4} = 1 \frac{3}{4}").scale(1.5).move_to(DOWN * 2.5)
        self.play(Write(conversion_eq), run_time=2)
        self.wait(10)
        self.play(FadeOut(dividend, divisor, vert_line, horiz_line, quotient, sub_val, minus, sub_line, remainder, box_q, box_r, box_d, conversion_eq), run_time=1)

        # Tam Sayılı -> Bileşik
        self.wait(4)
        tam_part = MathTex("1").scale(2)
        frac_line = Line(LEFT*0.3, RIGHT*0.3)
        num_part = MathTex("3").scale(1.5).next_to(frac_line, UP, buff=0.1)
        den_part = MathTex("4").scale(1.5).next_to(frac_line, DOWN, buff=0.1)
        frac_group = VGroup(num_part, frac_line, den_part).next_to(tam_part, RIGHT, buff=0.2)
        tam_to_bil_frac = VGroup(tam_part, frac_group).move_to(LEFT*1.5)

        self.play(Write(tam_to_bil_frac), run_time=2)
        self.wait(10)

        arrow_mul = CurvedArrow(den_part.get_bottom() + DOWN*0.2, tam_part.get_bottom() + DOWN*0.2, angle=PI/2, color=YELLOW)
        mul_sign = MathTex(r"\times").scale(0.8).next_to(arrow_mul, DOWN, buff=0.1).set_color(YELLOW)
        self.play(Create(arrow_mul), Write(mul_sign), run_time=2)
        self.wait(8)

        arrow_add = CurvedArrow(tam_part.get_top() + UP*0.2, num_part.get_top() + UP*0.2, angle=-PI/2, color=GREEN)
        add_sign = MathTex("+").scale(0.8).next_to(arrow_add, UP, buff=0.1).set_color(GREEN)
        self.play(Create(arrow_add), Write(add_sign), run_time=2)
        self.wait(8)

        final_bilesik = MathTex(r"= \frac{7}{4}").scale(2).next_to(tam_to_bil_frac, RIGHT, buff=1.5)
        self.play(Write(final_bilesik), run_time=2)
        self.wait(10)
        self.play(FadeOut(tam_to_bil_frac, arrow_mul, mul_sign, arrow_add, add_sign, final_bilesik), run_time=1)

        # Outro
        self.wait(4)
        outro_text = Text("Bir sonraki derste görüşmek üzere, hoşça kalın.").scale(0.7).set_color(WHITE)
        self.play(Write(outro_text), run_time=2)
        self.wait(3.5)
        self.play(FadeOut(outro_text), run_time=1)
