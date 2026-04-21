from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Renk Tanımlamaları
        BG_COLOR = "#FFFFFF"
        TEXT_COLOR = "#333333"
        PAY_COLOR = "#1976D2"
        PAYDA_COLOR = "#D32F2F"
        
        self.camera.background_color = BG_COLOR

        # Sahne 1: Giriş
        title = Text("Kesirler", color=TEXT_COLOR, font_size=64)
        self.play(Write(title))
        self.wait(13)
        self.play(FadeOut(title))

        # Sahne 2: Kesir Yapısı (Pay, Kesir Çizgisi, Payda)
        pay_text = Text("3", color=PAY_COLOR, font_size=96)
        line = Line(LEFT, RIGHT, color=TEXT_COLOR, stroke_width=8).scale(1.5)
        payda_text = Text("4", color=PAYDA_COLOR, font_size=96)

        fraction_group = VGroup(pay_text, line, payda_text).arrange(DOWN, buff=0.5)
        self.play(FadeIn(fraction_group))

        pay_label = Text("Pay", color=PAY_COLOR, font_size=48).next_to(pay_text, RIGHT, buff=1)
        payda_label = Text("Payda", color=PAYDA_COLOR, font_size=48).next_to(payda_text, RIGHT, buff=1)
        line_label = Text("Kesir Çizgisi", color=TEXT_COLOR, font_size=36).next_to(line, RIGHT, buff=1)

        self.play(Write(line_label))
        self.play(Write(pay_label), Write(payda_label))
        self.wait(20)

        # Sahne 3: Kesri Görselleştirme (Payda ve Pay açıklaması)
        self.play(FadeOut(pay_label), FadeOut(payda_label), FadeOut(line_label))
        self.play(fraction_group.animate.to_edge(LEFT, buff=2))

        circle_radius = 2
        sectors = VGroup()
        for i in range(4):
            # outer_radius kesinlikle kullanılmıyor, sadece radius
            sector = Sector(radius=circle_radius, angle=TAU/4, start_angle=i*TAU/4,
                            fill_color=PAYDA_COLOR, fill_opacity=0.1, stroke_color=TEXT_COLOR, stroke_width=4)
            sectors.add(sector)

        sectors.to_edge(RIGHT, buff=2)
        self.play(Create(sectors))
        self.wait(20) # Payda açıklaması süresi

        # Pay açıklaması (3 parçanın boyanması)
        self.play(
            sectors[0].animate.set_fill(PAY_COLOR, opacity=0.8),
            sectors[1].animate.set_fill(PAY_COLOR, opacity=0.8),
            sectors[2].animate.set_fill(PAY_COLOR, opacity=0.8)
        )
        self.wait(22)
        self.play(FadeOut(sectors))

        # Sahne 4: Kesirlerin Okunuşu
        self.play(fraction_group.animate.move_to(ORIGIN))
        self.wait(15) # Okuma yöntemlerine giriş süresi

        # Yöntem 1: Yukarıdan Aşağıya
        arrow_down = Arrow(start=UP, end=DOWN, color=TEXT_COLOR).next_to(fraction_group, LEFT, buff=1)
        read_1 = Text("Üç bölü dört", color=TEXT_COLOR, font_size=48).next_to(fraction_group, RIGHT, buff=1)

        self.play(GrowArrow(arrow_down), Write(read_1))
        self.wait(20)
        self.play(FadeOut(arrow_down), FadeOut(read_1))

        # Yöntem 2: Aşağıdan Yukarıya
        arrow_up = Arrow(start=DOWN, end=UP, color=TEXT_COLOR).next_to(fraction_group, LEFT, buff=1)
        read_2 = Text("Dörtte üç", color=TEXT_COLOR, font_size=48).next_to(fraction_group, RIGHT, buff=1)

        self.play(GrowArrow(arrow_up), Write(read_2))
        self.wait(21)
        self.play(FadeOut(arrow_up), FadeOut(read_2), FadeOut(fraction_group))

        # Sahne 5: Örnek 5/8
        pay_5 = Text("5", color=PAY_COLOR, font_size=72)
        line_8 = Line(LEFT, RIGHT, color=TEXT_COLOR, stroke_width=6).scale(1)
        payda_8 = Text("8", color=PAYDA_COLOR, font_size=72)
        frac_5_8 = VGroup(pay_5, line_8, payda_8).arrange(DOWN, buff=0.3).to_edge(LEFT, buff=2)

        self.play(FadeIn(frac_5_8))

        rects = VGroup()
        for i in range(8):
            rect = Rectangle(height=1, width=0.8, stroke_color=TEXT_COLOR, stroke_width=2, fill_color=PAYDA_COLOR, fill_opacity=0.1)
            rects.add(rect)
        rects.arrange(RIGHT, buff=0).next_to(frac_5_8, RIGHT, buff=1)

        self.play(Create(rects))

        fills = [rects[i].animate.set_fill(PAY_COLOR, opacity=0.8) for i in range(5)]
        self.play(*fills)

        text_5_8_1 = Text("Beş bölü sekiz", color=TEXT_COLOR, font_size=36).next_to(rects, DOWN, buff=1)
        text_5_8_2 = Text("Sekizde beş", color=TEXT_COLOR, font_size=36).next_to(text_5_8_1, DOWN, buff=0.5)

        self.play(Write(text_5_8_1))
        self.play(Write(text_5_8_2))
        self.wait(20)
        self.play(FadeOut(frac_5_8), FadeOut(rects), FadeOut(text_5_8_1), FadeOut(text_5_8_2))

        # Sahne 6: Kapanış ve Özet
        final_text = Text("Kesirler", color=TEXT_COLOR, font_size=64)
        pay_text_final = Text("Pay: Alınan Parça", color=PAY_COLOR, font_size=40)
        payda_text_final = Text("Payda: Toplam Eşit Parça", color=PAYDA_COLOR, font_size=40)

        final_group = VGroup(final_text, pay_text_final, payda_text_final).arrange(DOWN, buff=1)
        self.play(Write(final_group))

        # Toplam süreyi tam 181 saniyeye (543 kelime / 3) tamamlayan son bekleme
        self.wait(30)
        self.play(FadeOut(final_group))
