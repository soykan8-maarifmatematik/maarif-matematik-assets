from manim import *

class CarpmaIslemi(Scene):
    def construct(self):
        self.camera.background_color = '#000000'

        # 1. GÖRSEL HİYERARŞİ: BAŞLIK STANDARTI
        baslik = Paragraph('ÇARPMA İŞLEMİ', alignment='center', color='#FFFFFF', weight=BOLD)
        baslik.to_edge(UP, buff=1.1)
        baslik.scale_to_fit_width(7.0)
        self.play(Write(baslik))
        self.wait(2.0)

        # DİKEY İŞLEM KURALI: Sola çek (LEFT * 0.5)
        num1_4 = MathTex('4', color='#FFFFFF').scale(1.7)
        num1_3 = MathTex('3', color='#FFFFFF').scale(1.7)
        num1 = VGroup(num1_4, num1_3).arrange(RIGHT, buff=0.15).shift(LEFT * 0.5 + UP * 1.0)

        num2_2 = MathTex('2', color='#FFFFFF').scale(1.7)
        num2_5 = MathTex('5', color='#FFFFFF').scale(1.7)
        num2 = VGroup(num2_2, num2_5).arrange(RIGHT, buff=0.15).next_to(num1, DOWN, buff=0.4).align_to(num1, RIGHT)

        cizgi1 = Line(num2.get_left() + LEFT*0.8, num2.get_right() + RIGHT*0.2, color='#FFFFFF').next_to(num2, DOWN, buff=0.3)
        carpi = MathTex('\\times', color='#FFFFFF').scale(1.7).next_to(cizgi1, LEFT, buff=0.2).shift(UP * 0.4)

        # ZİNCİRLEME YASAK & HER RAKAM SONRASI ES (1.0 sn)
        self.play(Write(num1_4))
        self.wait(1.0)
        self.play(Write(num1_3))
        self.wait(1.0)
        self.play(Write(num2_2))
        self.wait(1.0)
        self.play(Write(num2_5))
        self.wait(1.0)
        self.play(Write(cizgi1))
        self.wait(1.0)
        self.play(Write(carpi))
        self.wait(4.0) # BLOK SONU BEKLEME

        # 1. SATIR İŞLEMİ (5 ile çarpma - Vurgu 1: #FFFF00)
        self.play(num2_5.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(num1_3.animate.set_color('#FFFF00'))
        self.wait(1.0)

        # 5x3 = 15
        satir1_5 = MathTex('5', color='#FFFFFF').scale(1.7).next_to(cizgi1, DOWN, buff=0.4).align_to(num1_3, RIGHT)
        elde1 = MathTex('1', color='#FFFF00').scale(0.8).next_to(num1_4, UP, buff=0.3)

        self.play(Write(satir1_5))
        self.wait(1.0)
        self.play(Write(elde1))
        self.wait(1.0)

        # 5x4 = 20 (+1 = 21)
        self.play(num1_4.animate.set_color('#FFFF00'))
        self.wait(1.0)

        satir1_1 = MathTex('1', color='#FFFFFF').scale(1.7).next_to(satir1_5, LEFT, buff=0.15)
        satir1_2 = MathTex('2', color='#FFFFFF').scale(1.7).next_to(satir1_1, LEFT, buff=0.15)

        self.play(Write(satir1_1))
        self.wait(1.0)
        self.play(Write(satir1_2))
        self.wait(4.0) # BLOK SONU BEKLEME

        # Renkleri sıfırla
        self.play(num2_5.animate.set_color('#FFFFFF'), num1_3.animate.set_color('#FFFFFF'), num1_4.animate.set_color('#FFFFFF'))
        self.wait(1.0)

        # GEÇİŞ SİNYALİ (Onlar basamağına geçiş)
        self.wait(3.0)

        # 2. SATIR İŞLEMİ (2 ile çarpma - Vurgu 2: #00FFFF)
        self.play(num2_2.animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.play(num1_3.animate.set_color('#00FFFF'))
        self.wait(1.0)

        # 2x3 = 6 (MİLMETRİK HİZALAMA: Onlar basamağı hizası)
        satir2_6 = MathTex('6', color='#FFFFFF').scale(1.7).next_to(satir1_5, DOWN, buff=0.4).align_to(satir1_1, RIGHT)
        self.play(Write(satir2_6))
        self.wait(1.0)

        # 2x4 = 8
        self.play(num1_4.animate.set_color('#00FFFF'))
        self.wait(1.0)

        satir2_8 = MathTex('8', color='#FFFFFF').scale(1.7).next_to(satir2_6, LEFT, buff=0.15)
        self.play(Write(satir2_8))
        self.wait(4.0) # BLOK SONU BEKLEME

        # TOPLAMA İŞLEMİ
        cizgi2 = Line(satir2_8.get_left() + LEFT*0.8, satir1_5.get_right() + RIGHT*0.2, color='#FFFFFF').next_to(satir2_6, DOWN, buff=0.3)
        # TOPLAMA İŞARETİ KURALI: shift(UP * 0.4)
        arti = MathTex('+', color='#FFFFFF').scale(1.7).next_to(cizgi2, LEFT, buff=0.2).shift(UP * 0.4)

        self.play(Write(cizgi2))
        self.wait(1.0)
        self.play(Write(arti))
        self.wait(1.0)

        # FİNAL SONUÇ (ÖLÇEK KURALI: scale 1.8)
        sonuc_5 = MathTex('5', color='#FFFF00').scale(1.8).next_to(cizgi2, DOWN, buff=0.4).align_to(satir1_5, RIGHT)
        self.play(Write(sonuc_5))
        self.wait(1.0)

        sonuc_7 = MathTex('7', color='#FFFF00').scale(1.8).next_to(sonuc_5, LEFT, buff=0.15)
        self.play(Write(sonuc_7))
        self.wait(1.0)

        sonuc_0 = MathTex('0', color='#FFFF00').scale(1.8).next_to(sonuc_7, LEFT, buff=0.15)
        elde2 = MathTex('1', color='#00FFFF').scale(0.8).next_to(satir1_2, UP, buff=0.1)
        self.play(Write(sonuc_0))
        self.wait(1.0)
        self.play(Write(elde2))
        self.wait(1.0)

        sonuc_1 = MathTex('1', color='#FFFF00').scale(1.8).next_to(sonuc_0, LEFT, buff=0.15)
        self.play(Write(sonuc_1))
        self.wait(4.0) # BLOK SONU BEKLEME

        # INSTAGRAM/SHORTS FIX
        self.wait(8.0)