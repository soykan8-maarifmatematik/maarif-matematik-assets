from manim import *

class MaarifScene(Scene):
    def construct(self):
        config.pixel_height = 1920
        config.pixel_width = 1080
        config.frame_height = 14.22
        config.frame_width = 8.0
        self.camera.background_color = "#002B4D"

        # KANCA (0-7 sn) - 15 kelime
        hook_text = Text("Payda büyüdükçe\nkesir küçülür mü?", font_size=60, color="#FFFFFF").scale(0.8)
        hook_text[0][0:5].set_color("#FFD700")
        self.play(Write(hook_text), run_time=1.5)
        self.wait(5.5)
        self.play(FadeOut(hook_text), run_time=0.5)

        # GÖVDE 1 (7-17 sn) - 23 kelime
        title = Text("BİRİM KESİRLER", font_size=70, color="#FFD700").to_edge(UP, buff=1.5).scale(0.8)
        self.play(FadeIn(title), run_time=1.0)

        pizza1_group = VGroup()
        pizza1 = Circle(radius=2, color="#FFFFFF", stroke_width=4)
        line1 = Line(pizza1.get_top(), pizza1.get_bottom(), color="#FFFFFF")
        frac1 = MathTex(r"\frac{1}{2}", font_size=90, color="#FFFFFF").next_to(pizza1, RIGHT, buff=0.5)
        pizza1_group.add(pizza1, line1, frac1)
        pizza1_group.move_to(UP * 2.5)

        pizza2_group = VGroup()
        pizza2 = Circle(radius=2, color="#FFFFFF", stroke_width=4)
        line2_1 = Line(pizza2.get_top(), pizza2.get_bottom(), color="#FFFFFF")
        line2_2 = Line(pizza2.get_left(), pizza2.get_right(), color="#FFFFFF")
        frac2 = MathTex(r"\frac{1}{4}", font_size=90, color="#FFFFFF").next_to(pizza2, RIGHT, buff=0.5)
        pizza2_group.add(pizza2, line2_1, line2_2, frac2)
        pizza2_group.move_to(DOWN * 2.5)

        pizza1_group.scale(0.7)
        pizza2_group.scale(0.7)

        self.play(Create(pizza1_group), Create(pizza2_group), run_time=2.0)
        self.wait(7.2)

        # GÖVDE 2 (17-26 sn) - 20 kelime
        slice1 = Sector(arc_center=pizza1.get_center(), radius=1.4, angle=PI, start_angle=PI/2, color="#FFD700", fill_opacity=0.8)
        slice2 = Sector(arc_center=pizza2.get_center(), radius=1.4, angle=PI/2, start_angle=PI/2, color="#D32F2F", fill_opacity=0.8)

        self.play(Create(slice1), Create(slice2), run_time=2.0)
        self.wait(7.0)

        # GÖVDE 3 (26-34 sn) - 16 kelime
        comp_text = Text("Hangisinin dilimi\ndaha büyük?", font_size=50, color="#FFFFFF").move_to(DOWN * 6).scale(0.8)
        self.play(Write(comp_text), run_time=1.0)
        self.wait(6.4)
        self.play(FadeOut(comp_text), run_time=0.5)

        # GÖVDE 4 (34-43 sn) - 20 kelime
        rule_text = Text("Kişi sayısı artarsa,\ndilim küçülür!", font_size=55, color="#FFD700").move_to(DOWN * 6).scale(0.8)
        self.play(Write(rule_text), run_time=1.0)
        self.wait(2.0)

        math_comp = MathTex(r"\frac{1}{2} > \frac{1}{4}", font_size=100, color="#FFFFFF").move_to(CENTER)
        math_comp[0][3].set_color("#D32F2F")
        
        self.play(FadeOut(pizza1_group), FadeOut(pizza2_group), FadeOut(slice1), FadeOut(slice2), FadeOut(rule_text), FadeOut(title), run_time=1.0)
        self.play(Write(math_comp), run_time=1.0)
        self.wait(4.0)

        # KAPANIŞ (43-50 sn) - 14 kelime
        self.play(FadeOut(math_comp), run_time=0.5)
        cta1 = Text("Maarif Matematik ile", font_size=60, color="#FFFFFF").move_to(UP*0.5).scale(0.8)
        cta2 = Text("Mantığını Kavra!", font_size=70, color="#FFD700").next_to(cta1, DOWN, buff=0.3).scale(0.8)
        self.play(FadeIn(cta1), FadeIn(cta2), run_time=1.0)
        self.wait(5.1)
