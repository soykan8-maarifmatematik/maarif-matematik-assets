from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class UnitFractions(Scene):
    def construct(self):
        # Merhaba, Maarif Matematik’e hoş geldiniz. (5 kelime)
        title = Text("BİRİM KESİRLER").scale(1.5).to_edge(UP, buff=2.0)
        self.play(Write(title))
        self.wait(1.66)

        # Birim kesirleri sıralarken kafanız mı karışıyor? (6 kelime)
        frac_half = MathTex(r"\frac{1}{2}").scale(3).move_to(LEFT * 2.5 + UP * 1)
        frac_eighth = MathTex(r"\frac{1}{8}").scale(3).move_to(RIGHT * 2.5 + UP * 1)
        self.play(FadeIn(frac_half), FadeIn(frac_eighth))
        self.wait(2.0)

        # Paydası büyük olan birim kesir aslında daha küçüktür. (8 kelime)
        rule = Text("Payda Büyürse\nDeğer Küçülür").scale(1.5).next_to(title, DOWN, buff=1.0)
        self.play(Write(rule))
        self.wait(2.66)

        # Düşünün, bir pastayı ikiye bölerseniz dilimler kocaman olur. (8 kelime)
        pizza1 = Circle(radius=1.5, color=WHITE).shift(LEFT * 2.5 + DOWN * 3)
        slice1 = Sector(radius=1.5, angle=PI, color=YELLOW, fill_opacity=0.8).shift(LEFT * 2.5 + DOWN * 3)
        self.play(Create(pizza1), FadeIn(slice1))
        self.wait(2.66)

        # Ama aynı pastayı sekize bölerseniz dilimler küçücük kalır. (8 kelime)
        pizza2 = Circle(radius=1.5, color=WHITE).shift(RIGHT * 2.5 + DOWN * 3)
        slice2 = Sector(radius=1.5, angle=PI/4, color=YELLOW, fill_opacity=0.8).shift(RIGHT * 2.5 + DOWN * 3)
        self.play(Create(pizza2), FadeIn(slice2))
        self.wait(2.66)

        # Yani bir bölü iki büyüktür bir bölü sekiz. (8 kelime)
        greater_sign = MathTex(">").scale(3).move_to(UP * 1)
        self.play(Write(greater_sign))
        self.wait(2.66)

        # Final beklemesi
        self.wait(1.5)

        # Her şeyi sil ve CTA getir
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Maarif Matematik ile mantığını kavra, takipte kal! (7 kelime)
        cta = Text("Maarif Matematik ile\nmantığını kavra,\ntakipte kal!").scale(1.5)
        self.play(Write(cta))
        self.wait(2.33)
