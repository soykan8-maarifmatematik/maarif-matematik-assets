from manim import *

class MaarifScene(Scene):
    def construct(self):
        # 1. Intro
        self.wait(1.67) # Merhaba, Maarif Matematik’e hoş geldiniz.

        # 2. Title
        title = Text("Birim Kesirler", font_size=48).to_edge(UP, buff=2.0).scale(1.2)
        self.play(Write(title))
        self.wait(1.67) # Bugün birim kesirlerin büyüklüklerini karşılaştırıyoruz.

        # 3. Models Setup
        circle1_outline = Circle(radius=1.2, color=WHITE)
        sector1 = Sector(radius=1.2, angle=PI, color=BLUE, fill_opacity=0.8)
        frac1 = MathTex(r"\frac{1}{2}", font_size=72)
        group1 = VGroup(VGroup(circle1_outline, sector1), frac1).arrange(RIGHT, buff=1.0)

        circle2_outline = Circle(radius=1.2, color=WHITE)
        sector2 = Sector(radius=1.2, angle=PI/2, color=RED, fill_opacity=0.8)
        frac2 = MathTex(r"\frac{1}{4}", font_size=72)
        group2 = VGroup(VGroup(circle2_outline, sector2), frac2).arrange(RIGHT, buff=1.0)

        # Central Placement (Safe Zone Uyumlu)
        main_group = VGroup(group1, group2).arrange(DOWN, buff=2.5)
        main_group.move_to(ORIGIN).shift(DOWN * 0.5)

        # 4. Animate 1/2
        self.play(Create(circle1_outline))
        self.play(Create(sector1))
        self.play(Write(frac1))
        self.wait(4.00) # Bir bütünü iki eş parçaya bölelim ve birini alalım. Bu ikide birdir.

        # 5. Transformation to 1/4
        circle2_copy = circle1_outline.copy()
        sector2_copy = sector1.copy()
        
        self.play(
            circle2_copy.animate.move_to(circle2_outline.get_center()),
            sector2_copy.animate.move_to(circle2_outline.get_center())
        )
        
        self.play(
            Transform(sector2_copy, sector2),
            circle2_copy.animate.set_color(WHITE)
        )
        self.play(Write(frac2))
        self.wait(4.67) # Şimdi aynı bütünü dört eş parçaya bölelim ve birini alalım. Bu da dörtte birdir.

        self.wait(2.33) # Gördüğünüz gibi, parça sayısı arttıkça dilim küçülüyor.

        # 6. Symbol Animation
        symbol = MathTex(">", font_size=96, color=YELLOW)
        symbol.move_to(VGroup(group1, group2).get_center())

        self.play(GrowFromCenter(symbol))
        self.play(Indicate(symbol, scale_factor=1.5, color=RED))
        self.wait(2.33) # Yani ikide bir, dörtte birden daha büyüktür.

        # 7. Outro
        self.wait(2.33) # Maarif Matematik ile mantığını kavra, takipte kal!
