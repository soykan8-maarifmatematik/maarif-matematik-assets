from manim import *

class Kesirler(Scene):
    def construct(self):
        # Renk Paleti
        BLUE_C = "#1976D2"
        RED_C = "#D32F2F"
        GRAY_C = "#333333"
        
        # Sabit Merkez Noktası
        main_center = DOWN * 0.5
        
        # 1. Giriş
        intro_text = Text("Merhaba, Maarif Matematik'e hoş geldiniz.", color=BLUE_C).scale(0.8)
        self.play(Write(intro_text))
        self.wait(5)
        self.play(FadeOut(intro_text))
        
        # 2. Kesir Nedir? (Pasta Modeli - Sector)
        title = Text("Kesirler: Bütünün Parçaları", color=BLUE_C).to_edge(UP)
        
        pie_group = VGroup()
        # 4 eşit parça (Başlangıçta hepsi gri)
        for i in range(4):
            slice = Sector(radius=1.8, angle=PI/2, start_angle=i*PI/2, color=GRAY_C, fill_opacity=0.3, stroke_color=WHITE, stroke_width=2)
            pie_group.add(slice)
        
        pie_group.move_to(main_center + LEFT * 3)
        
        self.play(Write(title), FadeIn(pie_group))
        self.wait(25)
        
        # 3. Payda Kavramı
        fraction_line = Line(LEFT, RIGHT, color=WHITE).move_to(main_center + RIGHT * 3)
        denom_num = MathTex("4", color=GRAY_C).next_to(fraction_line, DOWN, buff=0.3).scale(1.5)
        denom_text = Text("Payda (Toplam Parça)", color=GRAY_C).scale(0.5).next_to(denom_num, DOWN)
        
        self.play(Create(fraction_line), Write(denom_num), Write(denom_text))
        self.wait(30)
        
        # 4. Pay Kavramı
        # 3 dilimi maviye boyama
        self.play(
            pie_group[0].animate.set_color(BLUE_C).set_opacity(0.8),
            pie_group[1].animate.set_color(BLUE_C).set_opacity(0.8),
            pie_group[2].animate.set_color(BLUE_C).set_opacity(0.8)
        )
        
        num_num = MathTex("3", color=BLUE_C).next_to(fraction_line, UP, buff=0.3).scale(1.5)
        num_text = Text("Pay (Alınan Parça)", color=BLUE_C).scale(0.5).next_to(num_num, UP)
        
        self.play(Write(num_num), Write(num_text))
        self.wait(25)
        
        # 5. Okunuş 1 (a bölü b)
        arrow_down = Arrow(start=UP*1.5, end=DOWN*1.5, color=RED_C).next_to(fraction_line, LEFT, buff=1.2)
        read_text_1 = Text("3 bölü 4", color=RED_C).scale(0.6).next_to(arrow_down, LEFT)
        
        self.play(GrowArrow(arrow_down), Write(read_text_1))
        self.wait(30)
        
        # 6. Okunuş 2 (b'de a)
        arrow_up = Arrow(start=DOWN*1.5, end=UP*1.5, color=BLUE_C).next_to(fraction_line, RIGHT, buff=1.2)
        read_text_2 = Text("4'te 3", color=BLUE_C).scale(0.6).next_to(arrow_up, RIGHT)
        
        self.play(GrowArrow(arrow_up), Write(read_text_2))
        self.wait(35)
        
        # 7. Çıkış
        self.play(FadeOut(VGroup(pie_group, fraction_line, denom_num, denom_text, num_num, num_text, arrow_down, read_text_1, arrow_up, read_text_2, title)))
        
        outro_text = Text("Bir sonraki derste görüşmek üzere, hoşça kalın.", color=BLUE_C).scale(0.8)
        self.play(Write(outro_text))
        self.wait(20)
        self.play(FadeOut(outro_text))