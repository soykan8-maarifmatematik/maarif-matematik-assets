from manim import *
import numpy as np

# DIKEY FORMAT KESIN KILIT (9:16)
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class KesirlerdeToplama(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # Başlık (V52 Agnostik Standart)
        header = Paragraph(
            'KESİRLERDE\nTOPLAMA İŞLEMİ',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # --- 1. SATIR: 1/2 + 1/3 ---
        f1_pay = MathTex('1', color='#FFFFFF').scale(2.0).move_to(UP * 3.6 + LEFT * 1.5)
        f1_cizgi = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).move_to(UP * 3.0 + LEFT * 1.5)
        f1_payda = MathTex('2', color='#FFFFFF').scale(2.0).move_to(UP * 2.4 + LEFT * 1.5)
        
        plus_sign = MathTex('+', color='#FFFFFF').scale(2.0).move_to(UP * 3.0)
        
        f2_pay = MathTex('1', color='#FFFFFF').scale(2.0).move_to(UP * 3.6 + RIGHT * 1.5)
        f2_cizgi = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).move_to(UP * 3.0 + RIGHT * 1.5)
        f2_payda = MathTex('3', color='#FFFFFF').scale(2.0).move_to(UP * 2.4 + RIGHT * 1.5)

        # Genişletme Vurguları
        gen1 = MathTex('(3)', color='#FFFF00').scale(1.0).next_to(f1_payda, DOWN, buff=0.3)
        gen2 = MathTex('(2)', color='#00FFFF').scale(1.0).next_to(f2_payda, DOWN, buff=0.3)

        # --- 2. SATIR: = 3/6 + 2/6 ---
        row2_eq = MathTex('=', color='#FFFFFF').scale(2.0).move_to(LEFT * 2.0)
        
        ef1_pay = MathTex('3', color='#FFFF00').scale(2.0).move_to(UP * 0.6)
        ef1_cizgi = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).move_to(ORIGIN)
        ef1_payda = MathTex('6', color='#FFFF00').scale(2.0).move_to(DOWN * 0.6)
        
        eplus = MathTex('+', color='#FFFFFF').scale(2.0).move_to(RIGHT * 1.5)
        
        ef2_pay = MathTex('2', color='#00FFFF').scale(2.0).move_to(UP * 0.6 + RIGHT * 3.0)
        ef2_cizgi = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).move_to(RIGHT * 3.0)
        ef2_payda = MathTex('6', color='#00FFFF').scale(2.0).move_to(DOWN * 0.6 + RIGHT * 3.0)

        # --- 3. SATIR: = 5/6 (Final Sonuç) ---
        row3_eq = MathTex('=', color='#FFFFFF').scale(2.0).move_to(DOWN * 3.0 + LEFT * 2.0)
        
        res_pay = MathTex('5', color='#FFFFFF').scale(2.5).move_to(DOWN * 2.2)
        res_cizgi = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.0).move_to(DOWN * 3.0)
        res_payda = MathTex('6', color='#FFFFFF').scale(2.5).move_to(DOWN * 3.8)

        # --- ANİMASYON AKIŞI (TAM SENKRON VE ZİNCİRLEME YASAKLI) ---
        self.play(Write(header))
        self.wait(5.0) # Merhaba, bugün birlikte paydaları farklı olan iki kesri toplamayı öğreniyoruz.
        
        self.play(Write(f1_pay))
        self.wait(1.0)
        self.play(Write(f1_cizgi))
        self.wait(1.0)
        self.play(Write(f1_payda))
        self.wait(1.0)
        self.play(Write(plus_sign))
        self.wait(1.0)
        self.play(Write(f2_pay))
        self.wait(1.0)
        self.play(Write(f2_cizgi))
        self.wait(1.0)
        self.play(Write(f2_payda))
        self.wait(5.0) # Örneğimiz: bir bölü iki artı bir bölü üç. Dikkatle izle.
        
        self.wait(5.0) # Toplama yapabilmek için alt kısımdaki paydaların aynı olması gerekir.
        
        self.play(Write(gen1))
        self.wait(4.5) # İlk adımda, birinci kesrimizi üç ile genişletiyoruz.
        
        self.play(Write(row2_eq))
        self.wait(1.0)
        self.play(Write(ef1_pay))
        self.wait(1.0)
        self.play(Write(ef1_cizgi))
        self.wait(1.0)
        self.play(Write(ef1_payda))
        self.wait(5.0) # Üç kere bir, üç yapar. Üç kere iki, altı yapar.
        
        self.wait(4.5) # Yeni kesrimiz üç bölü altı oldu.
        
        self.play(Write(gen2))
        self.wait(4.5) # Şimdi ikinci kesrimizi iki ile genişletiyoruz.
        
        self.play(Write(eplus))
        self.wait(1.0)
        self.play(Write(ef2_pay))
        self.wait(1.0)
        self.play(Write(ef2_cizgi))
        self.wait(1.0)
        self.play(Write(ef2_payda))
        self.wait(5.0) # İki kere bir, iki yapar. İki kere üç, altı yapar.
        
        self.wait(4.5) # Bu kesrimiz de iki bölü altı oldu.
        
        self.wait(5.0) # Artık paydalarımız aynı olduğuna göre üst kısımları toplayabiliriz.
        
        self.play(Write(row3_eq))
        self.wait(1.0)
        self.play(Write(res_pay))
        self.wait(4.5) # Üç, iki daha, beş yapar.
        
        self.play(Write(res_cizgi))
        self.wait(1.0)
        self.play(Write(res_payda))
        self.wait(4.5) # Paydamız olan altı ise aynen kalır.
        
        self.play(res_pay.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(res_payda.animate.set_color('#00FFFF'))
        self.wait(5.0) # Sonucumuz: beş bölü altı. İşte bu kadar kolay!

        self.wait(8.0) # Statik kapanış beklemesi
