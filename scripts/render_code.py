from manim import *
import numpy as np

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        title = Text("Kesir Nedir?", font="Sans", color="#333333", font_size=48)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title))

        subtitle_box = Text("Merhaba! Bugün kesirleri öğreneceğiz.", font="Sans", color="#333333", font_size=24)
        subtitle_box.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(subtitle_box))

        def update_subtitle(text):
            new_sub = Text(text, font="Sans", color="#333333", font_size=24).to_edge(DOWN, buff=0.8)
            self.play(Transform(subtitle_box, new_sub))

        circle = Circle(radius=1.5, color="#333333", stroke_width=4)
        lines = VGroup(
            Line(circle.get_top(), circle.get_bottom(), color="#333333"),
            Line(circle.get_left(), circle.get_right(), color="#333333")
        )
        pie = VGroup(circle, lines).move_to(main_center + LEFT * 3)

        update_subtitle("Bir bütünü 4 eş parçaya bölelim. Bu toplam parça sayısıdır.")
        self.play(Create(circle))
        self.play(Create(lines))

        sectors = VGroup()
        angles = [0, PI/2, PI, 3*PI/2]
        for i in range(3):
            sector = Sector(outer_radius=1.5, angle=PI/2, start_angle=angles[i], color="#87CEEB", fill_opacity=0.8)
            sectors.add(sector)
        sectors.move_to(pie.get_center())

        update_subtitle("Bu parçalardan 3 tanesini alalım.")
        self.play(FadeIn(sectors))
        self.bring_to_front(lines)
        self.bring_to_front(circle)

        update_subtitle("Şimdi bunu kesir olarak yazalım.")
        num = Text("3", font="Sans", color="#2ECC71", font_size=72)
        line = Line(LEFT*0.6, RIGHT*0.6, color="#333333", stroke_width=6)
        den = Text("4", font="Sans", color="#E74C3C", font_size=72)
        
        frac_group = VGroup(num, line, den).arrange(DOWN, buff=0.3).move_to(main_center + RIGHT * 2)
        
        self.play(Write(line))
        
        update_subtitle("Bütünün kaç parçaya bölündüğünü alta yazarız. Buna 'Payda' denir.")
        self.play(Write(den))
        den_label = Text("Payda", font="Sans", color="#E74C3C", font_size=24).next_to(den, RIGHT, buff=0.5)
        self.play(Write(den_label))

        update_subtitle("Kaç parça aldığımızı üste yazarız. Buna 'Pay' denir.")
        self.play(Write(num))
        num_label = Text("Pay", font="Sans", color="#2ECC71", font_size=24).next_to(num, RIGHT, buff=0.5)
        self.play(Write(num_label))
        self.wait(1)

        update_subtitle("Ortadaki çizgiye ise 'Kesir Çizgisi' adı verilir.")
        line_label = Text("Kesir Çizgisi", font="Sans", color="#333333", font_size=24).next_to(line, RIGHT, buff=0.5)
        self.play(Write(line_label))
        self.wait(1)

        self.play(FadeOut(num_label), FadeOut(den_label), FadeOut(line_label))

        update_subtitle("Bu kesri iki farklı şekilde okuyabiliriz.")
        read1 = Text("1. Okunuş: Üç bölü dört", font="Sans", color="#333333", font_size=32).move_to(main_center + RIGHT * 2 + UP * 1.5)
        read2 = Text("2. Okunuş: Dörtte üç", font="Sans", color="#333333", font_size=32).next_to(read1, DOWN, buff=0.5)

        update_subtitle("Yukarıdan aşağıya doğru okurken: 'Üç bölü dört'")
        self.play(Write(read1))
        self.wait(1)

        update_subtitle("Aşağıdan yukarıya doğru okurken: 'Dörtte üç'")
        self.play(Write(read2))
        self.wait(2)

        update_subtitle("Tebrikler! Kesirlerin temel kavramlarını ve okunuşunu öğrendiniz.")
        self.wait(2)