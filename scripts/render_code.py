from manim import *

class MaarifScene(Scene):
    def construct(self):
        # S1: Intro (20s)
        title = Tex("Kesirler Dünyası").scale(1.5)
        subtitle = Tex("Basit, Bileşik ve Tam Sayılı Kesirler").next_to(title, DOWN)
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(15)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=2)

        # S2: Basit Kesir (47.6s)
        basit_title = Tex("Basit Kesir: Pay $<$ Payda").to_edge(UP)
        self.play(Write(basit_title), run_time=2)

        pizza_basit = VGroup()
        for i in range(4):
            color = ORANGE if i < 3 else DARK_GRAY
            slice_obj = Sector(radius=1.5, angle=TAU/4, start_angle=i*TAU/4, color=color, fill_opacity=0.8, stroke_color=WHITE, stroke_width=2)
            pizza_basit.add(slice_obj)

        frac_3_4 = MathTex(r"\frac{3}{4}").scale(2).next_to(pizza_basit, RIGHT, buff=1)

        self.play(Create(pizza_basit), run_time=3)
        self.play(Write(frac_3_4), run_time=2)
        self.wait(38.6)
        self.play(FadeOut(pizza_basit), FadeOut(frac_3_4), FadeOut(basit_title), run_time=2)

        # S3: Bileşik Kesir (68.8s)
        bilesik_title = Tex("Bileşik Kesir: Pay $\geq$ Payda").to_edge(UP)
        self.play(Write(bilesik_title), run_time=2)

        pizza_b1 = VGroup(*[Sector(radius=1.5, angle=TAU/4, start_angle=i*TAU/4, color=ORANGE, fill_opacity=0.8, stroke_color=WHITE, stroke_width=2) for i in range(4)])
        pizza_b2 = VGroup(*[Sector(radius=1.5, angle=TAU/4, start_angle=i*TAU/4, color=ORANGE if i < 1 else DARK_GRAY, fill_opacity=0.8, stroke_color=WHITE, stroke_width=2) for i in range(4)])

        pizzas = VGroup(pizza_b1, pizza_b2).arrange(RIGHT, buff=1).move_to(LEFT*1)
        frac_5_4 = MathTex(r"\frac{5}{4}").scale(2).next_to(pizzas, RIGHT, buff=1)

        self.play(Create(pizza_b1), run_time=3)
        self.play(Create(pizza_b2), run_time=3)
        self.play(Write(frac_5_4), run_time=2)
        self.wait(56.8)
        self.play(FadeOut(pizzas), FadeOut(frac_5_4), FadeOut(bilesik_title), run_time=2)

        # S4: Tam Sayılı Kesir (43.0s)
        tam_title = Tex("Tam Sayılı Kesir").to_edge(UP)
        self.play(Write(tam_title), run_time=2)

        pizza_t1 = VGroup(*[Sector(radius=1.5, angle=TAU/4, start_angle=i*TAU/4, color=ORANGE, fill_opacity=0.8, stroke_color=WHITE, stroke_width=2) for i in range(4)])
        pizza_t2 = VGroup(*[Sector(radius=1.5, angle=TAU/4, start_angle=i*TAU/4, color=ORANGE if i < 1 else DARK_GRAY, fill_opacity=0.8, stroke_color=WHITE, stroke_width=2) for i in range(4)])
        pizzas_t = VGroup(pizza_t1, pizza_t2).arrange(RIGHT, buff=1).move_to(LEFT*1)

        frac_mixed = MathTex(r"1 \frac{1}{4}").scale(2).next_to(pizzas_t, RIGHT, buff=1)

        self.play(FadeIn(pizzas_t), run_time=2)
        self.play(Write(frac_mixed), run_time=2)

        eq = MathTex(r"\frac{5}{4} = 1 \frac{1}{4}").scale(1.5).next_to(pizzas_t, DOWN, buff=1)
        self.play(Write(eq), run_time=2)

        self.wait(33.0)
        self.play(FadeOut(pizzas_t), FadeOut(frac_mixed), FadeOut(eq), FadeOut(tam_title), run_time=2)

        # S5: Conversion Bileşik -> Tam Sayılı (42.3s)
        conv1_title = Tex(r"Dönüşüm: $\frac{7}{3} \rightarrow$ Tam Sayılı").to_edge(UP)
        self.play(Write(conv1_title), run_time=2)

        eq_div = MathTex(r"7 \div 3 = 2 \text{ (Kalan } 1)").scale(1.2).move_to(UP*1)
        res_mixed = MathTex(r"\frac{7}{3} = 2 \frac{1}{3}").scale(1.5).next_to(eq_div, DOWN, buff=1)

        self.play(Write(eq_div), run_time=3)
        self.play(Write(res_mixed), run_time=3)

        self.wait(32.3)
        self.play(FadeOut(eq_div), FadeOut(res_mixed), FadeOut(conv1_title), run_time=2)

        # S6: Conversion Tam Sayılı -> Bileşik (38.8s)
        conv2_title = Tex(r"Dönüşüm: $2 \frac{1}{3} \rightarrow$ Bileşik").to_edge(UP)
        self.play(Write(conv2_title), run_time=2)

        eq_mul = MathTex(r"(2 \times 3) + 1 = 7").scale(1.2).move_to(UP*1)
        res_improper = MathTex(r"2 \frac{1}{3} = \frac{7}{3}").scale(1.5).next_to(eq_mul, DOWN, buff=1)

        self.play(Write(eq_mul), run_time=3)
        self.play(Write(res_improper), run_time=3)

        self.wait(28.8)
        self.play(FadeOut(eq_mul), FadeOut(res_improper), FadeOut(conv2_title), run_time=2)

        # S7: Outro & Philosophy (63.67s)
        phil_text1 = Tex("Matematikte ezber yoktur,").scale(1.2).move_to(UP*0.5)
        phil_text2 = Tex("mantıksal ispat vardır.").scale(1.2).next_to(phil_text1, DOWN)

        self.play(Write(phil_text1), run_time=2)
        self.play(Write(phil_text2), run_time=2)

        self.wait(57.67)
        self.play(FadeOut(phil_text1), FadeOut(phil_text2), run_time=2)
