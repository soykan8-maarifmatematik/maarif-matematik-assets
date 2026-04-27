from manim import *

class MaarifScene(Scene):
    def construct(self):
        # INTRO (15s)
        title = Text("Kesir Çeşitleri ve Dönüşümler", font_size=40, color=BLUE)
        self.play(Write(title), run_time=2)
        self.wait(13)

        # BASİT KESİR (35s)
        self.play(FadeOut(title), run_time=1)
        basit_text = Text("Basit Kesir", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(basit_text), run_time=2)
        self.wait(5)

        pizza1 = VGroup()
        colors = [ORANGE, ORANGE, ORANGE, DARK_GRAY]
        for i in range(4):
            slice_pizza = Sector(radius=1.5, angle=PI/2, start_angle=i*PI/2, color=colors[i], fill_opacity=0.8, stroke_width=2, stroke_color=WHITE)
            pizza1.add(slice_pizza)
        pizza1.move_to(LEFT * 2)
        
        self.play(Create(pizza1), run_time=3)
        self.wait(10)

        frac_3_4 = MathTex(r"\frac{3}{4}", font_size=60).next_to(pizza1, RIGHT, buff=1)
        self.play(Write(frac_3_4), run_time=2)
        self.wait(12)

        # BİLEŞİK KESİR (45s)
        self.play(FadeOut(VGroup(basit_text, pizza1, frac_3_4)), run_time=1)
        bilesik_text = Text("Bileşik Kesir", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(bilesik_text), run_time=2)
        self.wait(10)

        pizza2_1 = VGroup(*[Sector(radius=1.2, angle=PI/2, start_angle=i*PI/2, color=ORANGE, fill_opacity=0.8, stroke_width=2, stroke_color=WHITE) for i in range(4)])
        pizza2_2 = VGroup(*[Sector(radius=1.2, angle=PI/2, start_angle=i*PI/2, color=ORANGE if i==0 else DARK_GRAY, fill_opacity=0.8, stroke_width=2, stroke_color=WHITE) for i in range(4)])
        pizza2_1.move_to(LEFT * 3)
        pizza2_2.move_to(ORIGIN)

        self.play(Create(pizza2_1), Create(pizza2_2), run_time=4)
        self.wait(15)

        frac_5_4 = MathTex(r"\frac{5}{4}", font_size=60).next_to(pizza2_2, RIGHT, buff=1)
        self.play(Write(frac_5_4), run_time=2)
        self.wait(11)

        # TAM SAYILI KESİR (35s)
        tam_text = Text("Tam Sayılı Kesir", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Transform(bilesik_text, tam_text), run_time=2)
        self.wait(10)

        frac_1_1_4 = MathTex(r"1 \frac{1}{4}", font_size=60).move_to(frac_5_4.get_center())
        self.play(Transform(frac_5_4, frac_1_1_4), run_time=2)
        self.wait(21)

        # CONVERSION 1: BİLEŞİK -> TAM SAYILI (55s)
        self.play(FadeOut(VGroup(bilesik_text, pizza2_1, pizza2_2, frac_5_4)), run_time=1)
        conv1_text = Text("Bileşik Kesri Tam Sayılı Kesre Çevirme", font_size=32, color=YELLOW).to_edge(UP)
        self.play(Write(conv1_text), run_time=2)
        self.wait(10)

        # Division House (Bölme Evi)
        dividend = MathTex("7", font_size=48).move_to(LEFT * 1 + UP * 0.5)
        vert_line = Line(UP * 1.2, DOWN * 1.5).next_to(dividend, RIGHT, buff=0.3)
        divisor = MathTex("3", font_size=48).next_to(vert_line, RIGHT, buff=0.3).align_to(dividend, UP)
        horiz_line = Line(vert_line.get_start() + DOWN * 0.8, vert_line.get_start() + DOWN * 0.8 + RIGHT * 1.5)
        
        self.play(Write(dividend), Create(vert_line), Write(divisor), Create(horiz_line), run_time=4)
        self.wait(5)

        quotient = MathTex("2", font_size=48).next_to(horiz_line, DOWN, buff=0.3).align_to(divisor, LEFT)
        self.play(Write(quotient), run_time=2)
        self.wait(5)

        mult_res = MathTex("6", font_size=48).next_to(dividend, DOWN, buff=0.4)
        minus = MathTex("-", font_size=48).next_to(mult_res, LEFT, buff=0.1)
        sub_line = Line(minus.get_left() + DOWN * 0.2, mult_res.get_right() + DOWN * 0.2)
        
        self.play(Write(mult_res), Write(minus), Create(sub_line), run_time=3)
        self.wait(2)

        remainder = MathTex("1", font_size=48).next_to(sub_line, DOWN, buff=0.2).align_to(mult_res, RIGHT)
        self.play(Write(remainder), run_time=2)
        self.wait(2)

        box_q = SurroundingRectangle(quotient, color=GREEN, buff=0.1)
        q_label = Text("Tam Kısım", font_size=20, color=GREEN).next_to(box_q, RIGHT)
        self.play(Create(box_q), Write(q_label), run_time=2)
        self.wait(3)

        box_r = SurroundingRectangle(remainder, color=RED, buff=0.1)
        r_label = Text("Yeni Pay", font_size=20, color=RED).next_to(box_r, RIGHT)
        self.play(Create(box_r), Write(r_label), run_time=2)
        self.wait(2)

        result_conv1 = MathTex(r"\frac{7}{3} = 2 \frac{1}{3}", font_size=48).next_to(r_label, RIGHT, buff=1.5)
        self.play(Write(result_conv1), run_time=2)
        self.wait(10)

        # CONVERSION 2: TAM SAYILI -> BİLEŞİK (45s)
        div_group = VGroup(dividend, vert_line, divisor, horiz_line, quotient, mult_res, minus, sub_line, remainder, box_q, box_r, q_label, r_label)
        self.play(FadeOut(div_group), FadeOut(conv1_text), FadeOut(result_conv1), run_time=1)
        
        conv2_text = Text("Tam Sayılı Kesri Bileşik Kesre Çevirme", font_size=32, color=YELLOW).to_edge(UP)
        self.play(Write(conv2_text), run_time=2)
        self.wait(5)

        mix_frac = MathTex(r"2 \frac{3}{5}", font_size=60).move_to(LEFT * 3)
        self.play(Write(mix_frac), run_time=2)
        self.wait(5)

        step1 = MathTex(r"= \frac{2 \times 5 + 3}{5}", font_size=50).next_to(mix_frac, RIGHT)
        self.play(Write(step1), run_time=3)
        self.wait(5)

        step2 = MathTex(r"= \frac{10 + 3}{5}", font_size=50).next_to(step1, RIGHT)
        self.play(Write(step2), run_time=2)
        self.wait(5)

        step3 = MathTex(r"= \frac{13}{5}", font_size=50).next_to(step2, RIGHT)
        self.play(Write(step3), run_time=2)
        self.wait(13)

        # OUTRO (5s)
        self.play(FadeOut(VGroup(conv2_text, mix_frac, step1, step2, step3)), run_time=2)
        outro_text = Text("Maarif Matematik", font_size=40, color=BLUE)
        self.play(Write(outro_text), run_time=2)
        self.wait(1)
