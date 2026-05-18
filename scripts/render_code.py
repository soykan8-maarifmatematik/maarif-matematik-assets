from manim import * 
import numpy as np

# DIKEY FORMAT KESIN KILIT (9:16)
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class EvrenselKesirToplama(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # BAŞLIK
        header = Paragraph(
            'KESİRLERDE TOPLAMA\nİŞLEMİ',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)
        
        # --- BLOK 1: BAŞLIK YAZILIYOR ---
        self.play(Write(header))
        self.wait(1.0)
        self.wait(5.5) # 'Merhaba, Maarif Matematik ekranlarına hoş geldin...' bitene kadar bekler

        # ANA KESİR ELEMANLARI VE HİZALAMA (Merkez Odaklı)
        f2_line = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).move_to(ORIGIN)
        plus = MathTex('+', color='#FFFFFF').scale(1.8).next_to(f2_line, LEFT, buff=0.8)
        f1_line = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(plus, LEFT, buff=0.8)
        
        f1_pay = MathTex('1', color='#FFFFFF').scale(1.8).next_to(f1_line, UP, buff=0.3)
        f1_payda = MathTex('2', color='#FFFFFF').scale(1.8).next_to(f1_line, DOWN, buff=0.3)
        
        f2_pay = MathTex('1', color='#FFFFFF').scale(1.8).next_to(f2_line, UP, buff=0.3)
        f2_payda = MathTex('4', color='#FFFFFF').scale(1.8).next_to(f2_line, DOWN, buff=0.3)

        # --- BLOK 2: İLK KESİRLER EKRANA GELİYOR (ZİNCİRLEME YASAK) ---
        self.play(Create(f1_line))
        self.wait(1.0)
        self.play(Write(f1_pay))
        self.wait(1.0)
        self.play(Write(f1_payda))
        self.wait(1.0)
        
        self.play(Write(plus))
        self.wait(1.0)
        
        self.play(Create(f2_line))
        self.wait(1.0)
        self.play(Write(f2_pay))
        self.wait(1.0)
        self.play(Write(f2_payda))
        self.wait(1.0)
        self.wait(4.5) # 'Örneğimiz: bir bölü iki ile bir bölü dördü toplamak...' bitene kadar bekler

        # --- BLOK 3: PAYDALARA VURGU ---
        self.play(f1_payda.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(f2_payda.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.wait(5.0) # 'Ekranda gördüğün gibi, paydalarımız iki ve dört. Farklılar.' bitene kadar bekler

        # --- BLOK 4: GENİŞLETME ADIMI ---
        genisletme = MathTex('(2)', color='#00FFFF').scale(1.0).next_to(f1_payda, DOWN, buff=0.4)
        self.play(Write(genisletme))
        self.wait(1.0)
        self.wait(6.0) # 'Toplama yapabilmek için önce paydaları eşitlemeliyiz...' bitene kadar bekler

        # --- BLOK 5: ÇARPMA OKLARI ---
        ok_payda = CurvedArrow(genisletme.get_right(), f1_payda.get_right() + RIGHT*0.1, angle=-PI/2, color='#00FFFF')
        ok_pay = CurvedArrow(genisletme.get_left(), f1_pay.get_left() + LEFT*0.1, angle=PI/2, color='#00FFFF')
        
        self.play(Create(ok_payda))
        self.wait(1.0)
        self.play(Create(ok_pay))
        self.wait(1.0)
        self.wait(5.0) # 'Bunun için ilk kesrimizi iki ile genişletiyoruz...' bitene kadar bekler

        # --- BLOK 6: YENİ KESİR OLUŞUMU ---
        f1_new_pay = MathTex('2', color='#00FFFF').scale(1.8).move_to(f1_pay.get_center())
        f1_new_payda = MathTex('4', color='#00FFFF').scale(1.8).move_to(f1_payda.get_center())
        
        self.play(FadeOut(f1_pay), FadeOut(f1_payda), FadeOut(genisletme), FadeOut(ok_pay), FadeOut(ok_payda))
        self.wait(1.0)
        self.play(Write(f1_new_pay))
        self.wait(1.0)
        self.play(Write(f1_new_payda))
        self.wait(1.0)
        self.wait(6.0) # 'İki kere bir, iki yapar. İki kere iki, dört yapar...' bitene kadar bekler

        # GEÇİŞ SİNYALİ
        self.wait(3.0)

        # --- BLOK 7: SONUÇ ELEMANLARI (EN BÜYÜK ÖLÇEK) ---
        esit = MathTex('=', color='#FFFFFF').scale(1.8).next_to(f2_line, RIGHT, buff=0.8)
        f3_line = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(esit, RIGHT, buff=0.8)
        f3_pay = MathTex('3', color='#FFFF00').scale(2.5).next_to(f3_line, UP, buff=0.3)
        f3_payda = MathTex('4', color='#FFFFFF').scale(2.5).next_to(f3_line, DOWN, buff=0.3)

        self.play(Write(esit))
        self.wait(1.0)
        self.play(Create(f3_line))
        self.wait(1.0)
        self.play(Write(f3_pay))
        self.wait(1.0)
        self.wait(6.5) # 'Artık paydalarımız eşit. Payları topluyoruz...' bitene kadar bekler

        # --- BLOK 8: FİNAL PAYDA VE VEDA ---
        self.play(Write(f3_payda))
        self.wait(1.0)
        self.wait(6.0) # 'Payda ise değişmez, dört olarak kalır. Sonucumuz...' bitene kadar bekler

        # SHORTS / INSTAGRAM STATIC FIX
        self.wait(8.0)