from manim import *

config.pixel_height, config.pixel_width = 1920, 1080

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame_width = 9
        self.camera.frame_height = 16

        header = Text("BİRİM KESİRLER", color="#212121")
        header.scale_to_fit_width(6.5)
        header.to_edge(UP, buff=1.0)

        circle1_base = Circle(radius=1.0, color="#212121", stroke_width=2)
        slice1 = Sector(radius=1.0, angle=PI, color=BLUE, fill_opacity=0.8)
        label1 = MathTex(r"\frac{1}{2}", color="#212121").next_to(circle1_base, DOWN)
        model1 = VGroup(circle1_base, slice1, label1)

        circle2_base = Circle(radius=1.0, color="#212121", stroke_width=2)
        slice2 = Sector(radius=1.0, angle=PI/2, color=RED, fill_opacity=0.8)
        label2 = MathTex(r"\frac{1}{4}", color="#212121").next_to(circle2_base, DOWN)
        model2 = VGroup(circle2_base, slice2, label2)

        comp_sym = MathTex(">", color="#212121", font_size=72)

        model1.move_to(LEFT * 2)
        model2.move_to(RIGHT * 2)
        comp_sym.move_to(ORIGIN)

        group = VGroup(model1, comp_sym, model2)
        group.move_to(UP * 2.5)

        para = Paragraph("Payda büyüdükçe", "kesrin değeri küçülür.", alignment="center", color="#212121")
        para.scale_to_fit_width(6.5)
        para.move_to(DOWN * 3.0)

        self.play(Write(header))
        self.wait(0.5)
        
        self.play(Create(circle1_base), Create(circle2_base))
        self.play(Write(label1), Write(label2))
        self.wait(0.5)
        
        self.play(Create(slice1))
        self.play(Create(slice2))
        self.wait(0.5)
        
        self.play(Write(comp_sym))
        self.wait(1)
        
        self.play(Write(para))
        self.wait(2)