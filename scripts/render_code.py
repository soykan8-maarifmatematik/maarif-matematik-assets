from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi (Maarif Laciverti)
        self.camera.background_color = "#002B4D"

        # 1. KANCA (HOOK)
        hook_text1 = Text("PAYDA BÜYÜDÜKÇE", font_size=56, color=WHITE).shift(UP*2)
        hook_text2 = Text("KESİR KÜÇÜLÜR MÜ?", font_size=64, color="#FFD700").next_to(hook_text1, DOWN)
        
        self.play(Write(hook_text1), run_time=1)
        self.play(FadeIn(hook_text2, shift=UP), run_time=1)
        self.wait(2)
        self.play(FadeOut(hook_text1, hook_text2), run_time=0.5)

        # 2. GÖVDE (BODY)
        def_text = Text("BİRİM KESİR: Payı 1 olan kesir", font_size=40, color=WHITE).shift(UP*6)
        self.play(FadeIn(def_text, shift=DOWN), run_time=1)
        self.wait(1.5)

        # Pizza 1 (1/2)
        pizza1 = Circle(radius=2, color=WHITE, fill_opacity=0.1).shift(UP*2.5)
        # outer_radius KULLANILMADI, sadece radius kullanıldı.
        slice1 = Sector(radius=2, angle=PI, start_angle=PI/2, color="#D32F2F", fill_opacity=0.9).shift(UP*2.5)
        frac1 = MathTex(r"\frac{1}{2}", font_size=96, color=WHITE).next_to(pizza1, LEFT, buff=0.5)
        
        self.play(Create(pizza1), run_time=1)
        self.play(Create(slice1), run_time=1)
        self.play(Write(frac1), run_time=0.5)
        self.wait(2)

        # Pizza 2 (1/8)
        pizza2 = Circle(radius=2, color=WHITE, fill_opacity=0.1).shift(DOWN*2.5)
        slice2 = Sector(radius=2, angle=TAU/8, start_angle=PI/2, color="#FFD700", fill_opacity=0.9).shift(DOWN*2.5)
        frac2 = MathTex(r"\frac{1}{8}", font_size=96, color=WHITE).next_to(pizza2, LEFT, buff=0.5)

        self.play(Create(pizza2), run_time=1)
        self.play(Create(slice2), run_time=1)
        self.play(Write(frac2), run_time=0.5)
        self.wait(2)

        # Karşılaştırma
        comp_text = MathTex(r"\frac{1}{2} > \frac{1}{8}", font_size=120, color=WHITE).move_to(ORIGIN)
        comp_text[0][3].set_color("#FFD700") # Büyüktür işareti sarı
        
        # Pizzaları hafif sağa kaydırıp ortayı açalım
        self.play(
            pizza1.animate.shift(RIGHT*1.5),
            slice1.animate.shift(RIGHT*1.5),
            pizza2.animate.shift(RIGHT*1.5),
            slice2.animate.shift(RIGHT*1.5),
            FadeOut(frac1, frac2),
            run_time=1
        )
        self.play(Write(comp_text), run_time=1)
        self.wait(2.5)

        # Kural Metni
        rule_text = Text("Payda Küçük = Dilim Büyük!", font_size=48, color="#FFD700").shift(DOWN*6)
        self.play(FadeIn(rule_text, scale=0.5), run_time=1)
        self.wait(3)

        # 3. KAPANIŞ (CTA)
        self.play(
            FadeOut(def_text, pizza1, slice1, pizza2, slice2, comp_text, rule_text),
            run_time=0.5
        )
        
        cta1 = Text("Mantığını Ezberlemeden Öğren!", font_size=40, color=WHITE).shift(UP*0.5)
        cta2 = Text("Maarif Matematik'i Takip Et!", font_size=56, color="#FFD700").next_to(cta1, DOWN)
        
        self.play(Write(cta1), run_time=1)
        self.play(FadeIn(cta2, shift=UP), run_time=1)
        self.wait(3)
