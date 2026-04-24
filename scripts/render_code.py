from manim import *

config.pixel_width = 1080
config.pixel_height = 1920

class MaarifScene(Scene):
    def construct(self):
        # 1. GİRİŞ: "Merhaba, Maarif Matematik’e hoş geldiniz." (5 kelime -> 1.67 sn)
        title = Text("Maarif Matematik", font_size=60, color=YELLOW).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.67)
        self.wait(1.0)

        # 2. KANCA: "Birim kesirlerde payda büyüdükçe kesrin değeri neden küçülür? Gelin mantığını anlayalım." (11 kelime -> 3.67 sn)
        subtitle = Text("Birim Kesirler", font_size=50, color=WHITE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(subtitle), run_time=0.67)
        self.wait(3.0)

        # 3. AÇIKLAMA 1: "Bir pastayı ikiye böldüğünüzü düşünün. Bir dilimi bir bölü ikidir." (10 kelime -> 3.33 sn)
        pie1_group = VGroup()
        circle1 = Circle(radius=1.5, color=WHITE)
        slice1 = Sector(outer_radius=1.5, angle=PI, color=BLUE, fill_opacity=0.8)
        slice2 = Sector(outer_radius=1.5, angle=PI, start_angle=PI, color=DARK_GRAY, fill_opacity=0.5)
        label1 = MathTex(r"\frac{1}{2}", font_size=80).next_to(circle1, RIGHT, buff=1)
        pie1_group.add(slice1, slice2, circle1, label1)
        pie1_group.move_to(UP * 1.5)
        
        self.play(Create(circle1), FadeIn(slice1, slice2), run_time=1.33)
        self.play(Write(label1), run_time=1.0)
        self.wait(1.0)

        # 4. AÇIKLAMA 2: "Aynı pastayı dört kişiye paylaştırırsanız, her birinize düşen dilim bir bölü dört olur." (13 kelime -> 4.33 sn)
        pie2_group = VGroup()
        circle2 = Circle(radius=1.5, color=WHITE)
        slice3 = Sector(outer_radius=1.5, angle=PI/2, color=RED, fill_opacity=0.8)
        slice4 = Sector(outer_radius=1.5, angle=3*PI/2, start_angle=PI/2, color=DARK_GRAY, fill_opacity=0.5)
        label2 = MathTex(r"\frac{1}{4}", font_size=80).next_to(circle2, RIGHT, buff=1)
        pie2_group.add(slice3, slice4, circle2, label2)
        pie2_group.move_to(DOWN * 2.0)

        self.play(Create(circle2), FadeIn(slice3, slice4), run_time=1.33)
        self.play(Write(label2), run_time=1.0)
        self.wait(2.0)

        # 5. SONUÇ: "Yani parça sayısı arttıkça, size düşen pay ufalır. Bu yüzden bir bölü iki, bir bölü dörtten büyüktür." (17 kelime -> 5.67 sn)
        comparison = MathTex(r"\frac{1}{2} > \frac{1}{4}", font_size=100, color=YELLOW).move_to(DOWN * 5.0)
        self.play(Write(comparison), run_time=1.67)
        self.wait(4.0)

        # 6. ÇIKIŞ (MÜHÜR): "Maarif Matematik ile mantığını kavra, takipte kal!" (7 kelime -> 2.33 sn)
        outro = Text("Maarif Matematik ile mantığını kavra,\ntakipte kal!", font_size=36, color=GREEN, text_alignment="CENTER").move_to(DOWN * 6.5)
        self.play(FadeIn(outro), run_time=0.83)
        self.wait(1.5)

        # 7. FİNAL: Ekranı sabitleme
        self.wait(4)