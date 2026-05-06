from manim import *

config.pixel_height, config.pixel_width = 1920, 1080

class UnitFractions(Scene):
    def construct(self):
        self.camera.frame_width = 9
        self.camera.frame_height = 16
        self.camera.background_color = WHITE

        # 1. BAŞLIK (Üst)
        header = Text("BİRİM KESİRLERİ\nKARŞILAŞTIRMA", font_size=64, color=BLACK, weight=BOLD, text_align="center")
        header.to_edge(UP, buff=1.0)
        header.scale_to_fit_width(8.0)

        # 2. MODELLER (Orta-Üst)
        # 1/3 Modeli
        slices_3 = VGroup()
        for i in range(3):
            color = RED if i == 0 else LIGHT_GREY
            fill_opacity = 0.9 if i == 0 else 0.3
            # SECTOR KURALI: Sadece radius, outer_radius YOK. Çizgisel netlik eklendi.
            s = Sector(radius=1.8, angle=TAU/3, start_angle=i*TAU/3, color=color, fill_opacity=fill_opacity, stroke_width=3, stroke_color=BLACK)
            slices_3.add(s)
        label_3 = MathTex(r"\frac{1}{3}", color=BLACK, font_size=80).next_to(slices_3, DOWN, buff=0.5)
        group_3 = VGroup(slices_3, label_3)

        # 1/4 Modeli
        slices_4 = VGroup()
        for i in range(4):
            color = BLUE if i == 0 else LIGHT_GREY
            fill_opacity = 0.9 if i == 0 else 0.3
            # SECTOR KURALI: Sadece radius, outer_radius YOK. Çizgisel netlik eklendi.
            s = Sector(radius=1.8, angle=TAU/4, start_angle=i*TAU/4, color=color, fill_opacity=fill_opacity, stroke_width=3, stroke_color=BLACK)
            slices_4.add(s)
        label_4 = MathTex(r"\frac{1}{4}", color=BLACK, font_size=80).next_to(slices_4, DOWN, buff=0.5)
        group_4 = VGroup(slices_4, label_4)

        # Karşılaştırma Sembolü
        symbol = MathTex(">", color=BLACK, font_size=120)

        # Modelleri grupla ve kilitle
        models_group = VGroup(group_3, symbol, group_4).arrange(RIGHT, buff=0.6)
        models_group.move_to(UP * 2.8)

        # 3. AÇIKLAMA (Alt)
        explanation = Paragraph(
            "Payda büyüdükçe,",
            "dilim küçülür!",
            alignment="center",
            color=BLACK,
            font_size=64,
            weight=BOLD
        )
        explanation.move_to(DOWN * 3.5)
        explanation.scale_to_fit_width(6.5)

        # Animasyonlar
        self.play(Write(header))
        self.wait(0.5)
        
        self.play(FadeIn(group_3, shift=UP))
        self.wait(0.5)
        
        self.play(FadeIn(group_4, shift=UP))
        self.wait(0.5)
        
        self.play(Write(symbol))
        self.wait(1)
        
        self.play(Write(explanation))
        self.wait(2)
