from manim import *

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_width = 9
config.frame_height = 16

class BirimKesirKarsilastirma(Scene):
    def construct(self):
        # Arka Plan
        self.camera.background_color = "#F8F9FA"
        
        # 1. BAŞLIK (V18 Sabit - En Üst)
        header = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", color=BLACK, weight=BOLD)
        header.to_edge(UP, buff=0.8).scale_to_fit_width(8.5)
        
        # 2. MODELLER (V18 Sabit - Orta Üst)
        # Daire 1 (1/3)
        c1_slices = VGroup()
        angle1 = TAU / 3
        for i in range(3):
            fill_color = "#FF5722" if i == 0 else WHITE
            slice_obj = Sector(
                radius=1.3,
                angle=angle1,
                start_angle=PI/2 + i * angle1,
                fill_color=fill_color,
                fill_opacity=1.0,
                stroke_width=4,
                stroke_color=BLACK
            )
            c1_slices.add(slice_obj)
            
        label1 = MathTex(r"\frac{1}{3}", color=BLACK).scale(2.5)
        label1.next_to(c1_slices, DOWN, buff=0.6)
        group1 = VGroup(c1_slices, label1)
        
        # Daire 2 (1/5)
        c2_slices = VGroup()
        angle2 = TAU / 5
        for i in range(5):
            fill_color = "#03A9F4" if i == 0 else WHITE
            slice_obj = Sector(
                radius=1.3,
                angle=angle2,
                start_angle=PI/2 + i * angle2,
                fill_color=fill_color,
                fill_opacity=1.0,
                stroke_width=4,
                stroke_color=BLACK
            )
            c2_slices.add(slice_obj)
            
        label2 = MathTex(r"\frac{1}{5}", color=BLACK).scale(2.5)
        label2.next_to(c2_slices, DOWN, buff=0.6)
        group2 = VGroup(c2_slices, label2)
        
        # Karşılaştırma Sembolü
        symbol = MathTex(">", color=BLACK).scale(4)
        
        # Konumlandırma (VGroup ile birleştirip UP * 1.2'ye taşıma)
        models_group = VGroup(group1, symbol, group2).arrange(RIGHT, buff=0.8)
        models_group.move_to(UP * 1.2)
        
        # 3. AÇIKLAMA (V18 Sabit - En Alt)
        desc_text = "Paydası küçük olan\nbirim kesir daha büyüktür!"
        description = Text(desc_text, color=BLACK, weight=BOLD)
        description.move_to(DOWN * 3.5).scale_to_fit_width(7.5)
        
        # --- ANİMASYON SIRALAMASI (V19 HAREKETLİ ÇİZİM YASASI) ---
        
        self.play(Write(header))
        self.wait(0.5)
        
        # Önce birinci dairenin dilimleri tek tek çizilir
        for slice_obj in c1_slices:
            self.play(Create(slice_obj), run_time=0.4)
        self.play(Write(label1))
        self.wait(0.5)
        
        # Sonra ikinci dairenin dilimleri tek tek çizilir
        for slice_obj in c2_slices:
            self.play(Create(slice_obj), run_time=0.3)
        self.play(Write(label2))
        self.wait(0.5)
        
        # En son karşılaştırma sembolü görünür
        self.play(Write(symbol), run_time=0.8)
        self.wait(0.5)
        
        # Açıklama metni ekrana gelir
        self.play(Write(description))
        self.wait(2)
