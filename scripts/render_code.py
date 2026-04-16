from manim import *
import numpy as np

class MaarifScene(Scene):
    def construct(self):
        # 2. Ekran Düzeni ve Koordinatlar - Arka Plan
        self.camera.background_color = "#FFFFFF"
        
        # Ana Merkez Tanımı
        main_center = DOWN * 0.5

        # Başlık
        title = Text("Kesir Nedir? Pay ve Payda", font="Sans", color="#333333").scale(0.8)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title))

        # Altyazı Kutusu
        subtitle_box = Rectangle(width=12, height=1.2, color="#333333", fill_color="#333333", fill_opacity=0.05)
        subtitle_box.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(subtitle_box))

        # Görselleştirme: 4 parçaya bölünmüş bütün, 3'ü boyalı
        squares = VGroup(*[Square(side_length=1.0, color="#333333", stroke_width=2) for _ in range(4)])
        squares.arrange(RIGHT, buff=0.1)
        
        # 3. Renk Paleti Kullanımı
        for i in range(3):
            squares[i].set_fill("#87CEEB", opacity=1) # Maarif Mavisi
        squares[3].set_fill("#FFFFFF", opacity=1)

        # Kesir İfadeleri
        num = Text("3", font="Sans", color="#2ECC71") # Yeşil: Pay
        line = Line(LEFT, RIGHT, color="#333333").set_length(1.5) # Koyu Gri: Kesir Çizgisi
        den = Text("4", font="Sans", color="#E74C3C") # Kırmızı: Payda
        fraction = VGroup(num, line, den).arrange(DOWN, buff=0.2)

        # Etiketler
        pay_label = Text("<- Pay (Seçilen Parça)", font="Sans", color="#2ECC71").scale(0.5)
        payda_label = Text("<- Payda (Bütünün Parçaları)", font="Sans", color="#E74C3C").scale(0.5)
        line_label = Text("Kesir Çizgisi ->", font="Sans", color="#333333").scale(0.5)

        pay_label.next_to(num, RIGHT, buff=0.5)
        payda_label.next_to(den, RIGHT, buff=0.5)
        line_label.next_to(line, LEFT, buff=0.5)
        
        fraction_with_labels = VGroup(fraction, pay_label, payda_label, line_label)

        # Tüm objeleri main_center'a göre konumlandırma ve sabitleme
        center_group = VGroup(squares, fraction_with_labels).arrange(DOWN, buff=0.8)
        center_group.move_to(main_center)

        # Animasyonları Oynatma
        self.play(FadeIn(squares))
        self.wait(1)
        
        self.play(Write(fraction))
        self.wait(1)
        
        self.play(Write(pay_label))
        self.play(Write(payda_label))
        self.play(Write(line_label))
        self.wait(2)

        # Okunuşlar (Altyazı kutusunun içinde)
        read_1 = Text("Okunuşu 1: Üç bölü dört (a bölü b formatı)", font="Sans", color="#333333").scale(0.6)
        read_1.move_to(subtitle_box.get_center())
        self.play(Write(read_1))
        self.wait(2)

        read_2 = Text("Okunuşu 2: Dörtte üç (b'de a formatı)", font="Sans", color="#333333").scale(0.6)
        read_2.move_to(subtitle_box.get_center())
        self.play(ReplacementTransform(read_1, read_2))
        self.wait(3)
