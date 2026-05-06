from manim import *

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_width = 9
config.frame_height = 16

class UnitFractionsComparison(Scene):
    def construct(self):
        # ARKA PLAN
        self.camera.background_color = WHITE
        
        # BAŞLIK
        header = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", color=BLACK, weight=BOLD)
        header.to_edge(UP, buff=0.8).scale_to_fit_width(8.5)
        
        # MODELLER
        # 1/3 Modeli
        circle1 = VGroup()
        for i in range(3):
            angle = TAU / 3
            fill_c = BLUE if i == 0 else WHITE
            fill_o = 0.6 if i == 0 else 1.0
            sector = Sector(
                radius=1.3,
                angle=angle,
                start_angle=i * angle,
                fill_color=fill_c,
                fill_opacity=fill_o,
                stroke_width=4,
                stroke_color=BLACK
            )
            circle1.add(sector)
        
        label1 = MathTex(r"\frac{1}{3}", color=BLACK).scale(2).next_to(circle1, DOWN, buff=0.5)
        model1 = VGroup(circle1, label1)
        
        # 1/5 Modeli
        circle2 = VGroup()
        for i in range(5):
            angle = TAU / 5
            fill_c = RED if i == 0 else WHITE
            fill_o = 0.6 if i == 0 else 1.0
            sector = Sector(
                radius=1.3,
                angle=angle,
                start_angle=i * angle,
                fill_color=fill_c,
                fill_opacity=fill_o,
                stroke_width=4,
                stroke_color=BLACK
            )
            circle2.add(sector)
            
        label2 = MathTex(r"\frac{1}{5}", color=BLACK).scale(2).next_to(circle2, DOWN, buff=0.5)
        model2 = VGroup(circle2, label2)
        
        # Sembol
        symbol = Text(">", color=BLACK, weight=BOLD).scale(3)
        
        # Modelleri Gruplama ve Konumlandırma
        models_group = VGroup(model1, symbol, model2).arrange(RIGHT, buff=0.8)
        models_group.move_to(UP * 1.2)
        
        # AÇIKLAMA
        explanation = Paragraph(
            "Paydası küçük olan",
            "birim kesir daha büyüktür!",
            alignment="center",
            color=BLACK,
            weight=BOLD
        )
        explanation.move_to(DOWN * 3.5).scale_to_fit_width(7.5)
        
        # ANİMASYONLAR
        self.play(Write(header))
        self.wait(0.5)
        
        self.play(FadeIn(model1, shift=UP))
        self.wait(0.5)
        
        self.play(FadeIn(model2, shift=UP))
        self.wait(1)
        
        self.play(Write(symbol))
        self.wait(1)
        
        self.play(Write(explanation))
        self.wait(2)
