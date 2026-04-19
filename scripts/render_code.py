from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        title = Text("Kesir Kavramı", color=BLACK, font_size=48).to_edge(UP)
        self.play(Write(title))

        # Structure
        pay_text = Text("Pay", color=BLUE, font_size=48)
        payda_text = Text("Payda", color=RED, font_size=48)
        line = Line(LEFT, RIGHT, color=BLACK).set_length(2)

        fraction_group = VGroup(pay_text, line, payda_text).arrange(DOWN, buff=0.3)
        fraction_group.move_to(main_center)

        self.play(Write(fraction_group))
        self.wait(2)

        pay_desc = Text("Kaç parça alındı?", color=BLUE, font_size=24).next_to(pay_text, RIGHT, buff=0.5)
        payda_desc = Text("Kaç eş parçaya bölündü?", color=RED, font_size=24).next_to(payda_text, RIGHT, buff=0.5)

        self.play(FadeIn(pay_desc), FadeIn(payda_desc))
        self.wait(3)

        self.play(FadeOut(fraction_group), FadeOut(pay_desc), FadeOut(payda_desc))

        # Example 3/4
        num_3 = Text("3", color=BLUE, font_size=64)
        num_4 = Text("4", color=RED, font_size=64)
        line_ex = Line(LEFT, RIGHT, color=BLACK).set_length(1.5)

        ex_group = VGroup(num_3, line_ex, num_4).arrange(DOWN, buff=0.3)
        ex_group.move_to(main_center)

        self.play(Write(ex_group))
        self.wait(2)

        read1 = Text("Yukarıdan Aşağıya:\n'Üç bölü dört'", color=BLACK, font_size=32).next_to(ex_group, LEFT, buff=1)
        read2 = Text("Aşağıdan Yukarıya:\n'Dörtte üç'", color=BLACK, font_size=32).next_to(ex_group, RIGHT, buff=1)

        self.play(Write(read1))
        self.wait(2)
        self.play(Write(read2))
        self.wait(3)

        self.play(FadeOut(ex_group), FadeOut(read1), FadeOut(read2), FadeOut(title))
        self.wait(1)