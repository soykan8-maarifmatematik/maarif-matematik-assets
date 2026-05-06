from manim import *

config.pixel_height, config.pixel_width = 1920, 1080

class BirimKesirler(Scene):
    def construct(self):
        self.camera.frame_width = 9
        self.camera.frame_height = 16

        # ÜST BÖLGE (Başlık)
        title = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA")
        title.scale_to_fit_width(6.2)
        title.to_edge(UP, buff=1.0)

        # ORTA-ÜST BÖLGE (Modeller)
        # 1/3 Modeli
        sectors_3 = VGroup()
        for i in range(3):
            fill_opacity = 0.5 if i == 0 else 0
            fill_color = BLUE if i == 0 else BLACK
            sector = Sector(
                radius=1.0, 
                angle=TAU/3, 
                start_angle=i*TAU/3, 
                stroke_color=WHITE, 
                stroke_width=2, 
                fill_color=fill_color, 
                fill_opacity=fill_opacity
            )
            sectors_3.add(sector)
        
        label_3 = MathTex(r"\frac{1}{3}", font_size=64).next_to(sectors_3, DOWN, buff=0.5)
        group_3 = VGroup(sectors_3, label_3)

        # 1/4 Modeli
        sectors_4 = VGroup()
        for i in range(4):
            fill_opacity = 0.5 if i == 0 else 0
            fill_color = RED if i == 0 else BLACK
            sector = Sector(
                radius=1.0, 
                angle=TAU/4, 
                start_angle=i*TAU/4, 
                stroke_color=WHITE, 
                stroke_width=2, 
                fill_color=fill_color, 
                fill_opacity=fill_opacity
            )
            sectors_4.add(sector)
        
        label_4 = MathTex(r"\frac{1}{4}", font_size=64).next_to(sectors_4, DOWN, buff=0.5)
        group_4 = VGroup(sectors_4, label_4)

        # Sembol
        greater_sign = MathTex(">", font_size=72)

        # Modelleri Gruplama ve Konumlandırma
        models_group = VGroup(group_3, greater_sign, group_4).arrange(RIGHT, buff=0.8)
        models_group.move_to(ORIGIN).shift(UP * 3.8)

        # ALT-ORTA BÖLGE (Paragraf)
        paragraph = Paragraph(
            "Payda büyüdükçe",
            "dilimler küçülür!",
            "",
            "Bu yüzden:",
            "1/3 > 1/4",
            alignment="center"
        )
        paragraph.scale_to_fit_width(6.2)
        paragraph.to_edge(DOWN, buff=4.8)

        # Animasyonlar
        self.play(Write(title))
        self.wait(0.5)

        self.play(Create(sectors_3), Write(label_3))
        self.wait(0.5)

        self.play(Create(sectors_4), Write(label_4))
        self.wait(0.5)

        self.play(Write(greater_sign))
        self.wait(1)

        self.play(Write(paragraph))
        self.wait(2)