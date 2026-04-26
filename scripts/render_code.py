from manim import *

class FractionTypes(Scene):
    def construct(self):
        # Intro
        self.wait(2)
        title = Text("Kesir Çeşitleri", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(8)

        # Basit Kesir
        pizza_basit = VGroup()
        colors = [ORANGE, ORANGE, ORANGE, DARK_GRAY]
        for i in range(4):
            slice = Sector(radius=1.5, angle=PI/2, start_angle=i*PI/2, color=colors[i], fill_opacity=0.8, stroke_color=WHITE, stroke_width=2)
            pizza_basit.add(slice)
        
        basit_text = Text("Basit Kesir: 3/4", font_size=36).next_to(pizza_basit, DOWN, buff=0.5)
        
        self.play(FadeIn(pizza_basit))
        self.wait(6)
        self.play(Write(basit_text))
        self.wait(12)
        self.play(FadeOut(pizza_basit), FadeOut(basit_text))

        # Bileşik Kesir
        pizza_bilesik1 = VGroup(*[Sector(radius=1.2, angle=PI/2, start_angle=i*PI/2, color=ORANGE, fill_opacity=0.8, stroke_color=WHITE, stroke_width=2) for i in range(4)])
        pizza_bilesik2 = VGroup(*[Sector(radius=1.2, angle=PI/2, start_angle=i*PI/2, color=ORANGE if i<3 else DARK_GRAY, fill_opacity=0.8, stroke_color=WHITE, stroke_width=2) for i in range(4)])
        
        pizza_bilesik1.move_to(LEFT*2)
        pizza_bilesik2.move_to(RIGHT*2)
        
        bilesik_text = Text("Bileşik Kesir: 7/4", font_size=36).next_to(VGroup(pizza_bilesik1, pizza_bilesik2), DOWN, buff=0.5)
        
        self.play(FadeIn(pizza_bilesik1), FadeIn(pizza_bilesik2))
        self.wait(8)
        self.play(Write(bilesik_text))
        self.wait(14)

        # Tam Sayılı Kesir
        tam_text = Text("Tam Sayılı Kesir: 1 tam 3/4", font_size=36).move_to(bilesik_text.get_center())
        self.play(Transform(bilesik_text, tam_text))
        self.wait(26)
        self.play(FadeOut(pizza_bilesik1), FadeOut(pizza_bilesik2), FadeOut(bilesik_text), FadeOut(title))

        # Çevirme İşlemi - Bölme Evi
        dividend = MathTex("7").scale(1.5).move_to(UP*1 + LEFT*1)
        vline = Line(dividend.get_top() + RIGHT*0.5 + UP*0.2, dividend.get_bottom() + RIGHT*0.5 + DOWN*1.5)
        divisor = MathTex("4").scale(1.5).next_to(vline, RIGHT, buff=0.3).align_to(dividend, UP)
        hline = Line(divisor.get_bottom() + LEFT*0.2 + DOWN*0.1, divisor.get_bottom() + RIGHT*0.8 + DOWN*0.1)
        
        self.play(Write(dividend))
        self.wait(2)
        self.play(Write(vline), Write(divisor), Write(hline))
        self.wait(4)

        quotient = MathTex("1").scale(1.5).next_to(hline, DOWN, buff=0.3).align_to(divisor, LEFT)
        self.play(Write(quotient))
        self.wait(3)

        sub_num = MathTex("4").scale(1.5).next_to(dividend, DOWN, buff=0.5)
        minus = MathTex("-").scale(1.5).next_to(sub_num, LEFT, buff=0.2)
        sub_line = Line(minus.get_left() + DOWN*0.2, sub_num.get_right() + DOWN*0.2)
        
        self.play(Write(sub_num), Write(minus), Write(sub_line))
        self.wait(3)

        remainder = MathTex("3").scale(1.5).next_to(sub_line, DOWN, buff=0.2).align_to(sub_num, RIGHT)
        self.play(Write(remainder))
        self.wait(6)

        # Oklarla gösterme
        arrow_tam = Arrow(quotient.get_right(), quotient.get_right() + RIGHT*1.5, color=GREEN)
        text_tam = Text("Tam Kısım", color=GREEN, font_size=24).next_to(arrow_tam, RIGHT)
        
        arrow_pay = Arrow(remainder.get_right(), remainder.get_right() + RIGHT*1.5, color=BLUE)
        text_pay = Text("Yeni Pay", color=BLUE, font_size=24).next_to(arrow_pay, RIGHT)
        
        arrow_payda = Arrow(divisor.get_top(), divisor.get_top() + UP*1, color=RED)
        text_payda = Text("Payda (Değişmez)", color=RED, font_size=24).next_to(arrow_payda, UP)

        self.play(GrowArrow(arrow_tam), Write(text_tam))
        self.wait(3)
        self.play(GrowArrow(arrow_pay), Write(text_pay))
        self.wait(3)
        self.play(GrowArrow(arrow_payda), Write(text_payda))
        self.wait(4)

        # Sonuç yazımı
        sonuc = MathTex(r"\frac{7}{4} = 1 \frac{3}{4}").scale(1.5).move_to(DOWN*2.5 + LEFT*3)
        self.play(Write(sonuc))
        self.wait(8)

        # Outro
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(3)