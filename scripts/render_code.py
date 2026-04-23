from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class MaarifScene(Scene):
    def construct(self):
        # Objelerin Oluşturulması
        title = Text("Birim Kesirler", font="DejaVu Sans", color=YELLOW)
        question = Text("Payda büyüdükçe kesir küçülür", font="DejaVu Sans", color=WHITE)
        
        # 1/2 Kesir Modeli
        circle1 = Circle(radius=1.5, color=WHITE)
        line1 = Line(circle1.get_top(), circle1.get_bottom(), color=WHITE)
        lines1 = VGroup(line1)
        sector1 = Sector(outer_radius=1.5, angle=PI, start_angle=PI/2, color=BLUE, fill_opacity=0.7)
        label1 = MathTex(r"\frac{1}{2}").scale(2)
        pizza1_group = VGroup(circle1, lines1, sector1)
        group1 = VGroup(pizza1_group, label1).arrange(RIGHT, buff=2.5)

        # 1/4 Kesir Modeli
        circle2 = Circle(radius=1.5, color=WHITE)
        line2_v = Line(circle2.get_top(), circle2.get_bottom(), color=WHITE)
        line2_h = Line(circle2.get_left(), circle2.get_right(), color=WHITE)
        lines2 = VGroup(line2_v, line2_h)
        sector2 = Sector(outer_radius=1.5, angle=PI/2, start_angle=PI/2, color=RED, fill_opacity=0.7)
        label2 = MathTex(r"\frac{1}{4}").scale(2)
        pizza2_group = VGroup(circle2, lines2, sector2)
        group2 = VGroup(pizza2_group, label2).arrange(RIGHT, buff=2.5)

        conclusion = Text("Daha fazla parça daha küçük dilim", font="DejaVu Sans", color=GREEN)

        # Hizalama ve Ölçeklendirme Zırhı
        main_group = VGroup(title, question, group1, group2, conclusion).arrange(DOWN, buff=1.8)
        main_group.scale_to_fit_width(6.0)

        # Animasyon ve Senkronizasyon (Kelime / 3.0)
        # "Merhaba, Maarif Matematik’e hoş geldiniz." (5 kelime -> 1.67s)
        self.play(Write(title))
        self.wait(1.67)

        # "Birim kesirlerde payda büyüdükçe kesrin değeri neden küçülür?" (8 kelime -> 2.67s)
        self.play(Write(question))
        self.wait(2.67)

        # "Bir pastayı ikiye bölelim ve bir dilimini alalım. Bu ikide birdir." (11 kelime -> 3.67s)
        self.play(Create(circle1), Create(lines1)) # Bütünün kaça bölündüğü önce çizilir
        self.play(FadeIn(sector1))
        self.play(Write(label1))
        self.wait(3.67)

        # "Şimdi aynı pastayı dörde bölelim ve yine bir dilim alalım. Bu da dörtte birdir." (14 kelime -> 4.67s)
        self.play(Create(circle2), Create(lines2)) # Bütünün kaça bölündüğü önce çizilir
        self.play(FadeIn(sector2))
        self.play(Write(label2))
        self.wait(4.67)

        # "Gördüğünüz gibi, parça sayısı arttıkça size düşen dilim küçülüyor." (9 kelime -> 3.0s)
        self.play(Indicate(sector1, color=YELLOW), Indicate(sector2, color=YELLOW))
        self.wait(3.0)

        # "Yani paydası büyük olan birim kesir daha küçüktür." (8 kelime -> 2.67s)
        self.play(Write(conclusion))
        self.wait(2.67)

        # "Bir sonraki derste görüşmek üzere, hoşça kalın." (7 kelime -> 2.33s)
        self.play(FadeOut(main_group))
        outro = Text("Hoşça kalın", font="DejaVu Sans", color=YELLOW)
        outro.scale_to_fit_width(6.0)
        self.play(Write(outro))
        self.wait(2.33)

        # Kapanış Sabitleme
        self.wait(5)
