from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Ekran ayarları (Dikey format)
        self.camera.frame_width = 9
        self.camera.frame_height = 16

        # Altyazı fonksiyonu
        subtitle = Text("", font="DejaVu Sans", font_size=36).to_edge(DOWN, buff=1)
        self.add(subtitle)

        def update_sub(text):
            new_sub = Text(text, font="DejaVu Sans", font_size=36).to_edge(DOWN, buff=1)
            subtitle.become(new_sub)

        # 1. GİRİŞ (5 kelime -> 1.67 sn)
        update_sub("Merhaba, Maarif Matematik'e hoş geldiniz.")
        self.wait(1.67)

        # 2. KANCA (8 kelime -> 2.67 sn)
        update_sub("Birim kesirlerde payda büyüdükçe kesrin değeri neden küçülür?")
        self.wait(2.67)

        # Temel objelerin oluşturulması ve dikey istiflenmesi
        circle1 = Circle(radius=1.5, color=WHITE)
        label1 = MathTex(r"\frac{1}{2}", font_size=72)
        group1 = VGroup(label1, circle1).arrange(DOWN, buff=0.5)

        circle2 = Circle(radius=1.5, color=WHITE)
        label2 = MathTex(r"\frac{1}{10}", font_size=72)
        group2 = VGroup(label2, circle2).arrange(DOWN, buff=0.5)

        pizzas = VGroup(group1, group2).arrange(DOWN, buff=1.2).shift(UP*0.5)

        # Çember merkezlerine göre çizgi ve dilimlerin ayarlanması
        line1 = Line(circle1.get_top(), circle1.get_bottom(), color=WHITE)
        sector1 = Sector(radius=1.5, angle=PI, start_angle=PI/2, color=YELLOW, fill_opacity=0.7, arc_center=circle1.get_center())

        lines2 = VGroup()
        for i in range(5):
            angle = i * PI / 5 + PI/2
            start = circle2.get_center() + np.array([np.cos(angle), np.sin(angle), 0]) * 1.5
            end = circle2.get_center() + np.array([np.cos(angle + PI), np.sin(angle + PI), 0]) * 1.5
            lines2.add(Line(start, end, color=WHITE))
        
        sector2 = Sector(radius=1.5, angle=TAU/10, start_angle=PI/2, color=RED, fill_opacity=0.7, arc_center=circle2.get_center())

        # 3. PİZZA 1/2 (12 kelime -> 4.0 sn)
        update_sub("Bunu bir pizza ile düşünelim. Bir pizzayı ikiye bölersek, yarım pizza yeriz.")
        self.play(Create(circle1), Write(label1), run_time=1.0)
        self.play(Create(line1), run_time=1.0)
        self.play(FadeIn(sector1), run_time=1.0)
        self.wait(1.0)

        # 4. PİZZA 1/10 (9 kelime -> 3.0 sn)
        update_sub("Ama aynı pizzayı on parçaya bölersek, dilimler küçücük kalır.")
        self.play(Create(circle2), Write(label2), run_time=0.5)
        self.play(Create(lines2), run_time=1.0)
        self.play(FadeIn(sector2), run_time=0.5)
        self.wait(1.0)

        # 5. SONUÇ (9 kelime -> 3.0 sn)
        update_sub("Yani payda parça sayısını gösterir, parça arttıkça dilim ufalır.")
        self.play(Indicate(sector1, color=YELLOW), Indicate(sector2, color=RED), run_time=1.5)
        self.wait(1.5)

        # 6. ÇIKIŞ (7 kelime -> 2.33 sn)
        update_sub("Bir sonraki derste görüşmek üzere, hoşça kalın.")
        outro_text = Text("Maarif Matematik", font="DejaVu Sans", font_size=60, color=YELLOW).move_to(pizzas.get_center())
        self.play(FadeOut(pizzas), FadeOut(sector1), FadeOut(sector2), FadeOut(line1), FadeOut(lines2), FadeIn(outro_text), run_time=1.0)
        self.wait(1.33)

        # Kapanış yazısı çivili kalır
        self.wait(5)