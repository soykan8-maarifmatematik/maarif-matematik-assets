from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # 1. BÖLÜM: Giriş (16 kelime / 3.0 = 5.33 saniye)
        title = Text("Birim Kesirler", font="DejaVu Sans", color=YELLOW).to_edge(UP, buff=2.0)
        self.play(Write(title))
        self.wait(5.33)

        # 2. BÖLÜM: 1/2 Kesri (19 kelime / 3.0 = 6.33 saniye)
        circle1 = Circle(radius=1.3, color=WHITE)
        line1 = Line(circle1.get_top(), circle1.get_bottom(), color=WHITE)
        sector1 = Sector(outer_radius=1.3, angle=PI, start_angle=PI/2, color=BLUE, fill_opacity=0.7)
        label1 = MathTex(r"\frac{1}{2}").scale(1.5)
        
        pizza1_group = VGroup(label1, VGroup(circle1, line1, sector1)).arrange(RIGHT, buff=0.8)

        # 3. BÖLÜM: 1/4 Kesri Hazırlığı
        circle2 = Circle(radius=1.3, color=WHITE)
        line2_v = Line(circle2.get_top(), circle2.get_bottom(), color=WHITE)
        line2_h = Line(circle2.get_left(), circle2.get_right(), color=WHITE)
        sector2 = Sector(outer_radius=1.3, angle=PI/2, start_angle=PI/2, color=RED, fill_opacity=0.7)
        label2 = MathTex(r"\frac{1}{4}").scale(1.5)
        
        pizza2_group = VGroup(label2, VGroup(circle2, line2_v, line2_h, sector2)).arrange(RIGHT, buff=0.8)

        # Grupları ekrana hizalama
        pizzas = VGroup(pizza1_group, pizza2_group).arrange(DOWN, buff=1.6).move_to(ORIGIN)

        # 1/2 Animasyonu
        self.play(Create(circle1))
        self.play(Create(line1))
        self.play(FadeIn(sector1))
        self.play(Write(label1))
        self.wait(6.33)

        # 1/4 Animasyonu (15 kelime / 3.0 = 5.00 saniye)
        self.play(Create(circle2))
        self.play(Create(line2_v), Create(line2_h))
        self.play(FadeIn(sector2))
        self.play(Write(label2))
        self.wait(5.00)

        # 4. BÖLÜM: Karşılaştırma (18 kelime / 3.0 = 6.00 saniye)
        comp = MathTex(r"\frac{1}{2} > \frac{1}{4}").scale(2).next_to(pizzas, DOWN, buff=1.0)
        self.play(Write(comp))
        self.wait(6.00)

        # 5. BÖLÜM: Çıkış (Mühür) (7 kelime / 3.0 = 2.33 saniye)
        self.play(FadeOut(Group(*self.mobjects)))
        outro = Text("Maarif Matematik ile\nmantığını kavra,\ntakipte kal!", font="DejaVu Sans", text_alignment="CENTER").scale(1.2)
        self.play(Write(outro))
        self.wait(2.33)
        
        # Final sabitleme
        self.wait(4)
