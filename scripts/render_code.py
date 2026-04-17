from manim import *
import numpy as np

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        # Başlık
        title = Text("Kesir Nedir?", color="#333333", font_size=48, weight=BOLD)
        title.to_edge(UP, buff=0.7)

        # Kesir ve Etiketler
        fraction = MathTex(r"\frac{3}{4}", color="#333333", font_size=96)
        
        pay_text = Text("Pay: Alınan miktar", color="#87CEEB", font_size=24)
        payda_text = Text("Payda: Toplam eş parça", color="#333333", font_size=24)
        
        labels = VGroup(pay_text, fraction, payda_text).arrange(DOWN, buff=0.5)

        # Görsel Model (4 eş parça, 3'ü boyalı)
        rects = VGroup(*[Square(side_length=1.0, stroke_color="#333333", stroke_width=2, fill_color="#FFFFFF", fill_opacity=1) for _ in range(4)])
        rects.arrange(RIGHT, buff=0)
        for i in range(3):
            rects[i].set_fill(color="#87CEEB", opacity=0.8)

        # Okunuşlar
        read1 = Text("Yukarıdan Aşağıya: '3 bölü 4' (Bölme Mantığı)", color="#333333", font_size=24)
        read2 = Text("Aşağıdan Yukarıya: '4'te 3' (Parça-Bütün Mantığı)", color="#333333", font_size=24)
        reads = VGroup(read1, read2).arrange(DOWN, buff=0.3)

        # Ana grubu oluşturma ve merkeze sabitleme
        main_group = VGroup(labels, rects, reads).arrange(DOWN, buff=0.8)
        main_group.move_to(main_center)

        # Animasyonlar
        self.play(Write(title))
        self.play(Write(fraction))
        self.wait(1)
        self.play(Write(payda_text))
        self.wait(1)
        self.play(Write(pay_text))
        self.wait(1)
        self.play(Create(rects))
        self.wait(1)
        self.play(Write(reads))
        self.wait(2)
