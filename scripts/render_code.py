from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        # Title
        title = Tex("Kesirlerin Mantığı", color=BLACK).scale(1.2).to_edge(UP)
        self.play(Write(title))

        # Main Group to be centered
        main_group = VGroup()

        # Fraction
        line = Line(LEFT, RIGHT, color=BLACK).scale(0.8)
        num = MathTex("3", color=BLUE).scale(1.5).next_to(line, UP, buff=0.3)
        den = MathTex("4", color=RED).scale(1.5).next_to(line, DOWN, buff=0.3)
        fraction = VGroup(num, line, den)

        # Labels
        num_label = Tex("Pay (Bizim Payımız)", color=BLUE).scale(0.7).next_to(num, RIGHT, buff=0.5)
        den_label = Tex("Payda (Bütün Parçalar)", color=RED).scale(0.7).next_to(den, RIGHT, buff=0.5)
        
        fraction_with_labels = VGroup(fraction, num_label, den_label)

        # Readings
        read1 = Tex("- 3 bölü 4", color=BLACK).scale(0.8)
        read2 = Tex("- 4'te 3", color=BLACK).scale(0.8)
        readings = VGroup(read1, read2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        main_group.add(fraction_with_labels, readings).arrange(DOWN, buff=1)
        main_group.move_to(main_center)

        # Animation Sequence
        self.play(Create(line))
        self.wait(1)
        
        self.play(Write(den))
        self.play(FadeIn(den_label, shift=LEFT))
        self.wait(2)
        
        self.play(Write(num))
        self.play(FadeIn(num_label, shift=LEFT))
        self.wait(2)

        self.play(Write(read1))
        self.wait(2)
        self.play(Write(read2))
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))
