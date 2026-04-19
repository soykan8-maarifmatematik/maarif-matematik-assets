from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        # Intro
        title = Text("Maarif Matematik", color=BLACK, font_size=48)
        subtitle = Text("Kesirler: Pay, Payda ve Okunuş", color=BLUE, font_size=36).next_to(title, DOWN)
        intro_group = VGroup(title, subtitle).move_to(main_center)
        
        self.play(Write(intro_group), run_time=2)
        self.wait(15)
        self.play(FadeOut(intro_group))

        # Pizza / Circle concept
        circle = Circle(radius=1.5, color=BLACK, stroke_width=4).move_to(main_center + LEFT * 3)
        lines = VGroup(
            Line(circle.get_top(), circle.get_bottom(), color=BLACK),
            Line(circle.get_left(), circle.get_right(), color=BLACK)
        )
        pizza = VGroup(circle, lines)
        
        pizza_text = Text("Eş Parçalar", color=RED, font_size=32).next_to(pizza, UP)
        
        self.play(Create(pizza), Write(pizza_text), run_time=2)
        self.wait(18)

        # Highlight 3 slices
        sectors = VGroup()
        colors = [BLUE, BLUE, BLUE, WHITE]
        angles = [0, PI/2, PI, 3*PI/2]
        for i in range(4):
            sector = Sector(arc_center=circle.get_center(), outer_radius=1.5, angle=PI/2, start_angle=angles[i], color=colors[i], fill_opacity=0.6, stroke_color=BLACK, stroke_width=2)
            sectors.add(sector)
        
        self.play(FadeIn(sectors), run_time=2)
        self.wait(15)

        # Fraction 3/4
        fraction = MathTex(r"\frac{3}{4}", color=BLACK, font_size=120).move_to(main_center + RIGHT * 3)
        self.play(Write(fraction), run_time=2)
        self.wait(10)

        # Fraction line
        line_arrow = Arrow(start=fraction.get_center() + RIGHT * 2, end=fraction.get_center() + RIGHT * 0.8, color=RED)
        line_text = Text("Kesir Çizgisi", color=RED, font_size=28).next_to(line_arrow, RIGHT)
        self.play(GrowArrow(line_arrow), Write(line_text))
        self.wait(15)
        self.play(FadeOut(line_arrow), FadeOut(line_text))

        # Denominator (Payda)
        denom_arrow = Arrow(start=fraction.get_center() + DOWN * 0.8 + RIGHT * 2, end=fraction.get_center() + DOWN * 0.8 + RIGHT * 0.5, color=GREEN)
        denom_text = Text("Payda (Bütünün eş parçaları)", color=GREEN, font_size=28).next_to(denom_arrow, RIGHT)
        self.play(GrowArrow(denom_arrow), Write(denom_text))
        self.wait(25)
        self.play(FadeOut(denom_arrow), FadeOut(denom_text))

        # Numerator (Pay)
        num_arrow = Arrow(start=fraction.get_center() + UP * 0.8 + RIGHT * 2, end=fraction.get_center() + UP * 0.8 + RIGHT * 0.5, color=ORANGE)
        num_text = Text("Pay (Alınan parçalar)", color=ORANGE, font_size=28).next_to(num_arrow, RIGHT)
        self.play(GrowArrow(num_arrow), Write(num_text))
        self.wait(30)
        self.play(FadeOut(num_arrow), FadeOut(num_text))

        # Reading 1: 3 bölü 4
        read1_arrow = Arrow(start=fraction.get_top() + UP * 1.5, end=fraction.get_bottom() + DOWN * 0.5, color=PURPLE)
        read1_text = Text("Üç bölü dört", color=PURPLE, font_size=32).next_to(read1_arrow, LEFT)
        self.play(GrowArrow(read1_arrow), Write(read1_text))
        self.wait(25)
        self.play(FadeOut(read1_arrow), FadeOut(read1_text))

        # Reading 2: 4'te 3
        read2_arrow = Arrow(start=fraction.get_bottom() + DOWN * 1.5, end=fraction.get_top() + UP * 0.5, color=TEAL)
        read2_text = Text("Dörtte üç", color=TEAL, font_size=32).next_to(read2_arrow, RIGHT)
        self.play(GrowArrow(read2_arrow), Write(read2_text))
        self.wait(35)
        self.play(FadeOut(read2_arrow), FadeOut(read2_text), FadeOut(pizza_text), FadeOut(sectors), FadeOut(pizza), FadeOut(fraction))

        # Outro
        outro_text = Text("Mantığı Kavradınız!", color=BLACK, font_size=48).move_to(main_center)
        self.play(Write(outro_text))
        self.wait(25)
        self.play(FadeOut(outro_text))
