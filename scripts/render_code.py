from manim import *
import numpy as np

# DIKEY FORMAT KESIN KILIT (9:16)
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class DenklemCozumuDikeyV52(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # Başlık Standartı (V52 Agnostik)
        header = Paragraph(
            'BİRİNCİ DERECEDEN\nDENKLEM ÇÖZÜMÜ',
            alignment='center',
            line_spacing=0.8,
            color='#FFFFFF',
            weight=BOLD
        ).scale_to_fit_width(7.0).to_edge(UP, buff=1.1)

        self.play(Write(header))
        self.wait(4.5)

        # 1. Aşama: Denklem Kurulumu
        two_1 = MathTex('2', color='#FFFFFF').scale(2.0)
        x_1 = MathTex('x', color='#FFFFFF').scale(2.0)
        term1 = VGroup(two_1, x_1).arrange(RIGHT, buff=0.1)
        plus = MathTex('+', color='#FFFFFF').scale(2.0)
        four = MathTex('4', color='#FFFFFF').scale(2.0)
        eq1 = MathTex('=', color='#FFFFFF').scale(2.0)
        ten = MathTex('10', color='#FFFFFF').scale(2.0)
        
        eq_group1 = VGroup(term1, plus, four, eq1, ten).arrange(RIGHT, buff=0.4).move_to(UP * 3.0)

        # Zincirleme Yasak - Tek Tek Yazım
        self.play(Write(two_1))
        self.wait(1.0)
        self.play(Write(x_1))
        self.wait(1.0)
        self.play(Write(plus))
        self.wait(1.0)
        self.play(Write(four))
        self.wait(1.0)
        self.play(Write(eq1))
        self.wait(1.0)
        self.play(Write(ten))
        self.wait(4.5)

        # 2. Aşama: +4'ü Karşıya Atma (Sarı Vurgu)
        self.play(plus.animate.set_color('#FFFF00'))
        self.wait(1.0)
        self.play(four.animate.set_color('#FFFF00'))
        self.wait(4.5)

        cross = Cross(VGroup(plus, four), stroke_color='#FF0000')
        self.play(Create(cross))
        self.wait(1.0)

        minus_four = MathTex('-4', color='#FFFF00').scale(2.0).next_to(ten, RIGHT, buff=0.4)
        self.play(Write(minus_four))
        self.wait(4.5)

        # Geçiş Sinyali
        self.wait(3.0)

        # 3. Aşama: Yeni Denklem (2x = 6)
        two_2 = MathTex('2', color='#FFFFFF').scale(2.0)
        x_2 = MathTex('x', color='#FFFFFF').scale(2.0)
        term2 = VGroup(two_2, x_2).arrange(RIGHT, buff=0.1)
        eq2 = MathTex('=', color='#FFFFFF').scale(2.0)
        six = MathTex('6', color='#FFFF00').scale(2.0)
        
        eq_group2 = VGroup(term2, eq2, six).arrange(RIGHT, buff=0.4).next_to(eq_group1, DOWN, buff=2.0)

        self.play(Write(two_2))
        self.wait(1.0)
        self.play(Write(x_2))
        self.wait(1.0)
        self.play(Write(eq2))
        self.wait(1.0)
        self.play(Write(six))
        self.wait(4.5)

        # Geçiş Sinyali
        self.wait(3.0)

        # 4. Aşama: 2'ye Bölme (Turkuaz Vurgu)
        self.play(two_2.animate.set_color('#00FFFF'))
        self.wait(4.5)

        div_line = Line(LEFT, RIGHT, color='#FFFFFF').scale(0.8).next_to(six, DOWN, buff=0.2)
        div_two = MathTex('2', color='#00FFFF').scale(1.5).next_to(div_line, DOWN, buff=0.2)

        self.play(Write(div_line))
        self.wait(1.0)
        self.play(Write(div_two))
        self.wait(4.5)

        # Geçiş Sinyali
        self.wait(3.0)

        # 5. Aşama: Final Sonucu (En Büyük Ölçek)
        x_3 = MathTex('x', color='#FFFFFF').scale(2.5)
        eq3 = MathTex('=', color='#FFFFFF').scale(2.5)
        three = MathTex('3', color='#00FFFF').scale(2.5)
        
        eq_group3 = VGroup(x_3, eq3, three).arrange(RIGHT, buff=0.5).next_to(eq_group2, DOWN, buff=2.5)

        self.play(Write(x_3))
        self.wait(1.0)
        self.play(Write(eq3))
        self.wait(1.0)
        self.play(Write(three))
        self.wait(4.5)

        # Shorts/Instagram Fix - Kapanış Beklemesi
        self.wait(8.0)