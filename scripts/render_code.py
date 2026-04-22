from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi: Maarif Laciverti
        self.camera.background_color = "#002B4D"

        # KANCA (HOOK) [0-5 sn]
        hook_text = Text("Payda buyudukce\nkesir buyur mu?", font_size=70, color=WHITE).scale(0.8)
        hook_text.shift(UP * 2)
        self.play(Write(hook_text), run_time=1.5)
        self.wait(1)

        wrong_cross = Cross(hook_text, stroke_color=RED, stroke_width=10)
        self.play(Create(wrong_cross), run_time=0.5)
        self.wait(1)

        self.play(FadeOut(hook_text), FadeOut(wrong_cross))

        # GOVDE (BODY) [5-50 sn]
        # 1/2 Kesri (Pasta 2'ye bolunmus)
        circle_half_bg = Circle(radius=1.5, color=WHITE, stroke_width=4).shift(UP * 2)
        slice_half = Sector(radius=1.5, angle=PI, start_angle=0, color="#FFD700", fill_opacity=0.9).shift(UP * 2)
        label_half = MathTex(r"\frac{1}{2}", font_size=90, color=WHITE).next_to(circle_half_bg, LEFT, buff=0.5)

        self.play(Create(circle_half_bg), Write(label_half), run_time=1)
        self.play(Create(slice_half), run_time=1)
        self.wait(2)

        # 1/8 Kesri (Pasta 8'e bolunmus)
        circle_eighth_bg = Circle(radius=1.5, color=WHITE, stroke_width=4).shift(DOWN * 1.5)
        slice_eighth = Sector(radius=1.5, angle=PI/4, start_angle=0, color="#FFD700", fill_opacity=0.9).shift(DOWN * 1.5)
        label_eighth = MathTex(r"\frac{1}{8}", font_size=90, color=WHITE).next_to(circle_eighth_bg, LEFT, buff=0.5)

        self.play(Create(circle_eighth_bg), Write(label_eighth), run_time=1)
        self.play(Create(slice_eighth), run_time=1)
        self.wait(2)

        # Buyuktur Isareti
        greater_sign = MathTex(">", font_size=120, color="#FFD700").move_to(UP * 0.25)
        self.play(Write(greater_sign), run_time=0.5)
        self.wait(2)

        # Alt Kural Metni (Guvenli Alan Sinirinda)
        rule_text = Text("Payda Buyurse\nDilim Kuculur!", font_size=70, color="#FFD700", weight=BOLD).scale(0.8)
        rule_bg = BackgroundRectangle(rule_text, color=BLACK, fill_opacity=0.5, buff=0.2)
        rule_group = VGroup(rule_bg, rule_text).shift(DOWN * 4)
        
        self.play(FadeIn(rule_group, shift=UP))
        self.wait(3)

        # Ekranı Temizle
        self.play(FadeOut(Group(*self.mobjects)))

        # KAPANIS (CTA) [50-60 sn]
        cta_text1 = Text("Maarif Matematik ile", font_size=65, color=WHITE).scale(0.8).shift(UP * 0.5)
        cta_text2 = Text("mantigini kavra,", font_size=65, color="#FFD700").scale(0.8).next_to(cta_text1, DOWN)
        cta_text3 = Text("takipte kal!", font_size=65, color=WHITE).scale(0.8).next_to(cta_text2, DOWN)
        
        self.play(Write(cta_text1), run_time=0.8)
        self.play(Write(cta_text2), run_time=0.8)
        self.play(Write(cta_text3), run_time=0.8)
        self.wait(2)
