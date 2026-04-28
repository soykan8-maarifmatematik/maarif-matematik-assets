from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # Title
        title = Text("Birim Kesirler", color=BLACK, weight=BOLD).scale(1.2).to_edge(UP, buff=2.0)
        
        # Visuals
        circle_half = Circle(radius=1.5, color=BLACK)
        sector_half = Sector(radius=1.5, angle=PI, color=BLUE, fill_opacity=0.8)
        group_half = VGroup(circle_half, sector_half)
        label_half = MathTex(r"\frac{1}{2}", color=BLACK).scale(1.5).next_to(group_half, DOWN)
        half_comp = VGroup(group_half, label_half)
        
        circle_quarter = Circle(radius=1.5, color=BLACK)
        sector_quarter = Sector(radius=1.5, angle=PI/2, color=RED, fill_opacity=0.8)
        group_quarter = VGroup(circle_quarter, sector_quarter)
        label_quarter = MathTex(r"\frac{1}{4}", color=BLACK).scale(1.5).next_to(group_quarter, DOWN)
        quarter_comp = VGroup(group_quarter, label_quarter)
        
        visuals = VGroup(half_comp, quarter_comp).arrange(RIGHT, buff=1.0)
        
        # Math Text
        math_text = MathTex(r"\frac{1}{2} > \frac{1}{4}", color=BLACK).scale(2.5)
        
        # Central Layout
        main_group = VGroup(visuals, math_text).arrange(DOWN, buff=2.5)
        main_group.move_to(ORIGIN)
        
        # Animations & Sync
        # "Merhaba, Maarif Matematik’e hoş geldiniz." (6 kelime -> 2.0s)
        self.play(Write(title))
        self.wait(2.0)
        
        # "Birim kesirleri karşılaştırırken paydanın büyüklüğüne dikkat etmeliyiz." (7 kelime -> 2.33s)
        self.wait(2.33)
        
        # "Bir pastayı ikiye bölerseniz mi daha büyük bir dilim yersiniz, yoksa dörde bölerseniz mi?" (14 kelime -> 4.67s)
        self.play(FadeIn(visuals))
        self.wait(4.67)
        
        # "Tabii ki ikiye böldüğünüzde! Yani payda büyüdükçe, dilim küçülür." (9 kelime -> 3.0s)
        self.play(
            sector_half.animate.scale(1.1),
            sector_quarter.animate.scale(0.9)
        )
        self.wait(3.0)
        
        # "Bu yüzden bir bölü iki, bir bölü dörtten daha büyüktür." (10 kelime -> 3.33s)
        self.play(Write(math_text))
        self.wait(3.33)
        
        # "Maarif Matematik ile mantığını kavra, takipte kal!" (7 kelime -> 2.33s)
        self.play(Circumscribe(math_text, color=GREEN, time_width=2.0))
        self.wait(2.33)
