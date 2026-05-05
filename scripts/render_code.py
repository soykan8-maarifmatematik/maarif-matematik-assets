from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0
config.background_color = "#FFFFFF"

class MaarifScene(Scene):
    def construct(self):
        # Renk ayarları
        Text.set_default(color="#212121")
        MathTex.set_default(color="#212121")
        Tex.set_default(color="#212121")

        # 1. BAŞLIK STİLİ
        title = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", weight=BOLD).scale_to_fit_width(7.0).to_edge(UP, buff=1.0)
        self.play(Write(title))

        # 2. MODEL YERLEŞİMİ VE ÇİZİMİ
        left_center = LEFT * 2 + UP * 1.5
        right_center = RIGHT * 2 + UP * 1.5

        left_sectors = VGroup()
        for i in range(3):
            angle = 360 / 3 * DEGREES
            start_angle = i * angle
            if i == 0:
                sector = Sector(arc_center=left_center, radius=0.9, angle=angle, start_angle=start_angle, color=BLUE, fill_opacity=0.5, stroke_color=BLACK, stroke_width=2)
            else:
                sector = Sector(arc_center=left_center, radius=0.9, angle=angle, start_angle=start_angle, color=WHITE, fill_opacity=0, stroke_color=BLACK, stroke_width=2)
            left_sectors.add(sector)

        right_sectors = VGroup()
        for i in range(6):
            angle = 360 / 6 * DEGREES
            start_angle = i * angle
            if i == 0:
                sector = Sector(arc_center=right_center, radius=0.9, angle=angle, start_angle=start_angle, color=RED, fill_opacity=0.5, stroke_color=BLACK, stroke_width=2)
            else:
                sector = Sector(arc_center=right_center, radius=0.9, angle=angle, start_angle=start_angle, color=WHITE, fill_opacity=0, stroke_color=BLACK, stroke_width=2)
            right_sectors.add(sector)

        self.play(Create(left_sectors), Create(right_sectors), run_time=2)

        # 3. İŞARET KONUMU
        symbol = MathTex(">").scale(2.5).move_to(ORIGIN)
        self.play(Write(symbol))

        # 4. SONUÇ METNİ (GÜVENLİ ALAN)
        result_text = Text("Payda büyüdükçe kesrin değeri küçülür.", font_size=36).to_edge(DOWN, buff=3.5)
        self.play(Write(result_text))

        # 5. KESİR KONUMU VE FORMATI
        fraction_group = VGroup(
            MathTex(r"\frac{1}{3}").scale(1.5),
            MathTex(">").scale(1.5),
            MathTex(r"\frac{1}{6}").scale(1.5)
        ).arrange(RIGHT, buff=0.5).next_to(result_text, DOWN, buff=0.5)
        
        self.play(Write(fraction_group))
        self.wait(2)