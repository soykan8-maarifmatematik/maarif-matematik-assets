from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan ve renk ayarları
        self.camera.background_color = "#FFFFFF"
        maarif_blue = "#007BFF"
        navy_blue = "#002B4D"
        dark_gray = "#333333"

        # BÖLÜM 1: Giriş (19.3 saniye)
        title = Text("Doğal Sayı ve Kesir Karşılaştırması", color=navy_blue, font_size=40)
        self.play(Write(title), run_time=2)
        self.wait(16.3)
        self.play(FadeOut(title), run_time=1)

        # BÖLÜM 2: Mantık ve İki Dil (34.0 saniye)
        num_3 = MathTex("3", color=dark_gray, font_size=72).shift(LEFT * 2)
        frac_7_2 = MathTex("\\frac{7}{2}", color=maarif_blue, font_size=72).shift(RIGHT * 2)
        vs_text = Text("vs", color=dark_gray, font_size=36).move_to(ORIGIN)

        self.play(Write(num_3), run_time=1.5)
        self.play(Write(vs_text), run_time=1)
        self.play(Write(frac_7_2), run_time=1.5)
        self.wait(29)
        self.play(FadeOut(num_3, vs_text, frac_7_2), run_time=1)

        # BÖLÜM 3: Bölme Evi (27.9 saniye)
        dividend = MathTex("7", color=dark_gray, font_size=60).shift(LEFT * 1 + UP * 1)
        divisor = MathTex("2", color=dark_gray, font_size=60).shift(RIGHT * 0.5 + UP * 1)

        # Dikey çizgi (Bölünen ile Bölen arası)
        v_line = Line(UP * 1.5, UP * 0.5, color=dark_gray).shift(LEFT * 0.25)
        # Yatay çizgi (Bölenin ALTI)
        h_line = Line(LEFT * 0.25, RIGHT * 1.25, color=dark_gray).shift(UP * 0.5)

        self.play(Write(dividend), Write(divisor), run_time=2)
        self.play(Create(v_line), Create(h_line), run_time=2)

        quotient = MathTex("3", color=maarif_blue, font_size=60).next_to(h_line, DOWN, buff=0.3).align_to(divisor, LEFT)
        self.wait(10.9)
        self.play(Write(quotient), run_time=1.5)

        minus_six = MathTex("-6", color=dark_gray, font_size=60).next_to(dividend, DOWN, buff=0.3)
        sub_line = Line(LEFT * 1.5, LEFT * 0.5, color=dark_gray).next_to(minus_six, DOWN, buff=0.1)
        remainder = MathTex("1", color=navy_blue, font_size=60).next_to(sub_line, DOWN, buff=0.2)

        self.wait(6)
        self.play(Write(minus_six), Create(sub_line), run_time=2)
        self.play(Write(remainder), run_time=1.5)
        self.wait(2)

        # BÖLÜM 4: Vurgular ve Tam Sayılı Kesir (54.8 saniye)
        box_quotient = SurroundingRectangle(quotient, color=maarif_blue, buff=0.1)
        box_remainder = SurroundingRectangle(remainder, color=navy_blue, buff=0.1)

        self.play(Create(box_quotient), run_time=1.5)
        self.wait(4)
        self.play(Create(box_remainder), run_time=1.5)
        self.wait(4)

        mixed_num = MathTex("3", "\\frac{1}{2}", color=dark_gray, font_size=60).shift(RIGHT * 3 + DOWN * 1)
        mixed_num[0].set_color(maarif_blue)
        mixed_num[1].set_color(navy_blue)

        arrow = Arrow(start=RIGHT * 1, end=RIGHT * 2 + DOWN * 1, color=dark_gray)

        self.play(Create(arrow), Write(mixed_num), run_time=2)
        self.wait(10)

        self.play(FadeOut(dividend, divisor, v_line, h_line, quotient, minus_six, sub_line, remainder, box_quotient, box_remainder, arrow), run_time=2)
        self.play(mixed_num.animate.move_to(RIGHT * 2), run_time=1.5)

        num_3_again = MathTex("3", color=dark_gray, font_size=60).shift(LEFT * 2)
        self.play(Write(num_3_again), run_time=1.5)
        self.wait(16.8)

        less_than = MathTex("<", color=maarif_blue, font_size=60).move_to(ORIGIN)
        self.play(Write(less_than), run_time=1)
        self.wait(7)

        self.play(FadeOut(num_3_again, mixed_num, less_than), run_time=2)

        # BÖLÜM 5: Sayı Doğrusu (45.2 saniye)
        nl = NumberLine(
            x_range=[0, 5, 1],
            length=10,
            color=dark_gray,
            include_numbers=True,
            numbers_to_include=[0, 1, 2, 3, 4, 5]
        ).shift(DOWN * 1)

        self.play(Create(nl), run_time=2)
        self.wait(8)

        dot_3 = Dot(nl.n2p(3), color=maarif_blue, radius=0.15)
        label_3 = MathTex("3", color=maarif_blue).next_to(dot_3, UP)
        self.play(FadeIn(dot_3, label_3), run_time=1.5)
        self.wait(8.7)

        dot_3_5 = Dot(nl.n2p(3.5), color=navy_blue, radius=0.15)
        label_7_2 = MathTex("\\frac{7}{2}", color=navy_blue).next_to(dot_3_5, UP)
        self.play(FadeIn(dot_3_5, label_7_2), run_time=1.5)
        self.wait(10)

        arrow_right = Arrow(start=nl.n2p(3) + UP*0.5, end=nl.n2p(3.5) + UP*0.5, color=dark_gray, buff=0.1)
        self.play(Create(arrow_right), run_time=1.5)
        self.wait(10)

        self.play(FadeOut(nl, dot_3, label_3, dot_3_5, label_7_2, arrow_right), run_time=2)

        # BÖLÜM 6: Payda Eşitleme (36.0 saniye)
        eq_3 = MathTex("3", color=dark_gray, font_size=60).shift(LEFT * 3)
        eq_3_1 = MathTex("=", "\\frac{3}{1}", color=dark_gray, font_size=60).next_to(eq_3, RIGHT)

        self.wait(8)
        self.play(Write(eq_3), run_time=1.5)
        self.wait(5)
        self.play(Write(eq_3_1), run_time=1.5)
        self.wait(6)

        multiply_2 = MathTex("\\times \\frac{2}{2}", color=maarif_blue, font_size=50).next_to(eq_3_1, RIGHT)
        eq_6_2 = MathTex("=", "\\frac{6}{2}", color=navy_blue, font_size=60).next_to(multiply_2, RIGHT)

        self.play(Write(multiply_2), run_time=1.5)
        self.wait(3)
        self.play(Write(eq_6_2), run_time=1.5)
        self.wait(8)

        # BÖLÜM 7: Son Karşılaştırma ve Çıkış (41.1 saniye)
        self.play(FadeOut(eq_3, eq_3_1, multiply_2), eq_6_2.animate.move_to(LEFT * 2), run_time=2)

        final_7_2 = MathTex("\\frac{7}{2}", color=maarif_blue, font_size=60).shift(RIGHT * 2)
        self.play(Write(final_7_2), run_time=1.5)
        self.wait(10)

        final_less = MathTex("<", color=dark_gray, font_size=60).move_to(ORIGIN)
        self.play(Write(final_less), run_time=1.5)
        self.wait(10)

        box_final = SurroundingRectangle(VGroup(eq_6_2, final_less, final_7_2), color=navy_blue, buff=0.3)
        self.play(Create(box_final), run_time=1.5)
        self.wait(13.6)

        self.wait(1)
