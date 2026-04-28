from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan ve renk ayarları
        self.camera.background_color = "#FFFFFF"
        TEXT_COLOR = "#333333"
        MAARIF_BLUE = "#007BFF"
        NAVY = "#002B4D"

        # --- BÖLÜM 1: GİRİŞ (47.1 saniye) ---
        title = Text("Doğal Sayılar ve Kesirler", color=NAVY, font_size=48).shift(UP*1)
        subtitle = Text("Karşılaştırma Mantığı", color=MAARIF_BLUE, font_size=36).next_to(title, DOWN)
        
        self.play(Write(title), run_time=2)
        self.wait(15)
        self.play(FadeIn(subtitle), run_time=2)
        self.wait(27.1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=1)

        # --- BÖLÜM 2: ÖRNEK 1 KURULUMU (27.8 saniye) ---
        num_4 = MathTex("4", color=TEXT_COLOR, font_size=64).shift(LEFT*2 + UP*2)
        question = MathTex("?", color=MAARIF_BLUE, font_size=64).shift(UP*2)
        frac_17_4 = MathTex("\\frac{17}{4}", color=TEXT_COLOR, font_size=64).shift(RIGHT*2 + UP*2)
        
        self.play(Write(num_4), Write(question), Write(frac_17_4), run_time=3)
        self.wait(24.8)

        # --- BÖLÜM 3: BÖLME EVİ 1 (38.0 saniye) ---
        # Bölme Evi tasarımı
        dividend = MathTex("17", color=TEXT_COLOR, font_size=56).shift(LEFT*1 + DOWN*0.5)
        vline = Line(dividend.get_top() + RIGHT*0.4 + UP*0.2, dividend.get_bottom() + RIGHT*0.4 + DOWN*1.5, color=TEXT_COLOR)
        divisor = MathTex("4", color=TEXT_COLOR, font_size=56).next_to(vline, RIGHT, buff=0.4).align_to(dividend, UP)
        hline = Line(divisor.get_left() + DOWN*0.2 + LEFT*0.1, divisor.get_right() + DOWN*0.2 + RIGHT*0.1, color=TEXT_COLOR)
        
        self.play(Write(dividend), Create(vline), Write(divisor), Create(hline), run_time=3)
        self.wait(8)
        
        quotient = MathTex("4", color=MAARIF_BLUE, font_size=56).next_to(hline, DOWN, buff=0.3)
        self.play(Write(quotient), run_time=1)
        self.wait(6)
        
        product = MathTex("16", color=TEXT_COLOR, font_size=56).next_to(dividend, DOWN, buff=0.3)
        minus = MathTex("-", color=TEXT_COLOR, font_size=56).next_to(product, LEFT, buff=0.2)
        sub_line = Line(minus.get_left() + DOWN*0.2, product.get_right() + DOWN*0.2, color=TEXT_COLOR)
        
        self.play(Write(product), Write(minus), Create(sub_line), run_time=2)
        self.wait(6)
        
        remainder = MathTex("1", color=MAARIF_BLUE, font_size=56).next_to(sub_line, DOWN, buff=0.3).align_to(product, RIGHT)
        self.play(Write(remainder), run_time=1)
        self.wait(4)
        
        rect_q = SurroundingRectangle(quotient, color=NAVY, buff=0.1)
        rect_r = SurroundingRectangle(remainder, color=NAVY, buff=0.1)
        self.play(Create(rect_q), Create(rect_r), run_time=2)
        self.wait(4)

        # --- BÖLÜM 4: KARŞILAŞTIRMA 1 (34.9 saniye) ---
        mixed_frac = MathTex("4 \\frac{1}{4}", color=MAARIF_BLUE, font_size=64).move_to(frac_17_4.get_center())
        self.play(Transform(frac_17_4, mixed_frac), run_time=2)
        self.wait(15)
        
        less_than = MathTex("<", color=NAVY, font_size=64).move_to(question.get_center())
        self.play(Transform(question, less_than), run_time=1)
        self.wait(16.9)

        # Ekranı temizle
        group_1 = VGroup(num_4, question, frac_17_4, dividend, vline, divisor, hline, quotient, product, minus, sub_line, remainder, rect_q, rect_r)
        self.play(FadeOut(group_1), run_time=1)

        # --- BÖLÜM 5: ÖRNEK 2 KURULUMU VE BÖLME 2 (40.5 saniye) ---
        num_5 = MathTex("5", color=TEXT_COLOR, font_size=64).shift(LEFT*2 + UP*2)
        question2 = MathTex("?", color=MAARIF_BLUE, font_size=64).shift(UP*2)
        frac_14_3 = MathTex("\\frac{14}{3}", color=TEXT_COLOR, font_size=64).shift(RIGHT*2 + UP*2)
        
        self.play(Write(num_5), Write(question2), Write(frac_14_3), run_time=2)
        self.wait(8)

        dividend2 = MathTex("14", color=TEXT_COLOR, font_size=56).shift(LEFT*1 + DOWN*0.5)
        vline2 = Line(dividend2.get_top() + RIGHT*0.4 + UP*0.2, dividend2.get_bottom() + RIGHT*0.4 + DOWN*1.5, color=TEXT_COLOR)
        divisor2 = MathTex("3", color=TEXT_COLOR, font_size=56).next_to(vline2, RIGHT, buff=0.4).align_to(dividend2, UP)
        hline2 = Line(divisor2.get_left() + DOWN*0.2 + LEFT*0.1, divisor2.get_right() + DOWN*0.2 + RIGHT*0.1, color=TEXT_COLOR)
        
        self.play(Write(dividend2), Create(vline2), Write(divisor2), Create(hline2), run_time=2)
        self.wait(6)
        
        quotient2 = MathTex("4", color=MAARIF_BLUE, font_size=56).next_to(hline2, DOWN, buff=0.3)
        self.play(Write(quotient2), run_time=1)
        self.wait(4)
        
        product2 = MathTex("12", color=TEXT_COLOR, font_size=56).next_to(dividend2, DOWN, buff=0.3)
        minus2 = MathTex("-", color=TEXT_COLOR, font_size=56).next_to(product2, LEFT, buff=0.2)
        sub_line2 = Line(minus2.get_left() + DOWN*0.2, product2.get_right() + DOWN*0.2, color=TEXT_COLOR)
        
        self.play(Write(product2), Write(minus2), Create(sub_line2), run_time=2)
        self.wait(4)
        
        remainder2 = MathTex("2", color=MAARIF_BLUE, font_size=56).next_to(sub_line2, DOWN, buff=0.3).align_to(product2, RIGHT)
        self.play(Write(remainder2), run_time=1)
        self.wait(4)
        
        rect_q2 = SurroundingRectangle(quotient2, color=NAVY, buff=0.1)
        rect_r2 = SurroundingRectangle(remainder2, color=NAVY, buff=0.1)
        self.play(Create(rect_q2), Create(rect_r2), run_time=2)
        self.wait(4.5)

        # --- BÖLÜM 6: KARŞILAŞTIRMA 2 (26.8 saniye) ---
        mixed_frac2 = MathTex("4 \\frac{2}{3}", color=MAARIF_BLUE, font_size=64).move_to(frac_14_3.get_center())
        self.play(Transform(frac_14_3, mixed_frac2), run_time=2)
        self.wait(10)
        
        greater_than = MathTex(">", color=NAVY, font_size=64).move_to(question2.get_center())
        self.play(Transform(question2, greater_than), run_time=1)
        self.wait(13.8)

        group_2 = VGroup(num_5, question2, frac_14_3, dividend2, vline2, divisor2, hline2, quotient2, product2, minus2, sub_line2, remainder2, rect_q2, rect_r2)
        self.play(FadeOut(group_2), run_time=1)

        # --- BÖLÜM 7: ALTERNATİF YÖNTEM (48.6 saniye) ---
        alt_title = Text("Alternatif Yöntem: Payda Eşitleme", color=NAVY, font_size=40).shift(UP*3)
        self.play(Write(alt_title), run_time=2)
        self.wait(10)
        
        num_5_frac = MathTex("5 = \\frac{5}{1}", color=TEXT_COLOR, font_size=56).shift(LEFT*2 + UP*1)
        frac_14_3_orig = MathTex("\\frac{14}{3}", color=TEXT_COLOR, font_size=56).shift(RIGHT*2 + UP*1)
        self.play(Write(num_5_frac), Write(frac_14_3_orig), run_time=2)
        self.wait(12)
        
        expand_arrow = Arrow(num_5_frac.get_bottom(), num_5_frac.get_bottom() + DOWN*1.5, color=MAARIF_BLUE)
        expanded_frac = MathTex("\\frac{5 \\times 3}{1 \\times 3} = \\frac{15}{3}", color=MAARIF_BLUE, font_size=56).next_to(expand_arrow, DOWN)
        self.play(GrowArrow(expand_arrow), Write(expanded_frac), run_time=2)
        self.wait(10)
        
        final_comp = MathTex("\\frac{15}{3} > \\frac{14}{3}", color=NAVY, font_size=64).shift(DOWN*2.5)
        self.play(Write(final_comp), run_time=2)
        self.wait(8.6)

        group_3 = VGroup(alt_title, num_5_frac, frac_14_3_orig, expand_arrow, expanded_frac, final_comp)
        self.play(FadeOut(group_3), run_time=1.5)

        # --- BÖLÜM 8: ÇIKIŞ (3.5 saniye) ---
        outro_text = Text("Maarif Matematik", color=NAVY, font_size=48)
        self.play(Write(outro_text), run_time=1)
        self.wait(1)
