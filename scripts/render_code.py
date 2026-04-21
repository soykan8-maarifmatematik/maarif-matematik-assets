from manim import *

class MaarifScene(Scene):
    def construct(self):
        # 1. MARKA KİMLİĞİ VE ESTETİK
        self.camera.background_color = "#FFFFFF"
        
        # SCENE 1: Kesir Nedir? (25 kelime -> 10.0 sn)
        title = Text("Kesir Nedir?", color="#002B4D", font_size=48).to_edge(UP)
        self.play(Write(title)) # 1 sn
        
        whole_circle = Circle(radius=1.5, color="#002B4D", fill_opacity=0.1)
        self.play(Create(whole_circle)) # 1 sn
        
        self.wait(7.0) # (10.0 - 3 animasyon)
        self.play(FadeOut(whole_circle)) # 1 sn
        
        # SCENE 2: Pay ve Payda (33 kelime -> 13.2 sn)
        frac_line = Line(LEFT*0.5, RIGHT*0.5, color="#333333").shift(UP*0.5)
        pay_text = Text("3", color="#D32F2F", font_size=48).next_to(frac_line, UP)
        payda_text = Text("4", color="#002B4D", font_size=48).next_to(frac_line, DOWN)
        
        pay_label = Text("Pay (Seçilen Parça)", color="#D32F2F", font_size=24).next_to(pay_text, RIGHT*2)
        payda_label = Text("Payda (Bütün)", color="#002B4D", font_size=24).next_to(payda_text, RIGHT*2)
        
        arrow_payda = Arrow(payda_label.get_left(), payda_text.get_right(), color="#002B4D", buff=0.1)
        arrow_pay = Arrow(pay_label.get_left(), pay_text.get_right(), color="#D32F2F", buff=0.1)
        
        self.play(Create(frac_line)) # 1 sn
        self.play(Write(payda_text), Write(payda_label), Create(arrow_payda)) # 1 sn
        self.play(Write(pay_text), Write(pay_label), Create(arrow_pay)) # 1 sn
        
        self.wait(9.2) # (13.2 - 4 animasyon)
        self.play(FadeOut(VGroup(frac_line, pay_text, payda_text, pay_label, payda_label, arrow_pay, arrow_payda))) # 1 sn
        
        # SCENE 3: Görselleştirme (Pasta Dilimi ve Sayı Doğrusu) (32 kelime -> 12.8 sn)
        pie_group = VGroup()
        colors = ["#D32F2F", "#D32F2F", "#D32F2F", "#002B4D"]
        opacities = [0.8, 0.8, 0.8, 0.2]
        for i in range(4):
            sector = Sector(radius=1.5, angle=PI/2, start_angle=i*PI/2, color=colors[i], fill_opacity=opacities[i], stroke_width=2, stroke_color="#FFFFFF").shift(LEFT*3)
            pie_group.add(sector)
            
        nl = NumberLine(x_range=[0, 1, 0.25], length=5, color="#333333", include_numbers=False).shift(RIGHT*3 + DOWN*0.5)
        label_0 = Text("0", color="#333333", font_size=24).next_to(nl.n2p(0), DOWN)
        label_1 = Text("1", color="#333333", font_size=24).next_to(nl.n2p(1), DOWN)
        nl_group = VGroup(nl, label_0, label_1)
        
        arrow_nl = Arrow(nl.n2p(0.75) + UP*1, nl.n2p(0.75), color="#D32F2F", buff=0.1)
        nl_label = Text("3/4", color="#D32F2F", font_size=24).next_to(arrow_nl, UP)
        
        self.play(Create(pie_group)) # 1 sn
        self.play(Create(nl_group)) # 1 sn
        self.play(Create(arrow_nl), Write(nl_label)) # 1 sn
        
        self.wait(8.8) # (12.8 - 4 animasyon)
        self.play(FadeOut(pie_group), FadeOut(nl_group), FadeOut(arrow_nl), FadeOut(nl_label)) # 1 sn
        
        # SCENE 4: Kesrin Okunuşu (29 kelime -> 11.6 sn)
        frac_line2 = Line(LEFT*0.5, RIGHT*0.5, color="#333333")
        pay2 = Text("3", color="#D32F2F", font_size=48).next_to(frac_line2, UP)
        payda2 = Text("4", color="#002B4D", font_size=48).next_to(frac_line2, DOWN)
        frac_group = VGroup(frac_line2, pay2, payda2).shift(LEFT*3)
        
        read1_text = Text("1) Üç bölü dört", color="#333333", font_size=36)
        read1_arrow = Arrow(UP, DOWN, color="#D32F2F").next_to(read1_text, LEFT)
        read1_group = VGroup(read1_arrow, read1_text).shift(RIGHT*2 + UP*1)
        
        read2_text = Text("2) Dörtte üç", color="#333333", font_size=36)
        read2_arrow = Arrow(DOWN, UP, color="#002B4D").next_to(read2_text, LEFT)
        read2_group = VGroup(read2_arrow, read2_text).shift(RIGHT*2 + DOWN*1)
        
        self.play(Create(frac_group)) # 1 sn
        self.play(Write(read1_group)) # 1 sn
        self.play(Write(read2_group)) # 1 sn
        
        self.wait(8.6) # (11.6 - 3 animasyon)
