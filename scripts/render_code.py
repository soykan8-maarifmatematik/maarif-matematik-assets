from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan ve renkler
        self.camera.background_color = "#FFFFFF"
        text_color = "#333333"
        pay_color = "#1976D2"
        payda_color = "#D32F2F"

        # 1. Giriş
        title = Text("Kesirler", color=text_color, font_size=64)
        self.play(Write(title), run_time=2)
        self.wait(13)
        self.play(title.animate.to_edge(UP).scale(0.8), run_time=1)
        self.wait(4)

        # 2. Kesir Kavramı ve Pizza Modeli
        circle_group = VGroup()
        for i in range(8):
            sector = Sector(radius=2, angle=TAU/8, start_angle=i*TAU/8, color=text_color, fill_opacity=0, stroke_width=3)
            circle_group.add(sector)

        self.play(Create(circle_group), run_time=3)
        self.wait(10)

        colored_group = VGroup()
        for i in range(3):
            sector = Sector(radius=2, angle=TAU/8, start_angle=i*TAU/8, color=pay_color, fill_opacity=0.7, stroke_width=3, stroke_color=text_color)
            colored_group.add(sector)

        self.play(FadeIn(colored_group), run_time=2)
        self.wait(15)

        # 3. Pay, Payda ve Kesir Çizgisi
        self.play(circle_group.animate.shift(LEFT*3), colored_group.animate.shift(LEFT*3), run_time=2)
        self.wait(3)

        line = Line(LEFT*0.8, RIGHT*0.8, color=text_color, stroke_width=6)
        pay_num = MathTex("3", color=pay_color, font_size=96).next_to(line, UP, buff=0.3)
        payda_num = MathTex("8", color=payda_color, font_size=96).next_to(line, DOWN, buff=0.3)
        fraction = VGroup(pay_num, line, payda_num).shift(RIGHT*3)

        self.play(Create(line), run_time=1)
        self.wait(4)
        self.play(Write(payda_num), run_time=1)
        self.wait(10)
        self.play(Write(pay_num), run_time=1)
        self.wait(10)

        pay_label = Text("Pay", color=pay_color, font_size=36).next_to(pay_num, RIGHT, buff=0.5)
        payda_label = Text("Payda", color=payda_color, font_size=36).next_to(payda_num, RIGHT, buff=0.5)
        line_label = Text("Kesir Çizgisi", color=text_color, font_size=28).next_to(line, RIGHT, buff=0.5)

        self.play(Write(pay_label), Write(payda_label), Write(line_label), run_time=2)
        self.wait(16)

        # 4. İlişki ve Sıfır Kuralı
        self.wait(20)

        # 5. Kesirlerin Okunuşu
        read1 = Text("3 bölü 8", color=text_color, font_size=48).shift(RIGHT*3 + DOWN*2.5)
        self.play(Write(read1), run_time=2)
        self.wait(13)

        read2 = Text("8'de 3", color=text_color, font_size=48).shift(RIGHT*3 + DOWN*3.5)
        self.play(Write(read2), run_time=2)
        self.wait(13)

        # 6. Örnekler
        self.play(FadeOut(circle_group), FadeOut(colored_group), FadeOut(fraction), FadeOut(pay_label), FadeOut(payda_label), FadeOut(line_label), FadeOut(read1), FadeOut(read2), run_time=2)
        self.wait(2)

        ex1_line = Line(LEFT*0.6, RIGHT*0.6, color=text_color, stroke_width=5)
        ex1_pay = MathTex("5", color=pay_color, font_size=80).next_to(ex1_line, UP, buff=0.2)
        ex1_payda = MathTex("7", color=payda_color, font_size=80).next_to(ex1_line, DOWN, buff=0.2)
        ex1 = VGroup(ex1_pay, ex1_line, ex1_payda).shift(LEFT*4)
        ex1_r1 = Text("5 bölü 7", color=text_color, font_size=36).next_to(ex1, DOWN, buff=0.6)
        ex1_r2 = Text("7'de 5", color=text_color, font_size=36).next_to(ex1_r1, DOWN, buff=0.3)

        self.play(Write(ex1), run_time=1)
        self.play(Write(ex1_r1), Write(ex1_r2), run_time=2)
        self.wait(5)

        ex2_line = Line(LEFT*0.6, RIGHT*0.6, color=text_color, stroke_width=5)
        ex2_pay = MathTex("1", color=pay_color, font_size=80).next_to(ex2_line, UP, buff=0.2)
        ex2_payda = MathTex("4", color=payda_color, font_size=80).next_to(ex2_line, DOWN, buff=0.2)
        ex2 = VGroup(ex2_pay, ex2_line, ex2_payda)
        ex2_r1 = Text("1 bölü 4", color=text_color, font_size=36).next_to(ex2, DOWN, buff=0.6)
        ex2_r2 = Text("4'te 1", color=text_color, font_size=36).next_to(ex2_r1, DOWN, buff=0.3)

        self.play(Write(ex2), run_time=1)
        self.play(Write(ex2_r1), Write(ex2_r2), run_time=2)
        self.wait(5)

        ex3_line = Line(LEFT*0.6, RIGHT*0.6, color=text_color, stroke_width=5)
        ex3_pay = MathTex("1", color=pay_color, font_size=80).next_to(ex3_line, UP, buff=0.2)
        ex3_payda = MathTex("2", color=payda_color, font_size=80).next_to(ex3_line, DOWN, buff=0.2)
        ex3 = VGroup(ex3_pay, ex3_line, ex3_payda).shift(RIGHT*4)
        ex3_r1 = Text("1 bölü 2", color=text_color, font_size=36).next_to(ex3, DOWN, buff=0.6)
        ex3_r2 = Text("2'de 1", color=text_color, font_size=36).next_to(ex3_r1, DOWN, buff=0.3)

        self.play(Write(ex3), run_time=1)
        self.play(Write(ex3_r1), Write(ex3_r2), run_time=2)
        self.wait(5)

        # 7. Kapanış
        self.wait(17)
