from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi Maarif Laciverti
        self.camera.background_color = "#002B4D"

        # KANCA (0-5 sn)
        hook_q = Text("1 Pastayı...", font_size=70, color=WHITE).scale(0.8).shift(UP*3)
        hook_opt1 = Text("3 Kişi mi?", font_size=80, color="#FFD700").scale(0.8).next_to(hook_q, DOWN, buff=1)
        hook_opt2 = Text("100 Kişi mi?", font_size=80, color="#D32F2F").scale(0.8).next_to(hook_opt1, DOWN, buff=1)
        
        self.play(Write(hook_q), run_time=1)
        self.play(FadeIn(hook_opt1, shift=UP), run_time=1)
        self.play(FadeIn(hook_opt2, shift=UP), run_time=1)
        self.wait(2)
        self.play(FadeOut(hook_q, hook_opt1, hook_opt2))

        # GÖVDE - Tanım (5-20 sn)
        def_title = Text("BİRİM KESİR", font_size=70, color="#FFD700").scale(0.8).shift(UP*4)
        def_desc = Text("Payı 1 olan kesirdir.", font_size=50, color=WHITE).scale(0.8).next_to(def_title, DOWN, buff=0.5)
        
        frac1 = MathTex(r"\frac{1}{3}", color=WHITE).scale(3).shift(UP*0.5)
        frac2 = MathTex(r"\frac{1}{10}", color=WHITE).scale(3).next_to(frac1, DOWN, buff=1.5)
        
        self.play(Write(def_title), Write(def_desc), run_time=1.5)
        self.play(FadeIn(frac1), FadeIn(frac2), run_time=1.5)
        self.wait(3)
        self.play(FadeOut(def_title, def_desc, frac1, frac2))

        # GÖVDE - Kural ve İspat (20-45 sn)
        rule1 = Text("PAYDA BÜYÜDÜKÇE", font_size=60, color=WHITE).scale(0.8).shift(UP*3)
        rule2 = Text("(Kişi Sayısı Artar)", font_size=45, color="#FFD700").scale(0.8).next_to(rule1, DOWN, buff=0.3)
        rule3 = Text("DİLİM KÜÇÜLÜR!", font_size=75, color="#D32F2F").scale(0.8).next_to(rule2, DOWN, buff=1)
        
        self.play(Write(rule1), run_time=1)
        self.play(FadeIn(rule2), run_time=1)
        self.play(Write(rule3), run_time=1)
        self.wait(1.5)
        
        comp_group = VGroup(
            MathTex(r"\frac{1}{3}", color=WHITE).scale(3.5),
            MathTex(">", color="#FFD700").scale(3.5),
            MathTex(r"\frac{1}{10}", color=WHITE).scale(3.5)
        ).arrange(RIGHT, buff=0.8).next_to(rule3, DOWN, buff=1.5)
        
        self.play(FadeIn(comp_group, scale=0.5), run_time=1.5)
        self.wait(3)
        self.play(FadeOut(rule1, rule2, rule3, comp_group))

        # KAPANIŞ (45-55 sn)
        cta1 = Text("Artık Karıştırmak Yok!", font_size=60, color=WHITE).scale(0.8).shift(UP*1)
        cta2 = Text("Daha Fazlası İçin", font_size=50, color=WHITE).scale(0.8).next_to(cta1, DOWN, buff=0.5)
        cta3 = Text("TAKİP ET!", font_size=80, color="#FFD700").scale(0.8).next_to(cta2, DOWN, buff=0.5)
        
        self.play(Write(cta1), run_time=1)
        self.play(FadeIn(cta2, shift=UP), FadeIn(cta3, shift=UP), run_time=1)
        self.wait(2)
