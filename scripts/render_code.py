from manim import *

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_width = 9
config.frame_height = 16

class BirimKesirler(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # 1. BAŞLIK
        header = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", color=BLACK, font_weight=BOLD)
        header.scale_to_fit_width(8.5)
        header.to_edge(UP, buff=0.8)
        
        # 2. MODELLER
        # 1/3 Modeli
        pie1 = VGroup()
        for i in range(3):
            fill_c = ORANGE if i == 0 else WHITE
            fill_o = 0.6 if i == 0 else 0.0
            slice_1 = Sector(
                radius=1.3, 
                angle=TAU/3, 
                start_angle=i*TAU/3, 
                fill_color=fill_c, 
                fill_opacity=fill_o, 
                stroke_width=4, 
                stroke_color=BLACK
            )
            pie1.add(slice_1)
        
        label1 = MathTex(r"\frac{1}{3}", color=BLACK).scale(2.5).next_to(pie1, DOWN, buff=0.5)
        group1 = VGroup(pie1, label1)
        
        # 1/4 Modeli
        pie2 = VGroup()
        for i in range(4):
            fill_c = BLUE if i == 0 else WHITE
            fill_o = 0.6 if i == 0 else 0.0
            slice_2 = Sector(
                radius=1.3, 
                angle=TAU/4, 
                start_angle=i*TAU/4, 
                fill_color=fill_c, 
                fill_opacity=fill_o, 
                stroke_width=4, 
                stroke_color=BLACK
            )
            pie2.add(slice_2)
            
        label2 = MathTex(r"\frac{1}{4}", color=BLACK).scale(2.5).next_to(pie2, DOWN, buff=0.5)
        group2 = VGroup(pie2, label2)
        
        # Karşılaştırma Sembolü
        symbol = MathTex(">", color=BLACK).scale(3.5)
        
        # Modelleri Gruplama ve Konumlandırma
        models_group = VGroup(group1, symbol, group2).arrange(RIGHT, buff=0.8)
        models_group.move_to(UP * 1.2)
        
        # 3. AÇIKLAMA
        explanation = Paragraph(
            "Payda büyüdükçe,",
            "dilimler küçülür!",
            alignment="center",
            color=BLACK,
            font_weight=BOLD
        )
        explanation.scale_to_fit_width(7.5)
        explanation.move_to(DOWN * 3.5)
        
        # Animasyonlar
        self.play(Write(header), run_time=1)
        self.wait(0.5)
        
        self.play(FadeIn(group1, shift=UP), run_time=1)
        self.wait(1)
        
        self.play(FadeIn(group2, shift=UP), run_time=1)
        self.wait(1)
        
        self.play(Write(symbol), run_time=0.8)
        self.wait(1)
        
        self.play(Write(explanation), run_time=1.5)
        self.wait(2)