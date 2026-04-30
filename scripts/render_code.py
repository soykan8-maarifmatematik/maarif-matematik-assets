from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0
config.background_color = "#FFFFFF"

class MaarifScene(Scene):
    def construct(self):
        text_color = "#333333"

        title = Text("Birim Kesirlerin Büyüklüğü", color=text_color, weight=BOLD)
        title.to_edge(UP, buff=1.2)
        title.scale_to_fit_width(8.0)
        
        self.play(Write(title))
        self.wait(1)

        sector1 = Sector(radius=1.1, angle=PI, color=BLUE, fill_opacity=0.6)
        circle1 = Circle(radius=1.1, color=BLUE, stroke_width=4)
        line1 = Line(circle1.get_top(), circle1.get_bottom(), color=BLUE, stroke_width=4)
        group1 = VGroup(sector1, circle1, line1)
        label1 = MathTex(r"\frac{1}{2}", color=text_color, font_size=72).next_to(group1, DOWN, buff=0.5)
        model1 = VGroup(group1, label1)

        sector2 = Sector(radius=1.1, angle=PI/2, color=RED, fill_opacity=0.6)
        circle2 = Circle(radius=1.1, color=RED, stroke_width=4)
        lines2 = VGroup(
            Line(circle2.get_top(), circle2.get_bottom(), color=RED, stroke_width=4),
            Line(circle2.get_left(), circle2.get_right(), color=RED, stroke_width=4)
        )
        group2 = VGroup(sector2, circle2, lines2)
        label2 = MathTex(r"\frac{1}{4}", color=text_color, font_size=72).next_to(group2, DOWN, buff=0.5)
        model2 = VGroup(group2, label2)

        models = VGroup(model1, model2).arrange(RIGHT, buff=1.5)
        models.scale(0.85).shift(UP * 1.5)

        self.play(FadeIn(models))
        self.wait(2)

        result_text = Text("Payda büyüdükçe\nkesrin değeri küçülür!\n1/2 > 1/4", color=text_color, text_alignment=CENTER)
        result_text.to_edge(DOWN, buff=4.5)
        result_text.scale_to_fit_width(8.0)

        self.play(Write(result_text))
        self.wait(3)