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
        
        # 1. BAŞLIK (V52 Standart)
        header = Paragraph(
            'KESİRLERDE\\nTOPLAMA İŞLEMİ',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # 2. İLK DENKLEM (1/2 + 1/3)
        pay1 = MathTex('1', color='#FFFFFF').scale(2.0)
        cizgi1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(pay1, DOWN, buff=0.3)
        payda1 = MathTex('2', color='#FFFFFF').scale(2.0).next_to(cizgi1, DOWN, buff=0.3)
        kesir1 = VGroup(pay1, cizgi1, payda1).move_to(LEFT * 2.0 + UP * 2.5)

        arti1 = MathTex('+', color='#FFFFFF').scale(2.0).next_to(kesir1, RIGHT, buff=0.8)

        pay2 = MathTex('1', color='#FFFFFF').scale(2.0)
        cizgi2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(pay2, DOWN, buff=0.3)
        payda2 = MathTex('3', color='#FFFFFF').scale(2.0).next_to(cizgi2, DOWN, buff=0.3)
        kesir2 = VGroup(pay2, cizgi2, payda2).next_to(arti1, RIGHT, buff=0.8)

        # Genişletme Vurguları (Sarı ve Turkuaz)
        genislet1 = MathTex('(3)', color='#FFFF00').scale(1.2).next_to(payda1, DOWN, buff=0.4)
        genislet2 = MathTex('(2)', color='#00FFFF').scale(1.2).next_to(payda2, DOWN, buff=0.4)

        # 3. İKİNCİ DENKLEM (3/6 + 2/6)
        esit1 = MathTex('=', color='#FFFFFF').scale(2.0).next_to(kesir1, DOWN, buff=2.5).align_to(kesir1, LEFT)
        
        y_pay1 = MathTex('3', color='#FFFF00').scale(2.0)
        y_cizgi1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(y_pay1, DOWN, buff=0.3)
        y_payda1 = MathTex('6', color='#FFFF00').scale(2.0).next_to(y_cizgi1, DOWN, buff=0.3)
        y_kesir1 = VGroup(y_pay1, y_cizgi1, y_payda1).next_to(esit1, RIGHT, buff=0.8)

        arti2 = MathTex('+', color='#FFFFFF').scale(2.0).next_to(y_kesir1, RIGHT, buff=0.8)

        y_pay2 = MathTex('2', color='#00FFFF').scale(2.0)
        y_cizgi2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(y_pay2, DOWN, buff=0.3)
        y_payda2 = MathTex('6', color='#00FFFF').scale(2.0).next_to(y_cizgi2, DOWN, buff=0.3)
        y_kesir2 = VGroup(y_pay2, y_cizgi2, y_payda2).next_to(arti2, RIGHT, buff=0.8)

        # 4. SONUÇ (= 5/6)
        esit2 = MathTex('=', color='#FFFFFF').scale(2.5).next_to(esit1, DOWN, buff=2.5).align_to(esit1, LEFT)
        
        s_pay = MathTex('5', color='#FFFFFF').scale(2.5)
        s_cizgi = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.0).next_to(s_pay, DOWN, buff=0.3)
        s_payda = MathTex('6', color='#FFFFFF').scale(2.5).next_to(s_cizgi, DOWN, buff=0.3)
        sonuc = VGroup(s_pay, s_cizgi, s_payda).next_to(esit2, RIGHT, buff=0.8)

        # --- ANİMASYON AKIŞI (SENKRON KİLİTLİ) ---
        self.play(Write(header))
        self.wait(5.0) # Giriş cümlesini bekle
        
        # İlk kesirlerin yazımı
        self.play(Write(pay1))
        self.wait(1.0)
        self.play(Write(cizgi1))
        self.wait(1.0)
        self.play(Write(payda1))
        self.wait(1.0)
        self.play(Write(arti1))
        self.wait(1.0)
        self.play(Write(pay2))
        self.wait(1.0)
        self.play(Write(cizgi2))
        self.wait(1.0)
        self.play(Write(payda2))
        self.wait(5.0) # Örneği okumasını bekle

        self.wait(3.0) # Geçiş Sinyali: Payda eşitleme kuralı açıklaması

        # Genişletme adımları
        self.play(Write(genislet1))
        self.wait(5.0) # Birinci kesri genişletme açıklaması
        
        self.play(Write(genislet2))
        self.wait(5.0) # İkinci kesri genişletme açıklaması

        self.wait(3.0) # Geçiş Sinyali: Genişletilmiş hallere geçiş

        # İkinci denklem yazımı
        self.play(Write(esit1))
        self.wait(1.0)
        self.play(Write(y_pay1))
        self.wait(1.0)
        self.play(Write(y_cizgi1))
        self.wait(1.0)
        self.play(Write(y_payda1))
        self.wait(4.5) # Birinci kesrin yeni hali

        self.play(Write(arti2))
        self.wait(1.0)
        self.play(Write(y_pay2))
        self.wait(1.0)
        self.play(Write(y_cizgi2))
        self.wait(1.0)
        self.play(Write(y_payda2))
        self.wait(4.5) # İkinci kesrin yeni hali

        self.wait(3.0) # Geçiş Sinyali: Toplama işlemine geçiş

        # Sonuç yazımı
        self.play(Write(esit2))
        self.wait(1.0)
        self.play(Write(s_pay))
        self.wait(1.0)
        self.play(Write(s_cizgi))
        self.wait(1.0)
        self.play(Write(s_payda))
        self.wait(6.0) # Sonuç açıklaması ve veda

        # Kapanış statik bekleme
        self.wait(8.0)