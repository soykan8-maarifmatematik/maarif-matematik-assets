from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class MaarifScene(Scene):
    def construct(self):
        # 1. GİRİŞ (5 kelime -> 1.67 saniye)
        intro_text = Text("Maarif Matematik", font_size=60, color=YELLOW, weight=BOLD).to_edge(UP, buff=1.5)
        self.play(Write(intro_text), run_time=0.5)
        self.wait(1.67)

        # 2. KANCA / SORU (9 kelime -> 3.0 saniye)
        hook_text = Text("Payda büyüdükçe\nkesir neden küçülür?", font_size=45, text_alignment="CENTER").next_to(intro_text, DOWN, buff=0.8)
        self.play(FadeIn(hook_text, shift=UP), run_time=0.5)
        self.wait(3.0)

        # 3. ÖRNEK 1: 1/2 (13 kelime -> 4.33 saniye)
        circle_half = Circle(radius=1.5, color=WHITE, stroke_width=4).shift(UP * 1.5)
        line_half = Line(circle_half.get_top(), circle_half.get_bottom(), color=WHITE, stroke_width=4)
        fill_half = AnnularSector(inner_radius=0, outer_radius=1.5, angle=PI, start_angle=PI/2, color=BLUE, fill_opacity=0.8).shift(UP * 1.5)
        label_half = MathTex(r"\frac{1}{2}", font_size=80).next_to(circle_half, LEFT, buff=0.8)
        
        self.play(Create(circle_half), Create(line_half), run_time=0.5)
        self.play(FadeIn(fill_half), Write(label_half), run_time=0.5)
        self.wait(4.33)

        # 4. ÖRNEK 2: 1/4 (10 kelime -> 3.33 saniye)
        circle_quarter = Circle(radius=1.5, color=WHITE, stroke_width=4).shift(DOWN * 2.5)
        line_q1 = Line(circle_quarter.get_top(), circle_quarter.get_bottom(), color=WHITE, stroke_width=4)
        line_q2 = Line(circle_quarter.get_left(), circle_quarter.get_right(), color=WHITE, stroke_width=4)
        fill_quarter = AnnularSector(inner_radius=0, outer_radius=1.5, angle=PI/2, start_angle=PI/2, color=RED, fill_opacity=0.8).shift(DOWN * 2.5)
        label_quarter = MathTex(r"\frac{1}{4}", font_size=80).next_to(circle_quarter, LEFT, buff=0.8)

        self.play(Create(circle_quarter), Create(line_q1), Create(line_q2), run_time=0.5)
        self.play(FadeIn(fill_quarter), Write(label_quarter), run_time=0.5)
        self.wait(3.33)

        # 5. KARŞILAŞTIRMA (10 kelime -> 3.33 saniye)
        comp_text = MathTex(r"\frac{1}{2} > \frac{1}{4}", font_size=100, color=GREEN).move_to(DOWN * 6)
        self.play(Write(comp_text), run_time=0.5)
        self.wait(3.33)

        # 6. KURAL VE MANTIK (11 kelime -> 3.67 saniye)
        self.play(
            FadeOut(hook_text), FadeOut(circle_half), FadeOut(line_half), 
            FadeOut(fill_half), FadeOut(label_half), FadeOut(circle_quarter), 
            FadeOut(line_q1), FadeOut(line_q2), FadeOut(fill_quarter), 
            FadeOut(label_quarter), comp_text.animate.shift(UP * 6).scale(1.2),
            run_time=0.5
        )
        
        rule_text = Text("Kişi artarsa,\ndilim küçülür!", font_size=70, color=ORANGE, text_alignment="CENTER", weight=BOLD).next_to(comp_text, DOWN, buff=1.5)
        self.play(Write(rule_text), run_time=0.5)
        self.wait(3.67)

        # 7. ÇIKIŞ (MÜHÜR) (7 kelime -> 2.33 saniye)
        outro_text = Text("Maarif Matematik ile\nmantığını kavra,\ntakipte kal!", font_size=55, color=YELLOW, text_alignment="CENTER").next_to(rule_text, DOWN, buff=1.5)
        self.play(Write(outro_text), run_time=0.5)
        self.wait(2.33)

        # 8. FİNAL SABİTLEME
        self.wait(4)
