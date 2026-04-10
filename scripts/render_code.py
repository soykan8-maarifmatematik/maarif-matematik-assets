from manim import *
import numpy as np

class BirimKesirMerkezli(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        title = Text('Birim Kesir: En Sade Anlatım', color=DARK_GRAY, font_size=40).to_edge(UP)
        self.play(Write(title), run_time=2)
        self.wait(3)
        
        whole = Circle(radius=2, color=DARK_GRAY).move_to(ORIGIN)
        lines = VGroup(*[Line(ORIGIN, [2*np.cos(i*TAU/4), 2*np.sin(i*TAU/4), 0], color=DARK_GRAY) for i in range(4)])
        self.play(Create(whole), Create(lines), run_time=3)
        self.wait(7)

        unit_slice = AnnularSector(inner_radius=0, outer_radius=2, angle=TAU/4, start_angle=0, color=BLUE, fill_opacity=0.6).move_to(ORIGIN)
        self.play(FadeIn(unit_slice), run_time=2)
        self.wait(8)

        frac = MathTex(r'\frac{1}{4}', color=BLUE, font_size=100).next_to(whole, RIGHT, buff=1)
        self.play(Write(frac), run_time=2)
        self.wait(22)

        self.play(FadeOut(VGroup(whole, lines, unit_slice, frac, title)))
        self.play(Write(Text('Hoşça kalın...', color=BLUE, font_size=40)))
        self.wait(2)