from manim import *

class KesirNedir(Scene):
    def construct(self):
        # 1. KURALLAR: Renk ve Estetik
        self.camera.background_color = "#FFFFFF"
        TEXT_COLOR = "#333333"
        NUM_COLOR = "#1976D2"
        DENOM_COLOR = "#D32F2F"

        # 1. KURALLAR: Merkez Nokta Sabitleme
        main_center = DOWN * 0.5

        # GİRİŞ VE KESİR KAVRAMI (Yaklaşık 13 saniye bekleme)
        title = Tex("Kesir Nedir?", color=TEXT_COLOR).to_edge(UP)
        self.play(Write(title), run_time=1)
        self.wait(13)

        # GÖRSELLEŞTİRME: 4 parçaya bölünmüş, 3'ü alınmış bütün
        # 3. KURALLAR: Sector objesinde outer_radius yasak, sadece radius kullanıldı.
        circle_group = VGroup()
        s1 = Sector(radius=1.2, angle=PI/2, start_angle=0, color=NUM_COLOR, fill_opacity=1, stroke_color=DENOM_COLOR, stroke_width=4)
        s2 = Sector(radius=1.2, angle=PI/2, start_angle=PI/2, color=NUM_COLOR, fill_opacity=1, stroke_color=DENOM_COLOR, stroke_width=4)
        s3 = Sector(radius=1.2, angle=PI/2, start_angle=PI, color=NUM_COLOR, fill_opacity=1, stroke_color=DENOM_COLOR, stroke_width=4)
        s4 = Sector(radius=1.2, angle=PI/2, start_angle=3*PI/2, color="#FFFFFF", fill_opacity=1, stroke_color=DENOM_COLOR, stroke_width=4)
        
        circle_group.add(s1, s2, s3, s4).move_to(main_center + UP * 2)
        self.play(Create(circle_group), run_time=1.5)
        self.wait(10)

        # PAY VE PAYDA İLİŞKİSİ
        # Kesir çizgisi
        frac_line = Line(LEFT, RIGHT, color=TEXT_COLOR).set_length(1.5).move_to(main_center + DOWN * 0.5)
        self.play(Create(frac_line), run_time=0.5)
        self.wait(4)

        # Payda (Kırmızı)
        denom_num = MathTex("4", color=DENOM_COLOR).next_to(frac_line, DOWN, buff=0.3)
        denom_text = Tex("Payda", color=DENOM_COLOR).next_to(denom_num, RIGHT, buff=0.5)
        self.play(Write(denom_num), Write(denom_text), run_time=1)
        self.wait(9)

        # Pay (Mavi)
        num_num = MathTex("3", color=NUM_COLOR).next_to(frac_line, UP, buff=0.3)
        num_text = Tex("Pay", color=NUM_COLOR).next_to(num_num, RIGHT, buff=0.5)
        self.play(Write(num_num), Write(num_text), run_time=1)
        self.wait(9)

        # KESİRLERİN OKUNUŞU
        # 3. KURALLAR: Okunuş yönleri için Arrow ve GrowArrow kullanımı
        # Yukarıdan aşağıya okunuş (a bölü b)
        arrow_down = Arrow(start=main_center + LEFT*1.5 + UP*0.2, end=main_center + LEFT*1.5 + DOWN*1.2, color=TEXT_COLOR)
        read_down = Tex("Üç bölü dört", color=TEXT_COLOR).next_to(arrow_down, LEFT)
        self.play(GrowArrow(arrow_down), Write(read_down), run_time=1)
        self.wait(8)

        # Aşağıdan yukarıya okunuş (b'de a)
        arrow_up = Arrow(start=main_center + RIGHT*2.5 + DOWN*1.2, end=main_center + RIGHT*2.5 + UP*0.2, color=TEXT_COLOR)
        read_up = Tex("Dörtte üç", color=TEXT_COLOR).next_to(arrow_up, RIGHT)
        self.play(GrowArrow(arrow_up), Write(read_up), run_time=1)
        self.wait(8)

        # KAPANIŞ
        self.wait(3)
