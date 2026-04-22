from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi (Maarif Laciverti)
        self.camera.background_color = "#002B4D"

        # KANCA (HOOK)
        hook1 = Text("Paydası büyük olan", font_size=48, color=WHITE)
        hook2 = Text("daha mı büyüktür?", font_size=48, color=WHITE)
        hook_group = VGroup(hook1, hook2).arrange(DOWN)
        
        hook3 = Text("SAKIN TUZAĞA DÜŞME!", font_size=56, color="#D32F2F", weight=BOLD)
        
        self.play(Write(hook_group))
        self.wait(2)
        self.play(ReplacementTransform(hook_group, hook3))
        self.wait(2)
        self.play(FadeOut(hook3))

        # GÖVDE (BODY)
        title = Text("BİRİM KESİRLER", font_size=64, color="#FFD700", weight=BOLD).to_edge(UP, buff=1)
        self.play(FadeIn(title))
        self.wait(1)

        # 1/2 Kesri ve Pastası
        frac1 = MathTex(r"\frac{1}{2}", font_size=96, color=WHITE)
        pie1_base = Circle(radius=1.5, color=WHITE)
        pie1_slice = Sector(outer_radius=1.5, angle=PI, color="#FFD700", fill_opacity=0.8).rotate(PI/2)
        pie1_line = Line(pie1_base.get_top(), pie1_base.get_bottom(), color=WHITE)
        pie1 = VGroup(pie1_base, pie1_slice, pie1_line)
        group1 = VGroup(frac1, pie1).arrange(RIGHT, buff=1)

        # 1/4 Kesri ve Pastası
        frac2 = MathTex(r"\frac{1}{4}", font_size=96, color=WHITE)
        pie2_base = Circle(radius=1.5, color=WHITE)
        pie2_slice = Sector(outer_radius=1.5, angle=PI/2, color="#D32F2F", fill_opacity=0.8).rotate(PI/2)
        pie2_lines = VGroup(
            Line(pie2_base.get_top(), pie2_base.get_bottom(), color=WHITE),
            Line(pie2_base.get_left(), pie2_base.get_right(), color=WHITE)
        )
        pie2 = VGroup(pie2_base, pie2_slice, pie2_lines)
        group2 = VGroup(frac2, pie2).arrange(RIGHT, buff=1)

        # Grupları dikey hizalama
        pies = VGroup(group1, group2).arrange(DOWN, buff=1.5).move_to(CENTER).shift(UP*0.5)

        self.play(Write(frac1), Write(frac2))
        self.wait(3)
        
        self.play(FadeIn(pie1_base), FadeIn(pie1_line), FadeIn(pie2_base), FadeIn(pie2_lines))
        self.wait(3)
        
        self.play(FadeIn(pie1_slice), FadeIn(pie2_slice))
        self.wait(3)

        # Büyük dilimi vurgulama
        self.play(Indicate(pie1_slice, color="#FFD700", scale_factor=1.1))
        self.wait(3)

        # Kural Metni
        rule = Text("Payda KÜÇÜKSE, Kesir BÜYÜKTÜR!", font_size=40, color="#FFD700", weight=BOLD).to_edge(DOWN, buff=1.5)
        self.play(Write(rule))
        self.wait(4)

        # Final Karşılaştırması
        self.play(FadeOut(frac1), FadeOut(frac2), FadeOut(pie1), FadeOut(pie2), FadeOut(rule), FadeOut(title))
        
        final_comp = MathTex(r"\frac{1}{2}", ">", r"\frac{1}{4}", font_size=144, color=WHITE)
        final_comp[1].set_color("#FFD700")
        self.play(Write(final_comp))
        self.wait(4)
        
        self.play(FadeOut(final_comp))

        # KAPANIŞ (CTA)
        cta1 = Text("Daha fazlası için", font_size=48, color=WHITE)
        cta2 = Text("TAKİPTE KALIN!", font_size=56, color="#FFD700", weight=BOLD)
        cta_group = VGroup(cta1, cta2).arrange(DOWN)
        self.play(Write(cta_group))
        self.wait(3)
