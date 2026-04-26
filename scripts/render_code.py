from manim import *

class Kesirler(Scene):
    def construct(self):
        title = Tex('Maarif Matematik').scale(1.5)
        self.play(Write(title), run_time=1)
        self.wait(0.35)
        self.play(FadeOut(title), run_time=1)

        topic = Tex('Kesir Çeşitleri ve Dönüşümler').scale(1.2)
        self.play(FadeIn(topic), run_time=1)
        self.wait(3.88)
        self.play(FadeOut(topic), run_time=1)

        basit_title = Tex('Basit Kesir').to_edge(UP)
        basit_frac = MathTex(r'\frac{3}{4}').scale(2).shift(LEFT*3)
        self.play(Write(basit_title), run_time=1)
        self.wait(1.94)
        self.play(Write(basit_frac), run_time=1)
        self.wait(3.70)

        circle_group = VGroup()
        colors = [BLUE, BLUE, BLUE, DARK_GRAY]
        for i in range(4):
            sector = Sector(radius=1.5, angle=PI/2, start_angle=i*PI/2, color=colors[i], fill_opacity=0.8, stroke_width=2, stroke_color=WHITE)
            circle_group.add(sector)
        circle_group.shift(RIGHT*2)
        self.play(FadeIn(circle_group), run_time=1)
        self.wait(6.83)
        self.play(FadeOut(basit_title, basit_frac, circle_group), run_time=1)

        bilesik_title = Tex('Bileşik Kesir').to_edge(UP)
        bilesik_frac = MathTex(r'\frac{7}{3}').scale(2)
        self.play(Write(bilesik_title), run_time=1)
        self.wait(1.35)
        self.play(Write(bilesik_frac), run_time=1)
        self.wait(9.17)
        self.play(FadeOut(bilesik_title, bilesik_frac), run_time=1)

        tam_title = Tex('Tam Sayılı Kesir').to_edge(UP)
        tam_frac = MathTex(r'2 \frac{1}{3}').scale(2)
        self.play(Write(tam_title), run_time=1)
        self.wait(1.94)
        self.play(Write(tam_frac), run_time=1)
        self.wait(7.99)
        self.play(FadeOut(tam_title, tam_frac), run_time=1)

        conv1_title = Tex('Bileşik $\rightarrow$ Tam Sayılı').to_edge(UP)
        self.play(Write(conv1_title), run_time=1)
        self.wait(1.94)

        dividend = MathTex('7').scale(1.5).move_to(LEFT*1 + UP*0.5)
        divisor = MathTex('3').scale(1.5).move_to(RIGHT*0.5 + UP*0.5)
        v_line = Line(UP*1, DOWN*0.2).move_to(LEFT*0.2 + UP*0.5)
        h_line = Line(LEFT*0.1, RIGHT*1.1).move_to(RIGHT*0.5 + DOWN*0.1)
        self.play(Write(dividend), Write(divisor), run_time=1)
        self.wait(6.05)

        self.play(Create(v_line), Create(h_line), run_time=1)
        self.wait(1.94)

        quotient = MathTex('2').scale(1.5).move_to(RIGHT*0.5 + DOWN*0.8)
        self.play(Write(quotient), run_time=1)
        self.wait(2.52)

        product = MathTex('6').scale(1.5).move_to(LEFT*1 + DOWN*0.5)
        sub_line = Line(LEFT*1.5, LEFT*0.5).move_to(LEFT*1 + DOWN*1)
        minus = MathTex('-').scale(1.5).move_to(LEFT*1.7 + DOWN*0.5)
        remainder = MathTex('1').scale(1.5).move_to(LEFT*1 + DOWN*1.5)
        self.play(Write(product), run_time=1)
        self.play(Create(sub_line), Write(minus), run_time=1)
        self.play(Write(remainder), run_time=1)
        self.wait(2.39)

        box_q = SurroundingRectangle(quotient, color=YELLOW)
        box_r = SurroundingRectangle(remainder, color=GREEN)
        box_d = SurroundingRectangle(divisor, color=BLUE)
        self.play(Create(box_q), run_time=1)
        self.wait(1.94)
        self.play(Create(box_r), run_time=1)
        self.wait(1.35)
        self.play(Create(box_d), run_time=1)
        self.wait(0.76)

        final_frac1 = MathTex(r'\frac{7}{3} = 2 \frac{1}{3}').scale(1.5).move_to(RIGHT*3.5)
        self.play(Write(final_frac1), run_time=1)
        self.wait(6.05)
        self.play(FadeOut(conv1_title, dividend, divisor, v_line, h_line, quotient, product, sub_line, minus, remainder, box_q, box_r, box_d, final_frac1), run_time=1)

        conv2_title = Tex('Tam Sayılı $\rightarrow$ Bileşik').to_edge(UP)
        self.play(Write(conv2_title), run_time=1)
        self.wait(2.70)

        start_frac = MathTex(r'2 \frac{1}{3}').scale(2.5)
        self.play(Write(start_frac), run_time=1)
        self.wait(1.0)

        arrow_mul = CurvedArrow(start_frac[0][2].get_bottom() + DOWN*0.2, start_frac[0][0].get_bottom() + DOWN*0.2, angle=PI/2, color=YELLOW)
        mul_sign = MathTex(r'\times').scale(1).next_to(arrow_mul, DOWN, buff=0.1).set_color(YELLOW)
        self.play(Create(arrow_mul), Write(mul_sign), run_time=1)
        self.wait(3.82)

        arrow_add = CurvedArrow(start_frac[0][0].get_top() + UP*0.2, start_frac[0][1].get_top() + UP*0.2, angle=PI/2, color=GREEN)
        add_sign = MathTex('+').scale(1).next_to(arrow_add, UP, buff=0.1).set_color(GREEN)
        self.play(Create(arrow_add), Write(add_sign), run_time=1)
        self.wait(3.29)
        self.wait(2.94)

        eq_sign = MathTex('=').scale(2.5).next_to(start_frac, RIGHT, buff=0.5)
        end_frac = MathTex(r'\frac{7}{3}').scale(2.5).next_to(eq_sign, RIGHT, buff=0.5)
        self.play(Write(eq_sign), Write(end_frac), run_time=1)
        self.wait(3.88)
        self.wait(1.76)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1)
        self.wait(4.02)

        outro = Tex('Maarif Matematik').scale(1.5)
        self.play(Write(outro), run_time=1)
        self.wait(2.11)
        self.play(FadeOut(outro), run_time=1)
