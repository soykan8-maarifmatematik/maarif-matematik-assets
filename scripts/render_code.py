from manim import *
import numpy as np

class MaarifScene(Scene):
    def construct(self):
        # 1. Arka Plan ve Koordinat Ayarları
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5
        
        # 2. Başlık
        title = Text("Kesirler: Pay ve Payda", font="Sans", color="#333333")
        title.to_edge(UP, buff=0.7)
        
        # 3. Kesir Elemanları
        pay = Text("3", font="Sans", color="#E74C3C")
        cizgi = Line(LEFT, RIGHT, color="#333333").set_length(1.2)
        payda = Text("4", font="Sans", color="#2ECC71")
        kesir = VGroup(pay, cizgi, payda).arrange(DOWN, buff=0.2)
        
        pay_label = Text("<- Pay (Seçilen Parça)", font="Sans", color="#E74C3C").scale(0.5)
        pay_label.next_to(pay, RIGHT, buff=0.2)
        
        payda_label = Text("<- Payda (Toplam Parça)", font="Sans", color="#2ECC71").scale(0.5)
        payda_label.next_to(payda, RIGHT, buff=0.2)
        
        left_group = VGroup(kesir, pay_label, payda_label)
        
        # 4. Görselleştirme (Dikdörtgenler)
        rects = VGroup(*[Rectangle(height=0.8, width=0.8, color="#333333") for _ in range(4)])
        rects.arrange(RIGHT, buff=0)
        
        colored_rects = VGroup(*[Rectangle(height=0.8, width=0.8, color="#333333", fill_color="#87CEEB", fill_opacity=1) for _ in range(3)])
        colored_rects.arrange(RIGHT, buff=0)
        colored_rects.move_to(rects[0:3].get_center())
        
        visual_group = VGroup(rects, colored_rects)
        
        # 5. Okunuşlar
        okunus_title = Text("Nasıl Okunur?", font="Sans", color="#333333").scale(0.6)
        okunus1 = Text("1) Üç bölü dört (Yukarıdan Aşağıya)", font="Sans", color="#E74C3C").scale(0.5)
        okunus2 = Text("2) Dörtte üç (Aşağıdan Yukarıya)", font="Sans", color="#2ECC71").scale(0.5)
        readings = VGroup(okunus_title, okunus1, okunus2).arrange(DOWN, buff=0.2)
        
        right_group = VGroup(visual_group, readings).arrange(DOWN, buff=0.6)
        
        # 6. Ana Merkez Sabitlemesi (Kritik Kural)
        main_content = VGroup(left_group, right_group).arrange(RIGHT, buff=1.0)
        main_content.move_to(main_center)
        
        # 7. Animasyonlar
        self.play(Write(title))
        self.wait(0.5)
        
        # Payda ve Çizgi Animasyonu
        self.play(Create(cizgi))
        self.play(Write(payda))
        self.play(Write(payda_label))
        self.play(Create(rects))
        self.wait(1)
        
        # Pay Animasyonu
        self.play(Write(pay))
        self.play(Write(pay_label))
        self.play(FadeIn(colored_rects))
        self.wait(1)
        
        # Okunuş Animasyonları
        self.play(Write(okunus_title))
        self.wait(0.5)
        
        self.play(Write(okunus1))
        self.wait(1)
        
        self.play(Write(okunus2))
        self.wait(2)
        
        # Kapanış
        self.play(FadeOut(VGroup(title, main_content)))
        self.wait(1)