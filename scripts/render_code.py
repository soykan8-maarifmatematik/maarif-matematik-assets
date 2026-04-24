from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 1080 / 100
config.frame_height = 1920 / 100

class BirimKesirler(Scene):
    def construct(self):
        # 1. GİRİŞ VE BAŞLIK
        title = Text("Birim Kesirler", font="DejaVu Sans").to_edge(UP, buff=0.8)
        self.play(Write(title))
        self.wait(1.67)  # 5 kelime / 3.0 = 1.67s

        # 2. MATEMATİKSEL MODELLERİ OLUŞTURMA
        def create_fraction_model(denominator, color):
            group = VGroup()
            rect_width = 6.0 / denominator
            for i in range(denominator):
                rect = Rectangle(width=rect_width, height=1.0, color=WHITE)
                if i == 0:
                    rect.set_fill(color, opacity=0.8)
                group.add(rect)
            group.arrange(RIGHT, buff=0)
            label = MathTex(f"\\frac{{1}}{{{denominator}}}").scale(1.5)
            res = VGroup(group, label).arrange(RIGHT, buff=0.5)
            return res

        model_1_2 = create_fraction_model(2, BLUE)
        model_1_3 = create_fraction_model(3, GREEN)
        model_1_4 = create_fraction_model(4, RED)

        models = VGroup(model_1_2, model_1_3, model_1_4)
        models.arrange(DOWN, buff=2.0)
        models.scale_to_fit_width(6.5)

        # İLK ŞEKİL KESİNLİKLE UP * 2.5 NOKTASINDAN BAŞLAMALIDIR
        shift_amount = (UP * 2.5) - models[0].get_center()
        models.shift(shift_amount)

        # 3. ANLATIM VE ANİMASYONLAR
        # "Birim kesirlerde payda büyüdükçe kesrin değeri küçülür."
        self.play(FadeIn(model_1_2))
        self.wait(2.33)  # 7 kelime / 3.0 = 2.33s

        # "Örneğin, bir bütünün ikide biri, üçte birinden daha büyüktür."
        self.play(FadeIn(model_1_3))
        self.wait(3.00)  # 9 kelime / 3.0 = 3.00s

        # "Dörtte biri ise en küçüğüdür."
        self.play(FadeIn(model_1_4))
        self.wait(1.67)  # 5 kelime / 3.0 = 1.67s

        # "Çünkü aynı pastayı daha çok kişiye paylaştırıyorsunuz."
        # FORMÜL UYGULAMASI: (7 kelime / 3.0) + 1.5 = 3.83 saniye bekleme
        colored_parts = VGroup(model_1_2[0][0], model_1_3[0][0], model_1_4[0][0])
        self.play(Indicate(colored_parts, color=YELLOW, scale_factor=1.1)) # 1.0 saniye sürer
        self.wait(2.83)  # Toplam 3.83 saniye olması için 2.83 saniye daha bekle

        # 4. MUTLAK SENKRONİZASYON (TEMİZLİK VE ÇIKIŞ)
        self.play(FadeOut(models), FadeOut(title))

        # CTA: "Maarif Matematik ile mantığını kavra, takipte kal!"
        cta = Text("Maarif Matematik ile mantığını kavra,\ntakipte kal!", font="DejaVu Sans", color=YELLOW).scale_to_fit_width(6.5)
        self.play(Write(cta))
        self.wait(2.33)  # 7 kelime / 3.0 = 2.33s
