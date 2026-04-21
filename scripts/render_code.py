from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi
        self.camera.background_color = "#FFFFFF"

        # P1: Giriş (5 kelime -> 2 saniye)
        title = Text("Maarif Matematik", color="#333333", font_size=60)
        self.play(Write(title)) # 1s
        self.wait(1) # 1s

        # P2: Kesir Nedir? (79 kelime -> 26 saniye)
        self.play(FadeOut(title)) # 1s
        q_text = Text("Kesir Nedir?", color="#333333", font_size=48).to_edge(UP)
        self.play(Write(q_text)) # 1s
        circle_whole = Circle(radius=2, color="#333333", fill_opacity=0.1)
        self.play(Create(circle_whole)) # 1s
        self.wait(23) # 23s

        # P3: Pay ve Payda (81 kelime -> 27 saniye)
        self.play(FadeOut(circle_whole), FadeOut(q_text)) # 1s
        frac_line_main = Line(LEFT, RIGHT, color="#333333").scale(1.5)
        pay_text = Text("Pay", color="#1976D2", font_size=48).next_to(frac_line_main, UP, buff=0.5)
        payda_text = Text("Payda", color="#D32F2F", font_size=48).next_to(frac_line_main, DOWN, buff=0.5)
        self.play(Create(frac_line_main)) # 1s
        self.play(Write(payda_text)) # 1s
        self.play(Write(pay_text)) # 1s
        self.wait(23) # 23s

        # P4: Daire Örneği 3/4 (90 kelime -> 30 saniye)
        self.play(FadeOut(frac_line_main), FadeOut(pay_text), FadeOut(payda_text)) # 1s
        pie = Circle(radius=2, color="#333333", fill_opacity=0).shift(LEFT*3)
        self.play(Create(pie)) # 1s
        lines = VGroup(
            Line(pie.get_top(), pie.get_bottom(), color="#333333"),
            Line(pie.get_left(), pie.get_right(), color="#333333")
        )
        self.play(Create(lines)) # 1s
        frac_line = Line(LEFT, RIGHT, color="#333333").shift(RIGHT*3)
        denom_4 = Text("4", color="#D32F2F", font_size=60).next_to(frac_line, DOWN, buff=0.5)
        self.play(Create(frac_line), Write(denom_4)) # 1s
        
        sectors = VGroup()
        for i in range(3):
            sector = Sector(radius=2, angle=PI/2, start_angle=i*PI/2, color="#1976D2", fill_opacity=0.6).shift(LEFT*3)
            sectors.add(sector)
        self.play(FadeIn(sectors)) # 1s
        num_3 = Text("3", color="#1976D2", font_size=60).next_to(frac_line, UP, buff=0.5)
        self.play(Write(num_3)) # 1s
        self.wait(24) # 24s

        # P5: Okunuş 1 (79 kelime -> 26 saniye)
        read1 = Text("Üç bölü dört", color="#333333", font_size=36).next_to(frac_line, RIGHT, buff=1).shift(UP*0.5)
        self.play(Write(read1)) # 1s
        read2 = Text("Dörtte üç", color="#333333", font_size=36).next_to(frac_line, RIGHT, buff=1).shift(DOWN*0.5)
        self.play(Write(read2)) # 1s
        self.wait(24) # 24s

        # P6: Çikolata Örneği 5/8 (75 kelime -> 25 saniye)
        self.play(FadeOut(pie), FadeOut(lines), FadeOut(sectors), FadeOut(frac_line), FadeOut(denom_4), FadeOut(num_3), FadeOut(read1), FadeOut(read2)) # 1s
        rect = Rectangle(width=4, height=2, color="#333333").shift(LEFT*3)
        self.play(Create(rect)) # 1s
        v_lines = VGroup(*[Line(rect.get_corner(UL) + RIGHT*i, rect.get_corner(DL) + RIGHT*i, color="#333333") for i in range(1, 4)])
        h_line = Line(rect.get_left(), rect.get_right(), color="#333333")
        self.play(Create(v_lines), Create(h_line)) # 1s
        
        frac_line2 = Line(LEFT, RIGHT, color="#333333").shift(RIGHT*3)
        denom_8 = Text("8", color="#D32F2F", font_size=60).next_to(frac_line2, DOWN, buff=0.5)
        self.play(Create(frac_line2), Write(denom_8)) # 1s

        choc_pieces = VGroup()
        for i in range(5):
            row = i // 4
            col = i % 4
            piece = Rectangle(width=1, height=1, color="#333333", fill_color="#1976D2", fill_opacity=0.6)
            piece.move_to(rect.get_corner(UL) + RIGHT*(col + 0.5) + DOWN*(row + 0.5))
            choc_pieces.add(piece)
        self.play(FadeIn(choc_pieces)) # 1s
        
        num_5 = Text("5", color="#1976D2", font_size=60).next_to(frac_line2, UP, buff=0.5)
        self.play(Write(num_5)) # 1s
        self.wait(19) # 19s

        # P7: Okunuş 2 (75 kelime -> 25 saniye)
        read3 = Text("Beş bölü sekiz", color="#333333", font_size=36).next_to(frac_line2, RIGHT, buff=1).shift(UP*0.5)
        self.play(Write(read3)) # 1s
        read4 = Text("Sekizde beş", color="#333333", font_size=36).next_to(frac_line2, RIGHT, buff=1).shift(DOWN*0.5)
        self.play(Write(read4)) # 1s
        self.wait(23) # 23s

        # P8: Kapanış ve Özet (71 kelime -> 24 saniye)
        self.play(FadeOut(rect), FadeOut(v_lines), FadeOut(h_line), FadeOut(choc_pieces), FadeOut(frac_line2), FadeOut(denom_8), FadeOut(num_5), FadeOut(read3), FadeOut(read4)) # 1s
        summary = Text("a bölü b\nveya\nb'de a", color="#333333", font_size=48, text_align="center")
        self.play(Write(summary)) # 1s
        self.wait(20) # 20s
        self.play(FadeOut(summary)) # 1s
        outro = Text("Maarif Matematik", color="#333333", font_size=60)
        self.play(Write(outro)) # 1s
