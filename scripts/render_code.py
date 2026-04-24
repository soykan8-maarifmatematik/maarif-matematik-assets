from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # 1. Merhaba, Maarif Matematik’e hoş geldiniz. (5 kelime -> 1.66s)
        title = Text("Maarif Matematik", font="DejaVu Sans", color=YELLOW).scale_to_fit_width(6.0)
        self.play(Write(title), run_time=1.0)
        self.wait(0.66)

        # 2. Birim kesirlerde payda büyüdükçe kesrin değeri neden küçülür? (8 kelime -> 2.66s)
        q_text = Text("Payda büyüdükçe\ndeğer neden küçülür?", font="DejaVu Sans", color=WHITE).scale_to_fit_width(6.0)
        self.play(FadeOut(title), Write(q_text), run_time=1.0)
        self.wait(1.66)

        # 3. Gelin bunu bir pasta modeliyle mantığına oturtalım. (7 kelime -> 2.33s)
        self.play(FadeOut(q_text), run_time=0.5)
        self.wait(1.83)

        # Görsellerin Hazırlanması
        frac1_vis = VGroup(
            Circle(radius=1.3, color=WHITE),
            Line(UP*1.3, DOWN*1.3, color=WHITE),
            Sector(radius=1.3, angle=PI, start_angle=PI/2, color=BLUE, fill_opacity=0.7)
        )
        frac1_tex = MathTex(r"\frac{1}{2}").scale(2.5)
        g1 = VGroup(frac1_vis, frac1_tex).arrange(RIGHT, buff=1.0)

        frac2_vis = VGroup(
            Circle(radius=1.3, color=WHITE),
            Line(UP*1.3, DOWN*1.3, color=WHITE),
            Line(LEFT*1.3, RIGHT*1.3, color=WHITE),
            Sector(radius=1.3, angle=PI/2, start_angle=0, color=RED, fill_opacity=0.7)
        )
        frac2_tex = MathTex(r"\frac{1}{4}").scale(2.5)
        g2 = VGroup(frac2_vis, frac2_tex).arrange(RIGHT, buff=1.0)

        main_group = VGroup(g1, g2).arrange(DOWN, buff=1.6).move_to(ORIGIN)

        # 4. Elimizde iki aynı boyutta pasta var. (6 kelime -> 2.0s)
        self.play(Create(frac1_vis[0]), Create(frac2_vis[0]), run_time=1.0)
        self.wait(1.0)

        # 5. İlkini iki eş parçaya bölüp birini alalım, bu bir bölü ikidir. (11 kelime -> 3.66s)
        self.play(Create(frac1_vis[1]), run_time=0.5)
        self.play(FadeIn(frac1_vis[2]), run_time=0.5)
        self.play(Write(frac1_tex), run_time=0.5)
        self.wait(2.16)

        # 6. İkincisini dört eş parçaya bölüp birini alalım, bu da bir bölü dörttür. (12 kelime -> 4.0s)
        self.play(Create(VGroup(frac2_vis[1], frac2_vis[2])), run_time=0.5)
        self.play(FadeIn(frac2_vis[3]), run_time=0.5)
        self.play(Write(frac2_tex), run_time=0.5)
        self.wait(2.5)

        # 7. Gördüğünüz gibi ikiye bölünen pastanın dilimi çok daha büyük. (9 kelime -> 3.0s)
        self.play(Indicate(frac1_vis[2], color=YELLOW), run_time=1.0)
        self.wait(2.0)

        # 8. Yani payda parça sayısını gösterir, parça arttıkça dilim ufalır. (9 kelime -> 3.0s)
        conclusion = Text("Parça artar,\ndilim ufalır!", font="DejaVu Sans", color=GREEN).scale_to_fit_width(6.0)
        self.play(FadeOut(main_group), Write(conclusion), run_time=1.0)
        self.wait(2.0)

        # 9. Maarif Matematik ile mantığını kavra, takipte kal! (7 kelime -> 2.33s)
        outro = Text("Maarif Matematik ile\nmantığını kavra,\ntakipte kal!", font="DejaVu Sans", color=YELLOW, t2c={"Maarif Matematik": WHITE}).scale_to_fit_width(6.0)
        self.play(FadeOut(conclusion), Write(outro), run_time=1.0)
        self.wait(1.33)

        # Kapanış Mührü
        self.wait(4.0)