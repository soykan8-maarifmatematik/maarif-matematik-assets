from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # Başlık
        title = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", color="#212121", weight=BOLD)
        title.scale_to_fit_width(7.0)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        # Sol Kesir (1/3)
        left_group = VGroup()
        for i in range(3):
            sector = Sector(
                radius=0.9,
                angle=TAU/3,
                start_angle=i*TAU/3,
                fill_color=BLUE if i == 0 else WHITE,
                fill_opacity=0.5 if i == 0 else 0.0,
                stroke_color=BLACK,
                stroke_width=2
            )
            left_group.add(sector)
        left_group.move_to(LEFT * 2)
        
        left_tex = MathTex(r"\frac{1}{3}", color="#212121").scale(1.5)
        left_tex.next_to(left_group, DOWN, buff=0.8)
        
        # Sağ Kesir (1/5)
        right_group = VGroup()
        for i in range(5):
            sector = Sector(
                radius=0.9,
                angle=TAU/5,
                start_angle=i*TAU/5,
                fill_color=RED if i == 0 else WHITE,
                fill_opacity=0.5 if i == 0 else 0.0,
                stroke_color=BLACK,
                stroke_width=2
            )
            right_group.add(sector)
        right_group.move_to(RIGHT * 2)
        
        right_tex = MathTex(r"\frac{1}{5}", color="#212121").scale(1.5)
        right_tex.next_to(right_group, DOWN, buff=0.8)
        
        # Animasyonlar: Dilimlerin çizilerek oluşması
        self.play(Create(left_group), Create(right_group), run_time=2)
        self.play(Write(left_tex), Write(right_tex))
        
        # Karşılaştırma Sembolü (Tam Merkezde)
        symbol = MathTex(">", color="#212121").scale(2.5)
        symbol.move_to(ORIGIN)
        self.play(Write(symbol))
        
        # Sonuç Metni
        result_text = Text("Payda büyüdükçe kesir küçülür!", color="#212121")
        result_text.scale_to_fit_width(5.5)
        result_text.to_edge(DOWN, buff=5.2)
        self.play(Write(result_text))
        
        self.wait(2)