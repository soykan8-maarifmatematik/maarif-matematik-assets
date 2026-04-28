from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class BirimKesirler(Scene):
    def construct(self):
        # Arka plan
        self.camera.background_color = "#FFFFFF"

        # Başlık (UP, buff=2.0, scale=1.2)
        title = Tex("Birim Kesirler", color=BLACK).scale(1.2).to_edge(UP, buff=2.0)

        # Modeller (Pizzalar)
        # 1/2
        c1_outline = Circle(radius=1.2, color=BLACK)
        s1 = Sector(outer_radius=1.2, angle=PI, color=BLUE, fill_opacity=0.7)
        t1 = MathTex(r"\frac{1}{2}", color=BLACK).scale(1.5).next_to(c1_outline, DOWN)
        g1 = VGroup(c1_outline, s1, t1)

        # 1/10
        c2_outline = Circle(radius=1.2, color=BLACK)
        s2 = Sector(outer_radius=1.2, angle=TAU/10, color=RED, fill_opacity=0.7)
        lines = VGroup(*[Line(ORIGIN, [1.2*np.cos(i*TAU/10), 1.2*np.sin(i*TAU/10), 0], color=BLACK) for i in range(10)])
        t2 = MathTex(r"\frac{1}{10}", color=BLACK).scale(1.5).next_to(c2_outline, DOWN)
        g2 = VGroup(c2_outline, s2, lines, t2)

        circles_group = VGroup(g1, g2).arrange(RIGHT, buff=1.0)

        # Kural Yazısı
        rule_text = Tex(r"Payda Büyür $\rightarrow$ Dilim Küçülür", color=BLACK).scale(1.2)

        # Merkezi Yerleşim (arrange DOWN buff=2.5)
        main_group = VGroup(circles_group, rule_text).arrange(DOWN, buff=2.5)
        main_group.move_to(ORIGIN)

        # Animasyonlar ve Senkronizasyon
        # "Merhaba, Maarif Matematik’e hoş geldiniz." (6 kelime -> 2.0 sn)
        self.play(Write(title))
        self.wait(2.0)

        # "Birim kesirleri sıralarken kafan mı karışıyor? Hemen halledelim." (8 kelime -> 2.6 sn)
        self.wait(2.6)

        # "Bir pizzayı düşünün. İki kişiye bölerseniz mi daha çok yersiniz, yoksa on kişiye bölerseniz mi?" (15 kelime -> 5.0 sn)
        self.play(FadeIn(circles_group))
        self.wait(5.0)

        # "Tabii ki iki kişiye böldüğünüzde! Yani payda büyüdükçe, dilim küçülür." (10 kelime -> 3.3 sn)
        self.play(Write(rule_text))
        self.wait(3.3)

        # "Bu yüzden bir bölü iki, bir bölü ondan daha büyüktür." (10 kelime -> 3.3 sn)
        comparison = MathTex(r"\frac{1}{2} > \frac{1}{10}", color=BLACK).scale(2.0)
        comparison.move_to(rule_text.get_center())
        self.play(ReplacementTransform(rule_text, comparison))
        self.wait(3.3)

        # Son cümle bittikten sonra + 1.5 saniye bekle
        self.wait(1.5)

        # FadeOut(all) ve Kapanış (CTA)
        self.play(FadeOut(Group(*self.mobjects)))
        
        # "Maarif Matematik ile mantığını kavra, takipte kal!" (7 kelime -> 2.3 sn)
        cta = VGroup(
            Tex("Maarif Matematik ile", color=BLACK),
            Tex("mantığını kavra,", color=BLACK),
            Tex("takipte kal!", color=BLACK)
        ).arrange(DOWN, buff=0.5).scale(1.2)
        self.play(Write(cta))
        self.wait(2.3)