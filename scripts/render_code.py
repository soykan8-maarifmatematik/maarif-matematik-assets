from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class BirimKesirler(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # Title
        title = Text("BİRİM KESİRLER", color=BLACK, weight=BOLD, font_size=72)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(10 / 3.0)
        
        # Bottom Text 1
        bottom_text = Text("Payı 1 olan kesirlerdir", color=BLUE, weight=BOLD, font_size=48)
        bottom_text.to_edge(DOWN, buff=2.0)
        self.play(FadeIn(bottom_text))
        self.wait(6 / 3.0)
        
        self.wait(6 / 3.0)
        
        # Pizza 1 (1/2)
        circle1 = Circle(radius=2.5, color=BLACK, stroke_width=4)
        line1 = Line(circle1.get_top(), circle1.get_bottom(), color=BLACK)
        sector1 = Sector(radius=2.5, angle=PI, start_angle=PI/2, color=ORANGE, fill_opacity=0.8)
        frac1 = MathTex(r"\frac{1}{2}", color=BLACK, font_size=96).next_to(circle1, RIGHT, buff=1.0)
        
        group1 = VGroup(circle1, line1, sector1).move_to(ORIGIN)
        
        self.play(Create(circle1), Create(line1))
        self.play(FadeIn(sector1))
        self.play(Write(frac1))
        self.wait(10 / 3.0)
        
        # Pizza 2 (1/4)
        circle2 = Circle(radius=2.5, color=BLACK, stroke_width=4)
        lines2 = VGroup(
            Line(circle2.get_top(), circle2.get_bottom(), color=BLACK),
            Line(circle2.get_left(), circle2.get_right(), color=BLACK)
        )
        sector2 = Sector(radius=2.5, angle=PI/2, start_angle=PI/2, color=RED, fill_opacity=0.8)
        frac2 = MathTex(r"\frac{1}{4}", color=BLACK, font_size=96).next_to(circle2, RIGHT, buff=1.0)
        
        group2 = VGroup(circle2, lines2, sector2).move_to(ORIGIN)
        
        self.play(ReplacementTransform(group1, group2), ReplacementTransform(frac1, frac2))
        self.wait(10 / 3.0)
        
        # Pizza 3 (1/8)
        circle3 = Circle(radius=2.5, color=BLACK, stroke_width=4)
        lines3 = VGroup(
            Line(circle3.get_top(), circle3.get_bottom(), color=BLACK),
            Line(circle3.get_left(), circle3.get_right(), color=BLACK),
            Line(circle3.point_at_angle(PI/4), circle3.point_at_angle(5*PI/4), color=BLACK),
            Line(circle3.point_at_angle(3*PI/4), circle3.point_at_angle(7*PI/4), color=BLACK)
        )
        sector3 = Sector(radius=2.5, angle=PI/4, start_angle=PI/2, color=PURPLE, fill_opacity=0.8)
        frac3 = MathTex(r"\frac{1}{8}", color=BLACK, font_size=96).next_to(circle3, RIGHT, buff=1.0)
        
        group3 = VGroup(circle3, lines3, sector3).move_to(ORIGIN)
        
        self.play(ReplacementTransform(group2, group3), ReplacementTransform(frac2, frac3))
        self.wait(11 / 3.0)
        
        # Conclusion
        bottom_text_2 = Text("Payda BÜYÜDÜKÇE kesir KÜÇÜLÜR!", color=RED, weight=BOLD, font_size=48)
        bottom_text_2.to_edge(DOWN, buff=2.0)
        
        self.play(ReplacementTransform(bottom_text, bottom_text_2))
        self.wait(6 / 3.0)
        
        # Final inequality
        final_ineq = MathTex(r"\frac{1}{2} > \frac{1}{4} > \frac{1}{8}", color=BLACK, font_size=96)
        final_ineq.move_to(ORIGIN)
        
        self.play(FadeOut(group3), FadeOut(frac3))
        self.play(Write(final_ineq))
        self.wait(10 / 3.0)
        
        # Outro
        outro = Text("Maarif Matematik", color=BLUE, weight=BOLD, font_size=60).next_to(final_ineq, UP, buff=1.5)
        self.play(FadeIn(outro))
        self.wait(6 / 3.0)