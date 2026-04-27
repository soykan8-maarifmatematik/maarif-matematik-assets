from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Scene 1: Intro (20.5s)
        title = Text("Kesirler Dünyası", font_size=48, color=BLUE)
        self.play(Write(title), run_time=2)
        self.wait(17.5)
        self.play(FadeOut(title), run_time=1)

        # Scene 2: Basit Kesir (33.5s)
        pizza1 = VGroup()
        for i in range(8):
            slice_color = ORANGE if i < 3 else DARK_GRAY
            pizza_slice = Sector(radius=2, angle=TAU/8, start_angle=i*TAU/8, color=slice_color, fill_opacity=0.8, stroke_width=2, stroke_color=WHITE)
            pizza1.add(pizza_slice)
        
        pizza1.shift(LEFT*2)
        frac_basit = MathTex(r"\frac{3}{8}", font_size=64).shift(RIGHT*2)
        label_basit = Text("Basit Kesir", font_size=36, color=ORANGE).next_to(frac_basit, UP)

        self.play(Create(pizza1), run_time=3)
        self.play(Write(frac_basit), Write(label_basit), run_time=2)
        self.wait(27.5)
        self.play(FadeOut(pizza1, frac_basit, label_basit), run_time=1)

        # Scene 3: Bileşik Kesir (39s)
        pizza2_1 = VGroup()
        pizza2_2 = VGroup()
        for i in range(8):
            pizza2_1.add(Sector(radius=1.5, angle=TAU/8, start_angle=i*TAU/8, color=ORANGE, fill_opacity=0.8, stroke_width=2, stroke_color=WHITE))
            slice_color = ORANGE if i < 3 else DARK_GRAY
            pizza2_2.add(Sector(radius=1.5, angle=TAU/8, start_angle=i*TAU/8, color=slice_color, fill_opacity=0.8, stroke_width=2, stroke_color=WHITE))
        
        pizza2_1.shift(LEFT*4)
        pizza2_2.shift(LEFT*0.5)
        
        frac_bilesik = MathTex(r"\frac{11}{8}", font_size=64).shift(RIGHT*3.5)
        label_bilesik = Text("Bileşik Kesir", font_size=36, color=RED).next_to(frac_bilesik, UP)

        self.play(FadeIn(pizza2_1, pizza2_2), run_time=2)
        self.play(Write(frac_bilesik), Write(label_bilesik), run_time=2)
        self.wait(34)
        self.play(FadeOut(label_bilesik), run_time=1)

        # Scene 4: Tam Sayılı Kesir (33.5s)
        frac_tam = MathTex(r"1 \frac{3}{8}", font_size=64).shift(RIGHT*3.5)
        label_tam = Text("Tam Sayılı Kesir", font_size=36, color=GREEN).next_to(frac_tam, UP)
        
        self.play(Transform(frac_bilesik, frac_tam), Write(label_tam), run_time=3)
        self.wait(29.5)
        self.play(FadeOut(pizza2_1, pizza2_2, frac_bilesik, label_tam), run_time=1)

        # Scene 5: Bileşik -> Tam Sayılı (Bölme Evi) (70s)
        eq_start = MathTex(r"\frac{13}{4} = ?").shift(UP*3)
        self.play(Write(eq_start), run_time=2)

        dividend = MathTex("13").shift(LEFT*1 + UP*1)
        v_line = Line(UP*1.5, DOWN*0.5).shift(LEFT*0.3)
        divisor = MathTex("4").shift(RIGHT*0.5 + UP*1)
        h_line = Line(LEFT*0.3, RIGHT*1.3).shift(UP*0.5)
        
        self.play(Write(dividend), Write(divisor), Create(v_line), Create(h_line), run_time=4)
        self.wait(10)

        quotient = MathTex("3").shift(RIGHT*0.5 + DOWN*0.1)
        product = MathTex("12").shift(LEFT*1 + DOWN*0.1)
        minus = MathTex("-").next_to(product, LEFT, buff=0.1)
        sub_line = Line(LEFT*1.8, LEFT*0.2).shift(DOWN*0.5)
        remainder = MathTex("1").shift(LEFT*1 + DOWN*1)

        self.play(Write(quotient), run_time=2)
        self.play(Write(product), run_time=2)
        self.play(Create(sub_line), Write(minus), run_time=2)
        self.play(Write(remainder), run_time=2)
        self.wait(10)

        box_q = SurroundingRectangle(quotient, color=GREEN, buff=0.1)
        label_q = Text("Tam Kısım", font_size=24, color=GREEN).next_to(box_q, RIGHT)
        self.play(Create(box_q), Write(label_q), run_time=2)
        self.wait(5)

        box_r = SurroundingRectangle(remainder, color=YELLOW, buff=0.1)
        label_r = Text("Yeni Pay", font_size=24, color=YELLOW).next_to(box_r, RIGHT)
        self.play(Create(box_r), Write(label_r), run_time=2)
        self.wait(5)

        eq_end = MathTex(r"\frac{13}{4} = 3 \frac{1}{4}", font_size=48, color=YELLOW).shift(DOWN*2.5)
        self.play(Write(eq_end), run_time=3)
        self.wait(18)
        self.play(FadeOut(eq_start, dividend, divisor, v_line, h_line, quotient, product, minus, sub_line, remainder, box_q, label_q, box_r, label_r, eq_end), run_time=1)

        # Scene 6: Tam Sayılı -> Bileşik (38s)
        tam_kesir = MathTex(r"2 \frac{3}{5}", font_size=64)
        self.play(Write(tam_kesir), run_time=2)
        self.wait(5)

        arrow_mult = CurvedArrow(tam_kesir[0][0].get_bottom(), tam_kesir[0][2].get_bottom(), angle=TAU/4, color=RED)
        op_mult = MathTex(r"\times", color=RED, font_size=36).next_to(arrow_mult, DOWN, buff=0.1)
        
        arrow_add = CurvedArrow(tam_kesir[0][2].get_top(), tam_kesir[0][1].get_top(), angle=TAU/4, color=BLUE)
        op_add = MathTex(r"+", color=BLUE, font_size=36).next_to(arrow_add, UP, buff=0.1)

        self.play(Create(arrow_mult), Write(op_mult), run_time=2)
        self.wait(5)
        self.play(Create(arrow_add), Write(op_add), run_time=2)
        self.wait(5)

        bilesik_sonuc = MathTex(r"= \frac{13}{5}", font_size=64).next_to(tam_kesir, RIGHT)
        self.play(Write(bilesik_sonuc), run_time=2)
        self.wait(14)
        self.play(FadeOut(tam_kesir, arrow_mult, op_mult, arrow_add, op_add, bilesik_sonuc), run_time=1)

        # Scene 7: Outro (4s)
        outro_text = Text("Maarif Matematik", font_size=48, color=BLUE)
        self.play(Write(outro_text), run_time=2)
        self.wait(1)
        self.play(FadeOut(outro_text), run_time=1)
