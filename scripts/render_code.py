from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi
        self.camera.background_color = "#FFFFFF"

        # Başlık (Kurallara tam uygun)
        title = Text("BİRİM KESİRLER", weight=BOLD, color="#212121").scale_to_fit_width(7.0)
        title.to_edge(UP, buff=1.0)

        # Karşılaştırma Sembolü (DAİMA ORIGIN)
        sign = MathTex(">", color="#212121").scale(2.5).move_to(ORIGIN)

        # Sol Model ve Kesir (1/2)
        circle_left = Circle(radius=0.9, color="#212121")
        fill_left = Sector(radius=0.9, angle=PI, color=BLUE, fill_opacity=0.7)
        model_left = VGroup(circle_left, fill_left)
        # Modeli butonların altında kalmayacak şekilde yukarı kaydırma
        model_left.move_to(ORIGIN).shift(LEFT * 2.0 + np.array([0, 1.0, 0]))
        
        fraction_left = MathTex(r"\frac{1}{2}", color="#212121").scale(2.5)
        fraction_left.next_to(model_left, DOWN, buff=0.8)
        group_left = VGroup(model_left, fraction_left)

        # Sağ Model ve Kesir (1/4)
        circle_right = Circle(radius=0.9, color="#212121")
        fill_right = Sector(radius=0.9, angle=PI/2, color=RED, fill_opacity=0.7)
        model_right = VGroup(circle_right, fill_right)
        # Modeli butonların altında kalmayacak şekilde yukarı kaydırma
        model_right.move_to(ORIGIN).shift(RIGHT * 2.0 + np.array([0, 1.0, 0]))
        
        fraction_right = MathTex(r"\frac{1}{4}", color="#212121").scale(2.5)
        fraction_right.next_to(model_right, DOWN, buff=0.8)
        group_right = VGroup(model_right, fraction_right)

        # Sonuç Metni
        result_text = Text("Payda büyüdükçe kesir küçülür!", weight=BOLD, color="#212121").scale_to_fit_width(5.5)
        result_text.to_edge(DOWN, buff=2.5)

        # Animasyon Akışı
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeIn(group_left))
        self.wait(0.5)
        self.play(FadeIn(group_right))
        self.wait(1)
        self.play(Write(sign))
        self.wait(1)
        self.play(Write(result_text))
        self.wait(2)
