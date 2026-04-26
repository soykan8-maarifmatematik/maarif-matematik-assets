from manim import *

class MaarifScene(Scene):
    def construct(self):
        # P1: Intro (51 kelime / 1.7 = 30 sn)
        title = Tex(r"Kesirler: Basit, Bileşik ve Tam Sayılı").scale(1.2)
        self.play(Write(title), run_time=2)
        self.wait(28) # Seslendirme senkronu
        self.play(FadeOut(title))

        # P2: Basit Kesir (77 kelime / 1.7 = 45.3 sn)
        subtitle1 = Tex(r"Basit Kesir: $\frac{3}{4}$").to_edge(UP)
        self.play(Write(subtitle1), run_time=1)
        colors = [BLUE, BLUE, BLUE, DARK_GRAY]
        sectors = VGroup(*[Sector(radius=1.5, angle=PI/2, start_angle=i*PI/2, color=colors[i], fill_opacity=0.8).set_stroke(color=WHITE, width=2) for i in range(4)])
        self.play(Create(sectors), run_time=3)
        self.wait(41.3)
        self.play(FadeOut(sectors), FadeOut(subtitle1))

        # P3: Bileşik Kesir (96 kelime / 1.7 = 56.5 sn)
        subtitle2 = Tex(r"Bileşik Kesir: $\frac{7}{4}$").to_edge(UP)
        self.play(Write(subtitle2), run_time=1)
        pizza1 = VGroup(*[Sector(radius=1.2, angle=PI/2, start_angle=i*PI/2, color=ORANGE, fill_opacity=0.8).set_stroke(color=WHITE, width=2) for i in range(4)]).shift(LEFT*2)
        pizza2 = VGroup(*[Sector(radius=1.2, angle=PI/2, start_angle=i*PI/2, color=ORANGE if i<3 else DARK_GRAY, fill_opacity=0.8).set_stroke(color=WHITE, width=2) for i in range(4)]).shift(RIGHT*2)
        self.play(Create(pizza1), Create(pizza2), run_time=4)
        self.wait(51.5)
        self.play(FadeOut(pizza1), FadeOut(pizza2), FadeOut(subtitle2))

        # P4: Tam Sayılı Kesir (68 kelime / 1.7 = 40 sn)
        subtitle3 = Tex(r"Tam Sayılı Kesir: $1 \frac{3}{4}$").to_edge(UP)
        self.play(Write(subtitle3), run_time=1)
        eq = MathTex(r"\frac{7}{4} = 1 \frac{3}{4}").scale(1.5)
        self.play(Write(eq), run_time=2)
        self.wait(37)
        self.play(FadeOut(eq), FadeOut(subtitle3))

        # P5: Bölme Evi (122 kelime / 1.7 = 71.8 sn)
        subtitle4 = Tex(r"Bileşik $\rightarrow$ Tam Sayılı").to_edge(UP)
        self.play(Write(subtitle4), run_time=1)
        
        # Bölme Evi İnşası (Geometrik Çizim Zorunluluğu)
        dividend = MathTex("7").move_to(LEFT * 0.5 + UP * 0.5)
        divisor = MathTex("4").move_to(RIGHT * 0.5 + UP * 0.5)
        v_line = Line(UP * 1.0, DOWN * 1.0).move_to(ORIGIN)
        h_line_div = Line(ORIGIN, RIGHT * 1.0).move_to(RIGHT * 0.5)
        
        quotient = MathTex("1").move_to(RIGHT * 0.5 + DOWN * 0.5)
        
        sub_val = MathTex("4").move_to(LEFT * 0.5 + DOWN * 0.3)
        minus = MathTex("-").next_to(sub_val, LEFT, buff=0.1)
        h_line_sub = Line(LEFT * 1.2, ORIGIN).move_to(LEFT * 0.6 + DOWN * 0.7)
        
        remainder = MathTex("3").move_to(LEFT * 0.5 + DOWN * 1.2)
        
        house = VGroup(dividend, divisor, v_line, h_line_div)
        self.play(Create(house), run_time=3)
        self.wait(12)
        
        self.play(Write(quotient), run_time=1)
        self.wait(10)
        
        self.play(Write(sub_val), Write(minus), Create(h_line_sub), run_time=2)
        self.wait(10)
        
        self.play(Write(remainder), run_time=1)
        self.wait(18.8)
        
        result = MathTex(r"\frac{7}{4} = 1 \frac{3}{4}").move_to(RIGHT*3 + DOWN*0.5).scale(1.2)
        self.play(Write(result), run_time=1)
        self.wait(12)
        
        self.play(FadeOut(house), FadeOut(quotient), FadeOut(sub_val), FadeOut(minus), FadeOut(h_line_sub), FadeOut(remainder), FadeOut(result), FadeOut(subtitle4))

        # P6: Çevirme 2 (83 kelime / 1.7 = 48.8 sn)
        subtitle5 = Tex(r"Tam Sayılı $\rightarrow$ Bileşik").to_edge(UP)
        self.play(Write(subtitle5), run_time=1)
        mix_eq = MathTex(r"2 \frac{1}{3} = \frac{2 \times 3 + 1}{3} = \frac{7}{3}").scale(1.5)
        self.play(Write(mix_eq), run_time=3)
        self.wait(44.8)
        self.play(FadeOut(mix_eq), FadeOut(subtitle5))

        # P7: Outro (40 kelime / 1.7 = 23.5 sn)
        outro_text = Tex(r"Maarif Matematik ile Mantığı Keşfet!").scale(1.2)
        self.play(Write(outro_text), run_time=2)
        self.wait(19) # Sesin bitmesi için gereken süre
        self.wait(2.5) # OUTRO KURALI: Ses bittikten sonra maksimum 2-3 saniye bekleme
        self.play(FadeOut(Group(*self.mobjects)))