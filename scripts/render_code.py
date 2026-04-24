from manim import *

class BirimKesirler(Scene):
    def construct(self):
        config.pixel_width = 1080
        config.pixel_height = 1920
        config.frame_width = 9
        config.frame_height = 16

        title = Text("Birim Kesirler", font="DejaVu Sans", font_size=45).to_edge(UP, buff=2.0)

        c1_base = Circle(radius=1.5, color=WHITE)
        c1_line = Line(c1_base.get_top(), c1_base.get_bottom(), color=WHITE)
        c1_fill = Sector(radius=1.5, angle=PI, start_angle=PI/2, color=BLUE, fill_opacity=0.7)
        c1_label = MathTex(r"\frac{1}{2}", font_size=70).next_to(c1_base, RIGHT, buff=0.8)
        c1_group = VGroup(c1_base, c1_line, c1_fill, c1_label)

        c2_base = Circle(radius=1.5, color=WHITE)
        c2_line1 = Line(c2_base.get_top(), c2_base.get_bottom(), color=WHITE)
        c2_line2 = Line(c2_base.get_left(), c2_base.get_right(), color=WHITE)
        c2_fill = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color=RED, fill_opacity=0.7)
        c2_label = MathTex(r"\frac{1}{4}", font_size=70).next_to(c2_base, RIGHT, buff=0.8)
        c2_group = VGroup(c2_base, c2_line1, c2_line2, c2_fill, c2_label)

        comp_text = MathTex(r"\frac{1}{2} > \frac{1}{4}", font_size=90, color=YELLOW)

        content = VGroup(c1_group, c2_group, comp_text).arrange(DOWN, buff=1.8)
        content.move_to(UP * 2.0, aligned_edge=UP)

        # Merhaba, Maarif Matematik'e hoş geldiniz. (5 kelime -> 1.67s)
        self.play(Write(title))
        self.wait(1.67)

        # Bugün birim kesirlerin büyüklüğünü karşılaştırıyoruz. (5 kelime -> 1.67s)
        self.wait(1.67)

        # Bir pastayı ikiye böldüğümüzde elde ettiğimiz dilim, ikide birdir. (9 kelime -> 3.0s)
        self.play(FadeIn(c1_base), Create(c1_line), FadeIn(c1_fill), Write(c1_label))
        self.wait(3.0)

        # Aynı pastayı dörde bölersek, dilimler küçülür ve dörtte bir olur. (10 kelime -> 3.33s)
        self.play(FadeIn(c2_base), Create(c2_line1), Create(c2_line2), FadeIn(c2_fill), Write(c2_label))
        self.wait(3.33)

        # Yani payda büyüdükçe, parça sayısı artar ve birim kesir küçülür. (10 kelime -> 3.33s)
        self.play(Indicate(c1_label), Indicate(c2_label))
        self.wait(3.33)

        # İkide bir, dörtte birden büyüktür. (5 kelime -> 1.67s)
        self.play(Write(comp_text))
        self.wait(1.67)

        # Outro Kilidi: Matematik anlatımı tamamen bitmeden asla gelmez
        self.wait(2.0)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        outro = Text("Maarif Matematik ile\nmantığını kavra,\ntakipte kal!", font="DejaVu Sans", font_size=50)
        self.play(Write(outro))
        self.wait(4.0)