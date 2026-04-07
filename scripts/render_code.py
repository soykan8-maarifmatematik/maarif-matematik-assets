from manim import *

class MaarifMath(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        title = Text('Kesirlerde Toplama', color=BLUE).to_edge(UP)
        self.play(Write(title))
        self.wait(8)
        
        eq1 = MathTex(r'\frac{1}{2}', '+', r'\frac{1}{4}', color=DARK_GRAY).scale(1.5)
        self.play(FadeIn(eq1))
        self.wait(9)
        
        self.play(Indicate(eq1[0], color=GREEN), Indicate(eq1[2], color=GREEN))
        self.wait(6)
        
        eq_exp = MathTex(r'\frac{1 \times 2}{2 \times 2}', '+', r'\frac{1}{4}', color=DARK_GRAY).scale(1.5)
        eq_exp[0].set_color(BLUE)
        self.play(Transform(eq1, eq_exp))
        self.wait(8)
        
        eq2 = MathTex(r'\frac{2}{4}', '+', r'\frac{1}{4}', color=DARK_GRAY).scale(1.5)
        eq2[0].set_color(BLUE)
        self.play(Transform(eq1, eq2))
        self.wait(6)
        
        eq3 = MathTex(r'\frac{2}{4}', '+', r'\frac{1}{4}', '=', r'\frac{3}{4}', color=DARK_GRAY).scale(1.5)
        eq3[0].set_color(BLUE)
        eq3[-1].set_color(GREEN)
        self.play(Transform(eq1, eq3))
        self.wait(9)
        
        self.play(FadeOut(eq1), FadeOut(title))
        self.wait(4)
