from manim import *
import numpy as np

# Maarif Matematik Standartlarında Animasyon Dosyası
# Bu dosya Make.com tarafından her yeni derste otomatik güncellenir.

class MaarifScene(Scene):
    def construct(self):
        # 1. Sahne Ayarları ve Renk Paleti (Maarif Standartları)
        self.camera.background_color = "#FFFFFF" # Saf Beyaz Arka Plan
        dark_grey = "#333333"       # Ana Metin Rengi
        maarif_blue = "#87CEEB"     # Vurgu Rengi (Mavi)
        
        # Ana Odak Noktası (Altyazılarla çakışmaması için hafif yukarıda)
        main_center = DOWN * 0.5

        # 2. Başlık Katmanı
        title = Text("Birim Kesirler: Mantık Odaklı Anlatım", font="Sans", color=dark_grey).scale(0.8)
        title.to_edge(UP, buff=0.7)
        
        # 3. Görsel Objeler (Örnek: Birim Kesir Modeli)
        # Bütün (Daire)
        whole = Circle(radius=2, color=dark_grey, stroke_width=4).move_to(main_center)
        
        # Bölme Çizgileri
        lines = VGroup(
            Line(whole.get_left(), whole.get_right(), color=dark_grey),
            Line(whole.get_top(), whole.get_bottom(), color=dark_grey)
        ).move_to(whole)
        
        # Boyalı Birim Parça (1/4)
        unit_slice = Sector(
            radius=2, 
            angle=90*DEGREES, 
            start_angle=90*DEGREES, 
            color=maarif_blue, 
            fill_opacity=0.7
        ).move_to(whole)
        
        # 4. Matematiksel Gösterim
        frac = MathTex(r"\frac{1}{4}", color=maarif_blue).scale(2).next_to(whole, RIGHT, buff=1)

        # --- Animasyon Akışı (Öğretmen Tonunda Senkronize) ---
        
        # Giriş
        self.play(Write(title))
        self.wait(1)
        
        # Bütünü Oluştur
        self.play(Create(whole), Create(lines))
        self.wait(2)
        
        # Parçayı Vurgula
        self.play(FadeIn(unit_slice))
        self.play(Write(frac))
        self.wait(4)
        
        # Kapanış
        self.play(FadeOut(VGroup(whole, lines, unit_slice, frac, title)))
        
        outro_text = Text("Bir sonraki derste görüşmek üzere,\nhoşça kalın.", font="Sans", color=maarif_blue).scale(0.7)
        self.play(Write(outro_text))
        self.wait(2)

# Not: Make.com bu dosyayı güncellerken Gemini'ye 'MaarifScene' ismini 
# kullanmasını talimat verdiğimiz için çakışma yaşanmaz.
