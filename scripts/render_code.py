from manim import *
import numpy as np

class BirimKesirTamDers(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # 0-5. sn: Giriş ve Başlık
        title = Text('Birim Kesir: Tanım ve Karşılaştırma', color=DARK_GRAY, font_size=38).to_edge(UP)
        self.play(Write(title), run_time=2)
        self.wait(3)

        # 5-20. sn: Birim Kesrin Tanımı (1/4 Örneği)
        def_circle = Circle(radius=1.8, color=DARK_GRAY).shift(LEFT*3)
        def_lines = VGroup(*[Line(def_circle.get_center(), def_circle.get_center() + [1.8*np.cos(i*TAU/4), 1.8*np.sin(i*TAU/4), 0], color=DARK_GRAY) for i in range(4)])
        def_slice = AnnularSector(inner_radius=0, outer_radius=1.8, angle=TAU/4, start_angle=0, color=BLUE, fill_opacity=0.6).move_to(def_circle)
        def_label = MathTex(r'\frac{1}{4}', color=BLUE, font_size=80).next_to(def_circle, RIGHT, buff=1)
        
        self.play(Create(def_circle), Create(def_lines), run_time=3)
        self.wait(2)
        self.play(FadeIn(def_slice), Write(def_label), run_time=2)
        self.wait(8)

        # 20-45. sn: Karşılaştırma (1/2, 1/4, 1/8 Pasta Modelleri)
        # Eski elementleri temizle
        self.play(FadeOut(def_circle), FadeOut(def_lines), FadeOut(def_slice), FadeOut(def_label))
        
        comp_title = Text('Payda Büyüdükçe Dilim Küçülür', color=DARK_GRAY, font_size=35).to_edge(UP)
        self.play(Transform(title, comp_title))

        pastas = VGroup(
            Circle(radius=0.9, color=DARK_GRAY), # 1/2
            Circle(radius=0.9, color=DARK_GRAY), # 1/4
            Circle(radius=0.9, color=DARK_GRAY)  # 1/8
        ).arrange(RIGHT, buff=1.2).shift(UP*0.5)

        lines2 = VGroup(Line(UP*0.9, DOWN*0.9, color=LIGHT_GRAY)).move_to(pastas[0])
        lines4 = VGroup(Line(UP*0.9, DOWN*0.9, color=LIGHT_GRAY), Line(LEFT*0.9, RIGHT*0.9, color=LIGHT_GRAY)).move_to(pastas[1])
        lines8 = VGroup(*[Line(pastas[2].get_center(), pastas[2].get_center() + [0.9*np.cos(i*TAU/8), 0.9*np.sin(i*TAU/8), 0], color=LIGHT_GRAY) for i in range(8)])

        self.play(Create(pastas), Create(lines2), Create(lines4), Create(lines8), run_time=4)
        
        slice2 = AnnularSector(inner_radius=0, outer_radius=0.9, angle=TAU/2, color=BLUE, fill_opacity=0.6).move_to(pastas[0])
        slice4 = AnnularSector(inner_radius=0, outer_radius=0.9, angle=TAU/4, color=BLUE, fill_opacity=0.6).move_to(pastas[1])
        slice8 = AnnularSector(inner_radius=0, outer_radius=0.9, angle=TAU/8, color=BLUE, fill_opacity=0.6).move_to(pastas[2])

        l2 = MathTex(r'\frac{1}{2}', color=BLUE).next_to(pastas[0], DOWN)
        l4 = MathTex(r'\frac{1}{4}', color=BLUE).next_to(pastas[1], DOWN)
        l8 = MathTex(r'\frac{1}{8}', color=BLUE).next_to(pastas[2], DOWN)

        self.play(FadeIn(slice2), FadeIn(slice4), FadeIn(slice8), Write(l2), Write(l4), Write(l8), run_time=3)
        self.wait(15)

        # 45-75. sn: Sayı Doğrusu Modeli
        self.play(FadeOut(pastas), FadeOut(lines2), FadeOut(lines4), FadeOut(lines8), FadeOut(slice2), FadeOut(slice4), FadeOut(slice8))
        self.play(l2.animate.shift(UP*2.5), l4.animate.shift(UP*2.5), l8.animate.shift(UP*2.5))

        n_line = NumberLine(x_range=[0, 1, 0.125], length=10, color=DARK_GRAY, include_ticks=True).shift(DOWN*1)
        self.play(Create(n_line), run_time=2)

        d2 = Dot(n_line.n2p(0.5), color=BLUE)
        d4 = Dot(n_line.n2p(0.25), color=GREEN)
        d8 = Dot(n_line.n2p(0.125), color=ORANGE)

        self.play(Create(d2), l2.animate.next_to(d2, UP), run_time=2)
        self.play(Create(d4), l4.animate.next_to(d4, UP), run_time=2)
        self.play(Create(d8), l8.animate.next_to(d8, UP), run_time=2)
        self.wait(20)

        # 75-80. sn: Kapanış
        self.play(FadeOut(n_line), FadeOut(d2), FadeOut(d4), FadeOut(d8), FadeOut(l2), FadeOut(l4), FadeOut(l8), FadeOut(title))
        outro = Text('Bir sonraki derste görüşmek üzere, hoşça kalın.', color=BLUE, font_size=40)
        self.play(Write(outro))
        self.wait(2)