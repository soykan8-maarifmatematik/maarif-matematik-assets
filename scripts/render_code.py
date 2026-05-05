from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0
config.background_color = "#FFFFFF"

class MaarifScene(Scene):
    def construct(self):
        Text.set_default(color="#212121")
        MathTex.set_default(color="#212121")
        Tex.set_default(color="#212121")

        title = Text("BİRİM KESİRLER", weight=BOLD).scale_to_fit_width(7.0)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))

        circle_half = VGroup()
        for i in range(2):
            fill_op = 0.5 if i == 0 else 0.0
            fill_col = BLUE if i == 0 else WHITE
            slice_sector = Sector(
                radius=0.9,
                angle=TAU/2,
                start_angle=i*(TAU/2),
                color=BLACK,
                stroke_width=2,
                fill_color=fill_col,
                fill_opacity=fill_op
            )
            circle_half.add(slice_sector)
        
        circle_quarter = VGroup()
        for i in range(4):
            fill_op = 0.5 if i == 0 else 0.0
            fill_col = RED if i == 0 else WHITE
            slice_sector = Sector(
                radius=0.9,
                angle=TAU/4,
                start_angle=i*(TAU/4),
                color=BLACK,
                stroke_width=2,
                fill_color=fill_col,
                fill_opacity=fill_op
            )
            circle_quarter.add(slice_sector)

        circle_half.move_to(LEFT * 2)
        circle_quarter.move_to(RIGHT * 2)
        
        models_group = VGroup(circle_half, circle_quarter)
        models_group.shift(np.array([0, 1.0, 0]))

        frac_half = MathTex(r"\frac{1}{2}").next_to(circle_half, DOWN, buff=0.5)
        frac_quarter = MathTex(r"\frac{1}{4}").next_to(circle_quarter, DOWN, buff=0.5)

        self.play(Create(circle_half))
        self.play(Write(frac_half))
        self.wait(0.5)

        self.play(Create(circle_quarter))
        self.play(Write(frac_quarter))
        self.wait(0.5)

        sign = MathTex(">").scale(2).move_to(ORIGIN)
        self.play(Write(sign))
        self.wait(1)

        result_text = Text("Payda büyüdükçe dilim küçülür!", weight=BOLD).scale_to_fit_width(5.5)
        result_text.to_edge(DOWN, buff=1.5)
        self.play(Write(result_text))
        self.wait(2)