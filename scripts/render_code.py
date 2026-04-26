class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        # Intro
        title = Text("Kesir Çeşitleri ve Dönüşümler", color="#002B4D", font_size=48).to_edge(UP)
        self.play(Write(title), run_time=2)
        self.wait(12)

        # Basit Kesir
        basit_title = Text("Basit Kesir", color="#333333", font_size=36).move_to(LEFT*4 + UP*1)
        basit_frac = MathTex("\\frac{3}{4}", color="#D32F2F", font_size=64).next_to(basit_title, DOWN)
        self.play(Write(basit_title), Write(basit_frac))
        self.wait(12)

        # Bileşik Kesir
        bilesik_title = Text("Bileşik Kesir", color="#333333", font_size=36).move_to(ORIGIN + UP*1)
        bilesik_frac = MathTex("\\frac{7}{3}", color="#002B4D", font_size=64).next_to(bilesik_title, DOWN)
        self.play(Write(bilesik_title), Write(bilesik_frac))
        self.wait(12)

        # Tam Sayılı Kesir
        tam_title = Text("Tam Sayılı Kesir", color="#333333", font_size=36).move_to(RIGHT*4 + UP*1)
        tam_frac = MathTex("2\\frac{1}{3}", color="#D32F2F", font_size=64).next_to(tam_title, DOWN)
        self.play(Write(tam_title), Write(tam_frac))
        self.wait(12)

        self.play(FadeOut(basit_title), FadeOut(basit_frac), FadeOut(bilesik_title), FadeOut(tam_title), FadeOut(tam_frac))
        self.play(bilesik_frac.animate.move_to(LEFT*4 + UP*2))
        self.wait(5)

        # Division House (Bölme Evi)
        # Sol Üst: Bölünen (7)
        dividend = MathTex("7", color="#333333", font_size=64).move_to(LEFT*1 + UP*0.5)
        # Dikey Çizgi
        v_line = Line(UP*1, DOWN*1.5, color="#333333").next_to(dividend, RIGHT, buff=0.3)
        # Sağ Üst: Bölen (3)
        divisor = MathTex("3", color="#002B4D", font_size=64).next_to(v_line, RIGHT, buff=0.3).align_to(dividend, UP)
        # Yatay Çizgi (Bölenin Altında)
        h_line = Line(LEFT*0.4, RIGHT*0.4, color="#333333").next_to(divisor, DOWN, buff=0.1)
        # Sağ Alt: Bölüm (2)
        quotient = MathTex("2", color="#D32F2F", font_size=64).next_to(h_line, DOWN, buff=0.2)
        
        # Kalan hesaplama (Sol Alt)
        minus_six = MathTex("-6", color="#333333", font_size=48).next_to(dividend, DOWN, buff=0.2)
        sub_line = Line(LEFT*0.4, RIGHT*0.4, color="#333333").next_to(minus_six, DOWN, buff=0.1)
        remainder = MathTex("1", color="#D32F2F", font_size=64).next_to(sub_line, DOWN, buff=0.2)

        self.play(Create(dividend), Create(v_line), Create(divisor), Create(h_line))
        self.wait(8)
        
        self.play(Write(quotient))
        self.wait(5)
        
        self.play(Write(minus_six), Create(sub_line), Write(remainder))
        self.wait(8)

        # Arrows to Mixed Fraction
        mixed_result = MathTex("2", "\\frac{1}{3}", color="#333333", font_size=72).move_to(RIGHT*4)
        mixed_result[0].set_color("#D32F2F")
        
        arrow_quotient = CurvedArrow(quotient.get_right(), mixed_result[0].get_left(), color="#D32F2F")
        arrow_remainder = CurvedArrow(remainder.get_bottom(), mixed_result[1].get_top() + UP*0.5, color="#D32F2F")
        
        self.play(Write(mixed_result), Create(arrow_quotient), Create(arrow_remainder))
        self.wait(10)

        # Clear for reverse
        self.play(FadeOut(dividend), FadeOut(v_line), FadeOut(divisor), FadeOut(h_line), FadeOut(quotient), FadeOut(minus_six), FadeOut(sub_line), FadeOut(remainder), FadeOut(bilesik_frac), FadeOut(arrow_quotient), FadeOut(arrow_remainder))
        
        self.play(mixed_result.animate.move_to(ORIGIN))
        self.wait(5)

        # Mixed to Improper
        arc_mul = CurvedArrow(mixed_result[1].get_bottom(), mixed_result[0].get_bottom(), color="#002B4D", angle=PI/2)
        mul_sign = MathTex("\\times", color="#002B4D").next_to(arc_mul, DOWN, buff=0.1)
        
        arc_add = CurvedArrow(mixed_result[0].get_top(), mixed_result[1].get_top(), color="#D32F2F", angle=-PI/2)
        add_sign = MathTex("+", color="#D32F2F").next_to(arc_add, UP, buff=0.1)

        self.play(Create(arc_mul), Write(mul_sign))
        self.wait(8)
        
        self.play(Create(arc_add), Write(add_sign))
        self.wait(8)

        final_bilesik = MathTex("=", "\\frac{7}{3}", color="#333333", font_size=72).next_to(mixed_result, RIGHT, buff=1)
        final_bilesik[1].set_color("#002B4D")
        self.play(Write(final_bilesik))
        self.wait(15)
