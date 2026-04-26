from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan ve genel ayarlar
        self.camera.background_color = "#FFFFFF"
        text_color = "#333333"
        
        # GİRİŞ (Yaklaşık 15 saniye)
        self.wait(2)
        title = Text("Kesir Çeşitleri ve Dönüşümler", color=text_color, font_size=40)
        self.play(Write(title))
        self.wait(10)
        self.play(FadeOut(title))
        self.wait(3)

        # BASİT KESİR (Yaklaşık 40 saniye)
        basit_title = Text("Basit Kesir", color=text_color, font_size=36).to_edge(UP)
        basit_frac = MathTex("\\frac{3}{4}", color=text_color, font_size=60).move_to(LEFT * 3)
        
        # 4'e bölünmüş çember, 3'ü boyalı
        circle_basit = Circle(radius=1.5, color=text_color).move_to(RIGHT * 2)
        lines_basit = VGroup(*[Line(circle_basit.get_center(), circle_basit.point_at_angle(i * TAU / 4), color=text_color) for i in range(4)])
        sectors_basit = VGroup(*[Sector(arc_center=circle_basit.get_center(), radius=1.5, angle=TAU/4, start_angle=i*TAU/4, color=BLUE, fill_opacity=0.6) for i in range(3)])
        
        self.play(Write(basit_title))
        self.wait(5)
        self.play(Write(basit_frac))
        self.wait(6)
        self.play(Create(circle_basit), Create(lines_basit))
        self.wait(5)
        self.play(FadeIn(sectors_basit, lag_ratio=0.5))
        self.wait(15)
        self.play(FadeOut(basit_title, basit_frac, circle_basit, lines_basit, sectors_basit))
        self.wait(2)

        # BİLEŞİK KESİR (Yaklaşık 40 saniye)
        bilesik_title = Text("Bileşik Kesir", color=text_color, font_size=36).to_edge(UP)
        bilesik_frac = MathTex("\\frac{7}{3}", color=text_color, font_size=60).move_to(LEFT * 4)
        
        # 3 adet 3'e bölünmüş çember
        circles_bilesik = VGroup()
        for i in range(3):
            c = Circle(radius=1, color=text_color).move_to(RIGHT * (i * 2.5 - 1))
            l = VGroup(*[Line(c.get_center(), c.point_at_angle(j * TAU / 3 + TAU/4), color=text_color) for j in range(3)])
            circles_bilesik.add(VGroup(c, l))
            
        sectors_bilesik = VGroup()
        # İlk iki çember tam boyalı
        for i in range(2):
            for j in range(3):
                s = Sector(arc_center=circles_bilesik[i][0].get_center(), radius=1, angle=TAU/3, start_angle=j*TAU/3 + TAU/4, color=ORANGE, fill_opacity=0.6)
                sectors_bilesik.add(s)
        # Üçüncü çemberin 1 parçası boyalı
        s_last = Sector(arc_center=circles_bilesik[2][0].get_center(), radius=1, angle=TAU/3, start_angle=TAU/4, color=ORANGE, fill_opacity=0.6)
        sectors_bilesik.add(s_last)

        self.play(Write(bilesik_title))
        self.wait(4)
        self.play(Write(bilesik_frac))
        self.wait(6)
        self.play(Create(circles_bilesik))
        self.wait(5)
        self.play(FadeIn(sectors_bilesik, lag_ratio=0.2))
        self.wait(15)
        self.play(FadeOut(bilesik_title, circles_bilesik, sectors_bilesik))
        self.play(bilesik_frac.animate.to_edge(UP))
        self.wait(3)

        # BÖLME ALGORİTMASI VE TAM SAYILI KESRE ÇEVİRME (Yaklaşık 70 saniye)
        # KURAL 4: Cerrahi Bölme Algoritması Düzeni
        dividend = MathTex("7", color=text_color, font_size=60).move_to(LEFT * 2 + UP * 0.5)
        divisor = MathTex("3", color=text_color, font_size=60).move_to(LEFT * 0.5 + UP * 0.5)
        
        # 1. ANA ÇİZGİLER
        v_line = Line(UP * 1.2, DOWN * 0.2, color=text_color).move_to(LEFT * 1.25 + UP * 0.5)
        h_line1 = Line(LEFT * 1.25, RIGHT * 0.25, color=text_color).move_to(LEFT * 0.5 + ORIGIN)
        
        self.play(Write(dividend), Write(divisor))
        self.play(Create(v_line), Create(h_line1))
        self.wait(10)
        
        # Bölüm
        quotient = MathTex("2", color=text_color, font_size=60).move_to(LEFT * 0.5 + DOWN * 0.7)
        self.play(Write(quotient))
        self.wait(5)
        
        # 2. ÇIKARMA İŞLEMİ
        sub_num = MathTex("6", color=text_color, font_size=60).move_to(LEFT * 2 + DOWN * 0.7)
        minus = MathTex("-", color=text_color, font_size=60).next_to(sub_num, LEFT, buff=0.2)
        h_line2 = Line(LEFT * 2.8, LEFT * 1.5, color=text_color).move_to(LEFT * 2 + DOWN * 1.3)
        
        self.play(Write(sub_num))
        self.play(Write(minus), Create(h_line2))
        self.wait(5)
        
        # 3. KALAN
        remainder = MathTex("1", color=text_color, font_size=60).move_to(LEFT * 2 + DOWN * 2)
        self.play(Write(remainder))
        self.wait(10)
        
        # 4. YERLEŞİM VE 5. DÖNÜŞÜM OKLARI
        mixed_num = MathTex("2", "\\frac{1}{3}", color=text_color, font_size=70).move_to(RIGHT * 3 + DOWN * 0.5)
        
        self.play(Write(mixed_num[0])) # Tam kısım
        arrow_q = CurvedArrow(quotient.get_right(), mixed_num[0].get_left(), angle=-TAU/4, color=BLUE)
        self.play(Create(arrow_q))
        self.wait(8)
        
        self.play(Write(mixed_num[1])) # Kesir kısmı (Pay ve Payda)
        arrow_r = CurvedArrow(remainder.get_right(), mixed_num[1].get_left() + DOWN*0.2, angle=TAU/4, color=RED)
        self.play(Create(arrow_r))
        self.wait(10)
        
        self.play(FadeOut(dividend, divisor, v_line, h_line1, quotient, sub_num, minus, h_line2, remainder, arrow_q, arrow_r, bilesik_frac))
        self.play(mixed_num.animate.move_to(ORIGIN))
        self.wait(3)

        # TAM SAYILI KESRİ BİLEŞİĞE ÇEVİRME (Yaklaşık 35 saniye)
        # 2 tam 1/3 -> 7/3
        calc_text = MathTex("\\frac{2 \\times 3 + 1}{3}", color=text_color, font_size=60).move_to(RIGHT * 3)
        arrow_convert = Arrow(mixed_num.get_right(), calc_text.get_left(), color=text_color)
        
        self.wait(5)
        self.play(Create(arrow_convert))
        self.play(Write(calc_text))
        self.wait(10)
        
        final_result = MathTex("=", "\\frac{7}{3}", color=text_color, font_size=60).next_to(calc_text, RIGHT)
        self.play(Write(final_result))
        self.wait(15)
        
        # ÇIKIŞ (Yaklaşık 10 saniye)
        self.play(FadeOut(mixed_num, arrow_convert, calc_text, final_result))
        self.wait(5)
        outro_text = Text("Maarif Matematik", color=text_color, font_size=40)
        self.play(Write(outro_text))
        self.wait(5)
        self.play(FadeOut(outro_text))
        self.wait(2)
