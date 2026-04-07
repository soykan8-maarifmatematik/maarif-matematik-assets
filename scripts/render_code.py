from manim import *

class FractionsLogic(Scene):
    def construct(self):
        # KURAL: Arka plan BEYAZ, Yazılar KOYU GRİ
        self.camera.background_color = WHITE
        
        # BÖLÜM 1: GİRİŞ (Toplam 93.5 Saniye - 187 kelimeye denk)
        title = Text("Maarif Matematik", color=BLUE).scale(1.5)
        self.play(Write(title), run_time=2) # 2s
        self.wait(5.5) # Toplam 7.5s
        self.play(FadeOut(title), run_time=1) # Toplam 8.5s
        
        # Çikolatalı Pasta Modeli
        cake = Circle(radius=2, color=DARK_GRAY, fill_color="#8B4513", fill_opacity=0.8)
        self.play(DrawBorderThenFill(cake), run_time=3) # Toplam 11.5s
        self.wait(10) # Toplam 21.5s
        
        # Pastayı 8 eş parçaya bölme
        lines = VGroup(*[Line(cake.point_at_angle(a), cake.point_at_angle(a+PI), color=WHITE) for a in [0, PI/4, PI/2, 3*PI/4]])
        self.play(Create(lines), run_time=4) # Toplam 25.5s
        self.wait(15) # Toplam 40.5s
        
        # Bir dilimi (arkadaşa düşen payı) vurgulama
        slice_highlight = Sector(outer_radius=2, angle=PI/4, start_angle=0, color=BLUE, fill_opacity=0.5)
        self.play(FadeIn(slice_highlight), run_time=2) # Toplam 42.5s
        self.wait(15) # Toplam 57.5s
        
        text_adil = Text("Adil Paylaşım", color=BLUE).next_to(cake, DOWN)
        self.play(Write(text_adil), run_time=2) # Toplam 59.5s
        self.wait(15) # Toplam 74.5s
        
        text_kesir = Text("Kesirler", color=GREEN).next_to(text_adil, DOWN)
        self.play(Write(text_kesir), run_time=2) # Toplam 76.5s
        self.wait(15) # Toplam 91.5s
        
        self.play(FadeOut(Group(cake, lines, slice_highlight, text_adil, text_kesir)), run_time=2) # Toplam 93.5s
        
        
        # BÖLÜM 2: KAVRAMSAL DERİNLİK (Toplam 97 Saniye - 194 kelimeye denk)
        frac_word = MathTex(r"\frac{\text{Pay}}{\text{Payda}}", color=DARK_GRAY).scale(2)
        self.play(Write(frac_word), run_time=2) # 2s
        self.wait(10) # 12s
        
        payda_desc = Text("Bütün (Pay edilen)", color=BLUE, font_size=30).next_to(frac_word, DOWN, buff=1)
        self.play(Write(payda_desc), run_time=2) # 14s
        self.wait(20) # 34s
        
        pay_desc = Text("Hisse (Alınan parça)", color=GREEN, font_size=30).next_to(frac_word, UP, buff=1)
        self.play(Write(pay_desc), run_time=2) # 36s
        self.wait(20) # 56s
        
        frac_num = MathTex(r"\frac{3}{8}", color=DARK_GRAY).scale(2.5)
        self.play(ReplacementTransform(frac_word, frac_num), FadeOut(payda_desc), FadeOut(pay_desc), run_time=2) # 58s
        self.wait(10) # 68s
        
        read_1 = Text("Sekizde üç", color=BLUE, font_size=36).next_to(frac_num, DOWN, buff=1)
        read_2 = Text("Üç bölü sekiz", color=GREEN, font_size=36).next_to(read_1, DOWN, buff=0.5)
        self.play(Write(read_1), run_time=2) # 70s
        self.wait(10) # 80s
        
        self.play(Write(read_2), run_time=2) # 82s
        self.wait(13) # 95s
        
        self.play(FadeOut(Group(frac_num, read_1, read_2)), run_time=2) # 97s
        
        
        # BÖLÜM 3: İNTERAKTİF SORU-CEVAP (Toplam 93 Saniye - 166 kelime + 10s bekleme)
        rect = Rectangle(width=5, height=2, color=DARK_GRAY)
        v_lines = VGroup(*[Line(rect.get_corner(UL) + RIGHT*i, rect.get_corner(DL) + RIGHT*i, color=DARK_GRAY) for i in range(1, 5)])
        self.play(Create(rect), Create(v_lines), run_time=2) # 2s
        self.wait(10) # 12s
        
        # 3 parça boyanır
        fills = VGroup(*[Rectangle(width=1, height=2, color=DARK_GRAY, fill_color=BLUE, fill_opacity=0.7).move_to(rect.get_left() + RIGHT*0.5 + RIGHT*i) for i in range(3)])
        self.play(FadeIn(fills), run_time=2) # 14s
        self.wait(15) # 29s
        
        # Düşünme payı için saat animasyonu (10 saniye bekleme)
        clock = Circle(radius=0.5, color=BLUE).to_corner(UR)
        clock_hand = Line(clock.get_center(), clock.get_center() + UP*0.4, color=DARK_GRAY)
        self.play(Create(clock), Create(clock_hand), run_time=2) # 31s
        
        # Tam 10 saniyelik self.play(Rotate...) ile beklemeyi görselleştiriyoruz
        self.play(Rotate(clock_hand, angle=-2*PI, about_point=clock.get_center(), rate_func=linear), run_time=10) # 41s
        self.play(FadeOut(clock), FadeOut(clock_hand), run_time=1) # 42s
        self.wait(10) # 52s
        
        payda_text = Text("5 Eş Parça", color=BLUE).next_to(rect, DOWN)
        self.play(Write(payda_text), run_time=2) # 54s
        self.wait(10) # 64s
        
        pay_text = Text("3 Boyalı Parça", color=GREEN).next_to(rect, UP)
        self.play(Write(pay_text), run_time=2) # 66s
        self.wait(10) # 76s
        
        ans_frac = MathTex(r"\frac{3}{5}", color=DARK_GRAY).scale(2).next_to(rect, RIGHT, buff=1)
        self.play(Write(ans_frac), run_time=2) # 78s
        self.wait(13) # 91s
        
        self.play(FadeOut(Group(rect, v_lines, fills, payda_text, pay_text, ans_frac)), run_time=2) # 93s
        
        
        # BÖLÜM 4: ÇOKLU MODELLEME (Toplam 101 Saniye - 202 kelime)
        model_frac = MathTex(r"\frac{1}{4}", color=DARK_GRAY).scale(1.5).to_edge(UP)
        self.play(Write(model_frac), run_time=2) # 2s
        self.wait(5) # 7s
        
        # Dairesel Model
        circ = Circle(radius=1.5, color=DARK_GRAY).move_to(LEFT*3)
        c_lines = VGroup(Line(circ.get_top(), circ.get_bottom(), color=DARK_GRAY), Line(circ.get_left(), circ.get_right(), color=DARK_GRAY))
        self.play(Create(circ), Create(c_lines), run_time=2) # 9s
        self.wait(10) # 19s
        
        c_fill = Sector(outer_radius=1.5, angle=PI/2, start_angle=0, color=GREEN, fill_opacity=0.7).move_to(LEFT*3)
        self.play(FadeIn(c_fill), run_time=2) # 21s
        self.wait(15) # 36s
        
        # Sayı Doğrusu Modeli
        nl = NumberLine(x_range=[0, 1, 0.25], length=5, color=DARK_GRAY, include_numbers=False).move_to(RIGHT*3)
        nl_0 = MathTex("0", color=DARK_GRAY).next_to(nl.n2p(0), DOWN)
        nl_1 = MathTex("1", color=DARK_GRAY).next_to(nl.n2p(1), DOWN)
        self.play(Create(nl), Write(nl_0), Write(nl_1), run_time=3) # 39s
        self.wait(15) # 54s
        
        ticks = VGroup(*[nl.get_tick(x) for x in [0.25, 0.5, 0.75]])
        self.play(Create(ticks), run_time=2) # 56s
        self.wait(10) # 66s
        
        arc = CurvedArrow(nl.n2p(0), nl.n2p(0.25), angle=-PI/2, color=BLUE)
        self.play(Create(arc), run_time=2) # 68s
        self.wait(5) # 73s
        
        nl_frac = MathTex(r"\frac{1}{4}", color=BLUE).next_to(nl.n2p(0.25), UP)
        self.play(Write(nl_frac), run_time=2) # 75s
        self.wait(24) # 99s
        
        self.play(FadeOut(Group(model_frac, circ, c_lines, c_fill, nl, nl_0, nl_1, ticks, arc, nl_frac)), run_time=2) # 101s
        
        
        # BÖLÜM 5: ÖZET VE KAPANIŞ (Toplam 61 Saniye - 114 kelime + 4s kapanış)
        self.wait(10) # 10s (Özet konuşması başlarken boşluk)
        
        question_title = Text("Günün Sorusu", color=BLUE).to_edge(UP)
        self.play(Write(question_title), run_time=2) # 12s
        self.wait(5) # 17s
        
        hexa = RegularPolygon(n=6, radius=2, color=DARK_GRAY)
        h_lines = VGroup(*[Line(hexa.get_vertices()[i], hexa.get_center(), color=DARK_GRAY) for i in range(6)])
        self.play(Create(hexa), Create(h_lines), run_time=3) # 20s
        self.wait(5) # 25s
        
        h_fills = VGroup(*[Polygon(hexa.get_center(), hexa.get_vertices()[i], hexa.get_vertices()[(i+1)%6], color=DARK_GRAY, fill_color=BLUE, fill_opacity=0.7) for i in range(4)])
        self.play(FadeIn(h_fills), run_time=2) # 27s
        self.wait(15) # 42s
        
        farewell = Text("Hoşça kalın...", color=GREEN).next_to(hexa, DOWN, buff=1)
        self.play(Write(farewell), run_time=2) # 44s
        self.wait(13) # 57s
        
        # Kapanış cümlesi sonrası kural gereği 4 saniye bekleme
        self.wait(4) # 61s
