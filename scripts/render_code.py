from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        # Kesir ve metinleri oluşturma
        fraction = MathTex(r"\frac{1}{4}", color=BLACK, font_size=144)
        
        pay_text = Text("Pay (Alınan Parça)", color=BLUE, font_size=36)
        pay_text.next_to(fraction, UP, buff=0.8)
        
        payda_text = Text("Payda (Toplam Eş Parça)", color=RED, font_size=36)
        payda_text.next_to(fraction, DOWN, buff=0.8)

        frac_group = VGroup(pay_text, fraction, payda_text)
        frac_group.move_to(main_center)

        # Okunuş metinleri
        reading1 = Text("1 bölü 4", color=DARK_BLUE, font_size=48)
        reading2 = Text("4'te 1", color=DARK_RED, font_size=48)
        reading_group = VGroup(reading1, reading2).arrange(DOWN, buff=1)
        reading_group.move_to(main_center)

        # Animasyonlar
        self.play(Write(fraction), run_time=2)
        self.wait(1)
        
        self.play(FadeIn(payda_text, shift=UP))
        self.wait(2)
        
        self.play(FadeIn(pay_text, shift=DOWN))
        self.wait(3)
        
        self.play(FadeOut(frac_group))
        self.wait(1)
        
        self.play(Write(reading1))
        self.wait(2)
        
        self.play(Write(reading2))
        self.wait(3)
        
        self.play(FadeOut(reading_group))
        self.wait(1)