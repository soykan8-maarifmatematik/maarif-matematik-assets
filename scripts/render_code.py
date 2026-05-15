from manim import *
import numpy as np

# DIKEY FORMAT KESIN KILIT (9:16)
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class KesirlerdeToplamaEvrensel(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # 1. BAŞLIK STANDARTI (V52)
        header = Paragraph(
            'FARKLI PAYDALI KESİRLERDE\nTOPLAMA İŞLEMİ',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # 2. ANA DENKLEM (1/2 + 1/3) - YATAY İŞLEM MERKEZ ODAĞI
        arti = MathTex('+', color='#FFFFFF').scale(2.0).move_to(UP * 3.0)
        
        cizgi1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(arti, LEFT, buff=1.0)
        pay1 = MathTex('1', color='#FFFFFF').scale(2.0).next_to(cizgi1, UP, buff=0.3)
        payda1 = MathTex('2', color='#FFFFFF').scale(2.0).next_to(cizgi1, DOWN, buff=0.3)
        
        cizgi2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(arti, RIGHT, buff=1.0)
        pay2 = MathTex('1', color='#FFFFFF').scale(2.0).next_to(cizgi2, UP, buff=0.3)
        payda2 = MathTex('3', color='#FFFFFF').scale(2.0).next_to(cizgi2, DOWN, buff=0.3)

        # 3. GENİŞLETME SAYILARI (Yardımcı Vurgular - Sarı ve Turkuaz)
        gen1 = MathTex('(3)', color='#FFFF00').scale(1.0).next_to(payda1, DOWN, buff=0.5)
        gen2 = MathTex('(2)', color='#00FFFF').scale(1.0).next_to(payda2, DOWN, buff=0.5)

        # 4. GENİŞLETİLMİŞ DENKLEM (3/6 + 2/6)
        y_arti = MathTex('+', color='#FFFFFF').scale(2.0).move_to(ORIGIN)
        
        y_cizgi1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(y_arti, LEFT, buff=1.0)
        y_pay1 = MathTex('3', color='#FFFF00').scale(2.0).next_to(y_cizgi1, UP, buff=0.3)
        y_payda1 = MathTex('6', color='#FFFF00').scale(2.0).next_to(y_cizgi1, DOWN, buff=0.3)
        
        y_cizgi2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(y_arti, RIGHT, buff=1.0)
        y_pay2 = MathTex('2', color='#00FFFF').scale(2.0).next_to(y_cizgi2, UP, buff=0.3)
        y_payda2 = MathTex('6', color='#00FFFF').scale(2.0).next_to(y_cizgi2, DOWN, buff=0.3)

        # 5. FİNAL SONUCU (= 5/6) - EN BÜYÜK ÖLÇEK
        esittir = MathTex('=', color='#FFFFFF').scale(2.5).move_to(DOWN * 3.0 + LEFT * 1.5)
        
        f_cizgi = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.2).next_to(esittir, RIGHT, buff=0.8)
        f_pay = MathTex('5', color='#FFFFFF').scale(2.5).next_to(f_cizgi, UP, buff=0.3)
        f_payda = MathTex('6', color='#FFFFFF').scale(2.5).next_to(f_cizgi, DOWN, buff=0.3)

        # --- ANİMASYON AKIŞI (V52 BLOK-KİLİT SENKRON) ---
        self.play(Write(header))
        self.wait(4.5) # Giriş cümlesini bekle
        
        # ZİNCİRLEME YASAK: Her parça tek başına
        self.play(Write(pay1))
        self.play(Create(cizgi1))
        self.play(Write(payda1))
        self.wait(1.0) # Görsel parça sonrası es
        
        self.play(Write(arti))
        self.wait(1.0)
        
        self.play(Write(pay2))
        self.play(Create(cizgi2))
        self.play(Write(payda2))
        self.wait(5.0) # Örneği tanıtmasını bekle

        # Payda eşitleme açıklaması
        self.wait(4.5) # "Kesirlerde toplama yapabilmek için..."
        self.wait(5.0) # "Bu yüzden paydaları eşitliyoruz..."

        # Genişletme (Sarı ve Turkuaz)
        self.play(Write(gen1))
        self.wait(1.0)
        self.play(Write(gen2))
        self.wait(5.0) # Genişletme açıklamasını bekle

        # Birinci kesrin genişletilmesi (Sarı Vurgu)
        self.play(Write(y_pay1))
        self.play(Create(y_cizgi1))
        self.play(Write(y_payda1))
        self.wait(5.0) # "Üç kere bir üç..."
        
        self.wait(3.0) # "Birinci kesrimiz üç bölü altı oldu."
        self.wait(3.0) # GEÇİŞ SİNYALİ: "Şimdi ikinci kesre bakalım."

        # İkinci kesrin genişletilmesi (Turkuaz Vurgu)
        self.play(Write(y_arti))
        self.wait(1.0)
        self.play(Write(y_pay2))
        self.play(Create(y_cizgi2))
        self.play(Write(y_payda2))
        self.wait(5.0) # "İki kere bir iki..."
        
        self.wait(4.5) # "Artık paydalarımız eşit."

        # Final Sonucu
        self.play(Write(esittir))
        self.wait(1.0)
        self.play(Write(f_pay))
        self.play(Create(f_cizgi))
        self.wait(5.0) # Payların toplanması açıklaması
        
        self.play(Write(f_payda))
        self.wait(4.5) # Paydanın sabit kalması açıklaması

        self.wait(5.0) # Kapanış cümlesi
        
        # INSTAGRAM/SHORTS FIX: Kapanış Beklemesi
        self.wait(8.0)