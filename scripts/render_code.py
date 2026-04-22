from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi (Maarif Laciverti)
        self.camera.background_color = "#002B4D"

        # --- KANCA (HOOK) ---
        title = Text("HANGİSİ DAHA BÜYÜK?", font_size=48, color="#FFD700").to_edge(UP, buff=1.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        frac1 = MathTex(r"\frac{1}{2}", font_size=120, color=WHITE).move_to(UP*2 + LEFT*1.5)
        vs = Text("vs", font_size=48, color="#D32F2F").move_to(UP*2)
        frac2 = MathTex(r"\frac{1}{10}", font_size=120, color=WHITE).move_to(UP*2 + RIGHT*1.5)

        self.play(FadeIn(frac1, shift=UP), FadeIn(vs), FadeIn(frac2, shift=UP), run_time=1.5)
        self.wait(2.5)

        # --- GÖVDE (BODY) ---
        self.play(FadeOut(title), FadeOut(vs))
        self.play(
            frac1.animate.scale(0.6).move_to(UP*4 + LEFT*2),
            frac2.animate.scale(0.6).move_to(UP*4 + RIGHT*2),
            run_time=1
        )

        # Pasta/Çubuk Mantığı
        bar_bg_1 = Rectangle(width=6, height=1, color=WHITE)
        bar_fill_1 = Rectangle(width=3, height=1, color="#FFD700", fill_opacity=1)
        bar_fill_1.align_to(bar_bg_1, LEFT)
        bar_1 = VGroup(bar_bg_1, bar_fill_1).move_to(UP*1.5)

        bar_bg_2 = Rectangle(width=6, height=1, color=WHITE)
        bar_fill_2 = Rectangle(width=0.6, height=1, color="#D32F2F", fill_opacity=1)
        bar_fill_2.align_to(bar_bg_2, LEFT)
        bar_2 = VGroup(bar_bg_2, bar_fill_2).move_to(DOWN*1.5)

        label1 = Text("2 Parçadan 1'i", font_size=36, color=WHITE).next_to(bar_1, UP)
        label2 = Text("10 Parçadan 1'i", font_size=36, color=WHITE).next_to(bar_2, UP)

        self.play(Create(bar_bg_1), Create(bar_bg_2), run_time=1.5)
        self.play(Write(label1), Write(label2), run_time=1.5)
        self.wait(2)

        self.play(FadeIn(bar_fill_1), run_time=1)
        self.wait(2)
        self.play(FadeIn(bar_fill_2), run_time=1)
        self.wait(2.5)

        # Kural Ekranı
        self.play(
            FadeOut(bar_1), FadeOut(bar_2), 
            FadeOut(label1), FadeOut(label2), 
            FadeOut(frac1), FadeOut(frac2)
        )

        rule_title = Text("ALTIN KURAL", font_size=60, color="#FFD700").move_to(UP*2)
        rule_text1 = Text("Payda Büyüdükçe", font_size=48, color=WHITE).next_to(rule_title, DOWN, buff=1)
        rule_text2 = Text("Değer KÜÇÜLÜR!", font_size=56, color="#D32F2F").next_to(rule_text1, DOWN, buff=0.5)

        self.play(Write(rule_title), run_time=1)
        self.wait(1)
        self.play(FadeIn(rule_text1, shift=UP), run_time=1)
        self.wait(1)
        self.play(FadeIn(rule_text2, scale=1.5), run_time=1)
        self.wait(2)

        ineq = MathTex(r"\frac{1}{2} > \frac{1}{3} > \frac{1}{10}", font_size=80, color="#FFD700").next_to(rule_text2, DOWN, buff=1.5)
        self.play(Write(ineq), run_time=1.5)
        self.wait(3.5)

        # --- KAPANIŞ (CTA) ---
        self.play(FadeOut(rule_title), FadeOut(rule_text1), FadeOut(rule_text2), FadeOut(ineq))
        
        cta1 = Text("Daha fazlası için", font_size=48, color=WHITE).move_to(UP*0.5)
        cta2 = Text("TAKİPTE KAL!", font_size=64, color="#FFD700").next_to(cta1, DOWN, buff=0.5)

        self.play(Write(cta1), run_time=1)
        self.play(FadeIn(cta2, scale=1.2), run_time=1)
        self.wait(2)