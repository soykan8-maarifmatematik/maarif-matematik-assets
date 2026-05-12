from manim import *
import numpy as np

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # Başlık Standartı (V44 Mühürlü)
        header = Paragraph(
            'ÇARPMA İŞLEMİ\nİKİ BASAMAKLI SAYILAR',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # Koordinat Bazlı Milimetrik Hizalama (Merkez -0.5 olacak şekilde ayarlandı)
        num1_3 = MathTex('3', color='#FFFFFF').scale(1.7).move_to(RIGHT * 0.0 + UP * 1.5)
        num1_4 = MathTex('4', color='#FFFFFF').scale(1.7).move_to(RIGHT * 1.0 + UP * 1.5)
        
        num2_x = MathTex('\\times', color='#FFFFFF').scale(1.7).move_to(RIGHT * -2.0 + UP * 0.5)
        num2_1 = MathTex('1', color='#FFFFFF').scale(1.7).move_to(RIGHT * 0.0 + UP * 0.5)
        num2_2 = MathTex('2', color='#FFFFFF').scale(1.7).move_to(RIGHT * 1.0 + UP * 0.5)
        
        line1 = Line(LEFT * 2.5, RIGHT * 1.5, color='#FFFFFF').move_to(UP * -0.2)
        
        # 1. Satır Çarpım Sonucu (34 x 2 = 68)
        row1_6 = MathTex('6', color='#FFFF00').scale(1.7).move_to(RIGHT * 0.0 + UP * -1.0)
        row1_8 = MathTex('8', color='#FFFF00').scale(1.7).move_to(RIGHT * 1.0 + UP * -1.0)
        
        # 2. Satır Çarpım Sonucu (34 x 1 = 34) - Sola Kaydırılmış Milimetrik Kilit
        row2_3 = MathTex('3', color='#00FFFF').scale(1.7).move_to(RIGHT * -1.0 + UP * -2.0)
        row2_4 = MathTex('4', color='#00FFFF').scale(1.7).move_to(RIGHT * 0.0 + UP * -2.0)
        
        # Toplama Çizgisi ve İşareti (+ işareti shift(UP * 0.4) kuralı)
        line2 = Line(LEFT * 2.5, RIGHT * 1.5, color='#FFFFFF').move_to(UP * -2.7)
        plus_sign = MathTex('+', color='#FFFFFF').scale(1.7).next_to(line2, LEFT, buff=0.2).shift(UP * 0.4)
        
        # Final Sonuç (408) ve Elde
        res_4 = MathTex('4', color='#FFFFFF').scale(1.8).move_to(RIGHT * -1.0 + UP * -3.5)
        res_0 = MathTex('0', color='#FFFFFF').scale(1.8).move_to(RIGHT * 0.0 + UP * -3.5)
        res_8 = MathTex('8', color='#FFFFFF').scale(1.8).move_to(RIGHT * 1.0 + UP * -3.5)
        
        elde_1 = MathTex('1', color='#FFFF00').scale(0.8).move_to(RIGHT * -1.0 + UP * -1.2)

        # --- ANİMASYON AKIŞI (TAM SENKRON KİLİDİ) ---
        self.play(Write(header))
        self.wait(3.0)
        
        # Ana Sayıların Yazımı (Zincirleme Yasak)
        self.play(Write(num1_3))
        self.wait(1.0)
        self.play(Write(num1_4))
        self.wait(1.0)
        self.play(Write(num2_x))
        self.wait(1.0)
        self.play(Write(num2_1))
        self.wait(1.0)
        self.play(Write(num2_2))
        self.wait(1.0)
        self.play(Write(line1))
        self.wait(4.0) # Blok Sonu Bekleme

        # 1. Aşama: 2 ile Çarpma
        self.play(num2_2.animate.set_color('#FFFF00'), num1_4.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(Write(row1_8))
        self.wait(1.0)
        
        self.play(num1_4.animate.set_color('#FFFFFF'), num1_3.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(Write(row1_6))
        self.wait(1.0)
        
        self.play(num2_2.animate.set_color('#FFFFFF'), num1_3.animate.set_color('#FFFFFF'))
        self.wait(3.0) # Geçiş Sinyali Beklemesi

        # 2. Aşama: 1 ile Çarpma
        self.play(num2_1.animate.set_color('#00FFFF'), num1_4.animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.play(Write(row2_4))
        self.wait(1.0)
        
        self.play(num1_4.animate.set_color('#FFFFFF'), num1_3.animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.play(Write(row2_3))
        self.wait(1.0)
        
        self.play(num2_1.animate.set_color('#FFFFFF'), num1_3.animate.set_color('#FFFFFF'))
        self.wait(4.0) # Blok Sonu Bekleme

        # 3. Aşama: Toplama İşlemi
        self.play(Write(plus_sign))
        self.wait(1.0)
        self.play(Write(line2))
        self.wait(1.0)
        
        self.play(Write(res_8))
        self.wait(1.0)
        
        self.play(Write(res_0))
        self.wait(1.0)
        
        self.play(Write(elde_1))
        self.wait(1.0)
        
        self.play(Write(res_4))
        self.wait(4.0) # Blok Sonu Bekleme

        # Final Vurgusu
        self.play(res_4.animate.set_color('#FFFF00'), res_0.animate.set_color('#FFFF00'), res_8.animate.set_color('#FFFF00'))
        
        # Statik Bekleme (Instagram/Shorts Fix)
        self.wait(8.0)