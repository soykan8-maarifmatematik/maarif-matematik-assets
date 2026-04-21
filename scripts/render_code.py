from manim import *

class KesirMantigi(Scene):
    def construct(self):
        # Sahne 1: Bütünün parçalanması (38 kelime -> ~15 saniye)
        # Animasyonlar: 2 saniye, Bekleme: 13 saniye
        circle = Circle(radius=1.5, color=BLUE)
        self.play(Create(circle)) # 1 saniye
        
        line1 = Line(UP*1.5, DOWN*1.5)
        line2 = Line(LEFT*1.5, RIGHT*1.5)
        self.play(Create(VGroup(line1, line2))) # 1 saniye
        
        self.wait(13)
        self.clear()

        # Sahne 2: Pay, Payda ve Kesir Çizgisi (42 kelime -> ~17 saniye)
        # Animasyonlar: 2 saniye, Bekleme: 15 saniye
        fraction = MathTex(r"\frac{3}{4}").scale(3)
        self.play(Write(fraction)) # 1 saniye
        
        pay_text = Text("Pay: Seçilen parça miktarı", font_size=24, color=YELLOW).next_to(fraction, UP, buff=0.5)
        payda_text = Text("Payda: Toplam eşit parça", font_size=24, color=GREEN).next_to(fraction, DOWN, buff=0.5)
        cizgi_text = Text("Kesir Çizgisi (Bölme)", font_size=24, color=WHITE).next_to(fraction, RIGHT, buff=1)
        self.play(Write(VGroup(pay_text, payda_text, cizgi_text))) # 1 saniye
        
        self.wait(15)
        self.clear()

        # Sahne 3: Kesrin Okunuşu (46 kelime -> ~18 saniye)
        # Animasyonlar: 2 saniye, Bekleme: 16 saniye
        fraction2 = MathTex(r"\frac{3}{4}").scale(2).shift(LEFT*3)
        self.add(fraction2)
        
        read1 = Text("1. Okunuş: Üç bölü dört (Yukarıdan aşağıya)", font_size=28).shift(RIGHT*1.5 + UP*1)
        self.play(Write(read1)) # 1 saniye
        
        read2 = Text("2. Okunuş: Dörtte üç (Aşağıdan yukarıya)", font_size=28).shift(RIGHT*1.5 + DOWN*1)
        self.play(Write(read2)) # 1 saniye
        
        self.wait(16)
