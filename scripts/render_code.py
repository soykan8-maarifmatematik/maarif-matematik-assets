from manim import *
import numpy as np

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        title = Text("Kesirler: Pay ve Payda", font="Sans", color="#333333").scale(0.9)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title))

        subtitle_box = Rectangle(width=13, height=1.2, color="#87CEEB", fill_opacity=0.2, stroke_width=2)
        subtitle_box.to_edge(DOWN, buff=0.8)
        
        def update_subtitle(text):
            new_text = Text(text, font="Sans", color="#333333").scale(0.45)
            new_text.move_to(subtitle_box.get_center())
            return new_text

        subtitle_text = update_subtitle("Merhaba! Bugün kesirlerin ne olduğunu ve nasıl okunduğunu öğreneceğiz.")
        self.play(FadeIn(subtitle_box), Write(subtitle_text))
        self.wait(2)

        circle = Circle(radius=1.5, color="#333333", stroke_width=4)
        circle.move_to(main_center + RIGHT * 2.5 + UP * 0.5)
        
        new_sub = update_subtitle("Kesir, bir bütünün eş parçalara bölünmesiyle elde edilen parçaları ifade eder.")
        self.play(Transform(subtitle_text, new_sub), Create(circle))
        self.wait(2)

        sector1 = Sector(outer_radius=1.5, angle=PI/2, start_angle=0, color="#FFFFFF", fill_opacity=1, stroke_color="#333333", stroke_width=2)
        sector2 = Sector(outer_radius=1.5, angle=PI/2, start_angle=PI/2, color="#FFFFFF", fill_opacity=1, stroke_color="#333333", stroke_width=2)
        sector3 = Sector(outer_radius=1.5, angle=PI/2, start_angle=PI, color="#FFFFFF", fill_opacity=1, stroke_color="#333333", stroke_width=2)
        sector4 = Sector(outer_radius=1.5, angle=PI/2, start_angle=3*PI/2, color="#FFFFFF", fill_opacity=1, stroke_color="#333333", stroke_width=2)
        
        sectors = VGroup(sector1, sector2, sector3, sector4)
        sectors.move_to(main_center + RIGHT * 2.5 + UP * 0.5)

        new_sub = update_subtitle("Bütünümüzü 4 eşit parçaya bölelim. Bu toplam parça sayısına 'Payda' diyoruz.")
        self.play(Transform(subtitle_text, new_sub), FadeIn(sectors))
        self.remove(circle)
        self.wait(2)

        payda = Text("4", font="Sans", color="#E74C3C").scale(1.5)
        payda_label = Text("Payda (Toplam Parça)", font="Sans", color="#E74C3C").scale(0.5)
        
        line = Line(LEFT, RIGHT, color="#333333").set_length(1.5)
        cizgi_label = Text("Kesir Çizgisi", font="Sans", color="#333333").scale(0.4)
        
        pay = Text("3", font="Sans", color="#2ECC71").scale(1.5)
        pay_label = Text("Pay (Alınan Parça)", font="Sans", color="#2ECC71").scale(0.5)

        fraction_group = VGroup(pay, line, payda).arrange(DOWN, buff=0.3)
        fraction_group.move_to(main_center + LEFT * 2.5 + UP * 0.5)
        
        payda_label.next_to(payda, DOWN, buff=0.2)
        cizgi_label.next_to(line, LEFT, buff=0.3)
        pay_label.next_to(pay, UP, buff=0.2)

        self.play(Write(payda), Write(payda_label))
        self.wait(1)
        self.play(Create(line), Write(cizgi_label))
        self.wait(1)

        new_sub = update_subtitle("Şimdi bu 4 parçadan 3 tanesini alalım. Aldığımız parça sayısına 'Pay' denir.")
        self.play(Transform(subtitle_text, new_sub))
        
        self.play(
            sector1.animate.set_color("#87CEEB").set_stroke("#333333", 2),
            sector2.animate.set_color("#87CEEB").set_stroke("#333333", 2),
            sector3.animate.set_color("#87CEEB").set_stroke("#333333", 2)
        )
        
        self.play(Write(pay), Write(pay_label))
        self.wait(2)

        new_sub = update_subtitle("Kesirleri iki farklı şekilde okuyabiliriz: Yukarıdan aşağıya veya aşağıdan yukarıya.")
        self.play(Transform(subtitle_text, new_sub))
        self.wait(2)

        reading1 = Text("1. Okunuş: Üç bölü dört", font="Sans", color="#333333").scale(0.6)
        reading2 = Text("2. Okunuş: Dörtte üç", font="Sans", color="#333333").scale(0.6)
        
        readings = VGroup(reading1, reading2).arrange(DOWN, buff=0.4)
        readings.move_to(main_center + DOWN * 1.5)

        new_sub = update_subtitle("Yukarıdan aşağıya okurken önce pay, sonra 'bölü', sonra payda söylenir: 'Üç bölü dört'.")
        self.play(Transform(subtitle_text, new_sub), Write(reading1))
        self.wait(2)

        new_sub = update_subtitle("Aşağıdan yukarıya okurken önce payda, sonra 'de/da' eki, sonra pay söylenir: 'Dörtte üç'.")
        self.play(Transform(subtitle_text, new_sub), Write(reading2))
        self.wait(3)

        new_sub = update_subtitle("Tebrikler! Kesirlerin temel yapısını ve nasıl okunduğunu harika bir şekilde öğrendiniz.")
        self.play(Transform(subtitle_text, new_sub))
        self.wait(3)
