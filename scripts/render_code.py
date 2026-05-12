from manim import *

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class EldeliToplamaMaarif(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # 1. GÖRSEL HİYERARŞİ VE BAŞLIK STANDARTI
        header = Paragraph(
            'ELDELİ TOPLAMA İŞLEMİ',
            alignment='center',
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)
        
        # 2. DİKEY İŞLEM KURALI VE MİLMETRİK YERLEŞİM (LEFT * 0.5)
        # Ana Sayılar Ölçeği: 1.7
        n1_2 = MathTex('8', color='#FFFFFF').scale(1.7).move_to(LEFT * 0.5 + UP * 1.5)
        n1_1 = MathTex('6', color='#FFFFFF').scale(1.7).next_to(n1_2, LEFT, buff=0.5)
        
        n2_2 = MathTex('5', color='#FFFFFF').scale(1.7).next_to(n1_2, DOWN, buff=0.5)
        n2_1 = MathTex('2', color='#FFFFFF').scale(1.7).next_to(n1_1, DOWN, buff=0.5)
        
        # Toplama Çizgisi
        cizgi = Line(n2_1.get_left() + LEFT * 0.5, n2_2.get_right() + RIGHT * 0.5, color='#FFFFFF').next_to(n2_2, DOWN, buff=0.3)
        
        # Toplama İşareti (shift(UP * 0.4) kuralı)
        arti = MathTex('+', color='#FFFFFF').scale(1.7).next_to(cizgi, LEFT, buff=0.3).shift(UP * 0.4)
        
        # Elde Ölçeği: 0.8
        elde = MathTex('1', color='#FFFF00').scale(0.8).next_to(n1_1, UP, buff=0.4)
        
        # Final Sonuç Ölçeği: 1.8
        r_2 = MathTex('3', color='#FFFFFF').scale(1.8).next_to(cizgi, DOWN, buff=0.5).align_to(n2_2, RIGHT)
        r_1 = MathTex('9', color='#FFFFFF').scale(1.8).next_to(cizgi, DOWN, buff=0.5).align_to(n2_1, RIGHT)
        
        # --- KESİN SENKRON VE BLOK-KİLİT SİSTEMİ ---
        
        self.play(Write(header))
        self.wait(1.0)
        
        # Her rakam tek başına ve sonrası 1.0 sn es
        self.play(Write(n1_1))
        self.wait(1.0)
        self.play(Write(n1_2))
        self.wait(1.0)
        
        self.play(Write(n2_1))
        self.wait(1.0)
        self.play(Write(n2_2))
        self.wait(1.0)
        
        self.play(Write(cizgi))
        self.wait(1.0)
        
        self.play(Write(arti))
        self.wait(4.0) # Blok Sonu Bekleme (İşlem tanıtımı)
        
        # Birler Basamağı İşlemi (1. Vurgu Rengi: #FFFF00)
        self.play(n1_2.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(n2_2.animate.set_color('#FFFF00'))
        self.wait(4.0) # "Sekiz, beş daha, on üç eder."
        
        self.play(Write(r_2))
        self.wait(1.0)
        
        self.play(Write(elde))
        self.wait(4.0) # "Eldemiz var bir..."
        
        # GEÇİŞ SİNYALİ
        self.wait(3.0) # "Şimdi onlar basamağına geçiyoruz."
        
        # Onlar Basamağı İşlemi (2. Vurgu Rengi: #00FFFF)
        self.play(n1_1.animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.play(n2_1.animate.set_color('#00FFFF'))
        self.wait(4.0) # "Altı, iki daha, sekiz yapar."
        
        self.play(elde.animate.set_color('#00FFFF'))
        self.wait(4.0) # "Bir de eldemiz vardı..."
        
        self.play(Write(r_1))
        self.wait(4.0) # "Dokuzu onlar basamağının altına yazıyoruz."
        
        # Final Sonuç Vurgusu
        self.play(r_1.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(r_2.animate.set_color('#FFFF00'))
        self.wait(4.0) # "İşlemimizin sonucu: doksan üç."
        
        # INSTAGRAM/SHORTS FIX
        self.wait(8.0)