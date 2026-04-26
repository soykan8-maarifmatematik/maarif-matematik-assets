from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Block 1
        title = Tex(r'Kesir Çeşitleri').to_edge(UP)
        self.play(Write(title), run_time=2)

        basit_tex = Tex(r'Basit').shift(LEFT*4 + UP*1)
        bilesik_tex = Tex(r'Bileşik').shift(UP*1)
        tam_tex = Tex(r'Tam Sayılı').shift(RIGHT*4 + UP*1)

        f1 = MathTex(r'\frac{3}{5}').next_to(basit_tex, DOWN, buff=0.5)
        f2 = MathTex(r'\frac{7}{4}').next_to(bilesik_tex, DOWN, buff=0.5)
        f3 = MathTex(r'1\frac{3}{4}').next_to(tam_tex, DOWN, buff=0.5)

        sec = Sector(radius=0.8, angle=TAU * 3/5, color=BLUE, fill_opacity=0.7).next_to(f1, DOWN, buff=0.5)
        sec_bg = Circle(radius=0.8, color=WHITE).move_to(sec.get_arc_center())

        self.play(Write(basit_tex), Write(bilesik_tex), Write(tam_tex), run_time=3)
        self.play(Write(f1), Write(f2), Write(f3), run_time=3)
        self.play(Create(sec_bg), Create(sec), run_time=2)
        self.wait(11)

        # Block 2
        self.play(FadeOut(Group(title, basit_tex, bilesik_tex, tam_tex, f1, f2, f3, sec, sec_bg)), run_time=1)

        title2 = Tex(r'Bileşik $\rightarrow$ Tam Sayılı').to_edge(UP)
        self.play(Write(title2), run_time=2)

        eq1 = MathTex(r'\frac{7}{4}').shift(LEFT*4)
        self.play(Write(eq1), run_time=1)

        dividend = MathTex('7')
        vline = Line(dividend.get_top() + RIGHT*0.3, dividend.get_bottom() + RIGHT*0.3 + DOWN*1.5)
        divisor = MathTex('4').next_to(vline, RIGHT, buff=0.3).align_to(dividend, UP)
        hline = Line(vline.get_start() + DOWN*0.6, vline.get_start() + DOWN*0.6 + RIGHT*1.2)
        quotient = MathTex('1').next_to(hline, DOWN, buff=0.3).align_to(divisor, LEFT)

        minus = MathTex('-').next_to(dividend, DOWN, buff=0.5).shift(LEFT*0.6)
        sub_val = MathTex('4').next_to(dividend, DOWN, buff=0.5)
        sub_line = Line(minus.get_left() + DOWN*0.2, sub_val.get_right() + DOWN*0.2)
        remainder = MathTex('3').next_to(sub_line, DOWN, buff=0.2).align_to(sub_val, RIGHT)

        div_group = VGroup(dividend, vline, divisor, hline, quotient, minus, sub_val, sub_line, remainder).center()

        self.play(Write(dividend), Create(vline), Write(divisor), Create(hline), run_time=3)
        self.play(Write(quotient), run_time=1)
        self.play(Write(minus), Write(sub_val), Create(sub_line), run_time=2)
        self.play(Write(remainder), run_time=1)

        box_q = SurroundingRectangle(quotient, color=YELLOW)
        box_r = SurroundingRectangle(remainder, color=GREEN)
        box_d = SurroundingRectangle(divisor, color=RED)

        self.play(Create(box_q), Create(box_r), Create(box_d), run_time=2)

        result1 = MathTex(r'= 1\frac{3}{4}').next_to(div_group, RIGHT, buff=1.5)
        self.play(Write(result1), run_time=2)
        self.wait(7)

        # Block 3
        self.play(FadeOut(Group(title2, eq1, div_group, box_q, box_r, box_d, result1)), run_time=1)

        title3 = Tex(r'Tam Sayılı $\rightarrow$ Bileşik').to_edge(UP)
        self.play(Write(title3), run_time=2)

        eq2 = MathTex(r'2\frac{1}{3}').scale(1.5).shift(LEFT*3)
        self.play(Write(eq2), run_time=2)

        step1 = MathTex(r'= \frac{3 \times 2 + 1}{3}').next_to(eq2, RIGHT, buff=1)
        self.play(Write(step1), run_time=3)

        step2 = MathTex(r'= \frac{7}{3}').next_to(step1, RIGHT, buff=1)
        self.play(Write(step2), run_time=2)

        box_final = SurroundingRectangle(step2, color=YELLOW)
        self.play(Create(box_final), run_time=2)

        self.wait(10)

        # Block 4
        self.play(FadeOut(Group(title3, eq2, step1, step2, box_final)), run_time=1)

        outro_text = Tex(r'Harika! Bol bol pratik yapın!').scale(1.5)
        self.play(Write(outro_text), run_time=2)
        self.wait(6)
