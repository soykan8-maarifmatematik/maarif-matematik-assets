from manim import *

class MaarifScene(Scene):
    def construct(self):
        config.pixel_height = 1920
        config.pixel_width = 1080
        config.frame_height = 14.22
        config.frame_width = 8.0
        self.camera.background_color = "#002B4D"

        # Hook
        hook_text = Text("KESİRLERDE\nBÜYÜK HATA!", color="#D32F2F", font_size=72, weight=BOLD).scale(0.8)
        self.play(Write(hook_text), run_time=1.5)
        self.wait(4.1)
        self.play(FadeOut(hook_text), run_time=0.5)

        # Body 1
        wrong_math = MathTex(r"\frac{1}{10} > \frac{1}{2}", color="#FFFFFF", font_size=96).scale(0.8)
        wrong_math.to_edge(UP, buff=2)
        cross = Cross(wrong_math, stroke_color="#D32F2F", stroke_width=8)
        
        self.play(FadeIn(wrong_math), run_time=1)
        self.wait(3.0)
        self.play(Create(cross), run_time=1)
        self.wait(4.2)
        self.play(FadeOut(wrong_math), FadeOut(cross), run_time=0.5)

        # Body 2 & 3
        pizza_text = Text("PİZZA MANTIĞI", color="#FFD700", font_size=64, weight=BOLD).scale(0.8)
        pizza_text.to_edge(UP, buff=1.5)
        
        half_pizza = Sector(radius=2.5, angle=PI, color="#FFD700", fill_opacity=0.8)
        half_pizza.rotate(-PI/2)
        half_pizza.shift(UP * 1.5)
        half_label = MathTex(r"\frac{1}{2}", color="#002B4D", font_size=72).move_to(half_pizza.get_center())
        
        tenth_pizza = Sector(radius=2.5, angle=TAU/10, color="#D32F2F", fill_opacity=0.8)
        tenth_pizza.rotate(-PI/2 - TAU/20)
        tenth_pizza.shift(DOWN * 3.5)
        tenth_label = MathTex(r"\frac{1}{10}", color="#FFFFFF", font_size=72).move_to(tenth_pizza.get_center() + DOWN*0.5)

        self.play(Write(pizza_text), run_time=1)
        self.wait(5.0)
        
        self.play(Create(half_pizza), Write(half_label), run_time=1.5)
        self.wait(4.5)
        
        self.play(Create(tenth_pizza), Write(tenth_label), run_time=1.5)
        self.wait(6.5)
        
        self.play(FadeOut(half_pizza), FadeOut(half_label), FadeOut(tenth_pizza), FadeOut(tenth_label), FadeOut(pizza_text), run_time=0.5)

        # Body 4
        rule_text1 = MathTex(r"\frac{1}{2} > \frac{1}{10}", color="#FFD700", font_size=96).scale(0.8).shift(UP*2)
        rule_text2 = Text("PAYDA BÜYÜRSE", color="#FFFFFF", font_size=56).scale(0.8).next_to(rule_text1, DOWN, buff=1)
        rule_text3 = Text("DİLİM KÜÇÜLÜR!", color="#D32F2F", font_size=64, weight=BOLD).scale(0.8).next_to(rule_text2, DOWN, buff=0.5)
        
        self.play(Write(rule_text1), run_time=1)
        self.wait(2.0)
        self.play(Write(rule_text2), run_time=1)
        self.play(Write(rule_text3), run_time=1)
        self.wait(5.4)
        self.play(FadeOut(rule_text1), FadeOut(rule_text2), FadeOut(rule_text3), run_time=0.5)

        # CTA
        cta_1 = Text("MAARİF MATEMATİK", color="#FFD700", font_size=64, weight=BOLD).scale(0.8).shift(UP*0.5)
        cta_2 = Text("Mantığını Kavra!", color="#FFFFFF", font_size=56).scale(0.8).next_to(cta_1, DOWN, buff=0.5)
        
        self.play(Write(cta_1), Write(cta_2), run_time=1)
        self.wait(4.2)