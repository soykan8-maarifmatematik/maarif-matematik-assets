from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # 1. Merhaba, Maarif Matematik’e hoş geldiniz. (1.67s)
        self.wait(1.67)

        # Objeleri oluştur
        title = Text("Birim Kesirler", font="DejaVu Sans", color=YELLOW)
        title.scale_to_fit_width(6.0)

        c1 = Circle(radius=1.3, color=WHITE)
        l1 = Line(c1.get_top(), c1.get_bottom(), color=WHITE)
        s1 = Sector(radius=1.3, angle=PI, start_angle=PI/2, color=BLUE, fill_opacity=0.6)
        m1 = VGroup(c1, l1, s1)

        c2 = Circle(radius=1.3, color=WHITE)
        l2_1 = Line(c2.get_top(), c2.get_bottom(), color=WHITE)
        l2_2 = Line(c2.get_left(), c2.get_right(), color=WHITE)
        s2 = Sector(radius=1.3, angle=PI/2, start_angle=PI/2, color=RED, fill_opacity=0.6)
        m2 = VGroup(c2, l2_1, l2_2, s2)

        models_row = VGroup(m1, m2).arrange(RIGHT, buff=1.0)

        comp_1 = MathTex(r"\frac{1}{2}").scale(2)
        comp_sign = MathTex(">").scale(2).set_color(YELLOW)
        comp_2 = MathTex(r"\frac{1}{4}").scale(2)
        compare_label = VGroup(comp_1, comp_sign, comp_2).arrange(RIGHT, buff=0.8)

        # Dikey Dizilim Kuralı ve Güvenli Alan Hizalaması
        main_group = VGroup(title, models_row, compare_label).arrange(DOWN, buff=1.6)
        main_group.move_to(DOWN * 0.25)

        # 2. Birim kesirlerde payda büyüdükçe kesrin değeri küçülür. (2.33s)
        self.play(Write(title), run_time=1.0)
        self.wait(1.33)

        # 3. Örneğin bir bölü iki ve bir bölü dört kesirlerini karşılaştıralım. (3.33s)
        self.play(Write(comp_1), Write(comp_2), run_time=1.0)
        self.wait(2.33)

        # 4. Bir bütün pastayı ikiye böldüğümüzde elde ettiğimiz dilim oldukça büyüktür. (3.33s)
        self.play(Create(c1), run_time=0.5)
        self.play(Create(l1), run_time=0.5)
        self.play(FadeIn(s1), run_time=0.5)
        self.wait(1.83)

        # 5. Aynı pastayı dörde böldüğümüzde ise her bir dilim daha küçük olur. (3.67s)
        self.play(Create(c2), run_time=0.5)
        self.play(Create(l2_1), Create(l2_2), run_time=0.5)
        self.play(FadeIn(s2), run_time=0.5)
        self.wait(2.17)

        # 6. Bu yüzden bir bölü iki büyüktür bir bölü dört diyebiliriz. (3.33s)
        self.play(Write(comp_sign), run_time=1.0)
        self.wait(2.33)

        # 7. Bir sonraki derste görüşmek üzere, hoşça kalın. (2.33s)
        self.wait(2.33)

        # Kapanış
        self.wait(5)
