from manim import *

class MaarifScene(Scene):
    def construct(self):
        # 1. MARKA KİMLİĞİ VE ESTETİK
        self.camera.background_color = "#FFFFFF"
        text_color = "#333333"
        maarif_navy = "#002B4D"
        maarif_red = "#D32F2F"

        # SAHNE 1: Kesir Nedir?
        # Kelime sayısı: 36. Süre: 36 / 2.0 = 18.0 saniye.
        # Animasyon: 3 saniye. Bekleme: 15.0 saniye.
        title = Text("Kesir", color=maarif_navy, font_size=48).shift(UP*2.5)
        circle = Circle(radius=1.5, color=text_color)
        sector1 = Sector(radius=1.5, angle=PI, start_angle=0, color=maarif_navy, fill_opacity=0.2)
        sector2 = Sector(radius=1.5, angle=PI, start_angle=PI, color=maarif_red, fill_opacity=0.2)
        
        self.play(Create(circle), run_time=1)
        self.play(Create(VGroup(sector1, sector2)), run_time=1)
        self.play(Write(title), run_time=1)
        self.wait(15.0)
        self.clear()

        # SAHNE 2: Pay, Payda ve Kesir Çizgisi
        # Kelime sayısı: 39. Süre: 39 / 2.0 = 19.5 saniye.
        # Animasyon: 3 saniye. Bekleme: 16.5 saniye.
        fraction = MathTex(r"\frac{3}{4}", color=text_color, font_size=144)
        pay_text = Text("Pay", color=maarif_red, font_size=36).next_to(fraction, UP*2)
        pay_arrow = Arrow(pay_text.get_bottom(), fraction.get_top(), color=maarif_red)
        payda_text = Text("Payda", color=maarif_navy, font_size=36).next_to(fraction, DOWN*2)
        payda_arrow = Arrow(payda_text.get_top(), fraction.get_bottom(), color=maarif_navy)

        self.play(Write(fraction), run_time=1)
        self.play(Write(payda_text), GrowArrow(payda_arrow), run_time=1)
        self.play(Write(pay_text), GrowArrow(pay_arrow), run_time=1)
        self.wait(16.5)
        self.clear()

        # SAHNE 3: Model ve Sayı Doğrusu
        # Kelime sayısı: 41. Süre: 41 / 2.0 = 20.5 saniye.
        # Animasyon: 3 saniye. Bekleme: 17.5 saniye.
        s1 = Sector(radius=1.5, angle=PI/2, start_angle=0, color=maarif_red, fill_opacity=0.8)
        s2 = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color=maarif_red, fill_opacity=0.8)
        s3 = Sector(radius=1.5, angle=PI/2, start_angle=PI, color=maarif_red, fill_opacity=0.8)
        s4 = Sector(radius=1.5, angle=PI/2, start_angle=3*PI/2, color=text_color, fill_opacity=0.1)
        pie = VGroup(s1, s2, s3, s4).shift(UP*1.5)

        nl = NumberLine(x_range=[0, 1, 0.25], length=8, color=text_color, include_numbers=False).shift(DOWN*2)
        tick_0 = MathTex("0", color=text_color).next_to(nl.number_to_point(0), DOWN)
        tick_1 = MathTex("1", color=text_color).next_to(nl.number_to_point(1), DOWN)
        tick_34 = MathTex(r"\frac{3}{4}", color=maarif_navy).next_to(nl.number_to_point(0.75), DOWN)
        nl_group = VGroup(nl, tick_0, tick_1, tick_34)
        
        arrow_nl = Arrow(nl.number_to_point(0.75) + UP*1.5, nl.number_to_point(0.75), color=maarif_navy)

        self.play(Create(pie), run_time=1)
        self.play(Create(nl_group), run_time=1)
        self.play(GrowArrow(arrow_nl), run_time=1)
        self.wait(17.5)
        self.clear()

        # SAHNE 4: Kesrin Okunuşu
        # Kelime sayısı: 38. Süre: 38 / 2.0 = 19.0 saniye.
        # Animasyon: 2 saniye. Bekleme: 17.0 saniye.
        frac_final = MathTex(r"\frac{3}{4}", color=text_color, font_size=144)
        down_arrow = Arrow(LEFT*2 + UP*1.5, LEFT*2 + DOWN*1.5, color=maarif_red)
        read_down = Text("Üç bölü dört", color=maarif_red, font_size=36).next_to(down_arrow, LEFT)
        
        up_arrow = Arrow(RIGHT*2 + DOWN*1.5, RIGHT*2 + UP*1.5, color=maarif_navy)
        read_up = Text("Dörtte üç", color=maarif_navy, font_size=36).next_to(up_arrow, RIGHT)

        self.add(frac_final)
        self.play(GrowArrow(down_arrow), Write(read_down), run_time=1)
        self.play(GrowArrow(up_arrow), Write(read_up), run_time=1)
        self.wait(17.0)
