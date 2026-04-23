from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 8.0
config.frame_height = 14.22

class MaarifScene(Scene):
    def construct(self):
        title = Text("Birim Kesirler", font="DejaVu Sans", color=YELLOW)
        title.scale_to_fit_width(6.5)
        title.to_edge(UP, buff=1)
        self.play(Write(title))
        self.wait(2.08)

        question = Text("Payda buyudukce kesir kuculur mu?", font="DejaVu Sans", color=WHITE)
        question.scale_to_fit_width(6.5)
        question.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(question))
        self.wait(12.08)
        self.play(FadeOut(question))

        pizza1 = Circle(radius=2, color=ORANGE, fill_opacity=0.2)
        pizza2 = Circle(radius=2, color=ORANGE, fill_opacity=0.2)
        pizza1.move_to(UP * 2.5)
        pizza2.move_to(DOWN * 3.5)
        self.play(Create(pizza1), Create(pizza2))
        self.wait(2.92)

        line1 = Line(pizza1.get_top(), pizza1.get_bottom(), color=WHITE)
        self.play(Create(line1))
        slice1 = Sector(radius=2, angle=PI, start_angle=PI/2, color=YELLOW, fill_opacity=0.8, arc_center=pizza1.get_center())
        label1 = Text("1/2", font="DejaVu Sans", color=BLACK)
        label1.move_to(pizza1.get_center() + LEFT*1)
        self.play(Create(slice1))
        self.play(Write(label1))
        self.wait(5.83)

        lines2 = VGroup()
        for i in range(4):
            angle = i * PI / 4
            start = pizza2.get_center() + np.array([np.cos(angle), np.sin(angle), 0]) * 2
            end = pizza2.get_center() + np.array([np.cos(angle + PI), np.sin(angle + PI), 0]) * 2
            lines2.add(Line(start, end, color=WHITE))
        self.play(Create(lines2))
        slice2 = Sector(radius=2, angle=PI/4, start_angle=PI/2, color=YELLOW, fill_opacity=0.8, arc_center=pizza2.get_center())
        label2 = Text("1/8", font="DejaVu Sans", color=BLACK)
        label2.scale(0.6)
        label2.move_to(pizza2.get_center() + UP*1 + LEFT*0.4)
        self.play(Create(slice2))
        self.play(Write(label2))
        self.wait(7.08)

        comp_text = Text("1/2 > 1/8", font="DejaVu Sans", color=GREEN)
        comp_text.scale_to_fit_width(6.5)
        comp_text.move_to(DOWN * 0.5)
        self.play(Write(comp_text))
        self.wait(5.42)

        rule_text = Text("Payda buyudukce deger kuculur", font="DejaVu Sans", color=RED)
        rule_text.scale_to_fit_width(6.5)
        rule_text.next_to(comp_text, DOWN, buff=0.5)
        self.play(FadeIn(rule_text))
        self.wait(10.00)

        outro_text = Text("Maarif Matematik", font="DejaVu Sans", color=BLUE)
        outro_text.scale_to_fit_width(6.5)
        self.play(FadeOut(VGroup(pizza1, pizza2, line1, lines2, slice1, slice2, label1, label2, comp_text, rule_text, title)))
        self.play(Write(outro_text))
        self.wait(2.92)
