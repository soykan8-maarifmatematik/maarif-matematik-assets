from manim import *

class KesirlerinMantigi(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        BLUE_C = "#1976D2"
        RED_C = "#D32F2F"
        GRAY_C = "#333333"

        # P1: Intro
        title = Text("Kesirlerin Mantığı", color=GRAY_C, font_size=48)
        self.play(Write(title))
        self.wait(10)
        self.play(FadeOut(title))

        # P2: Pay and Payda
        fraction = MathTex(r"\frac{3}{4}", font_size=120, color=GRAY_C)
        pay_text = Text("Pay", color=RED_C, font_size=36).next_to(fraction, UP, buff=0.5)
        payda_text = Text("Payda", color=BLUE_C, font_size=36).next_to(fraction, DOWN, buff=0.5)
        line_text = Text("Kesir Çizgisi", color=GRAY_C, font_size=24).next_to(fraction, RIGHT, buff=1)
        line_arrow = Arrow(line_text.get_left(), fraction.get_center(), buff=0.1, color=GRAY_C)

        self.play(Write(fraction))
        self.play(Write(pay_text), Write(payda_text))
        self.play(Write(line_text), Create(line_arrow))
        self.wait(11)
        self.play(FadeOut(pay_text), FadeOut(payda_text), FadeOut(line_text), FadeOut(line_arrow))
        self.play(fraction.animate.shift(LEFT * 3))

        # P3: Sector Model
        pie = VGroup()
        for i in range(4):
            sector = Sector(outer_radius=2, angle=PI/2, start_angle=i*PI/2, color=RED_C if i < 3 else GRAY_C, fill_opacity=0.8 if i < 3 else 0.1, stroke_color=WHITE, stroke_width=4)
            pie.add(sector)
        pie.move_to(RIGHT * 3)

        self.play(Create(pie))
        self.wait(11)

        # P4: Reading Directions
        arrow_down = Arrow(start=UP*2 + LEFT*4.5, end=DOWN*2 + LEFT*4.5, color=RED_C, stroke_width=6)
        text_down = Text("Üç bölü dört", font_size=28, color=RED_C).next_to(arrow_down, LEFT)

        arrow_up = Arrow(start=DOWN*2 + LEFT*1.5, end=UP*2 + LEFT*1.5, color=BLUE_C, stroke_width=6)
        text_up = Text("Dörtte üç", font_size=28, color=BLUE_C).next_to(arrow_up, RIGHT)

        self.play(Create(arrow_down), Write(text_down))
        self.play(Create(arrow_up), Write(text_up))
        self.wait(14)

        # P5: Outro
        self.play(FadeOut(Group(fraction, pie, arrow_down, text_down, arrow_up, text_up)))
        outro = Text("Maarif Matematik", color=GRAY_C, font_size=48)
        self.play(Write(outro))
        self.wait(3)