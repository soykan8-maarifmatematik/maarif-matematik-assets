from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class BirimKesirler(Scene):
    def construct(self):
        # 1. GÜVENLİ ALAN: Üst Sınır (UP * 3.5)
        title = Text("BİRİM KESİRLER", font="DejaVu Sans", color=YELLOW, weight=BOLD).scale(1.2)
        title.move_to(UP * 3.2)

        # 2. GÜVENLİ ALAN: Alt Sınır (DOWN * 4.0)
        conclusion = Text("Payda büyüdükçe değer küçülür", font="DejaVu Sans", color=GREEN).scale(0.8)
        conclusion.move_to(DOWN * 3.8)

        # 3. GÖRSEL İSPAT MÜHRÜ: 1/2 Modeli
        frac1 = MathTex(r"\frac{1}{2}").scale(2.0)
        circle1 = Circle(radius=1.3, color=WHITE)
        line1 = Line(UP*1.3, DOWN*1.3, color=WHITE)
        slice1 = Sector(outer_radius=1.3, angle=PI, start_angle=PI/2, color=BLUE, fill_opacity=0.7)
        model1_parts = VGroup(circle1, line1, slice1)
        group1 = VGroup(frac1, model1_parts).arrange(RIGHT, buff=1.0)

        # 4. GÖRSEL İSPAT MÜHRÜ: 1/4 Modeli
        frac2 = MathTex(r"\frac{1}{4}").scale(2.0)
        circle2 = Circle(radius=1.3, color=WHITE)
        line2_v = Line(UP*1.3, DOWN*1.3, color=WHITE)
        line2_h = Line(LEFT*1.3, RIGHT*1.3, color=WHITE)
        slice2 = Sector(outer_radius=1.3, angle=PI/2, start_angle=PI/2, color=RED, fill_opacity=0.7)
        model2_parts = VGroup(circle2, line2_v, line2_h, slice2)
        group2 = VGroup(frac2, model2_parts).arrange(RIGHT, buff=1.0)

        # 5. DİKEY DİZİLİM MÜHRÜ: Jilet gibi aralık
        main_group = VGroup(group1, group2).arrange(DOWN, buff=1.5)
        main_group.move_to(DOWN * 0.3)

        # --- MİLİMETRİK SENKRONİZASYON --- 
        
        # GİRİŞ: "Merhaba, Maarif Matematik’e hoş geldiniz." (5 kelime -> 1.67s)
        self.play(Write(title), run_time=1.0)
        self.wait(0.67)

        # KONSEPT: "Birim kesirlerde payda büyüdükçe kesrin değeri küçülür." (7 kelime -> 2.33s)
        self.play(Write(conclusion), run_time=1.0)
        self.wait(1.33)

        # ÖRNEK 1: "Örneğin bir bölü iki kesrini düşünelim. Bir bütünü iki eş parçaya böldük ve birini aldık." (15 kelime -> 5.0s)
        self.play(Write(frac1), run_time=0.5)
        self.play(Create(circle1), run_time=1.0)
        self.play(Create(line1), run_time=0.5)
        self.play(FadeIn(slice1), run_time=1.0)
        self.wait(2.0)

        # ÖRNEK 2: "Şimdi de bir bölü dört kesrine bakalım. Aynı bütünü dört eş parçaya böldük ve birini aldık." (16 kelime -> 5.33s)
        self.play(Write(frac2), run_time=0.5)
        self.play(Create(circle2), run_time=1.0)
        self.play(Create(line2_v), Create(line2_h), run_time=0.5)
        self.play(FadeIn(slice2), run_time=1.0)
        self.wait(2.33)

        # KARŞILAŞTIRMA: "Gördüğünüz gibi bir bölü iki, bir bölü dörtten daha büyüktür. Parça sayısı arttıkça dilimler küçülür." (15 kelime -> 5.0s)
        self.play(Indicate(slice1, color=YELLOW, scale_factor=1.1), run_time=1.0)
        self.play(Indicate(slice2, color=YELLOW, scale_factor=1.1), run_time=1.0)
        self.wait(3.0)

        # ÇIKIŞ: "Bir sonraki derste görüşmek üzere, hoşça kalın." (7 kelime -> 2.33s)
        self.play(FadeOut(VGroup(title, conclusion, main_group)), run_time=1.0)
        self.wait(1.33)

        # EKRAN KARARMAMASI İÇİN GÜVENLİK BEKLEMESİ
        self.wait(5)