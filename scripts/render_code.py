from manim import *

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # 1. BAŞLIK STANDARTI
        header = Paragraph(
            'ÇARPMA İŞLEMİ',
            alignment='center',
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)
        
        self.play(Write(header))
        self.wait(1.0)
        
        # 1. DİKEY İŞLEM KURALI: Sayıları merkeze/sola çek (LEFT * 0.5)
        # 45 Sayısı
        num1_4 = MathTex('4', color='#FFFFFF').scale(1.7)
        num1_5 = MathTex('5', color='#FFFFFF').scale(1.7)
        num1_group = VGroup(num1_4, num1_5).arrange(RIGHT, buff=0.2).shift(UP * 1.5 + LEFT * 0.5)
        
        # 23 Sayısı
        num2_2 = MathTex('2', color='#FFFFFF').scale(1.7)
        num2_3 = MathTex('3', color='#FFFFFF').scale(1.7)
        num2_group = VGroup(num2_2, num2_3).arrange(RIGHT, buff=0.2).next_to(num1_group, DOWN, buff=0.5).align_to(num1_group, RIGHT)
        
        # Çarpma Çizgisi ve İşareti
        line1 = Line(num2_group.get_left() + LEFT * 1.0, num2_group.get_right() + RIGHT * 0.2, color='#FFFFFF')
        line1.next_to(num2_group, DOWN, buff=0.3)
        
        times_sign = MathTex('\\times', color='#FFFFFF').scale(1.7).next_to(line1, LEFT, buff=0.3).shift(UP * 0.4)
        
        # 2. ZİNCİRLEME YASAK & HER RAKAM SONRASI ES
        self.play(Write(num1_4))
        self.wait(1.0)
        self.play(Write(num1_5))
        self.wait(1.0)
        self.play(Write(num2_2))
        self.wait(1.0)
        self.play(Write(num2_3))
        self.wait(1.0)
        self.play(Write(line1))
        self.wait(1.0)
        self.play(Write(times_sign))
        self.wait(1.0)
        
        # --- BİRLER BASAMAĞI ÇARPIMI ---
        # 3 x 5 = 15
        self.play(num2_3.animate.set_color('#FFFF00'), num1_5.animate.set_color('#FFFF00'))
        self.wait(1.0)
        
        r1_5 = MathTex('5', color='#FFFFFF').scale(1.7).next_to(line1, DOWN, buff=0.5).align_to(num2_3, RIGHT)
        self.play(Write(r1_5))
        self.wait(1.0)
        
        # 1. ÖLÇEKLER: Eldeler scale(0.8)
        elde1 = MathTex('1', color='#FFFF00').scale(0.8).next_to(num1_4, UP, buff=0.3)
        self.play(Write(elde1))
        self.wait(1.0)
        
        self.play(num1_5.animate.set_color('#FFFFFF'), num1_4.animate.set_color('#FFFF00'))
        self.wait(1.0)
        
        # 3 x 4 = 12, +1 = 13
        r1_3 = MathTex('3', color='#FFFFFF').scale(1.7).next_to(r1_5, LEFT, buff=0.2)
        self.play(Write(r1_3))
        self.wait(1.0)
        
        r1_1 = MathTex('1', color='#FFFFFF').scale(1.7).next_to(r1_3, LEFT, buff=0.2)
        self.play(Write(r1_1))
        self.wait(1.0)
        
        # Renk sıfırlama ve elde çizme
        self.play(num2_3.animate.set_color('#FFFFFF'), num1_4.animate.set_color('#FFFFFF'))
        self.wait(1.0)
        elde1_cross = Line(elde1.get_bottom_left(), elde1.get_top_right(), color='#FF0000')
        self.play(Create(elde1_cross))
        self.wait(1.0)
        
        # 2. BLOK SONU BEKLEME (1. Satır Sonu)
        self.wait(4.0)
        
        # 2. GEÇİŞ SİNYALİ ("Şimdi onlar basamağına geçiyoruz")
        self.wait(3.0)
        
        # --- ONLAR BASAMAĞI ÇARPIMI ---
        # 2 x 5 = 10
        self.play(num2_2.animate.set_color('#00FFFF'), num1_5.animate.set_color('#00FFFF'))
        self.wait(1.0)
        
        # 1. MİLMETRİK HİZALAMA: İkinci satırın son rakamı, üstteki sayının onlar basamağının tam altına kilitlenir.
        r2_0 = MathTex('0', color='#FFFFFF').scale(1.7).next_to(r1_5, DOWN, buff=0.5).align_to(r1_3, RIGHT)
        self.play(Write(r2_0))
        self.wait(1.0)
        
        elde2 = MathTex('1', color='#00FFFF').scale(0.8).next_to(elde1, UP, buff=0.1)
        self.play(Write(elde2))
        self.wait(1.0)
        
        self.play(num1_5.animate.set_color('#FFFFFF'), num1_4.animate.set_color('#00FFFF'))
        self.wait(1.0)
        
        # 2 x 4 = 8, +1 = 9
        r2_9 = MathTex('9', color='#FFFFFF').scale(1.7).next_to(r2_0, LEFT, buff=0.2)
        self.play(Write(r2_9))
        self.wait(1.0)
        
        self.play(num2_2.animate.set_color('#FFFFFF'), num1_4.animate.set_color('#FFFFFF'))
        self.wait(1.0)
        elde2_cross = Line(elde2.get_bottom_left(), elde2.get_top_right(), color='#FF0000')
        self.play(Create(elde2_cross))
        self.wait(1.0)
        
        # 2. BLOK SONU BEKLEME (2. Satır Sonu)
        self.wait(4.0)
        
        # --- TOPLAMA İŞLEMİ ---
        line2 = Line(r2_9.get_left() + LEFT * 1.0, r1_5.get_right() + RIGHT * 0.2, color='#FFFFFF')
        line2.next_to(r2_0, DOWN, buff=0.3)
        self.play(Write(line2))
        self.wait(1.0)
        
        # 1. TOPLAMA İŞARETİ KURALI
        plus_sign = MathTex('+', color='#FFFFFF').scale(1.7).next_to(line2, LEFT, buff=0.3).align_to(r2_9, UP).shift(UP * 0.4)
        self.play(Write(plus_sign))
        self.wait(1.0)
        
        # 1. ÖLÇEKLER: Final sonuç vurgusu scale(1.8)
        res_5 = MathTex('5', color='#FFFF00').scale(1.8).next_to(line2, DOWN, buff=0.5).align_to(r1_5, RIGHT)
        self.play(Write(res_5))
        self.wait(1.0)
        
        res_3 = MathTex('3', color='#FFFF00').scale(1.8).next_to(res_5, LEFT, buff=0.2).align_to(r2_0, RIGHT)
        self.play(Write(res_3))
        self.wait(1.0)
        
        res_0 = MathTex('0', color='#FFFF00').scale(1.8).next_to(res_3, LEFT, buff=0.2).align_to(r2_9, RIGHT)
        self.play(Write(res_0))
        self.wait(1.0)
        
        res_1 = MathTex('1', color='#FFFF00').scale(1.8).next_to(res_0, LEFT, buff=0.2)
        self.play(Write(res_1))
        self.wait(1.0)
        
        # 2. BLOK SONU BEKLEME (Final Sonucu)
        self.wait(4.0)
        
        # 2. INSTAGRAM/SHORTS FIX
        self.wait(8.0)
