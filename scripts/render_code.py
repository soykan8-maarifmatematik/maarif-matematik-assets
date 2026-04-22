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
        title = Text("HANGİSİ DAHA BÜYÜK?", font_size=60, color="#FFD700", weight=BOLD).to_edge(UP, buff=2)
        frac1 = MathTex(r"\frac{1}{2}", font_size=150, color=WHITE)
        vs = Text("vs", font_size=80, color="#D32F2F")
        frac2 = MathTex(r"\frac{1}{10}", font_size=150, color=WHITE)
        
        hook_group = VGroup(frac1, vs, frac2).arrange(RIGHT, buff=1).next_to(title, DOWN, buff=2)
        
        self.play(Write(title), run_time=1)
        self.play(FadeIn(hook_group, shift=UP), run_time=1)
        self.wait(3)
        self.play(FadeOut(title), FadeOut(hook_group), run_time=1)

        # --- GÖVDE (BODY) - Görselleştirme ---
        # 1/2 Görseli
        c1 = Circle(radius=2, color=WHITE)
        s1 = Sector(outer_radius=2, angle=PI, start_angle=PI/2, color="#FFD700", fill_opacity=0.9)
        l1 = Line(c1.get_top(), c1.get_bottom(), color=WHITE, stroke_width=4)
        t1 = MathTex(r"\frac{1}{2}", font_size=90, color="#FFD700").next_to(c1, UP, buff=0.5)
        g1 = VGroup(t1, c1, s1, l1).move_to(UP * 3)

        # 1/4 Görseli
        c2 = Circle(radius=2, color=WHITE)
        s2 = Sector(outer_radius=2, angle=PI/2, start_angle=PI/2, color="#D32F2F", fill_opacity=0.9)
        l2_1 = Line(c2.get_top(), c2.get_bottom(), color=WHITE, stroke_width=4)
        l2_2 = Line(c2.get_left(), c2.get_right(), color=WHITE, stroke_width=4)
        t2 = MathTex(r"\frac{1}{4}", font_size=90, color="#D32F2F").next_to(c2, UP, buff=0.5)
        g2 = VGroup(t2, c2, s2, l2_1, l2_2).move_to(DOWN * 3)

        self.play(Create(c1), Create(c2), run_time=1.5)
        self.wait(1)
        self.play(Create(l1), Create(l2_1), Create(l2_2), run_time=1.5)
        self.wait(1)
        self.play(FadeIn(s1), Write(t1), run_time=1)
        self.play(FadeIn(s2), Write(t2), run_time=1)
        self.wait(5)
        self.play(FadeOut(g1), FadeOut(g2), run_time=1)

        # --- GÖVDE (BODY) - Kural ---
        rule1 = Text("PAYDA BÜYÜDÜKÇE", font_size=70, color=WHITE, weight=BOLD)
        rule2 = Text("DİLİM KÜÇÜLÜR!", font_size=85, color="#D32F2F", weight=BOLD)
        rule_group = VGroup(rule1, rule2).arrange(DOWN, buff=0.8).move_to(UP * 2)

        ineq = MathTex(r"\frac{1}{2} > \frac{1}{4} > \frac{1}{10}", font_size=120, color="#FFD700").next_to(rule_group, DOWN, buff=2)

        self.play(Write(rule1), run_time=1)
        self.play(Write(rule2), run_time=1)
        self.wait(2)
        self.play(FadeIn(ineq, shift=UP), run_time=1.5)
        self.wait(6)
        self.play(FadeOut(rule_group), FadeOut(ineq), run_time=1)

        # --- KAPANIŞ (CTA) ---
        logo = Text("Maarif Matematik", font_size=80, color=WHITE, weight=BOLD)
        cta = Text("Daha fazlası için takip et!", font_size=55, color="#FFD700")
        cta_group = VGroup(logo, cta).arrange(DOWN, buff=0.8).move_to(CENTER)

        self.play(FadeIn(cta_group, scale=0.8), run_time=1.5)
        self.wait(4)
