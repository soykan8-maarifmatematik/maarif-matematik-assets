from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan ve metin renkleri
        self.camera.background_color = "#FFFFFF"
        text_color = "#333333"

        # Giriş
        title = Tex("Kesir Çeşitleri ve Dönüşümler", color=text_color).scale(1.5)
        self.play(Write(title))
        self.wait(4)
        self.play(FadeOut(title))

        # Basit Kesir
        basit_title = Tex("Basit Kesir", color=text_color).to_edge(UP)
        basit_kesir = MathTex(r"\frac{3}{4}", color=text_color).scale(2.5)
        self.play(Write(basit_title))
        self.play(Write(basit_kesir))
        self.wait(10)
        self.play(FadeOut(basit_title), FadeOut(basit_kesir))

        # Bileşik Kesir
        bilesik_title = Tex("Bileşik Kesir", color=text_color).to_edge(UP)
        bilesik_kesir = MathTex(r"\frac{7}{4}", color=text_color).scale(2.5)
        self.play(Write(bilesik_title))
        self.play(Write(bilesik_kesir))
        self.wait(10)
        self.play(FadeOut(bilesik_title), FadeOut(bilesik_kesir))

        # Tam Sayılı Kesir
        tam_title = Tex("Tam Sayılı Kesir", color=text_color).to_edge(UP)
        tam_kesir = MathTex(r"1 \frac{3}{4}", color=text_color).scale(2.5)
        self.play(Write(tam_title))
        self.play(Write(tam_kesir))
        self.wait(10)
        self.play(FadeOut(tam_title), FadeOut(tam_kesir))

        # Dönüşüm: Bileşik -> Tam Sayılı (BÖLME EVİ ALGORİTMASI)
        donusum_title = Tex("Bileşik Kesri Tam Sayılı Kesre Çevirme", color=text_color).to_edge(UP)
        self.play(Write(donusum_title))

        # Bölme İşlemi Bileşenleri
        dividend = MathTex("7", color=text_color).shift(UP*0.5 + LEFT*0.5)
        divisor = MathTex("4", color=text_color).shift(UP*0.5 + RIGHT*0.5)
        
        # Dikey Çizgi: Bölünen ve Bölen arasına
        v_line = Line(UP*1.2, DOWN*0.2, color=text_color).move_to(UP*0.5)
        
        # Yatay Çizgi: Bölenin (4) ALTINA
        h_line = Line(LEFT*0.3, RIGHT*0.8, color=text_color).next_to(divisor, DOWN, buff=0.1)
        
        # Bölüm: Yatay çizginin altına
        quotient = MathTex("1", color=text_color).next_to(h_line, DOWN, buff=0.2)
        
        # Kalan: Bölünenin (7) altına
        remainder = MathTex("3", color=text_color).next_to(dividend, DOWN, buff=0.8)

        self.play(Write(dividend), Write(divisor))
        self.play(Create(v_line), Create(h_line))
        self.wait(6)
        self.play(Write(quotient))
        self.wait(4)
        self.play(Write(remainder))
        self.wait(6)

        # Sonuç Gösterimi
        sonuc = MathTex(r"\frac{7}{4} = 1 \frac{3}{4}", color=text_color).scale(1.5).shift(DOWN*2)
        self.play(Write(sonuc))
        self.wait(8)
        
        self.play(
            FadeOut(donusum_title), FadeOut(dividend), FadeOut(divisor), 
            FadeOut(v_line), FadeOut(h_line), FadeOut(quotient), 
            FadeOut(remainder), FadeOut(sonuc)
        )

        # Dönüşüm: Tam Sayılı -> Bileşik
        ters_title = Tex("Tam Sayılı Kesri Bileşik Kesre Çevirme", color=text_color).to_edge(UP)
        islem = MathTex(r"1 \frac{3}{4} = \frac{(1 \times 4) + 3}{4} = \frac{7}{4}", color=text_color).scale(1.5)
        
        self.play(Write(ters_title))
        self.wait(2)
        self.play(Write(islem))
        self.wait(15)

        self.play(FadeOut(ters_title), FadeOut(islem))
        self.wait(4)