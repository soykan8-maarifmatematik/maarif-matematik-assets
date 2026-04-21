from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5
        text_color = "#333333"
        maarif_blue = "#1976D2"
        maarif_red = "#D32F2F"

        # 1. Başlık
        title = Text("Kesirlerin Mantığı", color=text_color).scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # 2. Kesir ve Pasta Grubu (Merkezlenmiş)
        circle = Circle(radius=1.5, color=text_color).shift(LEFT*3 + DOWN*0.5)
        lines = VGroup(
            Line(circle.get_top(), circle.get_bottom(), color=text_color),
            Line(circle.get_left(), circle.get_right(), color=text_color)
        )
        
        # 3 parça boyalı
        sectors = VGroup(*[
            Sector(radius=1.48, angle=TAU/4, start_angle=i*TAU/4, 
                   color=maarif_blue, fill_opacity=0.7).move_to(circle)
            for i in range(3)
        ])
        
        fraction = MathTex(r"\frac{3}{4}", color=text_color).scale(2.5).shift(RIGHT*2 + DOWN*0.5)
        
        self.play(Create(circle), Create(lines))
        self.wait(5) # Tanım yapılırken bekleme
        self.play(FadeIn(sectors), Write(fraction))
        self.wait(10)

        # 3. Okunuş Okları (O profesyonel görünüm)
        up_arrow = Arrow(start=DOWN, end=UP, color=maarif_red).next_to(fraction, RIGHT, buff=0.5)
        down_arrow = Arrow(start=UP, end=DOWN, color=maarif_blue).next_to(fraction, LEFT, buff=0.5)
        
        read_1 = Text("Üç bölü dört", color=maarif_blue, font_size=24).next_to(down_arrow, LEFT)
        read_2 = Text("Dörtte üç", color=maarif_red, font_size=24).next_to(up_arrow, RIGHT)

        self.play(GrowArrow(down_arrow), Write(read_1))
        self.wait(15) # İlk okunuş anlatımı
        self.play(GrowArrow(up_arrow), Write(read_2))
        self.wait(20) # İkinci okunuş anlatımı

        # 4. Kapanış
        self.play(FadeOut(Group(*self.mobjects)))
        self.play(Write(Text("Bir sonraki derste görüşmek üzere...", color=maarif_blue).scale(0.7)))
        self.wait(3)
