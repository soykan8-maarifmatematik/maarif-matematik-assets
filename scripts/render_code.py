from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class BirimKesirler(Scene):
    def construct(self):
        def create_caption(text_str):
            cap = Text(text_str, font_size=85, weight=BOLD)
            cap.scale_to_fit_width(7)
            cap.move_to(UP * 4)
            return cap

        # Sahne 1: Kanca
        cap1 = create_caption("1/2 mi daha buyuk yoksa 1/8 mi?")
        frac1 = MathTex(r"\frac{1}{2}", font_size=100).scale(0.8).move_to(LEFT * 1.5)
        frac2 = MathTex(r"\frac{1}{8}", font_size=100).scale(0.8).move_to(RIGHT * 1.5)
        qm = Text("?", font_size=100).move_to(ORIGIN)
        
        self.play(Write(cap1), Write(frac1), Write(frac2), Write(qm))
        self.wait(3)

        # Sahne 2: Pizza 1/2
        self.play(FadeOut(cap1), FadeOut(frac1), FadeOut(frac2), FadeOut(qm))
        
        cap2 = create_caption("Bir pizza dusun 2 kisiye bolersen dev bir dilim yersin")
        circle1 = Circle(radius=1.6, color=WHITE).move_to(ORIGIN)
        sector1 = Sector(radius=1.6, angle=PI, color=ORANGE, fill_opacity=0.8)
        sector1.move_to(circle1.get_center())
        lbl1 = MathTex(r"\frac{1}{2}", font_size=100).scale(0.8).next_to(circle1, DOWN, buff=0.5)
        
        self.play(Write(cap2), Create(circle1), FadeIn(sector1), Write(lbl1))
        self.wait(4)

        # Sahne 3: Pizza 1/8
        self.play(FadeOut(cap2), FadeOut(circle1), FadeOut(sector1), FadeOut(lbl1))
        
        cap3 = create_caption("Ama 8 kisiye bolersen dilimin kucucuk kalir")
        circle2 = Circle(radius=1.6, color=WHITE).move_to(ORIGIN)
        sector2 = Sector(radius=1.6, angle=PI/4, color=RED, fill_opacity=0.8)
        sector2.move_to(circle2.get_center())
        lbl2 = MathTex(r"\frac{1}{8}", font_size=100).scale(0.8).next_to(circle2, DOWN, buff=0.5)
        
        self.play(Write(cap3), Create(circle2), FadeIn(sector2), Write(lbl2))
        self.wait(3)

        # Sahne 4: Kural
        self.play(FadeOut(cap3), FadeOut(circle2), FadeOut(sector2), FadeOut(lbl2))
        
        cap4 = create_caption("Yani payda buyudukce birim kesir kuculur")
        final_math = MathTex(r"\frac{1}{2} > \frac{1}{8}", font_size=100).scale(0.8).move_to(ORIGIN)
        
        self.play(Write(cap4), Write(final_math))
        self.wait(3)

        # Sahne 5: Kapanis
        self.play(FadeOut(cap4), FadeOut(final_math))
        
        cap5 = create_caption("Maarif Matematik ile mantigini kavra takipte kal")
        logo = Text("Maarif Matematik", font_size=100, color=YELLOW).scale_to_fit_width(6).move_to(ORIGIN)
        
        self.play(Write(cap5), Write(logo))
        self.wait(3)
