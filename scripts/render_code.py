from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0

class MaarifScene(Scene):
    def construct(self):
        # Intro
        text_intro = Text("Merhaba, Maarif Matematik'e hoş geldiniz.", font="DejaVu Sans", font_size=40, text_align="center").to_edge(UP, buff=1)
        self.play(Write(text_intro))
        self.wait(1.67)
        self.play(FadeOut(text_intro))

        # Hook
        text_hook = Text("Birim kesirlerde payda büyüdükçe\nkesrin değeri neden küçülür?", font="DejaVu Sans", font_size=40, text_align="center").to_edge(UP, buff=1)
        self.play(Write(text_hook))
        self.wait(2.67)
        self.play(FadeOut(text_hook))

        # Setup circles
        circle1 = Circle(radius=2.0, color=WHITE)
        circle2 = Circle(radius=2.0, color=WHITE)
        circles = VGroup(circle1, circle2).arrange(DOWN, buff=1.2)
        c1 = circle1.get_center()
        c2 = circle2.get_center()

        # 1/2 Model
        text_1 = Text("Bir pizzayı iki eş parçaya bölelim ve\nbir dilimini alalım. Bu bir bölü ikidir.", font="DejaVu Sans", font_size=36, text_align="center").to_edge(DOWN, buff=1)
        self.play(Write(text_1))
        self.play(Create(circle1))
        line1 = Line(c1 + UP*2.0, c1 + DOWN*2.0, color=WHITE)
        self.play(Create(line1))
        sector1 = Sector(outer_radius=2.0, angle=PI, start_angle=PI/2, color=YELLOW, fill_opacity=0.7, arc_center=c1)
        label1 = MathTex(r"\frac{1}{2}").scale(2).next_to(circle1, LEFT, buff=0.5)
        self.play(FadeIn(sector1), Write(label1))
        self.wait(4.67)
        self.play(FadeOut(text_1))

        # 1/8 Model
        text_2 = Text("Aynı pizzayı sekiz eş parçaya bölersek\nalacağımız bir dilim çok daha küçük olur.\nBu da bir bölü sekizdir.", font="DejaVu Sans", font_size=36, text_align="center").to_edge(DOWN, buff=1)
        self.play(Write(text_2))
        self.play(Create(circle2))
        lines2 = VGroup()
        for i in range(4):
            angle = i * PI / 4
            lines2.add(Line(c2 + np.array([np.cos(angle), np.sin(angle), 0])*2.0,
                            c2 - np.array([np.cos(angle), np.sin(angle), 0])*2.0, color=WHITE))
        self.play(Create(lines2))
        sector2 = Sector(outer_radius=2.0, angle=PI/4, start_angle=PI/2, color=RED, fill_opacity=0.7, arc_center=c2)
        label2 = MathTex(r"\frac{1}{8}").scale(2).next_to(circle2, LEFT, buff=0.5)
        self.play(FadeIn(sector2), Write(label2))
        self.wait(6.0)
        self.play(FadeOut(text_2))

        # Comparison
        text_comp = Text("Gördüğünüz gibi payda parça sayısını gösterir.\nParça sayısı artarsa dilim küçülür.", font="DejaVu Sans", font_size=36, text_align="center").to_edge(DOWN, buff=1)
        self.play(Write(text_comp))
        self.wait(3.67)
        self.play(FadeOut(text_comp))

        # Rule
        text_rule = Text("Yani bir bölü iki büyüktür bir bölü sekizden.", font="DejaVu Sans", font_size=36, text_align="center").to_edge(DOWN, buff=1)
        self.play(Write(text_rule))
        sign = MathTex(">").scale(3).move_to((c1+c2)/2)
        self.play(Write(sign))
        self.wait(2.67)
        self.play(FadeOut(text_rule))

        # Outro
        text_outro = Text("Bir sonraki derste görüşmek üzere, hoşça kalın.", font="DejaVu Sans", font_size=40, text_align="center").to_edge(DOWN, buff=1)
        self.play(Write(text_outro))
        self.wait(2.33)
        
        # Ending Fix
        self.wait(5)
