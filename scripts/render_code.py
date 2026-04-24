from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class MaarifScene(Scene):
    def construct(self):
        # Güvenli alan (Çentiğe çarpmaz)
        title = Text("Birim Kesirler", font="DejaVu Sans", font_size=65).to_edge(UP, buff=1.5)
        self.play(Write(title))

        # 1/2 Kesri ve Görseli
        frac1_text = MathTex(r"\frac{1}{2}", font_size=110)
        pizza1 = VGroup(
            Circle(radius=1.5, color=WHITE),
            Sector(outer_radius=1.5, angle=PI, color=YELLOW, fill_opacity=0.8).rotate(PI/2)
        )
        group1 = VGroup(frac1_text, pizza1).arrange(RIGHT, buff=1.0)

        # 1/4 Kesri ve Görseli
        frac2_text = MathTex(r"\frac{1}{4}", font_size=110)
        pizza2 = VGroup(
            Circle(radius=1.5, color=WHITE),
            Sector(outer_radius=1.5, angle=PI/2, color=ORANGE, fill_opacity=0.8).rotate(PI/2)
        )
        group2 = VGroup(frac2_text, pizza2).arrange(RIGHT, buff=1.0)

        # Karşılaştırma Sonucu
        comp_text = MathTex(r"\frac{1}{2} > \frac{1}{4}", font_size=130, color=GREEN)

        # Objelerin üst üste binmemesi için dikey düzenleme
        main_group = VGroup(group1, group2, comp_text).arrange(DOWN, buff=1.8)
        
        # Animasyonlar
        self.play(FadeIn(main_group[0], shift=UP))
        self.wait(2.5)
        
        self.play(FadeIn(main_group[1], shift=UP))
        self.wait(3.5)
        
        self.play(Write(main_group[2]))
        self.wait(2)
        
        # Kapanış Vurgusu
        box = SurroundingRectangle(main_group[2], color=YELLOW, buff=0.5)
        self.play(Create(box))
        self.wait(2)
