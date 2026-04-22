from manim import *

class MaarifScene(Scene):
    def construct(self):
        config.pixel_height = 1920
        config.pixel_width = 1080
        config.frame_height = 14.22
        config.frame_width = 8.0
        self.camera.background_color = "#002B4D"

        # Kanca (0-8s)
        frac1 = MathTex(r"\frac{1}{2}", font_size=144, color="#FFD700").move_to(UP*2)
        question = Text("Mİ BÜYÜK?", font_size=72, color="#FFFFFF").scale(0.8)
        frac2 = MathTex(r"\frac{1}{10}", font_size=144, color="#D32F2F").move_to(DOWN*2)
        
        self.play(Write(frac1), run_time=1)
        self.play(Write(question), run_time=1)
        self.play(Write(frac2), run_time=1)
        self.wait(5)
        
        # Kural (8-15s)
        self.play(FadeOut(frac1, question, frac2))
        rule1 = Text("PAYDA BÜYÜRSE", font_size=72, color="#FFD700", weight=BOLD).move_to(UP).scale(0.8)
        rule2 = Text("DEĞER KÜÇÜLÜR!", font_size=72, color="#D32F2F", weight=BOLD).move_to(DOWN).scale(0.8)
        
        self.play(FadeIn(rule1, shift=UP), run_time=1)
        self.play(FadeIn(rule2, shift=UP), run_time=1)
        self.wait(5)
        
        # Pizzalar (15-28s)
        self.play(FadeOut(rule1, rule2))
        
        pizza1_group = VGroup()
        circle1 = Circle(radius=2, color="#FFFFFF")
        line1 = Line(circle1.get_top(), circle1.get_bottom(), color="#FFFFFF")
        pizza1_group.add(circle1, line1).move_to(UP*3)
        
        pizza2_group = VGroup()
        circle2 = Circle(radius=2, color="#FFFFFF")
        lines2 = VGroup(*[Line(circle2.get_center(), circle2.point_at_angle(i * TAU / 10), color="#FFFFFF") for i in range(10)])
        pizza2_group.add(circle2, lines2).move_to(DOWN*3)
        
        self.play(Create(pizza1_group), run_time=1.5)
        self.play(Create(pizza2_group), run_time=1.5)
        self.wait(9.5)
        
        # Dilimler (28-40s)
        sector1 = Sector(arc_center=circle1.get_center(), radius=2, angle=PI, start_angle=PI/2, color="#FFD700", fill_opacity=0.8)
        sector2 = Sector(arc_center=circle2.get_center(), radius=2, angle=TAU/10, start_angle=PI/2, color="#D32F2F", fill_opacity=0.8)
        
        pizza1_full = VGroup(pizza1_group, sector1)
        pizza2_full = VGroup(pizza2_group, sector2)
        
        self.play(FadeIn(sector1), run_time=1)
        self.play(FadeIn(sector2), run_time=1)
        self.wait(9.5)
        
        # Sonuc (40-49s)
        conclusion = MathTex(r"\frac{1}{2} > \frac{1}{10}", font_size=120, color="#FFFFFF").move_to(ORIGIN)
        
        self.play(
            pizza1_full.animate.scale(0.6).move_to(UP*4 + LEFT*2),
            pizza2_full.animate.scale(0.6).move_to(UP*4 + RIGHT*2),
        )
        self.play(Write(conclusion), run_time=1)
        self.wait(8.5)
        
        # CTA (49-55s)
        self.play(FadeOut(pizza1_full, pizza2_full, conclusion))
        cta1 = Text("MAARİF MATEMATİK", font_size=80, color="#FFD700", weight=BOLD).move_to(UP).scale(0.8)
        cta2 = Text("Mantığını Kavra!", font_size=60, color="#FFFFFF").move_to(DOWN).scale(0.8)
        
        self.play(Write(cta1), run_time=1)
        self.play(Write(cta2), run_time=1)
        self.wait(4.5)