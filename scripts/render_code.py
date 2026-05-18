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
        
        # BAŞLIK
        header = Paragraph(
            'KESİRLERDE\nTOPLAMA İŞLEMİ',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)
        
        # --- BLOK 1: BAŞLIK YAZILIYOR VE SES BEKLENİYOR ---
        self.play(Write(header), run_time=1.0)
        self.wait(6.0) # Merhaba, Maarif Matematik ekranlarına hoş geldin. Bugün farklı paydalara sahip kesirleri nasıl toplayacağımızı öğreneceğiz.
        
        # DENKLEM 1
        arti1 = MathTex('+', color='#FFFFFF').scale(1.8).move_to(UP * 2.0)
        cizgi1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(arti1, LEFT, buff=0.8)
        pay1 = MathTex('1', color='#FFFFFF').scale(1.8).next_to(cizgi1, UP, buff=0.3)
        payda1 = MathTex('2', color='#FFFFFF').scale(1.8).next_to(cizgi1, DOWN, buff=0.3)
        
        cizgi2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(arti1, RIGHT, buff=0.8)
        pay2 = MathTex('1', color='#FFFFFF').scale(1.8).next_to(cizgi2, UP, buff=0.3)
        payda2 = MathTex('3', color='#FFFFFF').scale(1.8).next_to(cizgi2, DOWN, buff=0.3)
        
        # --- BLOK 2: İLK DENKLEM GELİYOR ---
        self.play(Write(pay1), Create(cizgi1), Write(payda1), run_time=1.0)
        self.wait(1.0)
        self.play(Write(arti1), run_time=0.5)
        self.wait(1.0)
        self.play(Write(pay2), Create(cizgi2), Write(payda2), run_time=1.0)
        self.wait(5.0) # Örneğimiz: bir bölü iki artı, bir bölü üç.
        
        self.wait(3.0) # GEÇİŞ SİNYALİ
        
        # GENİŞLETME
        gen1 = MathTex('(3)', color='#FFFF00').scale(1.2).next_to(payda1, DOWN, buff=0.4)
        gen2 = MathTex('(2)', color='#00FFFF').scale(1.2).next_to(payda2, DOWN, buff=0.4)
        
        # --- BLOK 3: GENİŞLETME SAYILARI GELİYOR ---
        self.play(Write(gen1), run_time=0.8)
        self.wait(1.0)
        self.play(Write(gen2), run_time=0.8)
        self.wait(7.0) # Toplama yapabilmek için paydaların aynı olması gerekir. İlk kesrimizi üç ile, ikinci kesrimizi iki ile genişletelim.
        
        # DENKLEM 2 (Genişletilmiş)
        ok_asagi = MathTex('\\downarrow', color='#FFFFFF').scale(2.0).move_to(UP * 0.3)
        self.play(Write(ok_asagi), run_time=0.8)
        self.wait(1.0)
        
        arti2 = MathTex('+', color='#FFFFFF').scale(1.8).move_to(DOWN * 1.5)
        cizgi3 = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(arti2, LEFT, buff=0.8)
        pay3 = MathTex('3', color='#FFFF00').scale(1.8).next_to(cizgi3, UP, buff=0.3)
        payda3 = MathTex('6', color='#FFFF00').scale(1.8).next_to(cizgi3, DOWN, buff=0.3)
        
        # --- BLOK 4: BİRİNCİ KESİR GENİŞLİYOR ---
        self.play(Write(pay3), Create(cizgi3), Write(payda3), run_time=1.0)
        self.wait(6.0) # Birinci kesri üç ile genişlettiğimizde, yeni kesrimiz üç bölü altı olur.
        
        self.play(Write(arti2), run_time=0.5)
        self.wait(1.0)
        
        cizgi4 = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(arti2, RIGHT, buff=0.8)
        pay4 = MathTex('2', color='#00FFFF').scale(1.8).next_to(cizgi4, UP, buff=0.3)
        payda4 = MathTex('6', color='#00FFFF').scale(1.8).next_to(cizgi4, DOWN, buff=0.3)
        
        # --- BLOK 5: İKİNCİ KESİR GENİŞLİYOR ---
        self.play(Write(pay4), Create(cizgi4), Write(payda4), run_time=1.0)
        self.wait(6.0) # İkinci kesri iki ile genişlettiğimizde, yeni kesrimiz iki bölü altı olur.
        
        self.wait(3.0) # GEÇİŞ SİNYALİ
        
        # SONUÇ
        esit = MathTex('=', color='#FFFFFF').scale(2.2).move_to(LEFT * 1.5 + DOWN * 4.5)
        cizgi5 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.0).next_to(esit, RIGHT, buff=0.6)
        pay5 = MathTex('5', color='#FFFFFF').scale(2.5).next_to(cizgi5, UP, buff=0.3)
        payda5 = MathTex('6', color='#FFFFFF').scale(2.5).next_to(cizgi5, DOWN, buff=0.3)
        
        # --- BLOK 6: EŞİTTİR VE YENİ PAY GELİYOR ---
        self.play(Write(esit), run_time=0.5)
        self.wait(1.0)
        self.play(Create(cizgi5), Write(pay5), run_time=1.0)
        self.wait(6.0) # Şimdi paydalarımız eşit. Payları topluyoruz: üç, iki daha beş yapar.
        
        # --- BLOK 7: PAYDA VE KAPANIŞ ---
        self.play(Write(payda5), run_time=1.0)
        self.wait(7.0) # Payda ise değişmez, altı olarak kalır. Sonucumuz: beş bölü altı. Maarif Matematik ile öğrenmek işte bu kadar kolay!
        
        # SHORTS FIX
        self.wait(8.0)