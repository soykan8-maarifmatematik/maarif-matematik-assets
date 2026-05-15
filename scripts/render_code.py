from manim import *

class MaarifEldeliToplama(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # 1. GÖRSEL HİYERARŞİ: BAŞLIK STANDARTI
        header = Paragraph(
            'TOPLAMA İŞLEMİ\nELDE KAVRAMI',
            alignment='center',
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # DİKEY İŞLEM KURALI: Sayıları merkeze/sola çek (LEFT * 0.5)
        # ÖLÇEKLER: Ana sayılar scale(1.7)
        num1_7 = MathTex('7', color='#FFFFFF').scale(1.7).move_to(LEFT * 0.5 + UP * 0.5)
        num1_4 = MathTex('4', color='#FFFFFF').scale(1.7).next_to(num1_7, LEFT, buff=0.5)
        
        num2_5 = MathTex('5', color='#FFFFFF').scale(1.7).next_to(num1_7, DOWN, buff=0.5)
        num2_3 = MathTex('3', color='#FFFFFF').scale(1.7).next_to(num1_4, DOWN, buff=0.5)
        
        line = Line(num2_3.get_left() + LEFT * 0.5, num2_5.get_right() + RIGHT * 0.5, color='#FFFFFF')
        
        # TOPLAMA İŞARETİ KURALI: Sol üst boşluk, dikey hiza shift(UP * 0.4)
        plus = MathTex('+', color='#FFFFFF').scale(1.7).next_to(line, LEFT, buff=0.3).shift(UP * 0.4)
        
        # ÖLÇEKLER: Final sonuç vurgusu scale(1.8)
        # MİLMETRİK HİZALAMA: align_to ile tam alt alta kilitli
        res_2 = MathTex('2', color='#FFFF00').scale(1.8).next_to(line, DOWN, buff=0.5).align_to(num1_7, RIGHT)
        res_8 = MathTex('8', color='#FFFF00').scale(1.8).next_to(line, DOWN, buff=0.5).align_to(num1_4, RIGHT)
        
        # ÖLÇEKLER: Eldeler scale(0.8)
        elde_1 = MathTex('1', color='#00FFFF').scale(0.8).next_to(num1_4, UP, buff=0.4)

        # --- 2. KESİN SENKRON VE BLOK-KİLİT SİSTEMİ ---
        
        self.play(Write(header))
        self.wait(1.0)
        
        # ZİNCİRLEME YASAK: Her rakam tek başına yazılır.
        self.play(Write(num1_4))
        self.wait(1.0)
        self.play(Write(num1_7))
        self.wait(1.0)
        
        self.play(Write(num2_3))
        self.wait(1.0)
        self.play(Write(num2_5))
        self.wait(1.0)
        
        self.play(Write(line))
        self.wait(1.0)
        self.play(Write(plus))
        self.wait(4.0) # BLOK SONU BEKLEME (En az 4.0s)
        
        # Birler basamağı işlemi
        self.play(Write(res_2))
        self.wait(1.0)
        self.play(Write(elde_1))
        self.wait(4.0) # BLOK SONU BEKLEME
        
        # GEÇİŞ SİNYALİ: "Şimdi onlar basamağına geçiyoruz" için boş ekran beklemesi
        self.wait(3.0)
        
        # Onlar basamağı işlemi
        self.play(Write(res_8))
        self.wait(1.0)
        self.wait(4.5) # BLOK SONU BEKLEME
        
        # INSTAGRAM/SHORTS FIX: Statik bitiş beklemesi
        self.wait(8.0)