from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_width = 9.0
config.frame_height = 16.0

class BirimKesirler(Scene):
    def construct(self):
        # 1. Merhaba, Maarif Matematik'e hoş geldiniz.
        intro_text = Text("Maarif Matematik", color=BLUE).scale(1.5)
        self.play(Write(intro_text))
        self.wait(1.7)
        self.play(FadeOut(intro_text))

        # 2. Birim kesirlerde payda büyüdükçe kesir neden küçülür?
        hook_text = Text("Payda büyüdükçe\nkesir neden küçülür?", text_alignment="CENTER").scale(1.5).shift(UP*4)
        self.play(Write(hook_text))
        self.wait(2.3)

        # 3. Düşünün ki elinizde harika bir pizza var.
        pizza1 = Circle(radius=1.5, color=WHITE, fill_opacity=0).shift(UP*1)
        self.play(Create(pizza1))
        self.wait(2.3)

        # 4. Eğer bu pizzayı iki kişi paylaşırsanız, kocaman bir dilim yersiniz.
        slice1 = Sector(outer_radius=1.5, angle=PI, color=ORANGE, fill_opacity=0.8).shift(UP*1)
        self.play(Create(slice1))
        self.wait(3.3)

        # 5. İşte bu ikide birdir.
        frac1 = MathTex(r"\frac{1}{2}").scale(2.5).next_to(pizza1, LEFT, buff=0.5)
        self.play(Write(frac1))
        self.wait(1.3)

        # 6. Ama aynı pizzayı sekiz kişi paylaşırsanız, diliminiz küçücük kalır.
        pizza2 = Circle(radius=1.5, color=WHITE, fill_opacity=0).shift(DOWN*2.5)
        slice2 = Sector(outer_radius=1.5, angle=PI/4, color=RED, fill_opacity=0.8).shift(DOWN*2.5)
        self.play(Create(pizza2))
        self.play(Create(slice2))
        self.wait(3.0)

        # 7. Bu da sekizde birdir.
        frac2 = MathTex(r"\frac{1}{8}").scale(2.5).next_to(pizza2, LEFT, buff=0.5)
        self.play(Write(frac2))
        self.wait(1.3)

        # 8. Yani payda kişi sayısıdır, kişi artarsa dilim küçülür.
        self.play(FadeOut(pizza1), FadeOut(slice1), FadeOut(pizza2), FadeOut(slice2), FadeOut(hook_text))
        
        final_frac1 = MathTex(r"\frac{1}{2}").scale(3.5).shift(LEFT*2)
        final_frac2 = MathTex(r"\frac{1}{8}").scale(3.5).shift(RIGHT*2)
        greater_than = MathTex(">").scale(5.0).set_color(YELLOW).move_to(ORIGIN)

        self.play(
            Transform(frac1, final_frac1),
            Transform(frac2, final_frac2)
        )
        self.play(Write(greater_than))
        
        rule_text = Text("Kişi artarsa\ndilim küçülür!", color=GREEN, text_alignment="CENTER").scale(1.5).shift(DOWN*3.5)
        self.play(Write(rule_text))
        self.wait(2.7)

        # Mutlak Senkronizasyon: Son cümle bittikten sonra +1.5 saniye bekle
        self.wait(1.5)

        # 9. Maarif Matematik ile mantığını kavra, takipte kal!
        self.play(FadeOut(*self.mobjects))
        outro_text = Text("Maarif Matematik ile\nmantığını kavra,\ntakipte kal!", text_alignment="CENTER", color=BLUE).scale(1.5)
        self.play(Write(outro_text))
        self.wait(2.3)
