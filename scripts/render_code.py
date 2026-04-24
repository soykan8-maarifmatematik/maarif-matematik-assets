from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Renk Tanımlamaları
        bg_color = "#FFFFFF"
        text_color = "#333333"
        navy_color = "#002B4D"
        red_color = "#D32F2F"
        
        self.camera.background_color = bg_color

        # BÖLÜM 1: Giriş ve Basit Kesir (Kelime: 70, Süre: ~38.8 sn, Animasyon: 4 sn, Bekleme: 35 sn)
        title_basit = Text("Basit Kesir", color=navy_color, font_size=48).to_edge(UP)
        fraction_3_4 = MathTex(r"\frac{3}{4}", color=text_color, font_size=72).next_to(title_basit, DOWN, buff=0.5)
        
        # 3/4 Pizza Modeli
        pizza1 = VGroup()
        for i in range(4):
            if i < 3:
                slice_color = red_color
                opacity = 0.8
            else:
                slice_color = text_color
                opacity = 0.1
            
            pizza_slice = Sector(radius=1.5, angle=PI/2, start_angle=i*PI/2, color=slice_color, fill_opacity=opacity, stroke_color=bg_color, stroke_width=2)
            pizza1.add(pizza_slice)
        
        pizza1.next_to(fraction_3_4, DOWN, buff=1)

        self.play(Write(title_basit), run_time=1)
        self.play(Write(fraction_3_4), run_time=1)
        self.play(FadeIn(pizza1), run_time=2)
        self.wait(35)

        # BÖLÜM 2: Bileşik Kesir (Kelime: 58, Süre: ~32.2 sn, Animasyon: 4 sn, Bekleme: 28 sn)
        self.play(FadeOut(title_basit), FadeOut(fraction_3_4), FadeOut(pizza1), run_time=1)
        
        title_bilesik = Text("Bileşik Kesir", color=navy_color, font_size=48).to_edge(UP)
        fraction_5_4 = MathTex(r"\frac{5}{4}", color=text_color, font_size=72).next_to(title_bilesik, DOWN, buff=0.5)
        
        # 5/4 Pizza Modeli (2 Pizza)
        pizzas = VGroup()
        pizza2_full = VGroup()
        for i in range(4):
            pizza_slice = Sector(radius=1.2, angle=PI/2, start_angle=i*PI/2, color=red_color, fill_opacity=0.8, stroke_color=bg_color, stroke_width=2)
            pizza2_full.add(pizza_slice)
            
        pizza3_part = VGroup()
        for i in range(4):
            if i < 1:
                slice_color = red_color
                opacity = 0.8
            else:
                slice_color = text_color
                opacity = 0.1
            pizza_slice = Sector(radius=1.2, angle=PI/2, start_angle=i*PI/2, color=slice_color, fill_opacity=opacity, stroke_color=bg_color, stroke_width=2)
            pizza3_part.add(pizza_slice)
            
        pizzas.add(pizza2_full, pizza3_part).arrange(RIGHT, buff=1).next_to(fraction_5_4, DOWN, buff=1)

        self.play(Write(title_bilesik), Write(fraction_5_4), run_time=1)
        self.play(FadeIn(pizzas), run_time=2)
        self.wait(28)

        # BÖLÜM 3: Tam Sayılı Kesir ve Dönüşüm (Kelime: 103, Süre: ~57.2 sn, Animasyon: 5 sn, Bekleme: 52.5 sn)
        title_tam = Text("Tam Sayılı Kesir & Dönüşüm", color=navy_color, font_size=48).to_edge(UP)
        
        # 5/4 -> 1 1/4 Dönüşümü
        fraction_mixed = MathTex(r"1 \frac{1}{4}", color=text_color, font_size=72).next_to(title_tam, DOWN, buff=0.5)
        
        # Bölme işlemi mantığı
        div_logic = MathTex(r"5 \div 4 = 1 \text{ (Kalan: } 1\text{)}", color=navy_color, font_size=48).next_to(pizzas, DOWN, buff=0.5)
        
        # Çarpma işlemi mantığı
        mult_logic = MathTex(r"1 \frac{1}{4} = \frac{(1 \times 4) + 1}{4} = \frac{5}{4}", color=red_color, font_size=48).next_to(div_logic, DOWN, buff=0.5)

        self.play(Transform(title_bilesik, title_tam), Transform(fraction_5_4, fraction_mixed), run_time=1)
        self.play(Write(div_logic), run_time=2)
        self.play(Write(mult_logic), run_time=2)
        self.wait(52.5)

        # BÖLÜM 4: Çıkış (Kelime: 7, Süre: ~3.8 sn, Animasyon: 2 sn, Bekleme: 2 sn)
        self.play(FadeOut(title_bilesik), FadeOut(fraction_5_4), FadeOut(pizzas), FadeOut(div_logic), FadeOut(mult_logic), run_time=1)
        
        outro_text = Text("Maarif Matematik", color=navy_color, font_size=60)
        self.play(Write(outro_text), run_time=1)
        self.wait(2)
