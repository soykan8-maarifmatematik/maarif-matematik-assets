from manim import *
import numpy as np

class UnitFractions(Scene):
    def construct(self):
        # DİKEY CONFIG MÜHRÜ
        config.pixel_height = 1920
        config.pixel_width = 1080
        self.camera.background_color = "#FFFFFF"

        # ÜST GÜVENLİ ALAN (ÇENTİK) - BAŞLIK
        title = Text("Birim Kesirler", color=BLACK, font_weight=BOLD).scale(1.2).to_edge(UP, buff=2.8)
        self.play(Write(title))
        self.wait(4.66) # 17 kelime / 3.0 = 5.66s (1s Write + 4.66s wait)

        # MODELLEME: 1/2 Kesri
        c1_pos = UP*0.5 + LEFT*2.5
        c1 = Circle(radius=1.0, color=GRAY).move_to(c1_pos)
        l1_1 = Line(c1_pos + UP*1.0, c1_pos + DOWN*1.0, color=GRAY)
        s1 = Sector(outer_radius=1.0, angle=PI, start_angle=-PI/2, color=RED, fill_opacity=0.7, arc_center=c1_pos)
        t1 = MathTex(r"\frac{1}{2}", color=BLACK).next_to(c1, DOWN, buff=0.5)

        self.play(Create(c1), Create(l1_1), run_time=1)
        self.play(FadeIn(s1), run_time=1)
        self.play(Write(t1), run_time=1)
        self.wait(1.0) # 12 kelime / 3.0 = 4.0s (3s anim + 1s wait)

        # MODELLEME: 1/3 Kesri
        c2_pos = UP*0.5
        c2 = Circle(radius=1.0, color=GRAY).move_to(c2_pos)
        l2_1 = Line(c2_pos, c2_pos + UP*1.0, color=GRAY)
        l2_2 = Line(c2_pos, c2_pos + np.array([np.cos(-PI/6), np.sin(-PI/6), 0])*1.0, color=GRAY)
        l2_3 = Line(c2_pos, c2_pos + np.array([np.cos(7*PI/6), np.sin(7*PI/6), 0])*1.0, color=GRAY)
        s2 = Sector(outer_radius=1.0, angle=2*PI/3, start_angle=-PI/6, color=BLUE, fill_opacity=0.7, arc_center=c2_pos)
        t2 = MathTex(r"\frac{1}{3}", color=BLACK).next_to(c2, DOWN, buff=0.5)

        self.play(Create(c2), Create(VGroup(l2_1, l2_2, l2_3)), run_time=1)
        self.play(FadeIn(s2), run_time=1)
        self.play(Write(t2), run_time=1)
        self.wait(1.33) # 13 kelime / 3.0 = 4.33s (3s anim + 1.33s wait)

        # MODELLEME: 1/4 Kesri
        c3_pos = UP*0.5 + RIGHT*2.5
        c3 = Circle(radius=1.0, color=GRAY).move_to(c3_pos)
        l3_1 = Line(c3_pos + UP*1.0, c3_pos + DOWN*1.0, color=GRAY)
        l3_2 = Line(c3_pos + LEFT*1.0, c3_pos + RIGHT*1.0, color=GRAY)
        s3 = Sector(outer_radius=1.0, angle=PI/2, start_angle=0, color=GREEN, fill_opacity=0.7, arc_center=c3_pos)
        t3 = MathTex(r"\frac{1}{4}", color=BLACK).next_to(c3, DOWN, buff=0.5)

        self.play(Create(c3), Create(VGroup(l3_1, l3_2)), run_time=1)
        self.play(FadeIn(s3), run_time=1)
        self.play(Write(t3), run_time=1)
        self.wait(1.33) # 13 kelime / 3.0 = 4.33s (3s anim + 1.33s wait)

        # AÇIKLAMA VURGUSU
        self.play(Indicate(s1, color=RED), Indicate(s2, color=BLUE), Indicate(s3, color=GREEN), run_time=2)
        self.wait(2.0) # 12 kelime / 3.0 = 4.0s (2s anim + 2s wait)

        # ALT GÜVENLİ ALAN - KARŞILAŞTIRMA (y = -3.5, sınır -4.2'den güvenli)
        eq = VGroup(
            MathTex(r"\frac{1}{2}", color=BLACK),
            MathTex(">", color=RED),
            MathTex(r"\frac{1}{3}", color=BLACK),
            MathTex(">", color=RED),
            MathTex(r"\frac{1}{4}", color=BLACK)
        ).arrange(RIGHT, buff=0.5).scale(1.5).move_to(DOWN * 3.5)

        self.play(TransformFromCopy(t1, eq[0]), run_time=0.5)
        self.play(GrowFromCenter(eq[1]), run_time=0.5)
        self.play(Indicate(eq[1], color=RED), run_time=0.5)
        self.play(TransformFromCopy(t2, eq[2]), run_time=0.5)
        self.play(GrowFromCenter(eq[3]), run_time=0.5)
        self.play(Indicate(eq[3], color=RED), run_time=0.5)
        self.play(TransformFromCopy(t3, eq[4]), run_time=0.5)
        
        self.wait(1.16) # 14 kelime / 3.0 = 4.66s (3.5s anim + 1.16s wait)

        # KAPANIŞ BEKLEMESİ (6 kelime / 3.0 = 2.0s + 2s ek bekleme = 4.0s)
        self.wait(4.0)
