from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5
        
        # Kesir ve yazıların oluşturulması
        fraction = MathTex(r"\frac{3}{4}", color=BLACK, font_size=144)
        pay_text = Text("Pay (Alınan Parça)", color=BLUE, font_size=32).next_to(fraction, UP, buff=0.6)
        payda_text = Text("Payda (Toplam Parça)", color=RED, font_size=32).next_to(fraction, DOWN, buff=0.6)
        
        # Ana grubu merkeze sabitleme
        core_group = VGroup(pay_text, fraction, payda_text)
        core_group.move_to(main_center)
        
        # Okunuşların oluşturulması
        read_1 = Text("1. Okunuş: Üç bölü dört (Yukarıdan Aşağıya)", color=BLACK, font_size=28)
        read_2 = Text("2. Okunuş: Dörtte üç (Aşağıdan Yukarıya)", color=BLACK, font_size=28)
        
        read_group = VGroup(read_1, read_2).arrange(DOWN, buff=0.3).to_edge(UP).shift(DOWN * 0.2)
        
        # Animasyonlar
        self.play(Write(fraction))
        self.wait(1)
        
        self.play(Write(payda_text))
        self.wait(1)
        
        self.play(Write(pay_text))
        self.wait(1)
        
        self.play(Write(read_1))
        self.wait(1)
        
        self.play(Write(read_2))
        self.wait(2)
        
        # Kapanış
        self.play(FadeOut(core_group), FadeOut(read_group))
        self.wait(1)
