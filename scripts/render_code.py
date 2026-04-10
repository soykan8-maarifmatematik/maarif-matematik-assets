from manim import 
import numpy as np

class BirimKesirDersi(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        title = Text('Birim Kesirlerin Mantığı', color=DARK_GRAY, font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        whole = Circle(radius=2, color=DARK_GRAY, stroke_width=4)
        # Çarpım işaretlerini () kesinleştirdik
        lines = VGroup([Line(ORIGIN, [2 * np.cos(i * TAU / 4), 2 * np.sin(i * TAU / 4), 0], color=DARK_GRAY) for i in range(4)])
        self.play(Create(whole), Create(lines))
        self.wait(1)
        
        unit_slice = AnnularSector(inner_radius=0, outer_radius=2, angle=TAU/4, start_angle=0, color=BLUE, fill_opacity=0.6)
        self.play(FadeIn(unit_slice))
        
        frac = MathTex(r'rac{1}{4}', color=BLUE, font_size=120).move_to(RIGHT4)
        self.play(Write(frac))
        self.wait(2)
        
        line = NumberLine(x_range=[0, 1, 0.25], length=8, color=DARK_GRAY, include_ticks=True).to_edge(DOWN, buff=1.5)
        dot = Dot(line.n2p(0.25), color=BLUE, radius=0.15)
        label = MathTex(r'rac{1}{4}', color=BLUE).next_to(dot, UP)
        
        self.play(FadeOut(whole), FadeOut(lines), FadeOut(unit_slice), FadeOut(frac))
        self.play(Create(line))
        self.play(Create(dot), Write(label))
        self.wait(3)
        
        self.play(FadeOut(line), FadeOut(dot), FadeOut(label), FadeOut(title))
        outro = Text('Hoşça kalın...', color=BLUE, font_size=40)
        self.play(Write(outro))
        self.wait(1)