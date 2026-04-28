from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class BirimKesirler(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        # Title
        title = Text("Birim Kesirler", color=BLACK, font_size=48).to_edge(UP, buff=2.0).scale(1.2)

        # 1/2 Model
        circle_half = Circle(radius=1.5, color=LIGHT_GRAY)
        lines_half = VGroup(Line(circle_half.get_top(), circle_half.get_bottom(), color=LIGHT_GRAY))
        sector_half = Sector(outer_radius=1.5, angle=PI, start_angle=PI/2, color=BLUE, fill_opacity=0.8)
        label_half = MathTex(r"\frac{1}{2}", color=BLACK, font_size=80)
        
        frac1_model = VGroup(circle_half, lines_half, sector_half)
        frac1_group = VGroup(frac1_model, label_half).arrange(RIGHT, buff=1.0)

        # 1/8 Model
        circle_eighth = Circle(radius=1.5, color=LIGHT_GRAY)
        lines_eighth = VGroup()
        for i in range(4):
            angle = i * PI / 4
            start = circle_eighth.get_center() + np.array([np.cos(angle)*1.5, np.sin(angle)*1.5, 0])
            end = circle_eighth.get_center() + np.array([-np.cos(angle)*1.5, -np.sin(angle)*1.5, 0])
            lines_eighth.add(Line(start, end, color=LIGHT_GRAY))
        sector_eighth = Sector(outer_radius=1.5, angle=PI/4, start_angle=PI/2, color=RED, fill_opacity=0.8)
        label_eighth = MathTex(r"\frac{1}{8}", color=BLACK, font_size=80)
        
        frac2_model = VGroup(circle_eighth, lines_eighth, sector_eighth)
        frac2_group = VGroup(frac2_model, label_eighth).arrange(RIGHT, buff=1.0)

        # Layout
        content = VGroup(frac1_group, frac2_group).arrange(DOWN, buff=2.5)
        content.next_to(title, DOWN, buff=1.0)

        # Animations and Sync
        # "Merhaba, Maarif Matematik’e hoş geldiniz." (6 words = 2.0s)
        self.play(Write(title), run_time=1.0)
        self.wait(1.0)

        # "Bugün birim kesirlerin büyüklüğünü karşılaştırıyoruz." (5 words = 1.6s)
        self.wait(1.6)

        # "Bir pastayı düşünün. Pastayı ikiye bölersek, bir dilim oldukça büyüktür." (10 words = 3.3s)
        self.play(Create(circle_half), Create(lines_half), run_time=1.3)
        self.play(FadeIn(sector_half), Write(label_half), run_time=1.0)
        self.wait(1.0)

        # "Ama aynı pastayı sekiz parçaya bölersek, bir dilim çok daha küçük olur." (12 words = 4.0s)
        self.play(Create(circle_eighth), Create(lines_eighth), run_time=1.5)
        self.play(FadeIn(sector_eighth), Write(label_eighth), run_time=1.0)
        self.wait(1.5)

        # "Yani, payda büyüdükçe birim kesrin değeri küçülür." (7 words = 2.3s)
        self.play(Indicate(label_half, color=BLUE), Indicate(label_eighth, color=RED), run_time=1.5)
        self.wait(0.8)

        # "Maarif Matematik ile mantığını kavra, takipte kal!" (7 words = 2.3s)
        self.wait(2.3)