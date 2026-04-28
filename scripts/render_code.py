from manim import *

class UnitFractions(Scene):
    def construct(self):
        # 1. BAŞLIK: UP, buff=1.0 noktasına sabitle. Scale (1.2) yap.
        title = Text("Birim Kesirler", font_size=48).scale(1.2).to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(0.5)

        # Modelleri oluştur
        rects_1_2 = VGroup(*[Rectangle(width=3, height=0.8, color=WHITE) for _ in range(2)]).arrange(RIGHT, buff=0)
        rects_1_2[0].set_fill(BLUE, opacity=0.8)
        label_1_2 = MathTex(r"\frac{1}{2}").scale(1.5).next_to(rects_1_2, UP, buff=0.2)
        model_1_2 = VGroup(rects_1_2, label_1_2)

        rects_1_4 = VGroup(*[Rectangle(width=1.5, height=0.8, color=WHITE) for _ in range(4)]).arrange(RIGHT, buff=0)
        rects_1_4[0].set_fill(RED, opacity=0.8)
        label_1_4 = MathTex(r"\frac{1}{4}").scale(1.5).next_to(rects_1_4, UP, buff=0.2)
        model_1_4 = VGroup(rects_1_4, label_1_4)

        # DİKEY MESAFE: VGroup(...).arrange(DOWN, buff=2.5) kullan
        models = VGroup(model_1_2, model_1_4).arrange(DOWN, buff=2.5)
        
        # İLK MODEL: Başlığın çok altında, UP * 3.0 noktasına koy
        models.move_to(UP * 3.0, aligned_edge=UP)

        self.play(FadeIn(rects_1_2), Write(label_1_2))
        self.wait(1)
        self.play(FadeIn(rects_1_4), Write(label_1_4))
        self.wait(1)

        # SONUÇ (ALT SINIR KONTROLÜ: y = -5.5'in altına inmez)
        conclusion = MathTex(r"\frac{1}{2} > \frac{1}{4}").scale(2)
        conclusion.next_to(models, DOWN, buff=1.0)
        
        self.play(Write(conclusion))
        self.play(Indicate(conclusion, color=YELLOW, scale_factor=1.2))
        self.wait(2)