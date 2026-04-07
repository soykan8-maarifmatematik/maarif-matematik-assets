from manim import *

config.background_color = WHITE
config.pixel_height = 720
config.pixel_width = 1280

class KesirlerinMantigi(Scene):
    def construct(self):
        # 1. Giriş Sahnesi
        title = Text("Kesirlerin Mantığı", color=DARK_GRAY, font_size=56)
        teacher = Text("İbrahim Soykan | Maarif Matematik", color=BLUE, font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(title))
        self.play(FadeIn(teacher))
        self.wait(17)
        self.play(FadeOut(title), FadeOut(teacher))

        # 2. Kesir Anatomisi Sahnesi
        frac = MathTex(r"3", r"\over", r"4", color=DARK_GRAY).scale(4)
        self.play(Write(frac))
        self.wait(4)

        payda_text = Text("Payda\n(Bölünen parça sayısı)", color=BLUE, font_size=28, line_spacing=1.2).next_to(frac, DOWN, buff=0.8)
        self.play(frac[2].animate.set_color(BLUE), Write(payda_text))
        self.wait(8)

        pay_text = Text("Pay\n(Alınan parça sayısı)", color=GREEN, font_size=28, line_spacing=1.2).next_to(frac, UP, buff=0.8)
        self.play(frac[0].animate.set_color(GREEN), Write(pay_text))
        self.wait(7)

        line_text = Text("Kesir Çizgisi", color=RED, font_size=28).next_to(frac, RIGHT, buff=1.5)
        arrow = Arrow(start=line_text.get_left(), end=frac[1].get_right(), color=RED, buff=0.2)
        self.play(frac[1].animate.set_color(RED), Write(line_text), GrowArrow(arrow))
        self.wait(6)

        self.play(FadeOut(frac), FadeOut(payda_text), FadeOut(pay_text), FadeOut(line_text), FadeOut(arrow))

        # 3. Yazım Kuralı Gösterimi Sahnesi
        uyari_baslik = Text("Önemli Bir Yazım Kuralı", color=RED, font_size=42).to_edge(UP, buff=1)
        self.play(Write(uyari_baslik))
        self.wait(4)

        kural1 = VGroup(
            Text("Okunuş: İkide bir", color=DARK_GRAY, font_size=32),
            MathTex(r"\rightarrow", color=DARK_GRAY),
            Text("Yazılış:", color=DARK_GRAY, font_size=32),
            MathTex(r"\frac{1}{2}", color=DARK_GRAY),
            Text("'i", color=BLUE, font_size=32)
        ).arrange(RIGHT, buff=0.25).shift(UP * 0.5)
        
        self.play(FadeIn(kural1))
        self.wait(12)

        kural2 = VGroup(
            Text("Okunuş: Bir bölü iki", color=DARK_GRAY, font_size=32),
            MathTex(r"\rightarrow", color=DARK_GRAY),
            Text("Yazılış:", color=DARK_GRAY, font_size=32),
            MathTex(r"\frac{1}{2}", color=DARK_GRAY),
            Text("'si", color=GREEN, font_size=32)
        ).arrange(RIGHT, buff=0.25).shift(DOWN * 0.5)

        self.play(FadeIn(kural2))
        self.wait(14)

        self.play(FadeOut(uyari_baslik), FadeOut(kural1), FadeOut(kural2))

        # 4. Görselleştirme (Pizza) Sahnesi
        circle = Circle(radius=2, color=DARK_GRAY, stroke_width=4)
        self.play(Create(circle))
        self.wait(5)

        h_line = Line(circle.get_left(), circle.get_right(), color=DARK_GRAY, stroke_width=4)
        v_line = Line(circle.get_top(), circle.get_bottom(), color=DARK_GRAY, stroke_width=4)
        self.play(Create(h_line), Create(v_line))
        self.wait(6)

        piece1 = Sector(outer_radius=2, angle=PI/2, start_angle=0, color=BLUE, fill_opacity=0.6, stroke_width=0)
        piece2 = Sector(outer_radius=2, angle=PI/2, start_angle=PI/2, color=BLUE, fill_opacity=0.6, stroke_width=0)
        piece3 = Sector(outer_radius=2, angle=PI/2, start_angle=PI, color=BLUE, fill_opacity=0.6, stroke_width=0)
        self.play(FadeIn(piece1), FadeIn(piece2), FadeIn(piece3))
        self.wait(12)

        self.play(FadeOut(circle), FadeOut(h_line), FadeOut(v_line), FadeOut(piece1), FadeOut(piece2), FadeOut(piece3))

        # 5. Kapanış Sahnesi
        final_text = Text("Matematik Hayattır...", color=BLUE, font_size=48)
        self.play(Write(final_text))
        self.wait(13)

        self.play(FadeOut(final_text))
        self.wait(4)
