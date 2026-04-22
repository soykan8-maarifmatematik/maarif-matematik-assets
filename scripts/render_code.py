from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#002B4D"

        # KANCA (Hook)
        title = Text("BİRİM KESİRLER", font_size=72, color="#FFD700", weight=BOLD).to_edge(UP, buff=1.5)
        self.play(Write(title), run_time=1)
        
        q_text = Text("Hangisi daha büyük?", font_size=56, color="#FFFFFF").next_to(title, DOWN, buff=1)
        self.play(Write(q_text), run_time=1)

        frac_half = MathTex(r"\frac{1}{2}", font_size=144, color="#FFFFFF").move_to(LEFT * 2 + UP * 1.5)
        frac_ten = MathTex(r"\frac{1}{10}", font_size=144, color="#FFFFFF").move_to(RIGHT * 2 + UP * 1.5)
        vs = Text("vs", font_size=48, color="#D32F2F").move_to(UP * 1.5)

        self.play(FadeIn(frac_half, shift=RIGHT), FadeIn(frac_ten, shift=LEFT), Write(vs), run_time=1)
        self.wait(3)

        # GÖVDE (Body)
        slice_half = Sector(outer_radius=2.5, angle=PI, color="#D32F2F", fill_opacity=0.9).next_to(frac_half, DOWN, buff=1.5)
        self.play(Create(slice_half), run_time=1)
        self.wait(3)

        slice_ten = Sector(outer_radius=2.5, angle=TAU/10, color="#FFD700", fill_opacity=0.9).next_to(frac_ten, DOWN, buff=1.5)
        self.play(Create(slice_ten), run_time=1)
        self.wait(3)

        greater_sign = MathTex(">", font_size=144, color="#FFD700").move_to(vs.get_center())
        self.play(Transform(vs, greater_sign), Indicate(slice_half, color="#FFD700", scale_factor=1.1), run_time=1)
        self.wait(3)

        self.play(FadeOut(slice_half), FadeOut(slice_ten), FadeOut(q_text), FadeOut(frac_half), FadeOut(frac_ten), FadeOut(vs), run_time=1)

        rule_box = Rectangle(width=7, height=3, color="#FFD700", fill_color="#002B4D", fill_opacity=1)
        rule_text1 = Text("Payda BÜYÜDÜKÇE", font_size=56, color="#FFFFFF").move_to(rule_box.get_center() + UP*0.5)
        rule_text2 = Text("Kesir KÜÇÜLÜR!", font_size=64, color="#D32F2F", weight=BOLD).move_to(rule_box.get_center() + DOWN*0.5)
        
        rule_group = VGroup(rule_box, rule_text1, rule_text2).move_to(CENTER)

        self.play(Create(rule_box), Write(rule_text1), run_time=1)
        self.play(Write(rule_text2), run_time=1)
        self.wait(4)

        # KAPANIŞ (CTA)
        cta = Text("Daha fazlası için takip et!", font_size=48, color="#FFD700").to_edge(DOWN, buff=2)
        self.play(Write(cta), run_time=1)
        self.wait(3)
