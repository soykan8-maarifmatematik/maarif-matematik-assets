from manim import *

class MaarifScene(Scene):
    def construct(self):
        config.pixel_height = 1920
        config.pixel_width = 1080
        config.frame_height = 14.22
        config.frame_width = 8.0
        self.camera.background_color = "#002B4D"

        # KANCA: 16 kelime = 6.4 saniye
        hook_text = MarkupText("Payda büyüdükçe<br>kesir <span fgcolor='#D32F2F'>BÜYÜR MÜ?</span>", justify=True).scale(1.2)
        self.play(Write(hook_text), run_time=1)
        self.wait(4.9)
        self.play(FadeOut(hook_text), run_time=0.5)

        # GÖVDE 1 (Tanım): 22 kelime = 8.8 saniye
        def_text = Text("Birim Kesir: Payı 1 olan kesir", color=WHITE).scale(0.7).to_edge(UP, buff=1)
        self.play(Write(def_text), run_time=1)
        self.wait(7.8)

        # GÖVDE 2 (1/2 Kesri): 15 kelime = 6.0 saniye
        pizza1 = Circle(radius=1.8, color=WHITE).shift(UP*2.5)
        line1 = Line(pizza1.get_left(), pizza1.get_right(), color=WHITE)
        slice1 = Sector(radius=1.8, angle=PI, start_angle=0, color="#FFD700", fill_opacity=0.8).shift(UP*2.5)
        label1 = MathTex(r"\frac{1}{2}", color=WHITE).scale(1.5).next_to(pizza1, LEFT, buff=0.5)
        
        self.play(Create(pizza1), Create(line1), run_time=0.5)
        self.play(FadeIn(slice1), Write(label1), run_time=1)
        self.wait(4.5)

        # GÖVDE 3 (1/8 Kesri): 16 kelime = 6.4 saniye
        pizza2 = Circle(radius=1.8, color=WHITE).shift(DOWN*2)
        lines2 = VGroup(*[Line(pizza2.get_center(), pizza2.get_boundary_point(angle), color=WHITE) for angle in [0, PI/4, PI/2, 3*PI/4, PI, 5*PI/4, 3*PI/2, 7*PI/4]])
        slice2 = Sector(radius=1.8, angle=PI/4, start_angle=0, color="#D32F2F", fill_opacity=0.8).shift(DOWN*2)
        label2 = MathTex(r"\frac{1}{8}", color=WHITE).scale(1.5).next_to(pizza2, LEFT, buff=0.5)

        self.play(Create(pizza2), Create(lines2), run_time=0.5)
        self.play(FadeIn(slice2), Write(label2), run_time=1)
        self.wait(4.9)

        # GÖVDE 4 (Kıyaslama ve Kural): 35 kelime = 14.0 saniye
        comp_text = MathTex(r"\frac{1}{2} > \frac{1}{8}", color="#FFD700").scale(1.8).move_to(ORIGIN)
        rule_text = Text("Payda Büyürse, Değer Küçülür!", color="#FFD700").scale(0.8).shift(DOWN*5.5)

        self.play(Write(comp_text), run_time=1)
        self.play(Write(rule_text), run_time=1)
        self.wait(12.0)

        # KAPANIŞ: 18 kelime = 7.2 saniye
        self.play(FadeOut(Group(def_text, pizza1, line1, slice1, label1, pizza2, lines2, slice2, label2, comp_text, rule_text)), run_time=0.5)
        cta_text = Text("Mantığını Kavra!\nMaarif Matematik'i Takip Et!", color=WHITE, t2c={"Maarif Matematik'i": "#FFD700"}, line_spacing=1.5).scale(0.8).move_to(ORIGIN)
        self.play(Write(cta_text), run_time=1)
        self.wait(5.7)