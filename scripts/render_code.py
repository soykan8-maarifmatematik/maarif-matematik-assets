from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class MaarifScene(Scene):
    def construct(self):
        # Title
        title = Text("BİRİM KESİRLER", font_size=48, color=YELLOW).to_edge(UP, buff=2.0)

        # Helper function for fractions
        def create_fraction(num, den):
            n = MathTex(num, font_size=60)
            l = Line(LEFT*0.4, RIGHT*0.4)
            d = MathTex(den, font_size=60)
            return VGroup(n, l, d).arrange(DOWN, buff=0.15)

        # Pizza 1 (1/2)
        c1 = Circle(radius=1.2, color=LIGHT_GRAY).move_to(UP*3.0)
        l1 = Line(c1.get_top(), c1.get_bottom(), color=LIGHT_GRAY)
        p1_group = VGroup(c1, l1)
        s1 = Sector(radius=1.2, angle=PI, start_angle=PI/2, color=RED, fill_opacity=0.8).move_to(UP*3.0)
        t1 = create_fraction("1", "2").next_to(c1, RIGHT, buff=1.0)

        # Pizza 2 (1/4)
        c2 = Circle(radius=1.2, color=LIGHT_GRAY).move_to(ORIGIN)
        l2_1 = Line(c2.get_top(), c2.get_bottom(), color=LIGHT_GRAY)
        l2_2 = Line(c2.get_left(), c2.get_right(), color=LIGHT_GRAY)
        p2_group = VGroup(c2, l2_1, l2_2)
        s2 = Sector(radius=1.2, angle=PI/2, start_angle=PI/2, color=BLUE, fill_opacity=0.8).move_to(ORIGIN)
        t2 = create_fraction("1", "4").next_to(c2, RIGHT, buff=1.0)

        # Pizza 3 (1/8)
        c3 = Circle(radius=1.2, color=LIGHT_GRAY).move_to(DOWN*3.0)
        l3_1 = Line(c3.get_top(), c3.get_bottom(), color=LIGHT_GRAY)
        l3_2 = Line(c3.get_left(), c3.get_right(), color=LIGHT_GRAY)
        l3_3 = Line(c3.point_at_angle(PI/4), c3.point_at_angle(5*PI/4), color=LIGHT_GRAY)
        l3_4 = Line(c3.point_at_angle(3*PI/4), c3.point_at_angle(7*PI/4), color=LIGHT_GRAY)
        p3_group = VGroup(c3, l3_1, l3_2, l3_3, l3_4)
        s3 = Sector(radius=1.2, angle=PI/4, start_angle=PI/2, color=GREEN, fill_opacity=0.8).move_to(DOWN*3.0)
        t3 = create_fraction("1", "8").next_to(c3, RIGHT, buff=1.0)

        # Animations
        # 0.0 - 3.67 sn
        self.play(Write(title), run_time=1.0)
        self.wait(2.67)

        # 3.67 - 7.0 sn
        self.play(Create(p1_group), run_time=1.0)
        self.play(Create(s1), run_time=1.0)
        self.wait(1.33)

        # 7.0 - 8.33 sn
        self.play(Write(t1), run_time=0.5)
        self.play(Indicate(t1[2], color=YELLOW), run_time=0.5)
        self.wait(0.33)

        # 8.33 - 12.0 sn
        self.play(Create(p2_group), run_time=1.0)
        self.play(Create(s2), run_time=1.0)
        self.wait(1.67)

        # 12.0 - 13.33 sn
        self.play(Write(t2), run_time=0.5)
        self.play(Indicate(t2[2], color=YELLOW), run_time=0.5)
        self.wait(0.33)

        # 13.33 - 15.33 sn
        self.play(Create(p3_group), run_time=1.0)
        self.wait(1.0)

        # 15.33 - 18.0 sn
        self.play(Create(s3), run_time=1.0)
        self.play(Write(t3), run_time=0.5)
        self.play(Indicate(t3[2], color=YELLOW), run_time=0.5)
        self.wait(0.67)

        # 18.0 - 23.0 sn
        self.play(Indicate(t1[2]), Indicate(t2[2]), Indicate(t3[2]), run_time=1.0)
        self.play(Indicate(s1), Indicate(s2), Indicate(s3), run_time=1.0)
        self.wait(3.0)

        # Final FadeOut (Son 1 saniye)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.0)