from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        text_color = "#212121"

        title = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", font="Montserrat", weight=BOLD, color=text_color)
        title.scale_to_fit_width(7.0)
        title.to_edge(np.array([0, 1, 0]), buff=1.0)
        self.play(Write(title))

        frac1 = MathTex(r"\frac{1}{2}", color=text_color).scale(2)
        frac2 = MathTex(r"\frac{1}{4}", color=text_color).scale(2)

        circle1 = Circle(radius=0.9, color=text_color)
        slice1 = Sector(radius=0.9, angle=PI, start_angle=0, color="#FF5722", fill_opacity=0.8)
        line1 = Line(start=np.array([0, -0.9, 0]), end=np.array([0, 0.9, 0]), color=text_color)
        model1 = VGroup(circle1, slice1, line1)

        circle2 = Circle(radius=0.9, color=text_color)
        slice2 = Sector(radius=0.9, angle=PI/2, start_angle=0, color="#2196F3", fill_opacity=0.8)
        line2_1 = Line(start=np.array([-0.9, 0, 0]), end=np.array([0.9, 0, 0]), color=text_color)
        line2_2 = Line(start=np.array([0, -0.9, 0]), end=np.array([0, 0.9, 0]), color=text_color)
        model2 = VGroup(circle2, slice2, line2_1, line2_2)

        symbol = MathTex(">", color=text_color).scale(2.5)

        group1 = VGroup(frac1, model1).arrange(np.array([0, -1, 0]), buff=0.5)
        group2 = VGroup(frac2, model2).arrange(np.array([0, -1, 0]), buff=0.5)

        main_group = VGroup(group1, symbol, group2).arrange(np.array([1, 0, 0]), buff=1.0)
        main_group.scale(0.8).shift(np.array([0, 1.0, 0]))

        self.play(Create(group1))
        self.play(Create(group2))
        self.play(Write(symbol))

        result_text = Text("Payda Büyüdükçe Kesir Küçülür!", font="Montserrat", weight=BOLD, color="#E91E63")
        result_text.scale_to_fit_width(6.0)
        result_text.to_edge(np.array([0, -1, 0]), buff=4.8)
        self.play(Write(result_text))
        self.wait(2)