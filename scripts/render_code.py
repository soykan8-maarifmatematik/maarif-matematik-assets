from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 8.0
config.frame_height = 14.22

class UnitFractions(Scene):
    def construct(self):
        # HOOK (12 words -> 4.8s)
        q1 = Text("1/2 mi daha büyük?").scale(0.8).move_to(UP*1.5)
        q2 = Text("Yoksa 1/10 mu?").scale(0.8).move_to(DOWN*0.5)
        self.play(Write(q1))
        self.wait(2.0)
        self.play(Write(q2))
        self.wait(2.8)
        self.play(FadeOut(q1), FadeOut(q2))

        # BODY 1 (12 words -> 4.8s)
        pizza1_base = Circle(radius=1.8, color=ORANGE, fill_opacity=0.2).scale(0.8).move_to(UP*2 + LEFT*1.5)
        pizza2_base = Circle(radius=1.8, color=ORANGE, fill_opacity=0.2).scale(0.8).move_to(DOWN*2 + LEFT*1.5)
        self.play(Create(pizza1_base), Create(pizza2_base))
        self.wait(4.8)

        # BODY 2 (12 words -> 4.8s)
        pizza1_line = Line(pizza1_base.get_top(), pizza1_base.get_bottom(), color=WHITE).scale(0.8)
        pizza1_slice = Sector(radius=1.8, angle=PI, start_angle=-PI/2, color=ORANGE, fill_opacity=0.8).scale(0.8).move_to(UP*2 + LEFT*1.5)
        label1 = Text("1/2").scale(0.8).next_to(pizza1_base, RIGHT, buff=1)
        self.play(Create(pizza1_line), FadeIn(pizza1_slice), Write(label1))
        self.wait(4.8)

        # BODY 3 (16 words -> 6.4s)
        lines2 = VGroup(*[Line(pizza2_base.get_center(), pizza2_base.get_center() + 1.8 * 0.8 * np.array([np.cos(i*TAU/10), np.sin(i*TAU/10), 0]), color=WHITE) for i in range(10)])
        pizza2_slice = Sector(radius=1.8, angle=TAU/10, start_angle=0, color=ORANGE, fill_opacity=0.8).scale(0.8).move_to(DOWN*2 + LEFT*1.5)
        label2 = Text("1/10").scale(0.8).next_to(pizza2_base, RIGHT, buff=1)
        self.play(Create(lines2), FadeIn(pizza2_slice), Write(label2))
        self.wait(6.4)

        # BODY 4 (10 words -> 4.0s)
        self.play(Indicate(pizza1_slice, color=YELLOW, scale_factor=1.1))
        self.wait(4.0)

        # BODY 5 (13 words -> 5.2s)
        rule_text1 = Text("Payda büyüdükçe").scale(0.7).move_to(DOWN*3.2)
        rule_text2 = Text("dilim küçülür!").scale(0.7).move_to(DOWN*3.8)
        self.play(Write(rule_text1), Write(rule_text2))
        self.wait(5.2)

        self.play(
            FadeOut(pizza1_base), FadeOut(pizza1_line), FadeOut(pizza1_slice), FadeOut(label1),
            FadeOut(pizza2_base), FadeOut(lines2), FadeOut(pizza2_slice), FadeOut(label2),
            FadeOut(rule_text1), FadeOut(rule_text2)
        )

        # CTA (14 words -> 5.6s)
        cta1 = Text("Birim kesirlerde payda büyüdükçe").scale(0.7).move_to(UP*1.5)
        cta2 = Text("değerin küçüldüğünü unutma.").scale(0.7).move_to(UP*0.5)
        cta3 = Text("Maarif Matematik ile mantığını kavra,").scale(0.7).move_to(DOWN*1.0)
        cta4 = Text("takipte kal!", color=YELLOW).scale(0.7).move_to(DOWN*2.0)
        
        self.play(Write(cta1), Write(cta2))
        self.wait(2.0)
        self.play(Write(cta3), Write(cta4))
        self.wait(3.6)