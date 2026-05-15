from manim import *

class MaarifCarpmaSistemi(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # 1. GÖRSEL HİYERARŞİ: Başlık Standartı
        header = Paragraph(
            'ÇARPMA İŞLEMİ\nADIM ADIM',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # 1. DİKEY İŞLEM KURALI: Sola çekme (LEFT * 0.5)
        num1 = VGroup(
            MathTex('3', color='#FFFFFF').scale(1.7),
            MathTex('4', color='#FFFFFF').scale(1.7)
        ).arrange(RIGHT, buff=0.1).move_to(LEFT * 0.5 + UP * 1.0)

        num2 = VGroup(
            MathTex('2', color='#FFFFFF').scale(1.7),
            MathTex('5', color='#FFFFFF').scale(1.7)
        ).arrange(RIGHT, buff=0.1).next_to(num1, DOWN, buff=0.3)
        num2.shift(RIGHT * (num1[1].get_center()[0] - num2[1].get_center()[0])) # Sağdan hizalama

        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.2).next_to(num2, DOWN, buff=0.2)
        times_sign = MathTex('\\times', color='#FFFFFF').scale(1.7).next_to(line1, LEFT, buff=0.2).shift(UP * 0.4)

        # 1. MİLMETRİK HİZALAMA: 1. Satır
        row1 = VGroup(
            MathTex('1', color='#FFFFFF').scale(1.7),
            MathTex('7', color='#FFFFFF').scale(1.7),
            MathTex('0', color='#FFFFFF').scale(1.7)
        ).arrange(RIGHT, buff=0.1).next_to(line1, DOWN, buff=0.3)
        row1.shift(RIGHT * (num2[1].get_center()[0] - row1[2].get_center()[0])) # 0 rakamı 5'in tam altına kilitli

        carry1 = MathTex('2', color='#FFFF00').scale(0.8).next_to(num1[0], UP, buff=0.2)

        # 1. MİLMETRİK HİZALAMA: 2. Satır
        row2 = VGroup(
            MathTex('6', color='#FFFFFF').scale(1.7),
            MathTex('8', color='#FFFFFF').scale(1.7)
        ).arrange(RIGHT, buff=0.1).next_to(row1, DOWN, buff=0.3)
        row2.shift(RIGHT * (row1[1].get_center()[0] - row2[1].get_center()[0])) # 8 rakamı 7'nin tam altına kilitli

        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.4).next_to(row2, DOWN, buff=0.2)
        # 1. TOPLAMA İŞARETİ KURALI
        plus_sign = MathTex('+', color='#FFFFFF').scale(1.7).next_to(line2, LEFT, buff=0.2).shift(UP * 0.4)

        carry2 = MathTex('1', color='#00FFFF').scale(0.8).next_to(row1[0], UP, buff=0.2)

        # 1. ÖLÇEKLER: Final sonuç vurgusu scale(1.8)
        res = VGroup(
            MathTex('8', color='#FFFF00').scale(1.8),
            MathTex('5', color='#FFFF00').scale(1.8),
            MathTex('0', color='#FFFF00').scale(1.8)
        ).arrange(RIGHT, buff=0.1).next_to(line2, DOWN, buff=0.3)
        res.shift(RIGHT * (row1[2].get_center()[0] - res[2].get_center()[0])) # 0 rakamı 0'ın tam altına kilitli

        # --- 2. KESİN SENKRON VE BLOK-KİLİT SİSTEMİ ANİMASYONLARI ---
        self.play(Write(header))
        self.wait(3.0)

        # ZİNCİRLEME YASAK: Her rakam tek başına
        self.play(Write(num1[0]))
        self.wait(1.0) # HER RAKAM SONRASI ES
        self.play(Write(num1[1]))
        self.wait(1.0)

        self.play(Write(num2[0]))
        self.wait(1.0)
        self.play(Write(num2[1]))
        self.wait(1.0)

        self.play(Write(line1))
        self.wait(1.0)
        self.play(Write(times_sign))
        self.wait(4.0) # BLOK SONU BEKLEME

        # 5x4 = 20 İşlemi
        self.play(num2[1].animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(num1[1].animate.set_color('#FFFF00'))
        self.wait(1.0)
        
        self.play(Write(row1[2]))
        self.wait(1.0)
        self.play(Write(carry1))
        self.wait(1.0)

        # 5x3 = 15 (+2 = 17) İşlemi
        self.play(num1[1].animate.set_color('#FFFFFF'))
        self.wait(1.0)
        self.play(num1[0].animate.set_color('#FFFF00'))
        self.wait(1.0)

        self.play(Write(row1[1]))
        self.wait(1.0)
        self.play(Write(row1[0]))
        self.wait(4.0) # BLOK SONU BEKLEME

        # GEÇİŞ SİNYALİ: Onlar basamağına geçiş
        self.play(num2[1].animate.set_color('#FFFFFF'))
        self.wait(1.0)
        self.play(num1[0].animate.set_color('#FFFFFF'))
        self.wait(3.0) # 3 SANİYE BOŞ EKRAN BEKLEMESİ

        # 2x4 = 8 İşlemi
        self.play(num2[0].animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.play(num1[1].animate.set_color('#00FFFF'))
        self.wait(1.0)

        self.play(Write(row2[1]))
        self.wait(1.0)

        # 2x3 = 6 İşlemi
        self.play(num1[1].animate.set_color('#FFFFFF'))
        self.wait(1.0)
        self.play(num1[0].animate.set_color('#00FFFF'))
        self.wait(1.0)

        self.play(Write(row2[0]))
        self.wait(4.0) # BLOK SONU BEKLEME

        # Toplama İşlemine Geçiş
        self.play(num2[0].animate.set_color('#FFFFFF'))
        self.wait(1.0)
        self.play(num1[0].animate.set_color('#FFFFFF'))
        self.wait(1.0)

        self.play(Write(line2))
        self.wait(1.0)
        self.play(Write(plus_sign))
        self.wait(4.0) # BLOK SONU BEKLEME

        # Sonuç: 0
        self.play(Write(res[2]))
        self.wait(1.0)

        # Sonuç: 5 (7+8=15)
        self.play(Write(res[1]))
        self.wait(1.0)
        self.play(Write(carry2))
        self.wait(1.0)

        # Sonuç: 8 (1+6+1=8)
        self.play(Write(res[0]))
        self.wait(4.0) # BLOK SONU BEKLEME

        # INSTAGRAM/SHORTS FIX: Statik bekleme
        self.wait(8.0)