from manim import *

class Kesirler(Scene):
    def construct(self):
        # 1. GİRİŞ
        title = Tex("Kesir Çeşitleri ve Dönüşümler", font_size=48, color=YELLOW)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.wait(5)

        # 2. BASİT KESİR
        basit_title = Tex("Basit Kesir: Pay $<$ Payda", font_size=40).shift(UP*1.5)
        basit_ex = MathTex(r"\frac{3}{5}", font_size=60).next_to(basit_title, DOWN, buff=0.5)
        self.play(Write(basit_title))
        self.play(FadeIn(basit_ex, shift=UP))
        self.wait(5)
        self.play(FadeOut(basit_title), FadeOut(basit_ex))

        # 3. BİLEŞİK KESİR
        bilesik_title = Tex("Bileşik Kesir: Pay $\geq$ Payda", font_size=40).shift(UP*1.5)
        bilesik_ex = MathTex(r"\frac{7}{4}", font_size=60).next_to(bilesik_title, DOWN, buff=0.5)
        self.play(Write(bilesik_title))
        self.play(FadeIn(bilesik_ex, shift=UP))
        self.wait(6)
        self.play(FadeOut(bilesik_title), FadeOut(bilesik_ex))

        # 4. TAM SAYILI KESİR
        tam_title = Tex("Tam Sayılı Kesir: Tam Sayı + Basit Kesir", font_size=40).shift(UP*1.5)
        tam_ex = MathTex(r"1 \frac{3}{4}", font_size=60).next_to(tam_title, DOWN, buff=0.5)
        self.play(Write(tam_title))
        self.play(FadeIn(tam_ex, shift=UP))
        self.wait(6)
        self.play(FadeOut(tam_title), FadeOut(tam_ex))

        # 5. DÖNÜŞÜM: TAM SAYILIDAN BİLEŞİĞE
        conv1_title = Tex("Tam Sayılı $\rightarrow$ Bileşik Kesir", font_size=40, color=BLUE).shift(UP*2)
        self.play(Write(conv1_title))
        
        step1 = MathTex(r"2 \frac{1}{3}", font_size=60)
        step2 = MathTex(r"= \frac{2 \times 3 + 1}{3}", font_size=60).next_to(step1, RIGHT)
        step3 = MathTex(r"= \frac{7}{3}", font_size=60).next_to(step2, RIGHT)
        
        eq_group = VGroup(step1, step2, step3).move_to(ORIGIN)
        
        self.play(Write(eq_group[0]))
        self.wait(2)
        self.play(Write(eq_group[1]))
        self.wait(5)
        self.play(Write(eq_group[2]))
        self.wait(4)
        self.play(FadeOut(conv1_title), FadeOut(eq_group))

        # 6. DÖNÜŞÜM: BİLEŞİKTEN TAM SAYILIYA (BÖLME EVİ)
        conv2_title = Tex("Bileşik $\rightarrow$ Tam Sayılı Kesir", font_size=40, color=GREEN).shift(UP*2.5)
        self.play(Write(conv2_title))
        
        start_frac = MathTex(r"\frac{11}{4}", font_size=60).shift(LEFT*4 + UP*0.5)
        self.play(Write(start_frac))
        self.wait(4)

        # Bölme Evi Kurulumu (Line objeleri ile)
        dividend = MathTex("11", font_size=48).move_to(LEFT * 0.5 + UP * 0.8)
        divisor = MathTex("4", font_size=48).move_to(RIGHT * 0.5 + UP * 0.8)
        
        v_line = Line(UP * 1.2, DOWN * 0.2).move_to(ORIGIN + UP * 0.5)
        h_line = Line(ORIGIN, RIGHT * 1).move_to(RIGHT * 0.5 + UP * 0.4)
        
        self.play(Write(dividend), Write(divisor))
        self.play(Create(v_line), Create(h_line))
        self.wait(3)

        # Bölme İşlemi Adımları
        quotient = MathTex("2", font_size=48, color=YELLOW).move_to(RIGHT * 0.5 + DOWN * 0.2)
        self.play(Write(quotient))
        self.wait(2)

        product = MathTex("8", font_size=48).move_to(LEFT * 0.5 + DOWN * 0.2)
        minus = MathTex("-", font_size=48).next_to(product, LEFT, buff=0.1)
        sub_line = Line(LEFT * 1, ORIGIN).move_to(LEFT * 0.5 + DOWN * 0.6)
        
        self.play(Write(product), Write(minus))
        self.play(Create(sub_line))
        self.wait(2)

        remainder = MathTex("3", font_size=48, color=RED).move_to(LEFT * 0.5 + DOWN * 1.1)
        self.play(Write(remainder))
        self.wait(3)

        # Sonucu Yazma
        arrow = Arrow(start=LEFT*2, end=RIGHT*2, color=WHITE).next_to(h_line, RIGHT, buff=1)
        final_result = MathTex(r"2 \frac{3}{4}", font_size=60)
        final_result[0][0].set_color(YELLOW) # Tam kısım (2)
        final_result[0][1].set_color(RED)    # Pay (3)
        final_result.next_to(arrow, RIGHT)

        self.play(GrowArrow(arrow))
        self.play(Write(final_result))
        self.wait(5)

        # 8. ÇIKIŞ
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != title]
        )
        self.play(title.animate.move_to(ORIGIN))
        self.wait(3)
