from manim import *

class UnitFractions(Scene):
    def construct(self):
        # ARKA PLAN: BEYAZ
        self.camera.background_color = "#FFFFFF"

        # 1. BAŞLIK (TITLE) - KESİNLİKLE to_edge(UP, buff=1.0) ve scale(1.2)
        title = Text("BİRİM KESİRLERİN BÜYÜKLÜĞÜ", font="DejaVu Sans", weight=BOLD, color="#333333").scale(1.2)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(3.0)

        # 2. MODELLER (MODELS) - KESİNLİKLE shift(UP * 2.0)
        # 1/2 Pizza
        pizza1_whole = Circle(radius=1.5, color="#333333", stroke_width=4).set_fill(WHITE, opacity=1)
        pizza1_slice = Sector(radius=1.5, angle=PI, start_angle=PI/2, color="#007BFF", fill_opacity=0.8)
        pizza1_line = Line(pizza1_whole.get_top(), pizza1_whole.get_bottom(), color="#333333", stroke_width=4)
        pizza1 = VGroup(pizza1_whole, pizza1_slice, pizza1_line)

        # 1/4 Pizza
        pizza2_whole = Circle(radius=1.5, color="#333333", stroke_width=4).set_fill(WHITE, opacity=1)
        pizza2_slice = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color="#FF0000", fill_opacity=0.8)
        pizza2_line_v = Line(pizza2_whole.get_top(), pizza2_whole.get_bottom(), color="#333333", stroke_width=4)
        pizza2_line_h = Line(pizza2_whole.get_left(), pizza2_whole.get_right(), color="#333333", stroke_width=4)
        pizza2_lines = VGroup(pizza2_line_v, pizza2_line_h)
        pizza2 = VGroup(pizza2_whole, pizza2_slice, pizza2_lines)

        # Modelleri yan yana koyup yukarı taşıma
        models = VGroup(pizza1, pizza2).arrange(RIGHT, buff=1.0)
        models.shift(UP * 2.0)

        self.play(FadeIn(pizza1_whole), FadeIn(pizza2_whole))
        self.wait(2.6)

        # 1/2 Animasyonu
        self.play(Create(pizza1_line))
        self.play(FadeIn(pizza1_slice))
        
        # 3. KESİR SAYILARI - KESİNLİKLE next_to(model, DOWN, buff=0.8)
        frac1 = MathTex(r"\frac{1}{2}", color="#007BFF").scale(2.0)
        frac1.next_to(pizza1, DOWN, buff=0.8)
        self.play(Write(frac1))
        self.wait(3.6)

        # 1/4 Animasyonu
        self.play(Create(pizza2_lines))
        self.play(FadeIn(pizza2_slice))
        
        frac2 = MathTex(r"\frac{1}{4}", color="#FF0000").scale(2.0)
        frac2.next_to(pizza2, DOWN, buff=0.8)
        self.play(Write(frac2))
        self.wait(4.0)

        # 4. ALT SONUÇ METNİ - KESİNLİKLE to_edge(DOWN, buff=3.5)
        bottom_text = Text("Payda büyüdükçe kesir küçülür!", font="DejaVu Sans", weight=BOLD, color="#FF0000").scale(0.9)
        bottom_text.to_edge(DOWN, buff=3.5)
        self.play(Write(bottom_text))
        self.wait(3.3)

        # Büyüktür işareti (Ortaya)
        greater_sign = MathTex(">", color="#333333").scale(2.5)
        greater_sign.move_to((frac1.get_center() + frac2.get_center()) / 2)
        self.play(Write(greater_sign))
        
        # Son bekleme süresi (+2.0 saniye eklendi)
        self.wait(5.3)
