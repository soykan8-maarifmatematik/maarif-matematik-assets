from manim import *

class Scene1(Scene):
    def construct(self):
        title = Text("Kesir Çeşitleri", font_size=48, color=BLUE)
        self.play(Write(title), run_time=3)
        self.wait(2)
        self.play(FadeOut(title), run_time=1)

        basit_title = Text("Basit Kesir", font_size=40, color=GREEN).to_edge(UP)
        self.play(Write(basit_title), run_time=2)

        frac1 = MathTex(r"\frac{3}{4}", font_size=72)
        self.play(Write(frac1), run_time=2)

        circle = Circle(radius=1.5, color=WHITE).shift(DOWN*1.5)
        sector1 = Sector(radius=1.5, angle=PI/2, start_angle=0, color=BLUE, fill_opacity=0.8).shift(DOWN*1.5)
        sector2 = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color=BLUE, fill_opacity=0.8).shift(DOWN*1.5)
        sector3 = Sector(radius=1.5, angle=PI/2, start_angle=PI, color=BLUE, fill_opacity=0.8).shift(DOWN*1.5)
        lines = VGroup(
            Line(circle.get_top(), circle.get_bottom(), color=WHITE),
            Line(circle.get_left(), circle.get_right(), color=WHITE)
        )

        self.play(Create(circle), Create(lines), run_time=3)
        self.play(FadeIn(sector1, sector2, sector3), run_time=3)
        self.wait(7.53)

class Scene2(Scene):
    def construct(self):
        bilesik_title = Text("Bileşik Kesir", font_size=40, color=RED).to_edge(UP)
        self.play(Write(bilesik_title), run_time=2)

        frac2 = MathTex(r"\frac{7}{3}", font_size=72)
        self.play(Write(frac2), run_time=2)

        box7 = SurroundingRectangle(frac2[0][0], color=YELLOW)
        self.play(Create(box7), run_time=2)
        self.wait(2)
        self.play(FadeOut(box7), run_time=1)

        self.wait(8.06)

class Scene3(Scene):
    def construct(self):
        tam_title = Text("Tam Sayılı Kesir", font_size=40, color=ORANGE).to_edge(UP)
        self.play(Write(tam_title), run_time=2)

        frac3 = MathTex(r"2 \frac{1}{3}", font_size=72)
        self.play(Write(frac3), run_time=2)

        box2 = SurroundingRectangle(frac3[0][0], color=GREEN)
        self.play(Create(box2), run_time=2)
        self.wait(2)
        self.play(FadeOut(box2), run_time=1)

        self.wait(11.59)

class Scene4(Scene):
    def construct(self):
        title = MathTex(r"Bileşik \rightarrow Tam Sayılı", font_size=40, color=YELLOW).to_edge(UP)
        self.play(Write(title), run_time=2)

        dividend = MathTex("7", font_size=48).move_to(LEFT*0.5)
        divisor = MathTex("3", font_size=48).move_to(RIGHT*0.5 + UP*0.5)
        quotient = MathTex("2", font_size=48).move_to(RIGHT*0.5 + DOWN*0.5)

        v_line = Line(UP*0.8, DOWN*0.8).move_to(ORIGIN)
        h_line = Line(ORIGIN, RIGHT*1.0).move_to(RIGHT*0.5)

        div_group = VGroup(dividend, divisor, v_line, h_line)
        self.play(Write(div_group), run_time=3)
        self.play(Write(quotient), run_time=2)

        sub_val = MathTex("6", font_size=48).move_to(LEFT*0.5 + DOWN*0.8)
        minus = MathTex("-", font_size=48).next_to(sub_val, LEFT, buff=0.1)
        sub_line = Line(LEFT*1.0, ORIGIN).move_to(LEFT*0.5 + DOWN*1.2)
        remainder = MathTex("1", font_size=48).move_to(LEFT*0.5 + DOWN*1.6)

        self.play(Write(sub_val), Write(minus), run_time=2)
        self.play(Create(sub_line), Write(remainder), run_time=2)

        box_q = SurroundingRectangle(quotient, color=GREEN)
        box_r = SurroundingRectangle(remainder, color=YELLOW)
        self.play(Create(box_q), run_time=1.5)
        self.play(Create(box_r), run_time=1.5)

        self.wait(4.24)

class Scene5(Scene):
    def construct(self):
        title = MathTex(r"Tam Sayılı \rightarrow Bileşik", font_size=40, color=YELLOW).to_edge(UP)
        self.play(Write(title), run_time=2)

        eq = MathTex(r"2 \frac{1}{3} = \frac{2 \times 3 + 1}{3} = \frac{7}{3}", font_size=48)
        self.play(Write(eq[0][0:3]), run_time=2)
        self.wait(1)
        self.play(Write(eq[0][3:11]), run_time=4)
        self.wait(1)
        self.play(Write(eq[0][11:]), run_time=3)

        box_final = SurroundingRectangle(eq[0][12:], color=RED)
        self.play(Create(box_final), run_time=2)

        self.wait(5.59)
