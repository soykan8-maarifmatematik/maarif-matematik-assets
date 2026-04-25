from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi
        self.camera.background_color = "#FFFFFF"
        
        # Renk paleti
        c_text = "#333333"
        c_navy = "#002B4D"
        c_red = "#D32F2F"

        # SAHNE 1: Basit Kesir (Yaklaşık 29 saniye)
        title_basit = Text("Basit Kesir", color=c_navy, font_size=48).to_edge(UP)
        frac_basit = MathTex(r"\frac{3}{4}", color=c_text, font_size=72).move_to(LEFT * 3)
        
        # Pizza çizimi (Basit Kesir)
        circle_basit = Circle(radius=1.5, color=c_text).move_to(RIGHT * 2)
        lines_basit = VGroup(*[Line(circle_basit.get_center(), circle_basit.point_at_angle(i*PI/2), color=c_text) for i in range(4)])
        sectors_basit = VGroup(*[Sector(arc_center=circle_basit.get_center(), radius=1.5, angle=PI/2, start_angle=i*PI/2, color=c_navy, fill_opacity=0.7) for i in range(3)])
        
        self.play(Write(title_basit))
        self.play(Write(frac_basit))
        self.play(Create(circle_basit), Create(lines_basit))
        self.play(FadeIn(sectors_basit, lag_ratio=0.5))
        self.wait(25)
        
        self.play(FadeOut(title_basit, frac_basit, circle_basit, lines_basit, sectors_basit))

        # SAHNE 2: Bileşik Kesir (Yaklaşık 25 saniye)
        title_bilesik = Text("Bileşik Kesir", color=c_red, font_size=48).to_edge(UP)
        frac_bilesik = MathTex(r"\frac{7}{4}", color=c_text, font_size=72).move_to(LEFT * 4)
        
        # 2 Pizza çizimi (Bileşik Kesir)
        circle1 = Circle(radius=1.2, color=c_text).move_to(RIGHT * 0.5)
        lines1 = VGroup(*[Line(circle1.get_center(), circle1.point_at_angle(i*PI/2), color=c_text) for i in range(4)])
        sectors1 = VGroup(*[Sector(arc_center=circle1.get_center(), radius=1.2, angle=PI/2, start_angle=i*PI/2, color=c_red, fill_opacity=0.7) for i in range(4)])
        
        circle2 = Circle(radius=1.2, color=c_text).move_to(RIGHT * 3.5)
        lines2 = VGroup(*[Line(circle2.get_center(), circle2.point_at_angle(i*PI/2), color=c_text) for i in range(4)])
        sectors2 = VGroup(*[Sector(arc_center=circle2.get_center(), radius=1.2, angle=PI/2, start_angle=i*PI/2, color=c_red, fill_opacity=0.7) for i in range(3)])
        
        self.play(Write(title_bilesik))
        self.play(Write(frac_bilesik))
        self.play(Create(circle1), Create(lines1), Create(circle2), Create(lines2))
        self.play(FadeIn(sectors1, lag_ratio=0.2), FadeIn(sectors2, lag_ratio=0.2))
        self.wait(21)
        
        self.play(FadeOut(title_bilesik, frac_bilesik, circle1, lines1, sectors1, circle2, lines2, sectors2))

        # SAHNE 3: Tam Sayılı Kesir (Yaklaşık 13 saniye)
        title_tam = Text("Tam Sayılı Kesir", color=c_navy, font_size=48).to_edge(UP)
        eq_tam = MathTex(r"\frac{7}{4} = 1 \frac{3}{4}", color=c_text, font_size=72)
        
        self.play(Write(title_tam))
        self.play(Write(eq_tam))
        self.wait(10)
        
        self.play(FadeOut(title_tam, eq_tam))

        # SAHNE 4: Bölme Evi ile Dönüşüm (Yaklaşık 46 saniye)
        title_donusum1 = Text("Bileşik Kesri Tam Sayılı Kesre Çevirme", color=c_text, font_size=40).to_edge(UP)
        
        # Bölme Evi Çizimi (Line objeleri ile)
        div_vert = Line(UP*1, DOWN*1, color=c_text)
        div_horiz = Line(ORIGIN, RIGHT*1.5, color=c_text).next_to(div_vert, RIGHT, aligned_edge=UP, buff=0)
        
        dividend = MathTex("7", color=c_text, font_size=60).next_to(div_vert, LEFT, buff=0.3).shift(UP*0.4)
        divisor = MathTex("4", color=c_text, font_size=60).next_to(div_vert, RIGHT, buff=0.3).shift(UP*0.4)
        quotient = MathTex("1", color=c_red, font_size=60).next_to(div_horiz, DOWN, buff=0.3)
        
        minus = MathTex("-", color=c_text, font_size=60).next_to(dividend, DOWN, buff=0.2).shift(LEFT*0.4)
        sub_val = MathTex("4", color=c_text, font_size=60).next_to(dividend, DOWN, buff=0.2)
        sub_line = Line(LEFT*0.5, RIGHT*0.5, color=c_text).next_to(sub_val, DOWN, buff=0.1)
        remainder = MathTex("3", color=c_navy, font_size=60).next_to(sub_line, DOWN, buff=0.2)
        
        div_group = VGroup(div_vert, div_horiz, dividend, divisor, quotient, minus, sub_val, sub_line, remainder)
        div_group.move_to(LEFT * 3)
        
        # Sonuç gösterimi
        result_frac = MathTex(r"1 \frac{3}{4}", color=c_text, font_size=80).move_to(RIGHT * 3)
        result_frac[0][0].set_color(c_red)   # Tam kısım (1)
        result_frac[0][1].set_color(c_navy)  # Pay (3)
        
        self.play(Write(title_donusum1))
        self.play(Create(div_vert), Create(div_horiz))
        self.play(Write(dividend), Write(divisor))
        self.wait(2)
        self.play(Write(quotient))
        self.wait(2)
        self.play(Write(minus), Write(sub_val), Create(sub_line))
        self.play(Write(remainder))
        self.wait(5)
        
        # Oklarla eşleştirme
        arrow_tam = Arrow(quotient.get_right(), result_frac[0][0].get_left(), color=c_red, buff=0.2)
        arrow_pay = Arrow(remainder.get_right(), result_frac[0][1].get_left(), color=c_navy, buff=0.2)
        
        self.play(GrowArrow(arrow_tam), Write(result_frac[0][0]))
        self.play(GrowArrow(arrow_pay), Write(result_frac[0][1]), Write(result_frac[0][2]), Write(result_frac[0][3]))
        self.wait(25)
        
        self.play(FadeOut(title_donusum1, div_group, arrow_tam, arrow_pay, result_frac))

        # SAHNE 5: Tam Sayılıdan Bileşiğe Dönüşüm (Yaklaşık 29 saniye)
        title_donusum2 = Text("Tam Sayılı Kesri Bileşik Kesre Çevirme", color=c_text, font_size=40).to_edge(UP)
        
        start_frac = MathTex(r"1 \frac{3}{4}", color=c_text, font_size=80).move_to(LEFT * 3)
        start_frac[0][0].set_color(c_red)
        start_frac[0][1].set_color(c_navy)
        
        calc_text = MathTex(r"\frac{(1 \times 4) + 3}{4}", color=c_text, font_size=72).move_to(RIGHT * 2)
        calc_text[0][1].set_color(c_red)
        calc_text[0][6].set_color(c_navy)
        
        final_result = MathTex(r"= \frac{7}{4}", color=c_text, font_size=80).next_to(calc_text, RIGHT)
        
        self.play(Write(title_donusum2))
        self.play(Write(start_frac))
        self.wait(5)
        self.play(Write(calc_text))
        self.wait(5)
        self.play(Write(final_result))
        self.wait(13)
        
        self.play(FadeOut(title_donusum2, start_frac, calc_text, final_result))
        self.wait(2)
