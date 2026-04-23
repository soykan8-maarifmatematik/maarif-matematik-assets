from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class UnitFractions(Scene):
    def construct(self):
        # 1. GİRİŞ
        text1 = Text("Merhaba, Maarif Matematik'e hoş geldiniz.", font="Arial", text_align="center")
        if text1.width > 6.5:
            text1.scale_to_fit_width(6.5)
        text1.move_to(UP * 5)
        self.play(Write(text1))
        self.wait(2.0) # 5 kelime / 2.5
        self.play(FadeOut(text1))

        # 2. KURAL
        text2 = Text("Birim kesirlerde payda büyüdükçe\nkesrin değeri küçülür.", font="Arial", text_align="center")
        if text2.width > 6.5:
            text2.scale_to_fit_width(6.5)
        text2.move_to(UP * 5)
        self.play(Write(text2))
        self.wait(2.8) # 7 kelime / 2.5

        # 3. PİZZA ÖRNEĞİ GİRİŞ
        text3 = Text("Bunu bir pizza ile düşünelim.", font="Arial", text_align="center")
        if text3.width > 6.5:
            text3.scale_to_fit_width(6.5)
        text3.move_to(DOWN * 4.5)
        self.play(Write(text3))
        self.wait(2.0) # 5 kelime / 2.5
        self.play(FadeOut(text3))

        # PİZZA 1 (1/2)
        circle1 = Circle(radius=1.5, color=WHITE).move_to(UP * 1.5 + LEFT * 1.5)
        sector1 = Sector(outer_radius=1.5, angle=PI, arc_center=circle1.get_center(), color=YELLOW, fill_opacity=0.7)
        sector1.rotate(PI/2, about_point=circle1.get_center())
        line1 = Line(circle1.get_top(), circle1.get_bottom())
        frac1 = MathTex(r"\frac{1}{2}")
        if frac1.width > 6.5:
            frac1.scale_to_fit_width(6.5)
        frac1.next_to(circle1, RIGHT, buff=0.8)

        # 4. İKİYE BÖLME
        text4 = Text("İkiye böldüğümüzde yarım pizza elde ederiz.", font="Arial", text_align="center")
        if text4.width > 6.5:
            text4.scale_to_fit_width(6.5)
        text4.move_to(DOWN * 4.5)
        self.play(Write(text4), Create(circle1), Create(line1), FadeIn(sector1), Write(frac1))
        self.wait(2.4) # 6 kelime / 2.5
        self.play(FadeOut(text4))

        # PİZZA 2 (1/8)
        circle2 = Circle(radius=1.5, color=WHITE).move_to(DOWN * 2.0 + LEFT * 1.5)
        sector2 = Sector(outer_radius=1.5, angle=TAU/8, arc_center=circle2.get_center(), color=ORANGE, fill_opacity=0.7)
        sector2.rotate(PI/2, about_point=circle2.get_center())
        lines2 = VGroup(*[Line(circle2.get_center(), circle2.get_center() + np.array([1.5*np.cos(i*TAU/8), 1.5*np.sin(i*TAU/8), 0])) for i in range(8)])
        lines2.rotate(PI/2, about_point=circle2.get_center())
        frac2 = MathTex(r"\frac{1}{8}")
        if frac2.width > 6.5:
            frac2.scale_to_fit_width(6.5)
        frac2.next_to(circle2, RIGHT, buff=0.8)

        # 5. SEKİZE BÖLME
        text5 = Text("Sekize böldüğümüzde ise\nçok daha küçük bir dilim düşer.", font="Arial", text_align="center")
        if text5.width > 6.5:
            text5.scale_to_fit_width(6.5)
        text5.move_to(DOWN * 4.5)
        self.play(Write(text5), Create(circle2), Create(lines2), FadeIn(sector2), Write(frac2))
        self.wait(3.6) # 9 kelime / 2.5
        self.play(FadeOut(text5))

        # 6. SONUÇ
        text6 = Text("Yani payda arttıkça dilim küçülür.", font="Arial", text_align="center")
        if text6.width > 6.5:
            text6.scale_to_fit_width(6.5)
        text6.move_to(DOWN * 4.5)
        self.play(Write(text6))
        self.wait(2.0) # 5 kelime / 2.5
        self.play(
            FadeOut(text6), FadeOut(text2),
            FadeOut(circle1), FadeOut(sector1), FadeOut(line1), FadeOut(frac1),
            FadeOut(circle2), FadeOut(lines2), FadeOut(sector2), FadeOut(frac2)
        )

        # 7. ÇIKIŞ
        text7 = Text("Bir sonraki derste görüşmek üzere, hoşça kalın.", font="Arial", text_align="center")
        if text7.width > 6.5:
            text7.scale_to_fit_width(6.5)
        text7.move_to(UP * 5)
        self.play(Write(text7))
        self.wait(2.8) # 7 kelime / 2.5
        self.play(FadeOut(text7))
