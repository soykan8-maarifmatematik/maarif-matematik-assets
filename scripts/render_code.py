from manim import *
import numpy as np

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class MaarifCarpmaIslemi(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # 1. BAŞLIK STANDARTI (V44 AYARLARIYLA KİLİTLİ)
        header = Paragraph(
            'ÇARPMA İŞLEMİ\nİKİ BASAMAKLI SAYILAR',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # 2. NESNE TANIMLARI VE MİLMETRİK YERLEŞİM (DİKEY İŞLEM KURALI)
        num1 = MathTex('3', '2', color='#FFFFFF').scale(1.7).move_to(LEFT * 0.5 + UP * 1.5)
        num2 = MathTex('1', '4', color='#FFFFFF').scale(1.7).next_to(num1, DOWN, buff=0.3)
        
        # İndex bazlı milimetrik kilitleme
        num2[1].align_to(num1[1], RIGHT)
        num2[0].align_to(num1[0], RIGHT)

        times_sign = MathTex('\\times', color='#FFFFFF').scale(1.7).next_to(num2, LEFT, buff=0.5)
        line1 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(num2, DOWN, buff=0.2).align_to(num2, RIGHT).shift(RIGHT * 0.5)

        # 1. Satır Sonucu (32 x 4 = 128)
        res1 = MathTex('1', '2', '8', color='#FFFF00').scale(1.7).next_to(line1, DOWN, buff=0.3)
        res1[2].align_to(num2[1], RIGHT)
        res1[1].align_to(num2[0], RIGHT)
        res1[0].next_to(res1[1], LEFT, buff=0.15)

        # 2. Satır Sonucu (32 x 1 = 32) - Sola kaydırma kilitli
        res2 = MathTex('3', '2', color='#00FFFF').scale(1.7).next_to(res1, DOWN, buff=0.3)
        res2[1].align_to(num2[0], RIGHT) # Onlar basamağının altına kilitli
        res2[0].align_to(res1[0], RIGHT)

        # Toplama İşareti ve Çizgisi (Kurala uygun shift)
        line2 = Line(LEFT, RIGHT, color='#FFFFFF').scale(1.5).next_to(res2, DOWN, buff=0.2).align_to(res2, RIGHT).shift(RIGHT * 0.5)
        plus_sign = MathTex('+', color='#FFFFFF').scale(1.7).next_to(line2, LEFT, buff=0.2).shift(UP * 0.4)

        # Final Sonuç (448) - Ölçek 1.8
        final_res = MathTex('4', '4', '8', color='#FFFFFF').scale(1.8).next_to(line2, DOWN, buff=0.3)
        final_res[2].align_to(res1[2], RIGHT)
        final_res[1].align_to(res2[1], RIGHT)
        final_res[0].align_to(res2[0], RIGHT)

        # --- ANİMASYON AKIŞI (BLOK-KİLİT VE SABIRLI SENKRON) ---
        self.play(Write(header))
        self.wait(1.0)

        # Üst sayının yazımı (Zincirleme yasak)
        self.play(Write(num1[0]))
        self.wait(1.0)
        self.play(Write(num1[1]))
        self.wait(1.0)

        # Alt sayının yazımı
        self.play(Write(num2[0]))
        self.wait(1.0)
        self.play(Write(num2[1]))
        self.wait(1.0)

        # Çizgi ve işaret
        self.play(Write(times_sign))
        self.wait(1.0)
        self.play(Write(line1))
        self.wait(4.0) # Blok sonu bekleme

        # Geçiş Sinyali (Birler basamağına geçiş)
        self.wait(3.0)

        # 1. Çarpım Aşaması
        self.play(num2[1].animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(Write(res1[2]))
        self.wait(1.0)
        self.play(Write(res1[1]))
        self.wait(1.0)
        self.play(Write(res1[0]))
        self.wait(4.0) # Blok sonu bekleme

        # Geçiş Sinyali (Onlar basamağına geçiş)
        self.wait(3.0)

        # 2. Çarpım Aşaması
        self.play(num2[1].animate.set_color('#FFFFFF'))
        self.wait(1.0)
        self.play(num2[0].animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.play(Write(res2[1]))
        self.wait(1.0)
        self.play(Write(res2[0]))
        self.wait(4.0) # Blok sonu bekleme

        # Geçiş Sinyali (Toplama işlemine geçiş)
        self.wait(3.0)

        # Toplama Aşaması
        self.play(Write(plus_sign))
        self.wait(1.0)
        self.play(Write(line2))
        self.wait(1.0)

        # Final Sonucunun Yazımı
        self.play(Write(final_res[2]))
        self.wait(1.0)
        self.play(Write(final_res[1]))
        self.wait(1.0)
        self.play(Write(final_res[0]))
        self.wait(4.0) # Blok sonu bekleme

        # Final Vurgusu
        self.play(final_res.animate.set_color('#FFFF00'))
        
        # INSTAGRAM/SHORTS FIX (Statik Bekleme)
        self.wait(8.0)