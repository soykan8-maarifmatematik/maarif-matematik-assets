from manim import *

class MaarifScene(Scene):
    def create_pizza(self, slices, filled_slices, radius=1.5, color="#007BFF"):
        pizza = VGroup()
        angle = TAU / slices
        for i in range(slices):
            fill_opacity = 0.8 if i < filled_slices else 0.2
            sector = Sector(radius=radius, angle=angle, start_angle=i*angle,
                            color=color, fill_opacity=fill_opacity, stroke_width=2, stroke_color="#FFFFFF")
            pizza.add(sector)
        return pizza

    def construct(self):
        self.camera.background_color = "#FFFFFF"

        # SCENE 1: Intro (25.38s)
        title = Text("Kesir Çeşitleri ve Dönüşümler", color="#002B4D", font_size=48)
        self.play(Write(title), run_time=3)
        self.wait(5)
        subtitle = Text("Maarif Modeli ile Mantıksal Yaklaşım", color="#007BFF", font_size=36).next_to(title, DOWN)
        self.play(FadeIn(subtitle), run_time=2)
        self.wait(10.38)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=2)
        self.wait(3)

        # SCENE 2: Simple Fractions (37.56s)
        simple_title = Text("Basit Kesir", color="#002B4D", font_size=42).to_edge(UP)
        self.play(Write(simple_title), run_time=2)
        self.wait(4)

        frac_3_4 = MathTex(r"\frac{3}{4}", color="#333333", font_size=72).shift(LEFT*3)
        self.play(Write(frac_3_4), run_time=2)
        self.wait(4)

        pizza1 = self.create_pizza(4, 3, radius=1.5, color="#007BFF").shift(RIGHT*2)
        self.play(FadeIn(pizza1), run_time=3)
        self.wait(6)

        desc1 = Text("Pay < Payda", color="#333333", font_size=36).next_to(frac_3_4, DOWN, buff=1)
        self.play(Write(desc1), run_time=2)
        self.wait(10.56)

        self.play(FadeOut(simple_title), FadeOut(frac_3_4), FadeOut(pizza1), FadeOut(desc1), run_time=4)

        # SCENE 3: Improper Fractions (46.19s)
        imp_title = Text("Bileşik Kesir", color="#002B4D", font_size=42).to_edge(UP)
        self.play(Write(imp_title), run_time=2)
        self.wait(4)

        frac_7_4 = MathTex(r"\frac{7}{4}", color="#333333", font_size=72).shift(LEFT*4)
        self.play(Write(frac_7_4), run_time=2)
        self.wait(5)

        pizza2 = self.create_pizza(4, 4, radius=1.5, color="#007BFF").shift(RIGHT*0.5)
        pizza3 = self.create_pizza(4, 3, radius=1.5, color="#007BFF").shift(RIGHT*4)
        self.play(FadeIn(pizza2), run_time=3)
        self.play(FadeIn(pizza3), run_time=3)
        self.wait(8)

        desc2 = Text("Pay ≥ Payda", color="#333333", font_size=36).next_to(frac_7_4, DOWN, buff=1)
        self.play(Write(desc2), run_time=2)
        self.wait(13.19)

        self.play(FadeOut(imp_title), FadeOut(desc2), run_time=4)

        # SCENE 4: Mixed Fractions Intro (35.53s)
        mix_title = Text("Tam Sayılı Kesir", color="#002B4D", font_size=42).to_edge(UP)
        self.play(Write(mix_title), run_time=2)
        self.wait(6)

        mix_frac = MathTex(r"1 \frac{3}{4}", color="#333333", font_size=72).next_to(frac_7_4, RIGHT, buff=1)
        eq_sign = MathTex("=", color="#333333", font_size=60).move_to((frac_7_4.get_right() + mix_frac.get_left())/2)

        self.play(Write(eq_sign), Write(mix_frac), run_time=3)
        self.wait(8)

        q_text = Text("Neden Bölme Yaparız?", color="#007BFF", font_size=36).to_edge(DOWN)
        self.play(Write(q_text), run_time=2)
        self.wait(10.53)

        self.play(FadeOut(mix_title), FadeOut(q_text), FadeOut(pizza2), FadeOut(pizza3), FadeOut(frac_7_4), FadeOut(eq_sign), FadeOut(mix_frac), run_time=4)

        # SCENE 5: Division House (37.05s)
        div_title = Text("Bölme Evi ile Dönüşüm", color="#002B4D", font_size=42).to_edge(UP)
        self.play(Write(div_title), run_time=2)
        self.wait(2)

        dividend = MathTex("7", color="#333333", font_size=60)
        divisor = MathTex("4", color="#333333", font_size=60)
        v_line = Line(UP*0.8, DOWN*0.8, color="#333333", stroke_width=4)
        h_line = Line(LEFT*0.5, RIGHT*0.8, color="#333333", stroke_width=4)

        v_line.next_to(dividend, RIGHT, buff=0.3)
        divisor.next_to(v_line, RIGHT, buff=0.3).align_to(dividend, UP)
        h_line.next_to(divisor, DOWN, buff=0.1).align_to(v_line, LEFT)

        div_group = VGroup(dividend, divisor, v_line, h_line).move_to(ORIGIN).shift(UP*0.5)
        self.play(Create(div_group), run_time=3)
        self.wait(3)

        quotient = MathTex("1", color="#333333", font_size=60).next_to(h_line, DOWN, buff=0.3)
        self.play(Write(quotient), run_time=2)
        self.wait(2)

        sub_val = MathTex("4", color="#333333", font_size=60).next_to(dividend, DOWN, buff=0.3)
        minus = MathTex("-", color="#333333", font_size=60).next_to(sub_val, LEFT, buff=0.2)
        sub_line = Line(minus.get_left() + LEFT*0.1, sub_val.get_right() + RIGHT*0.1, color="#333333", stroke_width=4).next_to(sub_val, DOWN, buff=0.1)

        self.play(Write(sub_val), Write(minus), Create(sub_line), run_time=3)
        self.wait(1)

        remainder = MathTex("3", color="#333333", font_size=60).next_to(sub_line, DOWN, buff=0.3)
        self.play(Write(remainder), run_time=2)
        self.wait(3)

        box_q = SurroundingRectangle(quotient, color="#007BFF", buff=0.1)
        label_q = Text("Tam Kısım", color="#007BFF", font_size=24).next_to(box_q, RIGHT)

        box_r = SurroundingRectangle(remainder, color="#002B4D", buff=0.1)
        label_r = Text("Yeni Pay", color="#002B4D", font_size=24).next_to(box_r, RIGHT)

        box_d = SurroundingRectangle(divisor, color="#333333", buff=0.1)
        label_d = Text("Payda (Değişmez)", color="#333333", font_size=24).next_to(box_d, RIGHT)

        self.play(Create(box_q), Write(label_q), run_time=2)
        self.play(Create(box_r), Write(label_r), run_time=2)
        self.play(Create(box_d), Write(label_d), run_time=2)
        self.wait(4.05)

        self.play(FadeOut(div_title), FadeOut(div_group), FadeOut(quotient), FadeOut(sub_val), FadeOut(minus), FadeOut(sub_line), FadeOut(remainder), FadeOut(box_q), FadeOut(label_q), FadeOut(box_r), FadeOut(label_r), FadeOut(box_d), FadeOut(label_d), run_time=4)

        # SCENE 6: Mixed to Improper (48.73s)
        rev_title = Text("Tam Sayılıdan Bileşiğe", color="#002B4D", font_size=42).to_edge(UP)
        self.play(Write(rev_title), run_time=2)
        self.wait(4)

        mix2 = MathTex(r"2 \frac{1}{3}", color="#333333", font_size=72).shift(LEFT*4 + UP*1)
        self.play(Write(mix2), run_time=2)
        self.wait(5)

        p1 = self.create_pizza(3, 3, radius=1, color="#007BFF").shift(RIGHT*0 + UP*1)
        p2 = self.create_pizza(3, 3, radius=1, color="#007BFF").shift(RIGHT*2.5 + UP*1)
        p3 = self.create_pizza(3, 1, radius=1, color="#007BFF").shift(RIGHT*5 + UP*1)

        self.play(FadeIn(p1), FadeIn(p2), run_time=3)
        self.wait(4)

        calc_text1 = MathTex(r"2 \times 3 = 6 \text{ dilim}", color="#333333", font_size=48).shift(DOWN*1.5)
        self.play(Write(calc_text1), run_time=2)
        self.wait(4)

        self.play(FadeIn(p3), run_time=2)
        self.wait(3)

        calc_text2 = MathTex(r"6 + 1 = 7 \text{ dilim}", color="#333333", font_size=48).next_to(calc_text1, DOWN)
        self.play(Write(calc_text2), run_time=2)
        self.wait(4)

        final_ans = MathTex(r"= \frac{7}{3}", color="#002B4D", font_size=72).next_to(mix2, RIGHT, buff=0.5)
        self.play(Write(final_ans), run_time=2)
        self.wait(5.73)

        self.play(FadeOut(rev_title), FadeOut(mix2), FadeOut(p1), FadeOut(p2), FadeOut(p3), FadeOut(calc_text1), FadeOut(calc_text2), FadeOut(final_ans), run_time=4)

        # SCENE 7: Outro (19.81s)
        outro_text1 = Text("Matematikte hiçbir kural sebepsiz değildir.", color="#002B4D", font_size=36)
        self.play(Write(outro_text1), run_time=3)
        self.wait(4)

        outro_text2 = Text("Mantığını kavra, ezberleme!", color="#007BFF", font_size=42).next_to(outro_text1, DOWN, buff=0.5)
        self.play(Write(outro_text2), run_time=3)
        self.wait(5.81)

        logo = Text("Maarif Matematik", color="#333333", font_size=60)
        self.play(FadeOut(outro_text1), FadeOut(outro_text2), FadeIn(logo), run_time=3)
        self.wait(1)
