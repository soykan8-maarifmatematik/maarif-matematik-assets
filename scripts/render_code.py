from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0

class MaarifScene(Scene):
    def construct(self):
        # 1. GİRİŞ (13 kelime -> 4.3 saniye)
        title = Text("Maarif Matematik", font="DejaVu Sans", color=YELLOW)
        title.scale_to_fit_width(7.0)
        subtitle = Text("Birim Kesirler", font="DejaVu Sans", color=WHITE)
        subtitle.scale_to_fit_width(7.0)
        
        group1 = VGroup(title, subtitle).arrange(DOWN, buff=1.2)
        self.play(Write(group1), run_time=1.0)
        self.wait(4.3)
        self.play(FadeOut(group1), run_time=0.5)

        # 2. SORU VE TANIM (21 kelime -> 7.0 saniye)
        q_text = Text("Hangisi Daha Büyük?", font="DejaVu Sans", color=BLUE)
        q_text.scale_to_fit_width(7.0)
        
        frac1 = MathTex(r"\frac{1}{2}").scale(4)
        q_mark = Text("?", font="DejaVu Sans", color=RED).scale(3)
        frac2 = MathTex(r"\frac{1}{8}").scale(4)
        
        frac_group = VGroup(frac1, q_mark, frac2).arrange(RIGHT, buff=1.5)
        group2 = VGroup(q_text, frac_group).arrange(DOWN, buff=1.2)
        
        self.play(FadeIn(group2, shift=UP), run_time=1.0)
        self.wait(7.0)
        self.play(FadeOut(group2, shift=DOWN), run_time=0.5)

        # 3. KURAL VE AÇIKLAMA (59 kelime -> 19.6 saniye)
        pizza_text = Text("Pizza Dilimleri", font="DejaVu Sans", color=ORANGE)
        pizza_text.scale_to_fit_width(7.0)
        
        rule_text1 = Text("Payda Büyüdükçe", font="DejaVu Sans", color=WHITE)
        rule_text1.scale_to_fit_width(7.0)
        
        rule_text2 = Text("Değer Küçülür", font="DejaVu Sans", color=GREEN)
        rule_text2.scale_to_fit_width(7.0)
        
        greater_sign = MathTex(">").scale(4).set_color(YELLOW)
        final_frac = VGroup(
            MathTex(r"\frac{1}{2}").scale(4),
            greater_sign,
            MathTex(r"\frac{1}{8}").scale(4)
        ).arrange(RIGHT, buff=1.0)
        
        group3 = VGroup(pizza_text, rule_text1, rule_text2, final_frac).arrange(DOWN, buff=1.2)
        
        self.play(Write(group3), run_time=1.5)
        self.wait(19.6)
        self.play(FadeOut(group3), run_time=0.5)

        # 4. ÇIKIŞ (7 kelime -> 2.3 saniye)
        outro_text = Text("Hoşça Kalın", font="DejaVu Sans", color=YELLOW)
        outro_text.scale_to_fit_width(7.0)
        
        self.play(FadeIn(outro_text, scale=1.2), run_time=1.0)
        self.wait(2.3)
        self.play(FadeOut(outro_text), run_time=0.5)
