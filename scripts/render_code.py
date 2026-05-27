from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # BLOCK 1: Intro (46 seconds)
        self.wait(2)
        title = Text("Kesirler: Basit, Bileşik ve Tam Sayılı", color="#002B4D").scale(0.8).to_edge(UP)
        self.play(Write(title), run_time=2)
        self.wait(5)

        basit_kesir = MathTex(r"\frac{2}{3}", color="#333333").scale(1.5).move_to(LEFT*3)
        self.play(Write(basit_kesir), run_time=1)
        self.wait(4)

        basit_text = Text("Basit Kesir", color="#007BFF").scale(0.6).next_to(basit_kesir, DOWN)
        self.play(Write(basit_text), run_time=1)
        self.wait(4)

        cross = Cross(basit_kesir, stroke_color=RED)
        no_tam = Text("Tam Sayılı Olamaz", color=RED).scale(0.6).next_to(basit_text, DOWN)
        self.play(Create(cross), Write(no_tam), run_time=2)
        self.wait(4)

        self.play(FadeOut(basit_kesir), FadeOut(basit_text), FadeOut(cross), FadeOut(no_tam), run_time=1)

        bilesik_kesir = MathTex(r"\frac{7}{3}", color="#333333").scale(1.5).move_to(RIGHT*3)
        self.play(Write(bilesik_kesir), run_time=1)
        self.wait(4)

        bilesik_text = Text("Bileşik Kesir", color="#007BFF").scale(0.6).next_to(bilesik_kesir, DOWN)
        self.play(Write(bilesik_text), run_time=1)
        self.wait(4)

        check = Text("✓", color=GREEN).scale(1.5).next_to(bilesik_kesir, UP)
        yes_tam = Text("Tam Sayılı Olabilir", color=GREEN).scale(0.6).next_to(bilesik_text, DOWN)
        self.play(Write(check), Write(yes_tam), run_time=2)
        self.wait(8)

        # BLOCK 2: Visuals (64 seconds)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1)
        self.wait(2)

        kesir_7_3 = MathTex(r"\frac{7}{3}", color="#002B4D").scale(2).to_edge(UP)
        self.play(Write(kesir_7_3), run_time=1)
        self.wait(4)

        pizzas = VGroup()
        for i in range(3):
            pizza = VGroup()
            for j in range(3):
                sector = Sector(radius=1.2, angle=TAU/3, start_angle=j*TAU/3, color="#333333", fill_opacity=0, stroke_width=2)
                pizza.add(sector)
            pizzas.add(pizza)
        pizzas.arrange(RIGHT, buff=1).move_to(DOWN*0.5)

        self.play(Create(pizzas), run_time=3)
        self.wait(6)

        self.play(pizzas[0].animate.set_style(fill_color="#007BFF", fill_opacity=0.8), run_time=3)
        self.wait(4)
        self.play(pizzas[1].animate.set_style(fill_color="#007BFF", fill_opacity=0.8), run_time=3)
        self.wait(4)
        self.play(pizzas[2][0].animate.set_style(fill_color="#007BFF", fill_opacity=0.8), run_time=2)
        self.wait(5)

        label_1 = Text("1 Tam", color="#333333").scale(0.6).next_to(pizzas[0], DOWN)
        self.play(Write(label_1), run_time=2)
        self.wait(4)

        label_2 = Text("1 Tam", color="#333333").scale(0.6).next_to(pizzas[1], DOWN)
        self.play(Write(label_2), run_time=2)
        self.wait(4)

        label_3 = MathTex(r"\frac{1}{3}", color="#333333").scale(0.8).next_to(pizzas[2], DOWN)
        self.play(Write(label_3), run_time=2)
        self.wait(4)

        tam_sayili = MathTex(r"= 2 \frac{1}{3}", color="#002B4D").scale(2).next_to(kesir_7_3, RIGHT)
        self.play(Write(tam_sayili), run_time=2)
        self.wait(6)

        # BLOCK 3: Bölme Evi (62 seconds)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1)
        self.wait(2)

        bolme_title = Text("Bölme Evi", color="#002B4D").scale(0.8).to_edge(UP)
        self.play(Write(bolme_title), run_time=2)
        self.wait(3)

        dividend = MathTex("7", color="#333333").scale(1.5).move_to(LEFT*0.5 + UP*0.5)
        self.play(Write(dividend), run_time=1)
        self.wait(2)

        v_line = Line(UP*1.2, DOWN*1.2, color="#333333").next_to(dividend, RIGHT, buff=0.3)
        self.play(Create(v_line), run_time=1)
        self.wait(2)

        divisor = MathTex("3", color="#333333").scale(1.5).next_to(v_line, RIGHT, buff=0.3).align_to(dividend, UP)
        self.play(Write(divisor), run_time=1)
        self.wait(2)

        h_line = Line(LEFT*0.5, RIGHT*0.5, color="#333333").next_to(divisor, DOWN, buff=0.1)
        self.play(Create(h_line), run_time=1)
        self.wait(3)

        quotient = MathTex("2", color="#007BFF").scale(1.5).next_to(h_line, DOWN, buff=0.2)
        self.play(Write(quotient), run_time=1)
        self.wait(4)

        product = MathTex("6", color="#333333").scale(1.5).next_to(dividend, DOWN, buff=0.5)
        self.play(Write(product), run_time=1)
        self.wait(3)

        sub_line = Line(LEFT*0.5, RIGHT*0.5, color="#333333").next_to(product, DOWN, buff=0.1)
        minus = MathTex("-", color="#333333").next_to(product, LEFT, buff=0.1)
        remainder = MathTex("1", color="#007BFF").scale(1.5).next_to(sub_line, DOWN, buff=0.2)
        self.play(Create(sub_line), Write(minus), Write(remainder), run_time=2)
        self.wait(4)

        rect_q = SurroundingRectangle(quotient, color="#007BFF")
        text_q = Text("Tam Kısım", color="#007BFF").scale(0.5).next_to(rect_q, RIGHT)
        self.play(Create(rect_q), run_time=1)
        self.play(Write(text_q), run_time=1)
        self.wait(6)

        rect_r = SurroundingRectangle(remainder, color="#007BFF")
        text_r = Text("Pay", color="#007BFF").scale(0.5).next_to(rect_r, RIGHT)
        self.play(Create(rect_r), run_time=1)
        self.play(Write(text_r), run_time=1)
        self.wait(6)

        rect_d = SurroundingRectangle(divisor, color="#002B4D")
        text_d = Text("Payda", color="#002B4D").scale(0.5).next_to(rect_d, RIGHT)
        self.play(Create(rect_d), run_time=1)
        self.play(Write(text_d), run_time=1)
        self.wait(6)

        # BLOCK 4: Conclusion (75 seconds)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1)
        self.wait(2)

        final_eq = MathTex(r"\frac{7}{3}", "=", "2", r"\frac{1}{3}", color="#002B4D").scale(2).move_to(UP*1.5)
        self.play(Write(final_eq), run_time=2)
        self.wait(5)

        div_house = VGroup(dividend, v_line, divisor, h_line, quotient, product, sub_line, minus, remainder).copy().scale(0.6).move_to(DOWN*1.5)
        self.play(FadeIn(div_house), run_time=2)
        self.wait(5)

        self.play(Indicate(div_house[4], color=RED), Indicate(final_eq[2], color=RED), run_time=2)
        self.wait(5)

        self.play(Indicate(div_house[8], color=GREEN), Indicate(final_eq[3][0], color=GREEN), run_time=2)
        self.wait(5)

        self.play(Indicate(div_house[2], color=BLUE), Indicate(final_eq[3][2], color=BLUE), run_time=2)
        self.wait(6)

        self.play(FadeOut(Group(*self.mobjects)), run_time=2)
        self.wait(2)

        final_text1 = Text("Matematik Ezber Değildir!", color="#002B4D").scale(1.2)
        self.play(Write(final_text1), run_time=2)
        self.wait(13)

        self.play(FadeOut(final_text1), run_time=1)
        final_text2 = Text("Maarif Matematik", color="#007BFF").scale(1.5)
        self.play(Write(final_text2), run_time=1)
        self.wait(14)

        self.wait(1)
