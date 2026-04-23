from manim import *

config.pixel_height=1920
config.pixel_width=1080
config.frame_height=14.22
config.frame_width=8.0

class MaarifScene(Scene):
    def construct(self):
        # 1. Merhaba, Maarif Matematik’e hoş geldiniz. (1.66s)
        intro_text = Text("Maarif Matematik", font="DejaVu Sans", color=YELLOW).scale_to_fit_width(6.2)
        self.play(Write(intro_text), run_time=0.66)
        self.wait(1.0)
        self.play(FadeOut(intro_text), run_time=0.5)

        # 2. Birim kesirlerde payda büyüdükçe kesrin değeri küçülür. (2.33s)
        rule_text = Text("Payda büyüdükçe\nkesrin değeri küçülür", font="DejaVu Sans", color=WHITE, text_align="center").scale_to_fit_width(6.2)
        self.play(Write(rule_text), run_time=1.0)
        self.wait(1.33)
        self.play(FadeOut(rule_text), run_time=0.5)

        # Görsel Objelerin Hazırlanması
        circle_half = Circle(radius=2, color=WHITE)
        slice_half = Sector(radius=2, angle=PI, color=BLUE, fill_opacity=0.7)
        label_half = MathTex(r"\frac{1}{2}").scale(3)
        group_half = VGroup(VGroup(circle_half, slice_half), label_half).arrange(RIGHT, buff=1)

        circle_eighth = Circle(radius=2, color=WHITE)
        slice_eighth = Sector(radius=2, angle=PI/4, color=RED, fill_opacity=0.7)
        label_eighth = MathTex(r"\frac{1}{8}").scale(3)
        group_eighth = VGroup(VGroup(circle_eighth, slice_eighth), label_eighth).arrange(RIGHT, buff=1)

        main_group = VGroup(group_half, group_eighth).arrange(DOWN, buff=2.2).scale_to_fit_width(6.2)

        # 3. Bunu bir pasta üzerinden düşünelim. (1.66s)
        self.play(FadeIn(circle_half), FadeIn(circle_eighth), run_time=0.66)
        self.wait(1.0)

        # 4. Bir pastayı ikiye böldüğünüzde alacağınız dilim büyüktür. (2.33s)
        self.play(FadeIn(slice_half), Write(label_half), run_time=1.0)
        self.wait(1.33)

        # 5. Ancak aynı pastayı sekize bölerseniz dilimler küçülür. (2.33s)
        self.play(FadeIn(slice_eighth), Write(label_eighth), run_time=1.0)
        self.wait(1.33)

        # 6. Yani ikide bir, sekizde birden daha büyüktür. (2.33s)
        gt_sign = MathTex(">").rotate(-PI/2).scale(3).move_to(main_group.get_center())
        self.play(Write(gt_sign), Indicate(label_half, color=YELLOW, scale_factor=1.2), run_time=1.0)
        self.wait(1.33)

        # 7. Bir sonraki derste görüşmek üzere, hoşça kalın. (2.33s)
        self.play(FadeOut(main_group), FadeOut(gt_sign), run_time=0.5)
        outro_text = Text("Bir sonraki derste görüşmek üzere,\nhoşça kalın.", font="DejaVu Sans", color=YELLOW, text_align="center").scale_to_fit_width(6.2)
        self.play(Write(outro_text), run_time=0.83)
        self.wait(1.0)
        self.play(FadeOut(outro_text), run_time=0.5)

        # Kapanış Sabitleme
        self.wait(5)
