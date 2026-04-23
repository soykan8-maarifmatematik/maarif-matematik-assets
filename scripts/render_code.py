from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class BirimKesirler(Scene):
    def construct(self):
        # Captions
        cap1 = Text("1/2 mi daha büyük yoksa 1/10 mu?", font_size=85, weight=BOLD).scale_to_fit_width(7).to_edge(DOWN, buff=1.0)
        cap2 = Text("Payda büyüdükçe kesir neden küçülür?", font_size=85, weight=BOLD).scale_to_fit_width(7).to_edge(DOWN, buff=1.0)
        cap3 = Text("Gelin bunu bir pizza üzerinden düşünelim.", font_size=85, weight=BOLD).scale_to_fit_width(7).to_edge(DOWN, buff=1.0)
        cap4 = Text("1/2 demek, pizzayı 2 eş parçaya bölüp", font_size=85, weight=BOLD).scale_to_fit_width(7).to_edge(DOWN, buff=1.0)
        cap5 = Text("1 dilimini almak demektir.", font_size=85, weight=BOLD).scale_to_fit_width(7).to_edge(DOWN, buff=1.0)
        cap6 = Text("1/10 ise, 10 eş parçaya bölüp", font_size=85, weight=BOLD).scale_to_fit_width(7).to_edge(DOWN, buff=1.0)
        cap7 = Text("1 dilimini almaktır.", font_size=85, weight=BOLD).scale_to_fit_width(7).to_edge(DOWN, buff=1.0)
        cap8 = Text("İkiye böldüğümüz dilim kocaman!", font_size=85, weight=BOLD).scale_to_fit_width(7).to_edge(DOWN, buff=1.0)
        cap9 = Text("Ona böldüğümüz dilim ise küçücük.", font_size=85, weight=BOLD).scale_to_fit_width(7).to_edge(DOWN, buff=1.0)
        cap10 = Text("Birim kesirlerde payda büyüdükçe", font_size=85, weight=BOLD).scale_to_fit_width(7).to_edge(DOWN, buff=1.0)
        cap11 = Text("değer küçülür.", font_size=85, weight=BOLD).scale_to_fit_width(7).to_edge(DOWN, buff=1.0)
        cap12 = Text("Maarif Matematik ile mantığını kavra,\ntakipte kal!", font_size=85, weight=BOLD, text_align="center").scale_to_fit_width(7).to_edge(DOWN, buff=1.0)

        # Objects
        frac1 = MathTex(r"\frac{1}{2}", font_size=110)
        circle1 = Circle(radius=1.5, color=WHITE)
        sector1 = Sector(radius=1.5, angle=PI, start_angle=PI/2, color=YELLOW, fill_opacity=0.8)
        line1 = Line(circle1.get_boundary_point(PI/2), circle1.get_boundary_point(3*PI/2), color=WHITE)
        pizza1 = VGroup(circle1, line1)

        frac2 = MathTex(r"\frac{1}{10}", font_size=110)
        circle2 = Circle(radius=1.5, color=WHITE)
        sector2 = Sector(radius=1.5, angle=TAU/10, start_angle=PI/2, color=RED, fill_opacity=0.8)
        lines2 = VGroup(*[Line(circle2.get_center(), circle2.get_boundary_point(i*TAU/10 + PI/2), color=WHITE) for i in range(10)])
        pizza2 = VGroup(circle2, lines2)

        item1 = VGroup(frac1, pizza1).arrange(RIGHT, buff=1.0)
        item2 = VGroup(frac2, pizza2).arrange(RIGHT, buff=1.0)
        comparison = VGroup(item1, item2).arrange(DOWN, buff=1.5).shift(UP*0.5)

        sector1.move_to(circle1.get_center())
        sector2.move_to(circle2.get_center())

        # Animations
        self.play(Write(cap1), run_time=1.5)
        self.play(FadeIn(frac1, shift=DOWN), FadeIn(frac2, shift=UP), run_time=1)
        self.play(Transform(cap1, cap2), run_time=1.5)
        self.play(Indicate(frac2, color=RED), run_time=1)

        self.play(Transform(cap1, cap3), run_time=1.5)
        self.play(FadeOut(frac1), FadeOut(frac2), run_time=0.5)

        self.play(Transform(cap1, cap4), FadeIn(frac1), Create(pizza1), run_time=2)
        self.play(Transform(cap1, cap5), run_time=1.5)
        self.play(FadeIn(sector1), run_time=0.5)
        self.play(Indicate(sector1, scale_factor=1.1), run_time=1)

        self.play(Transform(cap1, cap6), FadeIn(frac2), Create(pizza2), run_time=2)
        self.play(Transform(cap1, cap7), run_time=1.5)
        self.play(FadeIn(sector2), run_time=0.5)
        self.play(Indicate(sector2, scale_factor=1.1), run_time=1)

        self.play(Transform(cap1, cap8), run_time=1.5)
        self.play(Wiggle(sector1), Circumscribe(sector1, color=YELLOW), run_time=1.5)

        self.play(Transform(cap1, cap9), run_time=1.5)
        self.play(Wiggle(sector2), Circumscribe(sector2, color=RED), run_time=1.5)

        self.play(Transform(cap1, cap10), run_time=1.5)
        label_big = Text("BÜYÜK", font_size=60, color=GREEN).next_to(item1, LEFT, buff=0.5)
        label_small = Text("KÜÇÜK", font_size=60, color=RED).next_to(item2, LEFT, buff=0.5)
        self.play(Write(label_big), Write(label_small), run_time=1)
        
        self.play(Transform(cap1, cap11), run_time=1)
        self.play(Indicate(label_big), Indicate(label_small), run_time=1)

        self.play(Transform(cap1, cap12), run_time=1.5)
        self.play(
            FadeOut(comparison), FadeOut(sector1), FadeOut(sector2),
            FadeOut(label_big), FadeOut(label_small),
            run_time=1
        )
        logo = Text("Maarif Matematik", font_size=100, weight=BOLD, color=BLUE)
        self.play(Write(logo), run_time=1)
        self.play(Circumscribe(logo), run_time=1)