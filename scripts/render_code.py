from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        # Intro
        title = Text("Kesir Nedir?", color="#333333", font_size=48).move_to(main_center)
        self.play(Write(title))
        self.wait(15)
        self.play(FadeOut(title))

        # Pizza / Circle Concept
        pizza = Circle(radius=1.5, color="#FFC107", fill_opacity=0.5).move_to(main_center + LEFT * 3)
        self.play(Create(pizza))
        self.wait(25)

        # Slicing into 8 equal parts
        slices = VGroup()
        for i in range(8):
            pizza_slice = Sector(radius=1.5, angle=TAU/8, start_angle=i*TAU/8, color="#FFC107", fill_opacity=0.5).move_to(main_center + LEFT * 3)
            slices.add(pizza_slice)

        self.play(FadeOut(pizza), FadeIn(slices))
        lines = VGroup(*[Line(main_center + LEFT * 3, main_center + LEFT * 3 + np.array([1.5*np.cos(i*TAU/8), 1.5*np.sin(i*TAU/8), 0]), color="#FFFFFF") for i in range(8)])
        self.play(Create(lines))
        self.wait(25)

        # Fraction Elements Intro
        fraction_line = Line(LEFT*0.6, RIGHT*0.6, color="#333333", stroke_width=6).move_to(main_center + RIGHT * 3)
        self.play(Create(fraction_line))
        self.wait(10)

        # Denominator (Payda)
        den_text = Text("8", color="#1976D2", font_size=60).next_to(fraction_line, DOWN, buff=0.3)
        den_label = Text("Payda (Toplam Eş Parça)", color="#1976D2", font_size=24).next_to(den_text, DOWN)
        self.play(Write(den_text), Write(den_label))
        self.wait(25)

        # Numerator (Pay)
        highlight_slices = VGroup(*[Sector(radius=1.5, angle=TAU/8, start_angle=i*TAU/8, color="#D32F2F", fill_opacity=0.8).move_to(main_center + LEFT * 3) for i in range(3)])
        self.play(FadeIn(highlight_slices))

        num_text = Text("3", color="#D32F2F", font_size=60).next_to(fraction_line, UP, buff=0.3)
        num_label = Text("Pay (Alınan Parça)", color="#D32F2F", font_size=24).next_to(num_text, UP)
        self.play(Write(num_text), Write(num_label))
        self.wait(25)

        # Fraction Line Meaning
        line_label = Text("Kesir Çizgisi (Bölme)", color="#333333", font_size=24).next_to(fraction_line, RIGHT, buff=0.5)
        self.play(Write(line_label))
        self.wait(10)

        # Transition to Reading
        self.play(FadeOut(slices), FadeOut(lines), FadeOut(highlight_slices), FadeOut(den_label), FadeOut(num_label), FadeOut(line_label))
        self.play(VGroup(num_text, fraction_line, den_text).animate.move_to(main_center))
        self.wait(15)

        # Reading 1: Top to Bottom
        arrow_down = Arrow(start=UP, end=DOWN, color="#333333").next_to(fraction_line, LEFT, buff=1.5)
        read1_title = Text("1. Okunuş (Yukarıdan Aşağıya)", color="#1976D2", font_size=24).next_to(num_text, UP, buff=1)
        read1_text = Text("Üç Bölü Sekiz", color="#333333", font_size=36).next_to(arrow_down, LEFT)
        self.play(Create(arrow_down), Write(read1_title), Write(read1_text))
        self.wait(25)

        # Reading 2: Bottom to Top
        self.play(FadeOut(arrow_down), FadeOut(read1_title), FadeOut(read1_text))
        arrow_up = Arrow(start=DOWN, end=UP, color="#333333").next_to(fraction_line, LEFT, buff=1.5)
        read2_title = Text("2. Okunuş (Aşağıdan Yukarıya)", color="#D32F2F", font_size=24).next_to(num_text, UP, buff=1)
        read2_text = Text("Sekizde Üç", color="#333333", font_size=36).next_to(arrow_up, LEFT)
        self.play(Create(arrow_up), Write(read2_title), Write(read2_text))
        self.wait(25)

        # Conclusion
        self.play(FadeOut(arrow_up), FadeOut(read2_title), FadeOut(read2_text), FadeOut(num_text), FadeOut(fraction_line), FadeOut(den_text))
        conc_text = Text("Mantığını Kavra, Ezberleme!", color="#1976D2", font_size=40).move_to(main_center)
        self.play(Write(conc_text))
        self.wait(25)

        # Outro
        self.play(FadeOut(conc_text))
        self.wait(5)