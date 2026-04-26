from manim import *

class FractionConversion(Scene):
    def construct(self):
        # Paragraf 1 (25.3s)
        title = Tex(r"Kesir Çeşitleri ve Dönüşümler").scale(1.2)
        self.play(Write(title), run_time=2)
        self.wait(3)
        self.play(FadeOut(title), run_time=1)
        
        f1 = MathTex(r"\frac{1}{2}").shift(LEFT*3)
        f2 = MathTex(r"\frac{7}{4}")
        f3 = MathTex(r"2 \frac{3}{5}").shift(RIGHT*3)
        
        self.play(FadeIn(f1), FadeIn(f2), FadeIn(f3), run_time=3)
        self.wait(15.3)
        self.play(FadeOut(f1, f2, f3), run_time=1)
        
        # Paragraf 2 (29.4s)
        basit_title = Tex(r"Basit Kesir").shift(UP*2 + LEFT*3)
        basit_ex = MathTex(r"\frac{3}{5}, \frac{1}{2}").next_to(basit_title, DOWN)
        self.play(Write(basit_title), FadeIn(basit_ex), run_time=2)
        self.wait(10)
        
        bilesik_title = Tex(r"Bileşik Kesir").shift(UP*2 + RIGHT*3)
        bilesik_ex = MathTex(r"\frac{7}{4}, \frac{5}{5}").next_to(bilesik_title, DOWN)
        self.play(Write(bilesik_title), FadeIn(bilesik_ex), run_time=2)
        self.wait(10)
        
        self.play(FadeOut(basit_title, basit_ex, bilesik_title, bilesik_ex), run_time=1)
        self.wait(4.4)
        
        # Paragraf 3 (34.1s)
        conv_title = Tex(r"Bileşik $\rightarrow$ Tam Sayılı").to_edge(UP)
        self.play(Write(conv_title), run_time=2)
        self.wait(5)
        
        frac = MathTex(r"\frac{13}{5}").scale(1.5)
        self.play(FadeIn(frac), run_time=2)
        self.wait(5)
        
        self.play(frac.animate.shift(LEFT * 4), run_time=1)
        self.wait(4)
        
        dividend = MathTex("13").move_to(LEFT * 0.5 + UP * 0.5)
        v_line = Line(UP * 1.5, DOWN * 1.5).next_to(dividend, RIGHT, buff=0.3)
        h_line = Line(v_line.get_start() + DOWN * 0.8, v_line.get_start() + DOWN * 0.8 + RIGHT * 1.5)
        divisor = MathTex("5").next_to(h_line, UP, buff=0.2).align_to(h_line, LEFT).shift(RIGHT*0.3)
        
        self.play(Create(v_line), Create(h_line), run_time=1)
        self.play(Write(dividend), Write(divisor), run_time=2)
        self.wait(12.1)
        
        # Paragraf 4 (28.2s)
        quotient = MathTex("2").next_to(h_line, DOWN, buff=0.3).align_to(divisor, LEFT).shift(RIGHT*0.1)
        self.play(Write(quotient), run_time=1)
        self.wait(2)
        
        product = MathTex("10").next_to(dividend, DOWN, buff=0.3).align_to(dividend, RIGHT)
        self.play(Write(product), run_time=1)
        self.wait(2)
        
        minus = MathTex("-").next_to(product, LEFT, buff=0.1)
        minus_line = Line(product.get_bottom() + LEFT * 0.5 + DOWN * 0.1, product.get_bottom() + RIGHT * 0.5 + DOWN * 0.1)
        remainder = MathTex("3").next_to(minus_line, DOWN, buff=0.2).align_to(product, RIGHT)
        
        self.play(Write(minus), Create(minus_line), Write(remainder), run_time=2)
        self.wait(3)
        
        box_q = SurroundingRectangle(quotient, color=YELLOW)
        self.play(Create(box_q), run_time=1)
        self.wait(2)
        
        box_r = SurroundingRectangle(remainder, color=RED)
        self.play(Create(box_r), run_time=1)
        self.wait(2)
        
        result = MathTex(r"= 2 \frac{3}{5}").scale(1.5).next_to(frac, RIGHT, buff=0.5)
        self.play(Write(result), run_time=2)
        self.wait(7.2)
        
        self.play(FadeOut(Group(*self.mobjects)), run_time=1)
        self.wait(1)