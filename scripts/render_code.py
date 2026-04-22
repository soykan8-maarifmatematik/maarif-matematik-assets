from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Renk Paleti
        self.camera.background_color = "#FFFFFF"
        dark_gray = "#333333"
        maarif_navy = "#002B4D"
        maarif_red = "#D32F2F"

        # SAHNE 1: Giriş
        # Kelime: 35 -> Süre: 17.5 sn. Animasyon: 2 sn. Bekleme: 15.5 sn.
        title = Text("Kesirler ve Mantığı", color=maarif_navy, font_size=48)
        self.play(Write(title)) # 1 sn
        self.wait(15.5)
        self.play(FadeOut(title)) # 1 sn

        # SAHNE 2: Pay, Payda ve Kesir Çizgisi
        # Kelime: 47 -> Süre: 23.5 sn. Animasyon: 5 sn. Bekleme: 18.5 sn.
        frac_line = Line(LEFT, RIGHT, color=dark_gray).scale(0.5)
        pay_text = MathTex("3", color=maarif_red, font_size=72).next_to(frac_line, UP)
        payda_text = MathTex("4", color=maarif_navy, font_size=72).next_to(frac_line, DOWN)
        
        pay_label = Text("Pay (Seçilen)", color=maarif_red, font_size=24).next_to(pay_text, RIGHT, buff=1)
        pay_arrow = Arrow(pay_label.get_left(), pay_text.get_right(), color=maarif_red, buff=0.1)
        
        payda_label = Text("Payda (Bölünen Eş Parça)", color=maarif_navy, font_size=24).next_to(payda_text, RIGHT, buff=1)
        payda_arrow = Arrow(payda_label.get_left(), payda_text.get_right(), color=maarif_navy, buff=0.1)

        self.play(Create(frac_line)) # 1 sn
        self.play(Write(payda_text), Write(payda_label), Create(payda_arrow)) # 1 sn
        self.play(Write(pay_text), Write(pay_label), Create(pay_arrow)) # 1 sn
        self.wait(18.5)
        
        group_scene2 = VGroup(frac_line, pay_text, payda_text, pay_label, pay_arrow, payda_label, payda_arrow)
        self.play(group_scene2.animate.shift(LEFT * 4).scale(0.7)) # 1 sn
        self.play(FadeOut(pay_label, pay_arrow, payda_label, payda_arrow)) # 1 sn

        # SAHNE 3: Model Üzerinde Gösterim (Sector)
        # Kelime: 43 -> Süre: 21.5 sn. Animasyon: 3 sn. Bekleme: 18.5 sn.
        sectors = VGroup()
        for i in range(4):
            sector = Sector(radius=2.5, angle=PI/2, start_angle=i*PI/2, color=dark_gray, fill_opacity=0.05, stroke_width=2, stroke_color=dark_gray)
            sectors.add(sector)
        sectors.move_to(RIGHT * 3)
        
        self.play(Create(sectors)) # 1 sn
        
        colored_sectors = VGroup()
        for i in range(3):
            c_sec = Sector(radius=2.5, angle=PI/2, start_angle=i*PI/2, color=maarif_red, fill_opacity=0.8, stroke_width=2, stroke_color=dark_gray)
            colored_sectors.add(c_sec)
        colored_sectors.move_to(RIGHT * 3)

        self.play(Create(colored_sectors)) # 1 sn
        self.wait(18.5)
        self.play(FadeOut(sectors, colored_sectors, group_scene2)) # 1 sn

        # SAHNE 4: Kesrin Okunuşu
        # Kelime: 42 -> Süre: 21.0 sn. Animasyon: 4 sn. Bekleme: 17.0 sn.
        frac_read = VGroup(
            MathTex("3", color=maarif_red, font_size=72),
            Line(LEFT, RIGHT, color=dark_gray).scale(0.5),
            MathTex("4", color=maarif_navy, font_size=72)
        ).arrange(DOWN, buff=0.2)
        
        read1_text = Text("Üç bölü dört", color=dark_gray, font_size=36).next_to(frac_read, RIGHT, buff=2).shift(UP*1)
        arrow_down = Arrow(start=UP, end=DOWN, color=dark_gray).next_to(read1_text, LEFT)
        
        read2_text = Text("Dörtte üç", color=maarif_navy, font_size=36).next_to(frac_read, RIGHT, buff=2).shift(DOWN*1)
        arrow_up = Arrow(start=DOWN, end=UP, color=maarif_navy).next_to(read2_text, LEFT)

        self.play(Write(frac_read)) # 1 sn
        self.play(Create(arrow_down), Write(read1_text)) # 1 sn
        self.play(Create(arrow_up), Write(read2_text)) # 1 sn
        self.wait(17.0)
        self.play(FadeOut(frac_read, read1_text, arrow_down, read2_text, arrow_up)) # 1 sn

        # SAHNE 5: Sayı Doğrusu
        # Kelime: 45 -> Süre: 22.5 sn. Animasyon: 4 sn. Bekleme: 18.5 sn.
        nl = NumberLine(
            x_range=[0, 1, 0.25],
            length=8,
            color=dark_gray,
            include_numbers=False,
            tick_size=0.15
        )
        
        labels = VGroup(
            MathTex("0", color=dark_gray).next_to(nl.n2p(0), DOWN),
            MathTex("1", color=dark_gray).next_to(nl.n2p(1), DOWN)
        )
        
        self.play(Create(nl), Write(labels)) # 1 sn
        
        jumps = VGroup()
        for i in range(3):
            start_pt = nl.n2p(i * 0.25)
            end_pt = nl.n2p((i + 1) * 0.25)
            arc = ArcBetweenPoints(start_pt, end_pt, angle=-PI/2, color=maarif_red)
            jumps.add(arc)
        
        self.play(Create(jumps)) # 1 sn
        
        dot = Dot(nl.n2p(0.75), color=maarif_red, radius=0.15)
        dot_label = MathTex(r"\frac{3}{4}", color=maarif_red, font_size=48).next_to(dot, UP)
        
        self.play(Create(dot), Write(dot_label)) # 1 sn
        self.wait(18.5)
        self.play(FadeOut(nl, labels, jumps, dot, dot_label)) # 1 sn
