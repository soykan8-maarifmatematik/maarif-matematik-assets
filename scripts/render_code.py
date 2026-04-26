from manim import *

class FractionsLesson(Scene):
    def construct(self):
        # Intro
        title_main = Tex("Kesir Çeşitleri ve Dönüşümler", font_size=48, color=YELLOW)
        self.play(Write(title_main), run_time=1)
        self.wait(3)
        self.play(FadeOut(title_main), run_time=1)

        # Basit Kesir
        basit_text = Tex("Basit Kesir", font_size=40, color=BLUE).shift(UP*2)
        basit_frac = MathTex(r"\frac{3}{5}", font_size=72)
        basit_desc = Tex("Pay $<$ Payda", font_size=32).next_to(basit_frac, DOWN, buff=0.5)
        self.play(Write(basit_text), Write(basit_frac), run_time=2)
        self.play(Write(basit_desc), run_time=1)
        self.wait(5)
        self.play(FadeOut(basit_text, basit_frac, basit_desc), run_time=1)

        # Bileşik Kesir
        bilesik_text = Tex("Bileşik Kesir", font_size=40, color=RED).shift(UP*2)
        bilesik_frac = MathTex(r"\frac{7}{4}", font_size=72)
        bilesik_desc = Tex("Pay $\ge$ Payda", font_size=32).next_to(bilesik_frac, DOWN, buff=0.5)
        self.play(Write(bilesik_text), Write(bilesik_frac), run_time=2)
        self.play(Write(bilesik_desc), run_time=1)
        self.wait(5)
        self.play(FadeOut(bilesik_text, bilesik_frac, bilesik_desc), run_time=1)

        # Tam Sayılı Kesir
        tam_text = Tex("Tam Sayılı Kesir", font_size=40, color=GREEN).shift(UP*2)
        tam_frac = MathTex(r"2 \frac{1}{3}", font_size=72)
        tam_desc = Tex("Tam Sayı + Basit Kesir", font_size=32).next_to(tam_frac, DOWN, buff=0.5)
        self.play(Write(tam_text), Write(tam_frac), run_time=2)
        self.play(Write(tam_desc), run_time=1)
        self.wait(5)
        self.play(FadeOut(tam_text, tam_frac, tam_desc), run_time=1)

        # Bileşik -> Tam Sayılı
        conv1_title = MathTex(r"Bileşik \\rightarrow Tam Sayılı", font_size=40, color=YELLOW).shift(UP*3)
        self.play(Write(conv1_title), run_time=1.5)
        self.wait(2.5)

        # Division House
        dividend = MathTex("7", font_size=48).shift(LEFT*1 + UP*0.5)
        vline = Line(UP*1, DOWN*0.5).next_to(dividend, RIGHT, buff=0.2)
        divisor = MathTex("4", font_size=48).next_to(vline, RIGHT, buff=0.2).align_to(dividend, UP)
        hline = Line(divisor.get_bottom() + LEFT*0.3, divisor.get_bottom() + RIGHT*0.3).shift(DOWN*0.1)
        
        self.play(Write(dividend), Write(vline), Write(divisor), Write(hline), run_time=2)
        self.wait(2.5)

        quotient = MathTex("1", font_size=48).next_to(hline, DOWN, buff=0.2)
        self.play(Write(quotient), run_time=1)
        self.wait(2)

        minus = MathTex("-", font_size=48).next_to(dividend, DOWN, buff=0.2).shift(LEFT*0.5)
        sub_val = MathTex("4", font_size=48).next_to(dividend, DOWN, buff=0.2)
        sub_line = Line(minus.get_left() + DOWN*0.1, sub_val.get_right() + DOWN*0.1).shift(DOWN*0.1)
        self.play(Write(minus), Write(sub_val), Write(sub_line), run_time=1.5)
        self.wait(2)

        remainder = MathTex("3", font_size=48).next_to(sub_line, DOWN, buff=0.2).align_to(sub_val, RIGHT)
        self.play(Write(remainder), run_time=1)
        self.wait(2)

        box_quotient = SurroundingRectangle(quotient, color=GREEN, buff=0.1)
        box_remainder = SurroundingRectangle(remainder, color=YELLOW, buff=0.1)
        box_divisor = SurroundingRectangle(divisor, color=BLUE, buff=0.1)
        self.play(Create(box_quotient), Create(box_remainder), Create(box_divisor), run_time=2)
        self.wait(2.5)

        result1 = MathTex(r"= 1 \frac{3}{4}", font_size=60).next_to(vline, RIGHT, buff=2)
        self.play(Write(result1), run_time=2)
        self.wait(4.5)

        self.play(FadeOut(conv1_title, dividend, vline, divisor, hline, quotient, minus, sub_val, sub_line, remainder, box_quotient, box_remainder, box_divisor, result1), run_time=1)

        # Tam Sayılı -> Bileşik
        conv2_title = MathTex(r"Tam Sayılı \\rightarrow Bileşik", font_size=40, color=YELLOW).shift(UP*3)
        self.play(Write(conv2_title), run_time=1.5)
        self.wait(2.5)

        tam_frac2 = MathTex(r"2 \frac{1}{3}", font_size=72).shift(LEFT*2)
        self.play(Write(tam_frac2), run_time=1.5)
        self.wait(2.5)

        mul_text = Tex(r"$2 \times 3 = 6$", font_size=40, color=BLUE).shift(RIGHT*2 + UP*1)
        self.play(Write(mul_text), run_time=1.5)
        self.wait(2.5)

        add_text = Tex(r"$6 + 1 = 7$", font_size=40, color=GREEN).next_to(mul_text, DOWN, buff=0.5)
        self.play(Write(add_text), run_time=1.5)
        self.wait(2.5)

        result2 = MathTex(r"= \frac{7}{3}", font_size=72).next_to(tam_frac2, RIGHT, buff=1)
        self.play(Write(result2), run_time=2)
        self.wait(4.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1)
