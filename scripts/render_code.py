from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi
        self.camera.background_color = "#FFFFFF"
        
        # --- GİRİŞ ---
        title = Text("Maarif Matematik", color="#002B4D", font_size=48, weight=BOLD)
        subtitle = Text("Kesirler: Basit, Bileşik, Tam Sayılı", color="#333333", font_size=32).next_to(title, DOWN)
        self.play(Write(title), FadeIn(subtitle), run_time=2)
        self.wait(3) # Toplam: 5s
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # --- BASİT KESİR ---
        basit_title = Text("Basit Kesir", color="#002B4D", font_size=40).to_edge(UP)
        basit_kesir = MathTex(r"\frac{3}{4}", color="#333333", font_size=72).move_to(LEFT * 3)
        
        # Pizza görseli (3/4)
        pizza1 = VGroup()
        colors = ["#D32F2F", "#D32F2F", "#D32F2F", "#E0E0E0"]
        for i in range(4):
            slice = Sector(radius=1.5, angle=PI/2, start_angle=i*PI/2, color=colors[i], fill_opacity=0.8, stroke_width=2, stroke_color="#FFFFFF")
            pizza1.add(slice)
        pizza1.move_to(RIGHT * 2)
        
        self.play(Write(basit_title), Write(basit_kesir), run_time=2)
        self.play(FadeIn(pizza1, shift=UP), run_time=2)
        self.wait(15) # Toplam: 19s
        self.play(FadeOut(basit_title), FadeOut(basit_kesir), FadeOut(pizza1))
        
        # --- BİLEŞİK KESİR ---
        bilesik_title = Text("Bileşik Kesir", color="#002B4D", font_size=40).to_edge(UP)
        bilesik_kesir = MathTex(r"\frac{7}{4}", color="#333333", font_size=72).move_to(LEFT * 4)
        
        # Pizza görseli (7/4)
        pizza2_full = VGroup()
        for i in range(4):
            slice = Sector(radius=1.2, angle=PI/2, start_angle=i*PI/2, color="#D32F2F", fill_opacity=0.8, stroke_width=2, stroke_color="#FFFFFF")
            pizza2_full.add(slice)
        pizza2_full.move_to(RIGHT * 0.5)
        
        pizza2_part = VGroup()
        for i in range(4):
            color = "#D32F2F" if i < 3 else "#E0E0E0"
            slice = Sector(radius=1.2, angle=PI/2, start_angle=i*PI/2, color=color, fill_opacity=0.8, stroke_width=2, stroke_color="#FFFFFF")
            pizza2_part.add(slice)
        pizza2_part.move_to(RIGHT * 3.5)
        
        self.play(Write(bilesik_title), Write(bilesik_kesir), run_time=2)
        self.play(FadeIn(pizza2_full), FadeIn(pizza2_part), run_time=2)
        self.wait(15) # Toplam: 19s
        self.play(FadeOut(bilesik_title), FadeOut(bilesik_kesir), FadeOut(pizza2_full), FadeOut(pizza2_part))
        
        # --- BÖLME ALGORİTMASI (Bileşikten Tam Sayılıya) ---
        donusum_title = Text("Bileşik Kesri Tam Sayılıya Çevirme", color="#002B4D", font_size=36).to_edge(UP)
        self.play(Write(donusum_title), run_time=1)
        
        # Bölme Evi Kurulumu
        bölme_merkezi = LEFT * 3
        v_line = Line(UP * 0.5, DOWN * 1.5, color="#333333").move_to(bölme_merkezi)
        dividend = MathTex("7", color="#333333", font_size=60).next_to(v_line, LEFT, buff=0.4).shift(UP * 0.5)
        divisor = MathTex("4", color="#002B4D", font_size=60).next_to(v_line, RIGHT, buff=0.4).shift(UP * 0.5)
        
        # Yatay çizgi KESİNLİKLE bölenin altında
        h_line = Line(v_line.get_center(), v_line.get_center() + RIGHT * 1.2, color="#333333").next_to(divisor, DOWN, buff=0.1).align_to(v_line, LEFT)
        
        quotient = MathTex("1", color="#D32F2F", font_size=60).next_to(h_line, DOWN, buff=0.3)
        
        # Çıkarma işlemi ve kalan
        eksi = MathTex("-", color="#333333").next_to(dividend, DOWN, buff=0.3).shift(LEFT*0.5)
        dort_cikan = MathTex("4", color="#333333", font_size=60).next_to(dividend, DOWN, buff=0.3)
        cizgi_cikan = Line(eksi.get_left() + DOWN*0.2, dort_cikan.get_right() + DOWN*0.2 + RIGHT*0.2, color="#333333")
        remainder = MathTex("3", color="#002B4D", font_size=60).next_to(cizgi_cikan, DOWN, buff=0.2).align_to(dividend, RIGHT)
        
        # Sonuç Kesri
        sonuc_tam = MathTex("1", color="#D32F2F", font_size=72).move_to(RIGHT * 2)
        sonuc_kesir = MathTex(r"\frac{3}{4}", color="#002B4D", font_size=72).next_to(sonuc_tam, RIGHT, buff=0.1)
        
        # Oklar
        arrow_tam = CurvedArrow(quotient.get_bottom(), sonuc_tam.get_bottom() + DOWN*0.5, angle=PI/4, color="#D32F2F")
        arrow_pay = CurvedArrow(remainder.get_bottom(), sonuc_kesir.get_top() + UP*1.5, angle=-PI/3, color="#002B4D")
        
        self.play(Write(dividend), Write(divisor), Create(v_line), Create(h_line), run_time=2)
        self.wait(1)
        self.play(Write(quotient), run_time=1)
        self.play(Write(eksi), Write(dort_cikan), Create(cizgi_cikan), Write(remainder), run_time=2)
        self.wait(1)
        self.play(Create(arrow_tam), Write(sonuc_tam), run_time=1)
        self.play(Create(arrow_pay), Write(sonuc_kesir), run_time=1)
        self.wait(25) # Toplam: 35s
        
        self.play(FadeOut(donusum_title), FadeOut(VGroup(dividend, divisor, v_line, h_line, quotient, eksi, dort_cikan, cizgi_cikan, remainder, arrow_tam, arrow_pay, sonuc_tam, sonuc_kesir)))

        # --- TAM SAYILIDAN BİLEŞİĞE --- 
        ters_title = Text("Tam Sayılı Kesri Bileşiğe Çevirme", color="#002B4D", font_size=36).to_edge(UP)
        baslangic_tam = MathTex("1", color="#D32F2F", font_size=72).move_to(LEFT * 3)
        baslangic_kesir = MathTex(r"\frac{3}{4}", color="#002B4D", font_size=72).next_to(baslangic_tam, RIGHT, buff=0.1)
        
        ok_carp = CurvedArrow(baslangic_kesir.get_bottom() + LEFT*0.2, baslangic_tam.get_bottom() + RIGHT*0.2, angle=PI/2, color="#333333")
        isaret_carp = MathTex(r"\times", color="#333333", font_size=30).next_to(ok_carp, DOWN, buff=0.1)
        
        ok_topla = CurvedArrow(baslangic_tam.get_top() + RIGHT*0.2, baslangic_kesir.get_top() + LEFT*0.2, angle=PI/2, color="#333333")
        isaret_topla = MathTex("+", color="#333333", font_size=30).next_to(ok_topla, UP, buff=0.1)
        
        esittir = MathTex("=", color="#333333", font_size=60).move_to(ORIGIN)
        
        son_bilesik = MathTex(r"\frac{7}{4}", color="#333333", font_size=72).move_to(RIGHT * 3)
        
        self.play(Write(ters_title), Write(baslangic_tam), Write(baslangic_kesir), run_time=2)
        self.wait(1)
        self.play(Create(ok_carp), Write(isaret_carp), run_time=1.5)
        self.play(Create(ok_topla), Write(isaret_topla), run_time=1.5)
        self.play(Write(esittir), Write(son_bilesik), run_time=2)
        self.wait(20) # Toplam: 28s
        
        self.play(FadeOut(VGroup(ters_title, baslangic_tam, baslangic_kesir, ok_carp, isaret_carp, ok_topla, isaret_topla, esittir, son_bilesik)))
        
        # --- ÇIKIŞ ---
        logo = Text("Maarif Matematik", color="#002B4D", font_size=60, weight=BOLD)
        self.play(FadeIn(logo), run_time=2)
        self.wait(20.33) # Toplam: 22.33s
