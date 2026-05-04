from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        text_color = "#333333"
        highlight_color = "#007BFF"
        navy_color = "#002B4D"

        # Intro (12s)
        intro_text = Tex("Maarif Matematik", color=navy_color, font_size=48)
        self.play(Write(intro_text), run_time=4)
        self.wait(6)
        self.play(FadeOut(intro_text), run_time=2)

        # Repeated Addition (44s)
        eq1 = MathTex("3", "+", "3", "+", "3", "+", "3", "=", "12", color=text_color)
        self.play(Write(eq1), run_time=5)
        self.wait(12)
        eq2 = MathTex("4", "\\times", "3", "=", "12", color=text_color)
        eq2.next_to(eq1, DOWN, buff=1)
        self.play(TransformFromCopy(eq1, eq2), run_time=5)
        self.wait(20)
        self.play(FadeOut(eq1, eq2), run_time=2)

        # Area Model (96s)
        rect_full = Rectangle(width=6, height=5, color=text_color)
        self.play(Create(rect_full), run_time=5)
        self.wait(12)

        # Split lines
        v_line = Line(rect_full.get_top() + LEFT*1, rect_full.get_bottom() + LEFT*1, color=highlight_color)
        h_line = Line(rect_full.get_left() + DOWN*0.5, rect_full.get_right() + DOWN*0.5, color=highlight_color)
        self.play(Create(v_line), Create(h_line), run_time=5)
        self.wait(12)

        # Labels
        l_10 = MathTex("10", color=navy_color).move_to(rect_full.get_top() + DOWN*1.5 + LEFT*2)
        l_3 = MathTex("3", color=navy_color).move_to(rect_full.get_top() + DOWN*1.5 + RIGHT*1)
        l_10_v = MathTex("10", color=navy_color).move_to(rect_full.get_left() + RIGHT*1.5 + UP*1)
        l_2_v = MathTex("2", color=navy_color).move_to(rect_full.get_left() + RIGHT*1.5 + DOWN*1.5)

        self.play(Write(l_10), Write(l_3), Write(l_10_v), Write(l_2_v), run_time=5)
        self.wait(16)

        area_100 = MathTex("100", color=highlight_color).move_to(rect_full.get_center() + UP*1 + LEFT*1)
        area_30 = MathTex("30", color=highlight_color).move_to(rect_full.get_center() + UP*1 + RIGHT*1.5)
        area_20 = MathTex("20", color=highlight_color).move_to(rect_full.get_center() + DOWN*1.5 + LEFT*1)
        area_6 = MathTex("6", color=highlight_color).move_to(rect_full.get_center() + DOWN*1.5 + RIGHT*1.5)

        self.play(Write(area_100), Write(area_30), Write(area_20), Write(area_6), run_time=5)
        self.wait(17)

        area_sum = MathTex("100 + 30 + 20 + 6 = 156", color=navy_color).next_to(rect_full, DOWN, buff=0.5)
        self.play(Write(area_sum), run_time=5)
        self.wait(12)
        self.play(FadeOut(rect_full, v_line, h_line, l_10, l_3, l_10_v, l_2_v, area_100, area_30, area_20, area_6, area_sum), run_time=2)

        # Standard Algorithm (106s)
        num_top = MathTex("13", color=text_color).scale(1.5)
        num_bot = MathTex("12", color=text_color).scale(1.5)
        times_sym = MathTex("\\times", color=text_color).scale(1.5)

        num_top.move_to(UP*1)
        num_bot.next_to(num_top, DOWN, buff=0.3)
        times_sym.next_to(num_bot, LEFT, buff=0.5)

        # Rule 4: Yatay cizgi bolenin (ikinci sayinin) altinda
        h_line_alg = Line(times_sym.get_left() + DOWN*0.3, num_bot.get_right() + DOWN*0.3 + RIGHT*0.2, color=text_color)

        self.play(Write(num_top), Write(num_bot), Write(times_sym), Create(h_line_alg), run_time=5)
        self.wait(17)

        part1 = MathTex("26", color=navy_color).scale(1.5).next_to(h_line_alg, DOWN, buff=0.3).align_to(num_bot, RIGHT)
        self.play(Write(part1), run_time=5)
        self.wait(17)

        part2 = MathTex("130", color=navy_color).scale(1.5).next_to(part1, DOWN, buff=0.3).align_to(part1, RIGHT)
        self.play(Write(part2), run_time=5)
        self.wait(17)

        h_line_add = Line(times_sym.get_left() + DOWN*2, num_bot.get_right() + DOWN*2 + RIGHT*0.2, color=text_color)
        plus_sym = MathTex("+", color=text_color).scale(1.5).next_to(part2, LEFT, buff=0.5)

        self.play(Create(h_line_add), Write(plus_sym), run_time=4)
        self.wait(11)

        final_res = MathTex("156", color=text_color).scale(1.5).next_to(h_line_add, DOWN, buff=0.3).align_to(part2, RIGHT)
        self.play(Write(final_res), run_time=4)
        self.wait(11)

        # Rule 4: Kutucuklu vurgu
        box = SurroundingRectangle(final_res, color=highlight_color, buff=0.2)
        self.play(Create(box), run_time=4)
        self.wait(5)

        # Outro (1s wait)
        self.wait(1)
