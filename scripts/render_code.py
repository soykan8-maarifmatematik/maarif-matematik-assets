from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class BirimKesirler(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        # Başlık ve Güvenli Alan
        title = Tex("Birim Kesirler", color=BLACK).scale(1.2).to_edge(UP, buff=1.0)

        # İçerik Objeleri
        arrow_text = Tex(r"Payda Büyür $\rightarrow$ Değer Küçülür", color=BLACK).scale(1.2)
        
        frac1 = MathTex(r"\frac{1}{2}", color=BLACK).scale(2.0)
        model1 = VGroup(*[Rectangle(width=2, height=1, color=BLACK, fill_opacity=0.8 if i==0 else 0, fill_color=BLUE) for i in range(2)]).arrange(RIGHT, buff=0)
        row1 = VGroup(frac1, model1).arrange(RIGHT, buff=1.0)

        frac2 = MathTex(r"\frac{1}{4}", color=BLACK).scale(2.0)
        model2 = VGroup(*[Rectangle(width=1, height=1, color=BLACK, fill_opacity=0.8 if i==0 else 0, fill_color=RED) for i in range(4)]).arrange(RIGHT, buff=0)
        row2 = VGroup(frac2, model2).arrange(RIGHT, buff=1.0)

        math_comp = Tex(r"$\frac{1}{2} > \frac{1}{4}$", color=RED).scale(2.0)

        # Objelerin Birbirine Girmesini Engelleyen Zırh (buff=2.5)
        content_group = VGroup(arrow_text, row1, row2, math_comp).arrange(DOWN, buff=2.5)
        content_group.next_to(title, DOWN, buff=1.5)
        # Bu yerleşimle hiçbir obje y = -5.5 sınırının altına inmez.

        # Animasyon 1: Giriş (5 kelime)
        self.play(Write(title))
        self.wait(1.66)

        # Animasyon 2: Kural (7 kelime)
        self.play(Write(arrow_text))
        self.wait(2.33)

        # Animasyon 3: Modeller (12 kelime)
        self.play(FadeIn(row1), FadeIn(row2))
        self.wait(4.0)

        # Animasyon 4: Sonuç (8 kelime)
        self.play(Write(math_comp))
        self.wait(2.66)

        # Kapanış ve CTA (7 kelime)
        self.wait(1.5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        cta = Tex(r"Maarif Matematik ile\\mantığını kavra,\\takipte kal!", color=BLACK).scale(1.2)
        self.play(Write(cta))
        self.wait(2.33)
