from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi (Maarif Beyazı)
        self.camera.background_color = "#FFFFFF"
        
        # --- SAHNE 1: GİRİŞ ---
        # Kelime sayısı: 41. Süre: 20.5 saniye.
        # Animasyonlar: 2 saniye. Bekleme: 18.5 saniye.
        intro_text = Text("Kesir Kavramı", color="#333333", font_size=48)
        
        self.play(Write(intro_text)) # 1 sn
        self.wait(18.5) # 18.5 sn
        self.play(FadeOut(intro_text)) # 1 sn
        
        # --- SAHNE 2: PAY, PAYDA VE KESİR ÇİZGİSİ ---
        # Kelime sayısı: 42. Süre: 21.0 saniye.
        # Animasyonlar: 4 saniye. Bekleme: 17.0 saniye.
        frac_line = Line(LEFT*2, RIGHT*2, color="#333333", stroke_width=6)
        
        payda_text = Text("Payda", color="#002B4D", font_size=40).next_to(frac_line, DOWN, buff=0.5)
        payda_desc = Text("(Bütünün bölündüğü eş parça sayısı)", color="#333333", font_size=24).next_to(payda_text, DOWN)
        
        pay_text = Text("Pay", color="#D32F2F", font_size=40).next_to(frac_line, UP, buff=0.5)
        pay_desc = Text("(Alınan eş parça sayısı)", color="#333333", font_size=24).next_to(pay_text, UP)

        self.play(Create(frac_line)) # 1 sn
        self.wait(6.0) # 6 sn

        self.play(Write(VGroup(payda_text, payda_desc))) # 1 sn
        self.wait(6.0) # 6 sn

        self.play(Write(VGroup(pay_text, pay_desc))) # 1 sn
        self.wait(5.0) # 5 sn

        self.play(FadeOut(VGroup(frac_line, payda_text, payda_desc, pay_text, pay_desc))) # 1 sn

        # --- SAHNE 3: PİZZA MODELİ (SECTOR) ---
        # Kelime sayısı: 41. Süre: 20.5 saniye.
        # Animasyonlar: 4 saniye. Bekleme: 16.5 saniye.
        
        # Bütün pizza (4 eş parça çizgileriyle)
        circle = Circle(radius=2, color="#333333", stroke_width=4).shift(LEFT*3)
        l1 = Line(circle.get_top(), circle.get_bottom(), color="#333333")
        l2 = Line(circle.get_left(), circle.get_right(), color="#333333")
        pizza = VGroup(circle, l1, l2)

        frac_line_2 = Line(LEFT*0.5, RIGHT*0.5, color="#333333", stroke_width=6).shift(RIGHT*3)
        denom_4 = Text("4", color="#002B4D", font_size=48).next_to(frac_line_2, DOWN)
        num_3 = Text("3", color="#D32F2F", font_size=48).next_to(frac_line_2, UP)

        self.play(Create(pizza), Create(frac_line_2)) # 1 sn
        self.wait(8.5) # 8.5 sn

        self.play(Write(denom_4)) # 1 sn
        self.wait(1.5) # 1.5 sn

        # Alınan 3 parça (Sector objesinde outer_radius YASAK, radius kullanıldı)
        s1 = Sector(radius=2, angle=PI/2, start_angle=0, color="#D32F2F", fill_opacity=0.8).shift(LEFT*3)
        s2 = Sector(radius=2, angle=PI/2, start_angle=PI/2, color="#D32F2F", fill_opacity=0.8).shift(LEFT*3)
        s3 = Sector(radius=2, angle=PI/2, start_angle=PI, color="#D32F2F", fill_opacity=0.8).shift(LEFT*3)

        self.play(Create(VGroup(s1, s2, s3)), Write(num_3)) # 1 sn
        self.wait(6.5) # 6.5 sn

        self.play(FadeOut(VGroup(pizza, frac_line_2, denom_4, num_3, s1, s2, s3))) # 1 sn

        # --- SAHNE 4: KESRİN OKUNUŞU ---
        # Kelime sayısı: 43. Süre: 21.5 saniye.
        # Animasyonlar: 4 saniye. Bekleme: 17.5 saniye.
        
        frac_group = VGroup(
            Text("3", color="#D32F2F", font_size=72),
            Line(LEFT, RIGHT, color="#333333", stroke_width=6),
            Text("4", color="#002B4D", font_size=72)
        ).arrange(DOWN, buff=0.3)

        arrow_down = Arrow(start=UP*2, end=DOWN*2, color="#D32F2F", stroke_width=6, max_tip_length_to_length_ratio=0.15).next_to(frac_group, LEFT, buff=1.5)
        text_down = Text("Üç bölü dört", color="#D32F2F", font_size=36).next_to(arrow_down, LEFT)

        arrow_up = Arrow(start=DOWN*2, end=UP*2, color="#002B4D", stroke_width=6, max_tip_length_to_length_ratio=0.15).next_to(frac_group, RIGHT, buff=1.5)
        text_up = Text("Dörtte üç", color="#002B4D", font_size=36).next_to(arrow_up, RIGHT)

        self.play(Write(frac_group)) # 1 sn
        self.wait(4.0) # 4 sn

        self.play(Create(arrow_down), Write(text_down)) # 1 sn
        self.wait(4.0) # 4 sn

        self.play(Create(arrow_up), Write(text_up)) # 1 sn
        self.wait(6.5) # 6.5 sn

        self.play(Indicate(frac_group, color="#333333")) # 1 sn
        self.wait(3.0) # 3 sn
