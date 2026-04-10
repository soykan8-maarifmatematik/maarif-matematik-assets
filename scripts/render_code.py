import manim
import numpy

class BirimKesirDersi(manim.Scene):
    def construct(self):
        self.camera.background_color = manim.WHITE
        
        title = manim.Text('Birim Kesirlerin Mantığı', color=manim.DARK_GRAY, font_size=48).to_edge(manim.UP)
        self.play(manim.Write(title))
        self.wait(1)
        
        whole = manim.Circle(radius=2, color=manim.DARK_GRAY, stroke_width=4)
        lines = manim.VGroup(*[manim.Line(manim.ORIGIN, [2.0 * numpy.cos(i * manim.TAU / 4.0), 2.0 * numpy.sin(i * manim.TAU / 4.0), 0.0], color=manim.DARK_GRAY) for i in range(4)])
        self.play(manim.Create(whole), manim.Create(lines))
        self.wait(1)
        
        unit_slice = manim.AnnularSector(inner_radius=0, outer_radius=2, angle=manim.TAU/4, start_angle=0, color=manim.BLUE, fill_opacity=0.6)
        self.play(manim.FadeIn(unit_slice))
        
        frac = manim.MathTex(r'\frac{1}{4}', color=manim.BLUE, font_size=120).move_to(manim.RIGHT*4)
        self.play(manim.Write(frac))
        self.wait(2)
        
        line = manim.NumberLine(x_range=[0, 1, 0.25], length=8, color=manim.DARK_GRAY, include_ticks=True).to_edge(manim.DOWN, buff=1.5)
        dot = manim.Dot(line.n2p(0.25), color=manim.BLUE, radius=0.15)
        label = manim.MathTex(r'\frac{1}{4}', color=manim.BLUE).next_to(dot, manim.UP)
        
        self.play(manim.FadeOut(whole), manim.FadeOut(lines), manim.FadeOut(unit_slice), manim.FadeOut(frac))
        self.play(manim.Create(line))
        self.play(manim.Create(dot), manim.Write(label))
        self.wait(3)
        
        self.play(manim.FadeOut(line), manim.FadeOut(dot), manim.FadeOut(label), manim.FadeOut(title))
        outro = manim.Text('Hoşça kalın...', color=manim.BLUE, font_size=40)
        self.play(manim.Write(outro))
        self.wait(1)