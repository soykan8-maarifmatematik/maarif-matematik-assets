from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0

class KesirDonusum(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        # BAŞLIK
        header = Paragraph(
            'TAM SAYILI KESRİ',
            'BİLEŞİK KESRE ÇEVİRME',
            alignment='center',
            weight=BOLD
        ).scale_to_fit_width(8.0).to_edge(UP, buff=0.5)
        
        self.play(Write(header), run_time=0.8)
        self.wait(0.5)

        # İLK KESİR (2 3/4)
        tam = MathTex('2').scale(2.5)
        cizgi = Line(LEFT, RIGHT).scale(0.8).next_to(tam, RIGHT, buff=0.3)
        pay = MathTex('3').scale(2.0).next_to(cizgi, UP, buff=0.3)
        payda = MathTex('4').scale(2.0).next_to(cizgi, DOWN, buff=0.3)
        
        kesir_group = VGroup(tam, cizgi, pay, payda).move_to(UP * 2.5)

        self.play(Write(kesir_group), run_time=0.8)
        self.wait(0.5)

        # ÇARPMA İŞLEMİ (4 * 2)
        ok_carp = CurvedArrow(payda.get_bottom() + DOWN*0.2, tam.get_bottom() + DOWN*0.2, angle=PI/1.5, color='#FFFF00')
        isaret_carp = MathTex('\\times', color='#FFFF00').scale(1.5).next_to(ok_carp, DOWN, buff=0.2)
        
        self.play(Create(ok_carp), Write(isaret_carp), run_time=0.6)
        self.play(
            payda.animate.set_color('#FFFF00').scale(1.2),
            tam.animate.set_color('#FFFF00').scale(1.2),
            run_time=0.4
        )
        self.play(
            payda.animate.scale(1/1.2),
            tam.animate.scale(1/1.2),
            run_time=0.3
        )
        self.wait(0.5)

        # TOPLAMA İŞLEMİ (8 + 3)
        ok_topla = CurvedArrow(tam.get_top() + UP*0.2, pay.get_top() + UP*0.2, angle=-PI/1.5, color='#00FFFF')
        isaret_topla = MathTex('+', color='#00FFFF').scale(1.5).next_to(ok_topla, UP, buff=0.2)

        self.play(Create(ok_topla), Write(isaret_topla), run_time=0.6)
        self.play(
            pay.animate.set_color('#00FFFF').scale(1.2),
            run_time=0.4
        )
        self.play(
            pay.animate.scale(1/1.2),
            run_time=0.3
        )
        self.wait(0.5)

        # SONUÇ BÖLÜMÜ (DİKEY HİYERARŞİ)
        ust_grup = VGroup(kesir_group, ok_carp, isaret_carp, ok_topla, isaret_topla)
        
        esit = MathTex('=').scale(2.5).next_to(ust_grup, DOWN, buff=1.0)
        f_cizgi = Line(LEFT, RIGHT).scale(1.2).next_to(esit, DOWN, buff=1.0)
        f_pay = MathTex('11', color='#00FFFF').scale(2.5).next_to(f_cizgi, UP, buff=0.3)
        f_payda = MathTex('4', color='#FFFF00').scale(2.5).next_to(f_cizgi, DOWN, buff=0.3)

        self.play(Write(esit), run_time=0.5)
        self.play(Create(f_cizgi), run_time=0.4)
        
        # Yeni Pay (11)
        self.play(Write(f_pay), run_time=0.5)
        self.play(f_pay.animate.scale(1.2), run_time=0.3)
        self.play(f_pay.animate.scale(1/1.2), run_time=0.3)
        self.wait(0.5)

        # Yeni Payda (4)
        self.play(Write(f_payda), run_time=0.5)
        self.wait(0.5)

        # SHORTS DÖNGÜ BEKLEMESİ (SADECE 1.5 SN)
        self.wait(1.5)