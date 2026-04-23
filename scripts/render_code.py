from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class BirimKesirler(Scene):
    def construct(self):
        # KANCA
        hook_text = Text("Hangisi Daha Büyük?", font="sans-serif", font_size=60, color=YELLOW)
        self.play(Write(hook_text))
        self.wait(4.8)
        self.play(FadeOut(hook_text))

        # GÖVDE
        body_text1 = Text("Birim Kesirler", font="sans-serif", font_size=50, color=BLUE).shift(UP*5)
        self.play(Write(body_text1))
        self.wait(2.0)
        
        body_text2 = Text("Payı 1 olan kesirler", font="sans-serif", font_size=40).next_to(body_text1, DOWN)
        self.play(Write(body_text2))
        self.wait(2.8)

        circle_half = Circle(radius=1.8, color=WHITE).shift(UP*1.5)
        circle_tenth = Circle(radius=1.8, color=WHITE).shift(DOWN*2.5)
        
        label_half = MathTex("\\frac{1}{2}", font_size=96).next_to(circle_half, LEFT, buff=0.5)
        label_tenth = MathTex("\\frac{1}{10}", font_size=96).next_to(circle_tenth, LEFT, buff=0.5)

        self.play(Create(circle_half), Create(circle_tenth), Write(label_half), Write(label_tenth))
        self.wait(4.0)

        sector_half = Sector(radius=1.8, angle=PI, color=YELLOW, arc_center=circle_half.get_center())
        self.play(Create(sector_half))
        self.wait(4.8)

        sector_tenth = Sector(radius=1.8, angle=TAU/10, color=RED, arc_center=circle_tenth.get_center())
        self.play(Create(sector_tenth))
        self.wait(3.6)
        
        self.wait(1.2)

        rule_text = Text("Payda Büyüdükçe Dilim Küçülür", font="sans-serif", font_size=45, color=GREEN).shift(DOWN*5.5)
        self.play(Write(rule_text))
        self.wait(2.0)
        
        comp_text = MathTex("\\frac{1}{2} > \\frac{1}{10}", font_size=72, color=YELLOW).next_to(rule_text, UP)
        self.play(Write(comp_text))
        self.wait(3.6)
        
        self.wait(3.6)

        self.play(
            FadeOut(circle_half), FadeOut(circle_tenth), 
            FadeOut(sector_half), FadeOut(sector_tenth),
            FadeOut(label_half), FadeOut(label_tenth),
            FadeOut(body_text1), FadeOut(body_text2),
            FadeOut(rule_text), FadeOut(comp_text)
        )

        # KAPANIŞ
        closing_text1 = Text("Sen Maarif Matematik", font="sans-serif", font_size=60, color=YELLOW)
        closing_text2 = Text("Abone Ol", font="sans-serif", font_size=50, color=WHITE).next_to(closing_text1, DOWN)
        self.play(Write(closing_text1), Write(closing_text2))
        self.wait(3.2)
