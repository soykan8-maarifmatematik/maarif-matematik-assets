from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        txt = Text("Sistem Aktif!", color="#333333")
        circle = Circle(color="#87CEEB", fill_opacity=0.5)
        self.play(Write(txt))
        self.play(Create(circle))
        self.wait(2)
