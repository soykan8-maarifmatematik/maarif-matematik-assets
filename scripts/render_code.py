from manim import *

class MaarifKesirToplama(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        header = Paragraph(
            'KESİRLERDE TOPLAMA\nPAYDA EŞİTLEME',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        # 1. Kesir: 1/2
        f1_pay = MathTex('1', color='#FFFFFF').scale(2.0)
        f1_line = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.6)
        f1_payda = MathTex('2', color='#FFFFFF').scale(2.0)
        f1_pay.next_to(f1_line, UP, buff=0.2)
        f1_payda.next_to(f1_line, DOWN, buff=0.2)
        f1 = VGroup(f1_pay, f1_line, f1_payda)

        plus1 = MathTex('+', color='#FFFFFF').scale(2.0)

        # 2. Kesir: 1/4
        f2_pay = MathTex('1', color='#FFFFFF').scale(2.0)
        f2_line = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.6)
        f2_payda = MathTex('4', color='#FFFFFF').scale(2.0)
        f2_pay.next_to(f2_line, UP, buff=0.2)
        f2_payda.next_to(f2_line, DOWN, buff=0.2)
        f2 = VGroup(f2_pay, f2_line, f2_payda)

        # İlk İşlem Satırı
        eq1 = VGroup(f1, plus1, f2).arrange(RIGHT, buff=0.8).move_to(UP * 1.2)
        
        # Genişletme İşareti (2)
        exp2 = MathTex('(2)', color='#FFFF00').scale(1.2).next_to(f1_payda, DOWN, buff=0.2)

        # 2. İşlem Satırı: = 2/4 + 1/4
        eq_sign1 = MathTex('=', color='#FFFFFF').scale(2.0).next_to(eq1, DOWN, buff=1.2).align_to(plus1, LEFT)
        
        f3_pay = MathTex('2', color='#FFFF00').scale(2.0)
        f3_line = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.6)
        f3_payda = MathTex('4', color='#FFFF00').scale(2.0)
        f3_pay.next_to(f3_line, UP, buff=0.2)
        f3_payda.next_to(f3_line, DOWN, buff=0.2)
        f3 = VGroup(f3_pay, f3_line, f3_payda).next_to(eq_sign1, RIGHT, buff=0.5)

        plus2 = MathTex('+', color='#FFFFFF').scale(2.0).next_to(f3, RIGHT, buff=0.5)

        f4_pay = MathTex('1', color='#FFFFFF').scale(2.0)
        f4_line = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.6)
        f4_payda = MathTex('4', color='#FFFFFF').scale(2.0)
        f4_pay.next_to(f4_line, UP, buff=0.2)
        f4_payda.next_to(f4_line, DOWN, buff=0.2)
        f4 = VGroup(f4_pay, f4_line, f4_payda).next_to(plus2, RIGHT, buff=0.5)

        # 3. İşlem Satırı (Sonuç): = 3/4
        eq_sign2 = MathTex('=', color='#FFFFFF').scale(2.0).next_to(eq_sign1, DOWN, buff=1.5).align_to(eq_sign1, LEFT)
        
        f5_pay = MathTex('3', color='#00FFFF').scale(2.5)
        f5_line = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8)
        f5_payda = MathTex('4', color='#FFFFFF').scale(2.5)
        f5_pay.next_to(f5_line, UP, buff=0.2)
        f5_payda.next_to(f5_line, DOWN, buff=0.2)
        f5 = VGroup(f5_pay, f5_line, f5_payda).next_to(eq_sign2, RIGHT, buff=0.5)

        # --- ANİMASYON (SABIRLI SENKRON VE BLOK KİLİT) ---
        self.play(Write(header))
        self.wait(3.0)

        self.play(Write(f1_pay))
        self.wait(1.0)
        self.play(Write(f1_line))
        self.wait(1.0)
        self.play(Write(f1_payda))
        self.wait(1.0)
        self.play(Write(plus1))
        self.wait(1.0)
        self.play(Write(f2_pay))
        self.wait(1.0)
        self.play(Write(f2_line))
        self.wait(1.0)
        self.play(Write(f2_payda))
        self.wait(5.0)

        self.play(Write(exp2))
        self.wait(4.5)

        self.play(Write(eq_sign1))
        self.wait(1.0)
        self.play(Write(f3_line))
        self.wait(1.0)
        self.play(Write(f3_pay))
        self.wait(4.5)

        self.play(Write(f3_payda))
        self.wait(4.5)

        self.play(Write(plus2))
        self.wait(1.0)
        self.play(Write(f4_pay))
        self.wait(1.0)
        self.play(Write(f4_line))
        self.wait(1.0)
        self.play(Write(f4_payda))
        self.wait(5.0)

        # İkinci odak noktası: Payların toplanması (Turkuaz renk)
        self.play(f3_pay.animate.set_color('#00FFFF'))
        self.wait(1.0)
        self.play(f4_pay.animate.set_color('#00FFFF'))
        self.wait(5.0)

        self.play(Write(eq_sign2))
        self.wait(1.0)
        self.play(Write(f5_line))
        self.wait(1.0)
        self.play(Write(f5_pay))
        self.wait(4.5)

        self.play(Write(f5_payda))
        self.wait(5.0)

        self.wait(8.0)