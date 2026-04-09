from manim import *

class KesirTanimiKisa(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Giriş
        title = Text('Maarif Matematik', font_size=55, color=BLUE).move_to(ORIGIN)
        self.play(Write(title))
        self.wait(5)
        self.play(FadeOut(title))
        
        sub_title = Text('Kesirin Tanımı', font_size=45, color=BLUE).to_edge(UP)
        self.play(Write(sub_title))
        self.wait(10)
        
        # Karpuz/Daire Görseli
        whole = Circle(radius=1.8, color=DARK_GRAY, stroke_width=4)
        parts = VGroup(*[Sector(1.8, angle=TAU/4, start_angle=i*TAU/4, color=WHITE, stroke_color=DARK_GRAY, stroke_width=2, fill_opacity=1) for i in range(4)])
        self.play(Create(whole), FadeIn(parts))
        self.wait(12)
        
        # Bir parçayı boyama ve çıkarma
        self.play(parts[0].animate.set_fill(BLUE, opacity=0.5).shift(UP*0.2 + RIGHT*0.2))
        self.wait(15)
        
        # Pay ve Payda Tanımı
        self.play(FadeOut(whole), FadeOut(parts))
        frac = MathTex(r'\frac{\text{Pay}}{\text{Payda}}', color=DARK_GRAY, font_size=100)
        self.play(Write(frac))
        self.wait(12)
        
        payda_txt = Text('Payda: Kaç parçaya bölündü?', color=GREEN, font_size=32).next_to(frac, DOWN, buff=1)
        self.play(Write(payda_txt))
        self.wait(15)
        
        pay_txt = Text('Pay: Kaç parça alındı?', color=BLUE, font_size=32).next_to(frac, UP, buff=1)
        self.play(Write(pay_txt))
        self.wait(15)
        
        # Örnek 1/4
        example = MathTex(r'\frac{1}{4}', color=DARK_GRAY, font_size=100)
        self.play(Transform(frac, example))
        self.wait(10)
        
        reading = Text('Dörtte bir', color=DARK_GRAY, font_size=40).next_to(example, RIGHT, buff=0.8)
        self.play(Write(reading))
        self.wait(20)
        
        # Outro
        self.play(FadeOut(example), FadeOut(payda_txt), FadeOut(pay_txt), FadeOut(reading))
        outro = Text('Bir sonraki derste görüşmek üzere.', color=BLUE, font_size=35)
        self.play(Write(outro))
        self.wait(4)