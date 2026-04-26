from manim import *

class MaarifScene(Scene):
    def construct(self):
        def create_pizza(slices, colored_slices, radius=1.5):
            pizza = VGroup()
            angle = TAU / slices
            for i in range(slices):
                color = ORANGE if i < colored_slices else DARK_GRAY
                sector = Sector(outer_radius=radius, angle=angle, start_angle=i*angle, color=color, fill_opacity=0.8, stroke_width=2, stroke_color=WHITE)
                pizza.add(sector)
            return pizza

        # Scene 1: Basit Kesir (67.2s)
        intro_text = Text("Maarif Matematik", font_size=48, color=BLUE)
        self.play(Write(intro_text), run_time=2)
        self.wait(3)
        self.play(FadeOut(intro_text), run_time=1)

        title_basit = Tex(r"Basit Kesir", font_size=60, color=YELLOW).to_edge(UP)
        self.play(Write(title_basit), run_time=1)
        self.wait(2)

        frac_basit = MathTex(r"\frac{3}{4}", font_size=96).move_to(LEFT * 3)
        self.play(Write(frac_basit), run_time=1)
        self.wait(4)

        pizza_basit = create_pizza(4, 3).move_to(RIGHT * 2)
        self.play(DrawBorderThenFill(pizza_basit), run_time=4)
        self.wait(10)

        box_num = SurroundingRectangle(frac_basit[0][0], color=GREEN)
        box_den = SurroundingRectangle(frac_basit[0][2], color=RED)
        self.play(Create(box_den), Create(box_num), run_time=2)
        self.wait(15)

        text_kucuk = Text("Bütünden Küçük", font_size=36, color=GREEN).next_to(pizza_basit, DOWN)
        self.play(Write(text_kucuk), run_time=1)
        self.wait(20.2)

        self.play(FadeOut(Group(title_basit, frac_basit, pizza_basit, box_num, box_den, text_kucuk)), run_time=1)

        # Scene 2: Bileşik Kesir (54.7s)
        title_bilesik = Tex(r"Bileşik Kesir", font_size=60, color=YELLOW).to_edge(UP)
        self.play(Write(title_bilesik), run_time=1)
        self.wait(3)

        frac_bilesik = MathTex(r"\frac{7}{4}", font_size=96).move_to(LEFT * 4)
        self.play(Write(frac_bilesik), run_time=1)
        self.wait(5)

        pizza_bilesik1 = create_pizza(4, 4).move_to(RIGHT * 1)
        pizza_bilesik2 = create_pizza(4, 3).move_to(RIGHT * 4.5)
        self.play(DrawBorderThenFill(pizza_bilesik1), DrawBorderThenFill(pizza_bilesik2), run_time=4)
        self.wait(15)

        self.play(Indicate(frac_bilesik[0][0], color=ORANGE, scale_factor=1.5), run_time=2)
        self.wait(10)

        text_buyuk = Text("Bütünden Büyük", font_size=36, color=ORANGE).next_to(pizza_bilesik1, DOWN).shift(RIGHT*1.75)
        self.play(Write(text_buyuk), run_time=1)
        self.wait(11.7)

        self.play(FadeOut(Group(title_bilesik, frac_bilesik, pizza_bilesik1, pizza_bilesik2, text_buyuk)), run_time=1)

        # Scene 3: Bölme / Tam Sayılı (67.0s)
        title_tam = Tex(r"Tam Sayılı Kesir", font_size=60, color=YELLOW).to_edge(UP)
        self.play(Write(title_tam), run_time=1)
        self.wait(5)

        frac_tam = MathTex(r"1 \frac{3}{4}", font_size=96).move_to(LEFT * 4)
        self.play(Write(frac_tam), run_time=1)
        self.wait(8)

        title_conv1 = Tex(r"Bileşik $\rightarrow$ Tam Sayılı", font_size=48, color=BLUE).to_edge(UP)
        self.play(Transform(title_tam, title_conv1), run_time=1)
        self.wait(4)

        dividend = MathTex("7", font_size=72)
        vline = Line(UP*1.2, DOWN*1.2).next_to(dividend, RIGHT, buff=0.3)
        divisor = MathTex("4", font_size=72).next_to(vline, RIGHT, buff=0.3).shift(UP*0.5)
        hline = Line(LEFT, RIGHT).scale(0.8).next_to(divisor, DOWN, buff=0.2)
        quotient = MathTex("1", font_size=72).next_to(hline, DOWN, buff=0.2)
        sub_val = MathTex("4", font_size=72).next_to(dividend, DOWN, buff=0.4)
        minus = MathTex("-", font_size=72).next_to(sub_val, LEFT, buff=0.2)
        sub_line = Line(LEFT, RIGHT).scale(0.8).next_to(sub_val, DOWN, buff=0.2)
        remainder = MathTex("3", font_size=72).next_to(sub_line, DOWN, buff=0.2)

        div_group = VGroup(dividend, vline, divisor, hline).move_to(RIGHT * 3)
        self.play(Create(div_group), run_time=3)
        self.wait(5)

        div_calc = VGroup(quotient, sub_val, minus, sub_line, remainder)
        self.play(Write(div_calc), run_time=4)
        self.wait(10)

        box_q = SurroundingRectangle(quotient, color=YELLOW, buff=0.1)
        self.play(Create(box_q), run_time=2)
        self.wait(6)

        box_r = SurroundingRectangle(remainder, color=GREEN, buff=0.1)
        self.play(Create(box_r), run_time=2)
        self.wait(6)

        box_d = SurroundingRectangle(divisor, color=BLUE, buff=0.1)
        self.play(Create(box_d), run_time=2)
        self.wait(6)

        self.play(FadeOut(Group(title_tam, frac_tam, div_group, div_calc, box_q, box_r, box_d)), run_time=1)

        # Scene 4: Çarpma / Ters Dönüşüm (75.8s)
        title_conv2 = Tex(r"Tam Sayılı $\rightarrow$ Bileşik", font_size=48, color=BLUE).to_edge(UP)
        self.play(Write(title_conv2), run_time=1)
        self.wait(5)

        whole = MathTex("1", font_size=96)
        frac_line = Line(LEFT, RIGHT).scale(0.4).next_to(whole, RIGHT, buff=0.2)
        num = MathTex("3", font_size=72).next_to(frac_line, UP, buff=0.1)
        den = MathTex("4", font_size=72).next_to(frac_line, DOWN, buff=0.1)
        mixed_group = VGroup(whole, frac_line, num, den).move_to(LEFT*2)

        self.play(Write(mixed_group), run_time=1)
        self.wait(5)

        arrow_mul = CurvedArrow(whole.get_bottom() + DOWN*0.1, den.get_bottom() + DOWN*0.1, angle=PI/2, color=YELLOW)
        mul_sign = MathTex(r"\times", font_size=48).next_to(arrow_mul, DOWN, buff=0.1).set_color(YELLOW)
        self.play(Create(arrow_mul), Write(mul_sign), run_time=2)
        self.wait(10)

        arrow_add = CurvedArrow(den.get_right() + RIGHT*0.1, num.get_right() + RIGHT*0.1, angle=-PI/2, color=GREEN)
        add_sign = MathTex(r"+", font_size=48).next_to(arrow_add, RIGHT, buff=0.1).set_color(GREEN)
        self.play(Create(arrow_add), Write(add_sign), run_time=2)
        self.wait(10)

        result_frac = MathTex(r"= \frac{7}{4}", font_size=96).next_to(mixed_group, RIGHT, buff=2)
        self.play(Write(result_frac), run_time=2)
        self.wait(15)

        final_text = Text("Mantığı Kavra!", font_size=48, color=ORANGE).to_edge(DOWN)
        self.play(Write(final_text), run_time=2)
        self.wait(11.8)

        self.play(FadeOut(Group(title_conv2, mixed_group, arrow_mul, mul_sign, arrow_add, add_sign, result_frac, final_text)), run_time=1)
        self.wait(8)
