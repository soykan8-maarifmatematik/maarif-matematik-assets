from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # BAŞLIK
        title = Text("Birim Kesirler", font="DejaVu Sans").to_edge(UP, buff=1.0)

        # DAİRE MODELLERİ
        def create_fraction_model(fraction_tex, angle, color):
            circle = Circle(radius=1.5, color=WHITE)
            sector = Sector(radius=1.5, angle=angle, color=color, fill_opacity=0.8)
            lines = VGroup(*[Line(ORIGIN, circle.point_at_angle(i * angle), color=WHITE) for i in range(int(round(2*PI/angle)))])
            pie = VGroup(circle, sector, lines)
            label = MathTex(fraction_tex).scale(2.0)
            return VGroup(pie, label).arrange(RIGHT, buff=1.0)

        model1 = create_fraction_model(r"\frac{1}{2}", PI, BLUE)
        model2 = create_fraction_model(r"\frac{1}{3}", 2*PI/3, GREEN)
        model3 = create_fraction_model(r"\frac{1}{4}", PI/2, RED)

        # DİKEY DİZİLİM
        models = VGroup(model1, model2, model3).arrange(DOWN, buff=1.8)
        
        # ÖLÇEK
        models.scale_to_fit_width(6.5)
        
        # KESİN YERLEŞİM: İlk model KESİNLİKLE UP * 2.0 noktasından başlamalıdır
        models.shift(UP * 2.0 - model1.get_center())

        # GİRİŞ (5 kelime = 1.67s)
        self.play(Write(title), run_time=1.0)
        self.wait(0.67)

        # Cümle 1 (5 kelime = 1.67s)
        self.wait(1.67)

        # Cümle 2 (7 kelime = 2.33s)
        self.wait(2.33)

        # Cümle 3 (8 kelime = 2.67s)
        self.play(FadeIn(model1), run_time=1.0)
        self.wait(1.67)

        # Cümle 4 (8 kelime = 2.67s)
        self.play(FadeIn(model2), run_time=1.0)
        self.wait(1.67)

        # Cümle 5 (8 kelime = 2.67s)
        self.play(FadeIn(model3), run_time=1.0)
        self.wait(1.67)

        # Cümle 6 - SON MATEMATİK CÜMLESİ (6 kelime)
        # 6 / 3.0 = 2.0 saniye. +1 saniye ekstra = 3.0 saniye bekleme.
        self.wait(3.0)

        # EKRANI TEMİZLE (Tüm matematiksel objeler FadeOut ile silinir)
        self.play(FadeOut(title), FadeOut(models), run_time=1.0)

        # ÇIKIŞ MÜHRÜ (7 kelime = 2.33s)
        outro = Text("Maarif Matematik ile\nmantığını kavra,\ntakipte kal!", font="DejaVu Sans", text_alignment="CENTER")
        self.play(Write(outro), run_time=1.0)
        self.wait(1.33)
