from manim import *
import numpy as np

# Maarif Matematik - Hata Giderilmiş Master Sahne
class MaarifScene(Scene):
    def construct(self):
        # 1. Sahne Ayarları
        self.camera.background_color = "#FFFFFF"
        dark_grey = "#333333"
        maarif_blue = "#87CEEB"
        maarif_red = "#FF0000"
        
        main_center = DOWN * 0.5

        # 2. Başlık
        title = Text("Kesir Kavramı: Pay ve Payda", color=dark_grey).scale(0.8)
        title.to_edge(UP, buff=0.7)
        
        # 3. Kesir Modeli (Daire)
        whole = Circle(radius=1.8, color=dark_grey, stroke_width=4).move_to(main_center)
        lines = VGroup(
            Line(whole.get_left(), whole.get_right(), color=dark_grey),
            Line(whole.get_top(), whole.get_bottom(), color=dark_grey)
        ).move_to(whole)
        
        # 4. Kesir Yazısı (MathTex her zaman daha güvenlidir)
        fraction = MathTex(r"\frac{3}{4}", color=dark_grey).scale(2).next_to(whole, RIGHT, buff=1.2)
        num = fraction[0][0] # 3
        den = fraction[0][2] # 4

        # 5. Etiketler (Hata veren kısım düzeltildi)
        # Çoklu satır yerine tekli Text objeleri kullanarak riski sıfırlıyoruz
        pay_label = Text("Pay (Alınan Parça)", color=maarif_blue).scale(0.5)
        pay_label.next_to(fraction, UP, buff=0.8)
        
        payda_label = Text("Payda (Eş Parça Sayısı)", color=maarif_red).scale(0.5)
        payda_label.next_to(fraction, DOWN, buff=0.8)

        # --- Animasyon Akışı ---
        self.play(Write(title))
        self.wait(1)
        
        self.play(Create(whole), Create(lines))
        self.wait(2)
        
        # Birim parçaları boya (Örnek: 3 parça)
        slices = VGroup(*[
            Sector(radius=1.8, angle=90*DEGREES, start_angle=i*90*DEGREES, 
                   color=maarif_blue, fill_opacity=0.7).move_to(whole)
            for i in range(3)
        ])
        
        self.play(FadeIn(slices), Write(fraction))
        self.wait(1)
        
        # Pay ve Payda Vurgusu
        self.play(Indicate(num), Write(pay_label))
        self.wait(2)
        self.play(Indicate(den), Write(payda_label))
        self.wait(4)
        
        # Kapanış
        self.play(FadeOut(VGroup(whole, lines, slices, fraction, pay_label, payda_label, title)))
        outro = Text("Bir sonraki derste görüşmek üzere,\nhoşça kalın.", color=maarif_blue).scale(0.7)
        self.play(Write(outro))
        self.wait(2)
