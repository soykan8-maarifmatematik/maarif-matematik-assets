from manim import *
import numpy as np

class MaarifScene(Scene):
    def construct(self):
        # Arka Plan
        self.camera.background_color = "#FFFFFF"
        
        # Ana Merkez
        main_center = DOWN * 0.5
        
        # Baslik
        title = Text("Kesirler: Pay, Payda ve Okunus", font="Sans", color="#333333", font_size=40)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title))
        
        # Altyazi Kutusu
        subtitle_box = Rectangle(width=12, height=1.2, color="#87CEEB", fill_color="#FFFFFF", fill_opacity=1)
        subtitle_box.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(subtitle_box))
        
        subtitle_text = Text("Kesirler, bir butunun es parcalarindan kacinin alindigini gosterir.", font="Sans", color="#333333", font_size=24)
        subtitle_text.move_to(subtitle_box.get_center())
        self.play(Write(subtitle_text))
        
        # Objeleri gruplayip merkeze sabitlemek icin ana grup
        content_group = VGroup()
        
        # Kesir: 3/4
        num = Text("3", font="Sans", color="#E74C3C", font_size=60)
        line = Line(LEFT, RIGHT, color="#333333").scale(0.8)
        den = Text("4", font="Sans", color="#2ECC71", font_size=60)
        fraction = VGroup(num, line, den).arrange(DOWN, buff=0.3)
        
        # Oklar ve Aciklamalar
        num_arrow = Arrow(start=RIGHT, end=LEFT, color="#E74C3C").next_to(num, RIGHT, buff=0.2)
        num_text = Text("Pay: Alinan parca sayisi", font="Sans", color="#E74C3C", font_size=24).next_to(num_arrow, RIGHT, buff=0.2)
        
        line_arrow = Arrow(start=RIGHT, end=LEFT, color="#333333").next_to(line, RIGHT, buff=0.2)
        line_text = Text("Kesir Cizgisi", font="Sans", color="#333333", font_size=24).next_to(line_arrow, RIGHT, buff=0.2)
        
        den_arrow = Arrow(start=RIGHT, end=LEFT, color="#2ECC71").next_to(den, RIGHT, buff=0.2)
        den_text = Text("Payda: Butunun bolundugu es parca sayisi", font="Sans", color="#2ECC71", font_size=24).next_to(den_arrow, RIGHT, buff=0.2)
        
        explanation_group = VGroup(fraction, num_arrow, num_text, line_arrow, line_text, den_arrow, den_text)
        
        # Gorsel Temsil (Dikdortgenler)
        rects = VGroup()
        for i in range(4):
            rect = Rectangle(height=0.8, width=0.8, color="#333333", fill_opacity=0.8)
            if i < 3:
                rect.set_fill("#87CEEB") # Maarif Mavisi (Alinan parcalar)
            else:
                rect.set_fill("#FFFFFF") # Beyaz (Alinmayan parca)
            rects.add(rect)
        rects.arrange(RIGHT, buff=0)
        
        # Okunuslar
        read_1 = Text("1. Okunus: Uc bolu Dort (a bolu b)", font="Sans", color="#333333", font_size=28)
        read_2 = Text("2. Okunus: Dortte Uc (b'de a)", font="Sans", color="#333333", font_size=28)
        readings = VGroup(read_1, read_2).arrange(DOWN, buff=0.3)
        
        # Tum icerikleri dikey olarak sirala ve content_group'a ekle
        content_group.add(explanation_group, rects, readings).arrange(DOWN, buff=0.6)
        
        # Sabitleme: Objeleri main_center'a kilitle
        content_group.move_to(main_center)
        
        # Animasyonlar
        self.play(Write(fraction))
        self.play(GrowArrow(num_arrow), Write(num_text))
        self.play(GrowArrow(line_arrow), Write(line_text))
        self.play(GrowArrow(den_arrow), Write(den_text))
        self.wait(1)
        
        # Altyazi guncelleme
        new_subtitle_1 = Text("Payda butunu, pay ise alinan kismi temsil eder.", font="Sans", color="#333333", font_size=24).move_to(subtitle_box.get_center())
        self.play(Transform(subtitle_text, new_subtitle_1))
        
        self.play(Create(rects))
        self.wait(1)
        
        # Altyazi guncelleme
        new_subtitle_2 = Text("Kesirler iki farkli yonde okunabilir.", font="Sans", color="#333333", font_size=24).move_to(subtitle_box.get_center())
        self.play(Transform(subtitle_text, new_subtitle_2))
        
        self.play(Write(readings))
        self.wait(2)