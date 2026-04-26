from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # Section 1: Basit Kesir
        title_basit = Text("Basit Kesir", color="#333333").to_edge(UP)
        basit_eq = MathTex(r"\frac{3}{5}", color="#333333").scale(2)
        self.play(Write(title_basit), run_time=2)
        self.play(Write(basit_eq), run_time=2)
        self.wait(30.7)
        
        # Section 2: Bileşik ve Tam Sayılı Kesir
        self.play(FadeOut(title_basit), FadeOut(basit_eq), run_time=1)
        title_bilesik = Text("Bileşik Kesir ve Tam Sayılı Kesir", color="#333333").to_edge(UP)
        bilesik_eq = MathTex(r"\frac{7}{4}", color="#333333").scale(1.5).move_to(LEFT * 2)
        tam_eq = MathTex(r"1 \frac{3}{4}", color="#333333").scale(1.5).move_to(RIGHT * 2)
        self.play(Write(title_bilesik), run_time=1.5)
        self.play(Write(bilesik_eq), run_time=1.5)
        self.play(Write(tam_eq), run_time=1.5)
        self.wait(28.0)
        
        # Section 3: Bölme Algoritması (Bileşik -> Tam Sayılı)
        self.play(FadeOut(title_bilesik), FadeOut(bilesik_eq), FadeOut(tam_eq), run_time=1)
        
        div_7 = MathTex("7", color="#333333").move_to(LEFT * 1 + UP * 1)
        div_4 = MathTex("4", color="#333333").move_to(RIGHT * 0.5 + UP * 1)
        v_line = Line(UP * 1.5, UP * 0.5, color="#333333").move_to(LEFT * 0.25 + UP * 1)
        h_line = Line(LEFT * 0.2, RIGHT * 1.2, color="#333333").next_to(div_4, DOWN, buff=0.1)
        
        self.play(Write(div_7), Write(div_4), run_time=2)
        self.play(Create(v_line), Create(h_line), run_time=2)
        self.wait(10.0)
        
        quot_1 = MathTex("1", color="#333333").next_to(h_line, DOWN, buff=0.2)
        self.play(Write(quot_1), run_time=1)
        self.wait(5.0)
        
        sub_4 = MathTex("4", color="#333333").next_to(div_7, DOWN, buff=0.2)
        minus = MathTex("-", color="#333333").next_to(sub_4, LEFT, buff=0.1)
        sub_line = Line(LEFT * 1.5, LEFT * 0.5, color="#333333").next_to(sub_4, DOWN, buff=0.1)
        
        self.play(Write(sub_4), Write(minus), Create(sub_line), run_time=2)
        self.wait(5.0)
        
        rem_3 = MathTex("3", color="#333333").next_to(sub_line, DOWN, buff=0.1)
        self.play(Write(rem_3), run_time=1)
        self.wait(16.3)
        
        # Section 4: Oklarla Yerleşim
        arrow_tam = Arrow(quot_1.get_right(), RIGHT * 3 + DOWN * 0.5, color="#333333")
        label_tam = Text("Tam Kısım", color="#333333", font_size=24).next_to(arrow_tam, RIGHT)
        
        arrow_pay = Arrow(rem_3.get_bottom(), DOWN * 2.5 + LEFT * 1, color="#333333")
        label_pay = Text("Yeni Pay", color="#333333", font_size=24).next_to(arrow_pay, DOWN)
        
        arrow_payda = Arrow(div_4.get_right(), RIGHT * 3 + UP * 1.5, color="#333333")
        label_payda = Text("Payda", color="#333333", font_size=24).next_to(arrow_payda, RIGHT)
        
        self.play(Create(arrow_tam), Write(label_tam), run_time=2)
        self.play(Create(arrow_pay), Write(label_pay), run_time=2)
        self.play(Create(arrow_payda), Write(label_payda), run_time=2)
        
        result_eq = MathTex(r"\frac{7}{4} = 1 \frac{3}{4}", color="#333333").move_to(DOWN * 2 + RIGHT * 2)
        self.play(Write(result_eq), run_time=2)
        self.wait(14.3)
        
        # Section 5: Tam Sayılı -> Bileşik
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        
        mixed_to_imp = MathTex(r"1 \frac{3}{4}", color="#333333").scale(2).move_to(LEFT * 3)
        self.play(Write(mixed_to_imp), run_time=2)
        self.wait(8.0)
        
        step1 = MathTex(r"1 \times 4 = 4", color="#333333").next_to(mixed_to_imp, RIGHT, buff=1).shift(UP * 0.5)
        self.play(Write(step1), run_time=2)
        self.wait(5.0)
        
        step2 = MathTex(r"4 + 3 = 7", color="#333333").next_to(step1, DOWN, buff=0.5)
        self.play(Write(step2), run_time=2)
        self.wait(5.0)
        
        final_eq = MathTex(r"= \frac{7}{4}", color="#333333").scale(2).next_to(step2, RIGHT, buff=1).shift(UP * 0.25)
        self.play(Write(final_eq), run_time=2)
        self.wait(14.7)
