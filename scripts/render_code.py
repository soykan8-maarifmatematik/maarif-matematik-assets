from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # GİRİŞ SAHNESİ
        self.wait(2)
        intro_text = VGroup(
            Text("MAARİF MATEMATİK", color="#002B4D", weight=BOLD).scale(1.2),
            Text("Kesir Dönüşümlerinin Mantığı", color="#007BFF").scale(0.9)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(intro_text), run_time=2)
        self.wait(21)
        self.play(FadeOut(intro_text), run_time=1)
        self.wait(2)
        
        # BÖLÜM 1: TAM SAYILI KESRİ BİLEŞİK KESRE ÇEVİRME
        def make_whole():
            return VGroup(*[Sector(angle=PI/2, start_angle=i*PI/2, radius=0.8, color="#007BFF", stroke_color="#FFFFFF", stroke_width=2) for i in range(4)])
            
        w1 = make_whole().move_to(LEFT*3.5 + UP*1.5)
        w2 = make_whole().move_to(LEFT*1.0 + UP*1.5)
        w3 = VGroup(*[Sector(angle=PI/2, start_angle=i*PI/2, radius=0.8, color="#007BFF", stroke_color="#FFFFFF", stroke_width=2) for i in range(3)]).move_to(RIGHT*1.5 + UP*1.5)
        sectors_group = VGroup(w1, w2, w3)
        
        self.play(FadeIn(sectors_group, shift=UP), run_time=2.5)
        self.wait(5)
        
        tam = MathTex("2", color="#333333").scale(1.5)
        pay = MathTex("3", color="#333333")
        payda = MathTex("4", color="#333333")
        kesir_cizgisi = Line(LEFT*0.3, RIGHT*0.3, color="#333333")
        pay.next_to(kesir_cizgisi, UP, buff=0.1)
        payda.next_to(kesir_cizgisi, DOWN, buff=0.1)
        kesir_kismi = VGroup(pay, kesir_cizgisi, payda)
        kesir_kismi.next_to(tam, RIGHT, buff=0.2)
        tam_sayili_kesir = VGroup(tam, kesir_kismi).move_to(LEFT*2.5 + DOWN*1.5)
        
        self.play(Write(tam_sayili_kesir), run_time=2)
        self.wait(10)
        self.wait(25) # Bütünlerin ve pizzanın açıklaması
        
        arrow_mul = CurvedArrow(payda.get_bottom() + DOWN*0.1, tam.get_bottom() + DOWN*0.1, angle=PI/2, color="#002B4D")
        mul_text = MathTex("\\times", color="#002B4D").next_to(arrow_mul, DOWN, buff=0.1)
        self.play(Create(arrow_mul), Write(mul_text), run_time=2)
        self.wait(18)
        
        arrow_add = CurvedArrow(tam.get_top() + UP*0.1, pay.get_top() + UP*0.1, angle=-PI/2, color="#007BFF")
        add_text = MathTex("+", color="#007BFF").next_to(arrow_add, UP, buff=0.1)
        self.play(Create(arrow_add), Write(add_text), run_time=2)
        self.wait(18)
        
        eq_sign = MathTex("=", color="#333333").scale(1.5).next_to(tam_sayili_kesir, RIGHT, buff=0.8)
        yeni_pay = MathTex("11", color="#007BFF")
        yeni_payda = MathTex("4", color="#333333")
        yeni_cizgi = Line(LEFT*0.4, RIGHT*0.4, color="#333333")
        yeni_pay.next_to(yeni_cizgi, UP, buff=0.1)
        yeni_payda.next_to(yeni_cizgi, DOWN, buff=0.1)
        bilesik_kesir = VGroup(yeni_pay, yeni_cizgi, yeni_payda).next_to(eq_sign, RIGHT, buff=0.8)
        
        self.play(Write(eq_sign), Write(bilesik_kesir), run_time=2)
        self.wait(20)
        
        self.play(FadeOut(sectors_group), FadeOut(tam_sayili_kesir), FadeOut(arrow_mul), FadeOut(mul_text), FadeOut(arrow_add), FadeOut(add_text), FadeOut(eq_sign), FadeOut(bilesik_kesir), run_time=1)
        self.wait(2)
        
        # BÖLÜM 2: BİLEŞİK KESRİ TAM SAYILI KESRE ÇEVİRME (BÖLME EVİ)
        b_pay = MathTex("11", color="#007BFF").scale(1.2)
        b_payda = MathTex("4", color="#333333").scale(1.2)
        b_cizgi = Line(LEFT*0.5, RIGHT*0.5, color="#333333")
        b_pay.next_to(b_cizgi, UP, buff=0.1)
        b_payda.next_to(b_cizgi, DOWN, buff=0.1)
        b_kesir = VGroup(b_pay, b_cizgi, b_payda).move_to(LEFT*4 + UP*1.5)
        
        self.play(Write(b_kesir), run_time=2)
        self.wait(15)
        self.wait(15) # Bölme mantığı açıklaması
        
        dividend = MathTex("11", color="#333333").scale(1.2).move_to(LEFT*1.0)
        v_line = Line(UP*0.8, DOWN*1.5, color="#333333").next_to(dividend, RIGHT, buff=0.3)
        divisor = MathTex("4", color="#333333").scale(1.2).next_to(v_line, RIGHT, buff=0.3).align_to(dividend, UP)
        h_line = Line(ORIGIN, RIGHT*1.2, color="#333333").next_to(divisor, DOWN, buff=0.1).align_to(v_line, LEFT)
        
        self.play(Write(dividend), Create(v_line), Write(divisor), Create(h_line), run_time=2.5)
        self.wait(12)
        
        quotient = MathTex("2", color="#007BFF").scale(1.2).next_to(h_line, DOWN, buff=0.2).align_to(divisor, ORIGIN)
        self.play(Write(quotient), run_time=1)
        
        minus_8 = MathTex("-8", color="#333333").scale(1.2).next_to(dividend, DOWN, buff=0.2)
        sub_line = Line(LEFT*0.6, RIGHT*0.6, color="#333333").next_to(minus_8, DOWN, buff=0.1).align_to(dividend, ORIGIN)
        self.play(Write(minus_8), Create(sub_line), run_time=1)
        
        remainder = MathTex("3", color="#002B4D").scale(1.2).next_to(sub_line, DOWN, buff=0.2).align_to(dividend, ORIGIN)
        self.play(Write(remainder), run_time=1)
        self.wait(17)
        
        box_quotient = SurroundingRectangle(quotient, color="#007BFF", buff=0.1)
        self.play(Create(box_quotient), run_time=1.5)
        self.wait(15)
        
        box_remainder = SurroundingRectangle(remainder, color="#002B4D", buff=0.1)
        self.play(Create(box_remainder), run_time=1.5)
        self.wait(15)
        
        f_eq = MathTex("=", color="#333333").scale(1.5).next_to(b_kesir, RIGHT, buff=0.8)
        f_tam = MathTex("2", color="#007BFF").scale(1.5)
        f_pay = MathTex("3", color="#002B4D")
        f_payda = MathTex("4", color="#333333")
        f_cizgi = Line(LEFT*0.3, RIGHT*0.3, color="#333333")
        f_pay.next_to(f_cizgi, UP, buff=0.1)
        f_payda.next_to(f_cizgi, DOWN, buff=0.1)
        f_kesir_kismi = VGroup(f_pay, f_cizgi, f_payda)
        f_kesir_kismi.next_to(f_tam, RIGHT, buff=0.2)
        f_sonuc = VGroup(f_tam, f_kesir_kismi).next_to(f_eq, RIGHT, buff=0.8)
        
        self.play(Write(f_eq), Write(f_sonuc), run_time=2)
        self.wait(3.5)
        
        # ÇIKIŞ
        self.wait(1)