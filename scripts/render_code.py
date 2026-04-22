from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Renk Paleti
        self.camera.background_color = "#FFFFFF"
        dark_gray = "#333333"
        maarif_navy = "#002B4D"
        maarif_red = "#D32F2F"

        # BÖLÜM 1: Giriş ve Kesir Kavramı (28 kelime / 2.0 = 14.0 saniye)
        title = Text("Kesir Nedir?", color=maarif_navy, font_size=48).to_edge(UP)
        self.play(Write(title)) # 1 sn
        self.wait(3) # 3 sn

        whole_circle = Circle(radius=1.5, color=dark_gray, fill_opacity=0.1).shift(LEFT*3)
        self.play(Create(whole_circle)) # 1 sn
        self.wait(4) # 4 sn

        # Sector objeleri (outer_radius KESİNLİKLE YOK, sadece radius)
        sector_1 = Sector(radius=1.5, angle=PI/2, start_angle=0, color=maarif_red, fill_opacity=0.8).shift(LEFT*3)
        sector_2 = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color=maarif_red, fill_opacity=0.8).shift(LEFT*3)
        sector_3 = Sector(radius=1.5, angle=PI/2, start_angle=PI, color=maarif_red, fill_opacity=0.8).shift(LEFT*3)
        
        self.play(FadeIn(sector_1, sector_2, sector_3)) # 1 sn
        self.wait(4) # 4 sn
        # Toplam Bölüm 1: 1+3+1+4+1+4 = 14.0 sn

        # BÖLÜM 2: Pay, Payda ve Kesir Çizgisi (35 kelime / 2.0 = 17.5 saniye)
        fraction_line = Line(start=LEFT*0.5, end=RIGHT*0.5, color=dark_gray, stroke_width=6).shift(RIGHT*3)
        self.play(Create(fraction_line)) # 1 sn
        self.wait(3) # 3 sn

        payda_text = Text("4", color=maarif_navy, font_size=48).next_to(fraction_line, DOWN)
        payda_label = Text("Payda (Bütün)", color=maarif_navy, font_size=24).next_to(payda_text, DOWN)
        arrow_payda = Arrow(start=payda_label.get_top(), end=payda_text.get_bottom(), color=maarif_navy, buff=0.1)
        
        self.play(Write(payda_text), Write(payda_label), GrowArrow(arrow_payda)) # 1 sn
        self.wait(4.5) # 4.5 sn

        pay_text = Text("3", color=maarif_red, font_size=48).next_to(fraction_line, UP)
        pay_label = Text("Pay (Alınan)", color=maarif_red, font_size=24).next_to(pay_text, UP)
        arrow_pay = Arrow(start=pay_label.get_bottom(), end=pay_text.get_top(), color=maarif_red, buff=0.1)

        self.play(Write(pay_text), Write(pay_label), GrowArrow(arrow_pay)) # 1 sn
        self.wait(5) # 5 sn
        
        self.play(Indicate(pay_text, color=maarif_red), Indicate(payda_text, color=maarif_navy)) # 1 sn
        self.wait(1) # 1 sn
        # Toplam Bölüm 2: 1+3+1+4.5+1+5+1+1 = 17.5 sn

        # BÖLÜM 3: Kesrin Okunuşu (36 kelime / 2.0 = 18.0 saniye)
        read_1 = Text("1) Üç bölü dört", color=dark_gray, font_size=36).shift(RIGHT*3 + UP*2)
        read_2 = Text("2) Dörtte üç", color=dark_gray, font_size=36).next_to(read_1, DOWN, aligned_edge=LEFT)

        self.play(FadeOut(pay_label, arrow_pay, payda_label, arrow_payda, whole_circle, sector_1, sector_2, sector_3)) # 1 sn
        self.wait(3) # 3 sn

        self.play(Write(read_1)) # 1 sn
        self.wait(6) # 6 sn

        self.play(Write(read_2)) # 1 sn
        self.wait(6) # 6 sn
        # Toplam Bölüm 3: 1+3+1+6+1+6 = 18.0 sn

        # BÖLÜM 4: Sayı Doğrusu (34 kelime / 2.0 = 17.0 saniye)
        self.play(FadeOut(read_1, read_2, pay_text, payda_text, fraction_line, title)) # 1 sn
        self.wait(2) # 2 sn

        nl = NumberLine(
            x_range=[0, 1, 0.25],
            length=8,
            color=dark_gray,
            include_numbers=False,
            label_direction=DOWN
        ).shift(DOWN*0.5)
        
        zero_label = MathTex("0", color=dark_gray).next_to(nl.n2p(0), DOWN)
        one_label = MathTex("1", color=dark_gray).next_to(nl.n2p(1), DOWN)

        self.play(Create(nl), Write(zero_label), Write(one_label)) # 1 sn
        self.wait(5) # 5 sn

        dot = Dot(nl.n2p(0.75), color=maarif_red, radius=0.15)
        dot_label = MathTex("\\frac{3}{4}", color=maarif_red).next_to(dot, UP)
        
        self.play(FadeIn(dot, scale=0.5), Write(dot_label)) # 1 sn
        self.wait(4) # 4 sn
        
        nl_arrow = Arrow(start=dot_label.get_top() + UP, end=dot_label.get_top(), color=maarif_navy, buff=0.1)
        self.play(GrowArrow(nl_arrow)) # 1 sn
        self.wait(2) # 2 sn
        # Toplam Bölüm 4: 1+2+1+5+1+4+1+2 = 17.0 sn
