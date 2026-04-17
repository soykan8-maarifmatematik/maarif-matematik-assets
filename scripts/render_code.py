from manim import *
import numpy as np

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        # Title
        title = Text("Kesirler: Pay ve Payda", color="#333333", font_size=48)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title))
        self.wait(22)

        # Fraction Structure
        fraction_group = VGroup()
        pay = Text("Pay", color="#87CEEB", font_size=64)
        line = Line(LEFT*2, RIGHT*2, color="#333333", stroke_width=8)
        payda = Text("Payda", color="#333333", font_size=64)
        
        pay.next_to(line, UP, buff=0.7)
        payda.next_to(line, DOWN, buff=0.7)
        fraction_group.add(pay, line, payda).move_to(main_center)

        self.play(Create(line))
        self.wait(6)
        
        self.play(Write(payda))
        self.wait(14)
        
        self.play(Write(pay))
        self.wait(14)

        self.play(FadeOut(fraction_group))
        self.wait(2)

        # Example Fraction 3/5
        example_group = VGroup()
        num_3 = Text("3", color="#87CEEB", font_size=80)
        ex_line = Line(LEFT*1.5, RIGHT*1.5, color="#333333", stroke_width=8)
        num_5 = Text("5", color="#333333", font_size=80)
        
        num_3.next_to(ex_line, UP, buff=0.7)
        num_5.next_to(ex_line, DOWN, buff=0.7)
        example_group.add(num_3, ex_line, num_5).move_to(main_center)

        self.play(FadeIn(example_group))
        self.wait(8)

        # Reading 1: 3 bölü 5
        read1_text = Text("3 bölü 5", color="#333333", font_size=48).next_to(example_group, RIGHT, buff=2)
        arrow1 = Arrow(num_3.get_right(), num_5.get_right(), path_arc=-1.5, color="#87CEEB", stroke_width=6)
        
        self.play(Create(arrow1), Write(read1_text))
        self.wait(14)
        
        self.play(FadeOut(read1_text), FadeOut(arrow1))
        self.wait(2)

        # Reading 2: 5'te 3
        read2_text = Text("5'te 3", color="#333333", font_size=48).next_to(example_group, LEFT, buff=2)
        arrow2 = Arrow(num_5.get_left(), num_3.get_left(), path_arc=-1.5, color="#87CEEB", stroke_width=6)

        self.play(Create(arrow2), Write(read2_text))
        self.wait(14)

        self.play(FadeOut(example_group), FadeOut(read2_text), FadeOut(arrow2), FadeOut(title))
        self.wait(10)