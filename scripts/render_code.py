from manim import *
import numpy as np

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi
        self.camera.background_color = "#FFFFFF"
        
        # Ana merkez noktasi
        main_center = DOWN * 0.5
        
        # Baslik
        title = Text("Kesir Nedir?", font="Sans", color="#333333").scale(1.2)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title))
        
        # Altyazi Kutusu
        subtitle_box = Rectangle(width=12, height=1.2, color="#333333", fill_color="#FFFFFF", fill_opacity=1)
        subtitle_box.to_edge(DOWN, buff=0.8)
        self.add(subtitle_box)
        
        # Kesir Elemanlari
        num = Text("3", font="Sans", color="#E74C3C").scale(1.5)
        line = Line(LEFT, RIGHT, color="#333333").scale(0.6)
        den = Text("4", font="Sans", color="#2ECC71").scale(1.5)
        frac = VGroup(num, line, den).arrange(DOWN, buff=0.2)
        
        pay_label = Text("Pay (Alinan Parca)", font="Sans", color="#E74C3C").scale(0.6)
        pay_label.next_to(num, RIGHT, buff=0.5)
        cizgi_label = Text("Kesir Cizgisi", font="Sans", color="#333333").scale(0.6)
        cizgi_label.next_to(line, RIGHT, buff=0.5)
        payda_label = Text("Payda (Butun)", font="Sans", color="#2ECC71").scale(0.6)
        payda_label.next_to(den, RIGHT, buff=0.5)
        
        frac_group = VGroup(frac, pay_label, cizgi_label, payda_label)
        
        # Gorsel Elemanlar (4 es parca)
        rects = VGroup(*[Rectangle(height=1, width=1, stroke_color="#333333", stroke_width=2) for _ in range(4)])
        rects.arrange(RIGHT, buff=0)
        
        # Okunus Elemanlari
        read1 = Text("Okunusu 1: Uc bolu Dort", font="Sans", color="#333333").scale(0.7)
        read2 = Text("Okunusu 2: Dortte Uc", font="Sans", color="#333333").scale(0.7)
        read_group = VGroup(read1, read2).arrange(DOWN, buff=0.3)
        
        # Tum icerigi ana merkeze gore hizalama ve sabitleme
        all_content = VGroup(frac_group, rects, read_group).arrange(DOWN, buff=0.7)
        all_content.move_to(main_center)
        
        # Animasyonlar
        self.play(Write(frac))
        self.wait(1)
        
        # Payda aciklamasi
        self.play(Write(payda_label))
        self.play(Create(rects))
        self.wait(1)
        
        # Pay aciklamasi
        self.play(Write(pay_label), Write(cizgi_label))
        fills = VGroup(*[Rectangle(height=1, width=1, fill_color="#87CEEB", fill_opacity=1, stroke_width=0).move_to(rects[i]) for i in range(3)])
        self.play(FadeIn(fills))
        self.wait(1)
        
        # Okunuslar
        self.play(Write(read1))
        self.wait(1)
        self.play(Write(read2))
        self.wait(2)
