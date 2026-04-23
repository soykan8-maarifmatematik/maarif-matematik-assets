from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class MaarifScene(Scene):
    def construct(self):
        # Objeleri oluşturma ve Türkçe karakter / Font ayarları
        title = Text("Birim Kesirler", font="DejaVu Sans", color=BLUE)
        question = Text("Payda büyüdükçe değer küçülür", font="DejaVu Sans", color=WHITE)
        
        # 1/2 Modeli (Pizza 1)
        circle1 = Circle(radius=1.0, color=WHITE)
        lines1 = VGroup(Line(circle1.get_top(), circle1.get_bottom()))
        sector1 = Sector(outer_radius=1.0, angle=PI, start_angle=PI/2, color=YELLOW, fill_opacity=0.7)
        label1 = MathTex(r"\frac{1}{2}").scale(1.5)
        pizza1_visual = VGroup(circle1, lines1, sector1)
        pizza1_group = VGroup(pizza1_visual, label1).arrange(DOWN, buff=0.5)

        # 1/4 Modeli (Pizza 2)
        circle2 = Circle(radius=1.0, color=WHITE)
        lines2 = VGroup(Line(circle2.get_top(), circle2.get_bottom()), Line(circle2.get_left(), circle2.get_right()))
        sector2 = Sector(outer_radius=1.0, angle=PI/2, start_angle=PI/2, color=ORANGE, fill_opacity=0.7)
        label2 = MathTex(r"\frac{1}{4}").scale(1.5)
        pizza2_visual = VGroup(circle2, lines2, sector2)
        pizza2_group = VGroup(pizza2_visual, label2).arrange(DOWN, buff=0.5)

        comparison = MathTex(r"\frac{1}{2} > \frac{1}{4}", color=GREEN).scale(1.5)

        # Hizalama ve Ölçeklendirme Koruması (Zırh V4.4)
        main_group = VGroup(title, question, pizza1_group, pizza2_group, comparison).arrange(DOWN, buff=1.8)
        main_group.scale_to_fit_width(6.0)
        main_group.move_to(ORIGIN)

        # Animasyonlar ve Milimetrik Senkronizasyon (Hız: 3.0 kelime/sn)
        
        # "Merhaba, Maarif Matematik’e hoş geldiniz." (5 kelime -> 1.67s)
        self.play(Write(title), run_time=1.0)
        self.wait(0.67)

        # "Birim kesirlerde payda büyüdükçe kesrin değeri neden küçülür?" (8 kelime -> 2.67s)
        self.play(Write(question), run_time=1.5)
        self.wait(1.17)

        # "Bir pizzayı iki eş parçaya bölelim ve bir dilim alalım. Bu ikide birdir." (13 kelime -> 4.33s)
        # Görsel İspat: Boyalı dilimden ÖNCE bütünün kaça bölündüğünü gösteren çizgiler çizilir.
        self.play(Create(circle1), Create(lines1), run_time=1.5)
        self.play(FadeIn(sector1), Write(label1), run_time=1.5)
        self.wait(1.33)

        # "Şimdi aynı pizzayı dört eş parçaya bölelim ve yine bir dilim alalım. Bu da dörtte birdir." (16 kelime -> 5.33s)
        self.play(Create(circle2), Create(lines2), run_time=1.5)
        self.play(FadeIn(sector2), Write(label2), run_time=1.5)
        self.wait(2.33)

        # "Gördüğünüz gibi, parça sayısı arttıkça size düşen dilim küçülüyor." (9 kelime -> 3.0s)
        self.play(Indicate(sector1), Indicate(sector2), run_time=1.5)
        self.wait(1.5)

        # "Yani ikide bir, dörtte birden daha büyüktür." (7 kelime -> 2.33s)
        self.play(Write(comparison), run_time=1.0)
        self.wait(1.33)

        # "Bir sonraki derste görüşmek üzere, hoşça kalın." (7 kelime -> 2.33s)
        outro = Text("Hoşça kalın", font="DejaVu Sans", color=BLUE).move_to(comparison.get_center())
        self.play(Transform(comparison, outro), run_time=1.0)
        self.wait(1.33)

        # Kapanış Sabitleme
        self.wait(5)
