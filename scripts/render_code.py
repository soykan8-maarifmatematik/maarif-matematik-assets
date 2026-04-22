from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi (Kural 1: Beyaz)
        self.camera.background_color = "#FFFFFF"
        
        # --- BÖLÜM 1: GİRİŞ ---
        # Kelime sayısı: 30. Süre: 30 / 2.5 = 12 saniye.
        title = Text("Kesirler: Pay ve Payda", color="#002B4D").scale(1.2).to_edge(UP)
        subtitle = Text("Bir bütünün eş parçaları", color="#333333").scale(0.8).next_to(title, DOWN)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle), run_time=0.5)
        # Kalan süre: 12 - 2 = 10 saniye
        self.wait(10)
        
        # --- BÖLÜM 2: PAY VE PAYDA KAVRAMI ---
        # Kelime sayısı: 30. Süre: 30 / 2.5 = 12 saniye.
        fraction = MathTex(r"\frac{3}{4}", color="#333333").scale(3).shift(LEFT*3)
        pay_text = Text("Pay (Alınan Parça)", color="#D32F2F").scale(0.6).next_to(fraction, UP, buff=1)
        payda_text = Text("Payda (Toplam Parça)", color="#002B4D").scale(0.6).next_to(fraction, DOWN, buff=1)
        
        arrow_pay = Arrow(pay_text.get_bottom(), fraction.get_top(), color="#D32F2F", buff=0.1)
        arrow_payda = Arrow(payda_text.get_top(), fraction.get_bottom(), color="#002B4D", buff=0.1)
        
        self.play(Write(fraction), run_time=1)
        self.play(FadeIn(pay_text), GrowArrow(arrow_pay), run_time=1)
        self.play(FadeIn(payda_text), GrowArrow(arrow_payda), run_time=1)
        # Kalan süre: 12 - 3 = 9 saniye
        self.wait(9)
        
        # --- BÖLÜM 3: PASTA DİLİMİ MODELİ (SECTOR) ---
        # Kelime sayısı: 27. Süre: 27 / 2.5 = 10.8 saniye.
        pie = VGroup()
        colors = ["#D32F2F", "#D32F2F", "#D32F2F", "#E0E0E0"]
        for i in range(4):
            # Kural 3: outer_radius ASLA kullanılmaz, radius kullanılır.
            sector = Sector(radius=1.5, angle=PI/2, start_angle=i*PI/2, color=colors[i], fill_opacity=0.9, stroke_color="#FFFFFF", stroke_width=3)
            pie.add(sector)
        pie.shift(RIGHT*3)
        
        self.play(DrawBorderThenFill(pie), run_time=1.8)
        # Kalan süre: 10.8 - 1.8 = 9 saniye
        self.wait(9)
        
        # --- BÖLÜM 4: KESRİN OKUNUŞU ---
        # Kelime sayısı: 31. Süre: 31 / 2.5 = 12.4 saniye.
        self.play(
            FadeOut(pie),
            FadeOut(pay_text),
            FadeOut(payda_text),
            FadeOut(arrow_pay),
            FadeOut(arrow_payda),
            run_time=1
        )
        
        self.play(fraction.animate.move_to(ORIGIN), run_time=1)
        
        read1 = Text("3 bölü 4", color="#D32F2F").scale(0.8).next_to(fraction, RIGHT, buff=2).shift(UP*0.5)
        read2 = Text("4'te 3", color="#002B4D").scale(0.8).next_to(fraction, RIGHT, buff=2).shift(DOWN*0.5)
        
        arrow_down = Arrow(fraction.get_top() + RIGHT*0.5, fraction.get_bottom() + RIGHT*0.5, color="#D32F2F")
        arrow_up = Arrow(fraction.get_bottom() + LEFT*0.5, fraction.get_top() + LEFT*0.5, color="#002B4D")
        
        self.play(GrowArrow(arrow_down), Write(read1), run_time=1)
        self.play(GrowArrow(arrow_up), Write(read2), run_time=1)
        # Kalan süre: 12.4 - 4 = 8.4 saniye
        self.wait(8.4)
        
        # --- BÖLÜM 5: SAYI DOĞRUSU (NUMBERLINE) ---
        # Kelime sayısı: 27. Süre: 27 / 2.5 = 10.8 saniye.
        self.play(
            FadeOut(fraction),
            FadeOut(read1),
            FadeOut(read2),
            FadeOut(arrow_down),
            FadeOut(arrow_up),
            run_time=1
        )
        
        nl = NumberLine(
            x_range=[0, 1, 0.25],
            length=8,
            color="#333333",
            include_numbers=False,
            label_direction=DOWN
        ).shift(DOWN*1)
        
        labels = VGroup(
            MathTex("0", color="#333333").next_to(nl.n2p(0), DOWN),
            MathTex("1", color="#333333").next_to(nl.n2p(1), DOWN)
        )
        
        dot = Dot(nl.n2p(0.75), color="#D32F2F", radius=0.15)
        dot_label = MathTex(r"\frac{3}{4}", color="#D32F2F").next_to(dot, UP)
        jump_arrow = CurvedArrow(nl.n2p(0), nl.n2p(0.75), angle=-TAU/4, color="#002B4D")
        
        self.play(Create(nl), Write(labels), run_time=1)
        self.play(Create(jump_arrow), run_time=1)
        self.play(FadeIn(dot), Write(dot_label), run_time=0.8)
        # Kalan süre: 10.8 - 3.8 = 7 saniye
        self.wait(7)
