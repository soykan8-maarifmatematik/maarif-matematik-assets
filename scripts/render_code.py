from manim import *

class BirimKesirler(Scene):
    def construct(self):
        config.pixel_height = 1920
        config.pixel_width = 1080
        config.frame_height = 16.0
        config.frame_width = 9.0

        # Başlık (iPhone 16 Fix)
        title = Text("Birim Kesirler", font="DejaVu Sans", font_size=60).to_edge(UP, buff=2.0)
        
        self.play(Write(title))
        # "Merhaba, Maarif Matematik’e hoş geldiniz." (5 kelime)
        self.wait(5 / 3.0)

        # Modeller
        # 1/2 Modeli
        rect1_outline = Rectangle(height=2, width=6, color=WHITE)
        line1 = Line(rect1_outline.get_top(), rect1_outline.get_bottom(), color=WHITE)
        fill1 = Rectangle(height=2, width=3, color=BLUE, fill_opacity=0.7).align_to(rect1_outline, LEFT)
        label1 = MathTex(r"\frac{1}{2}", font_size=72).next_to(rect1_outline, UP, buff=0.5)
        model1 = VGroup(label1, VGroup(rect1_outline, line1, fill1))

        # 1/4 Modeli
        rect2_outline = Rectangle(height=2, width=6, color=WHITE)
        line2_1 = Line(rect2_outline.get_top() + LEFT*1.5, rect2_outline.get_bottom() + LEFT*1.5, color=WHITE)
        line2_2 = Line(rect2_outline.get_top(), rect2_outline.get_bottom(), color=WHITE)
        line2_3 = Line(rect2_outline.get_top() + RIGHT*1.5, rect2_outline.get_bottom() + RIGHT*1.5, color=WHITE)
        fill2 = Rectangle(height=2, width=1.5, color=RED, fill_opacity=0.7).align_to(rect2_outline, LEFT)
        label2 = MathTex(r"\frac{1}{4}", font_size=72).next_to(rect2_outline, UP, buff=0.5)
        model2 = VGroup(label2, VGroup(rect2_outline, line2_1, line2_2, line2_3, fill2))

        # Yerleşim
        model1.move_to(UP * 2.0)
        model2.next_to(model1, DOWN, buff=1.8)

        self.play(FadeIn(rect1_outline))
        # "Bugün birim kesirlerin büyüklüğünü karşılaştıracağız." (5 kelime)
        self.wait(5 / 3.0)

        self.play(Write(label1))
        # "Birim kesir, payı bir olan kesirdir." (6 kelime)
        self.wait(6 / 3.0)

        self.play(FadeIn(rect2_outline), Write(label2))
        # "Örneğin, bir bölü iki ve bir bölü dört kesirlerini düşünelim." (10 kelime)
        self.wait(10 / 3.0)

        self.play(Create(line1), FadeIn(fill1))
        # "Bir bütünü ikiye bölersek, parçalar büyük olur." (7 kelime)
        self.wait(7 / 3.0)

        self.play(Create(VGroup(line2_1, line2_2, line2_3)), FadeIn(fill2))
        # "Ama dörde bölersek, parçalar küçülür." (5 kelime)
        self.wait(5 / 3.0)

        greater_sign = MathTex(">", font_size=96).move_to((model1.get_bottom() + model2.get_top()) / 2)
        self.play(Write(greater_sign))
        # "Yani, payda büyüdükçe birim kesrin değeri küçülür." (7 kelime)
        self.wait(7 / 3.0)

        # Outro Kilidi ve Temizleme
        self.wait(2.0)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        outro_text = Text("Maarif Matematik ile\nmantığını kavra,\ntakipte kal!", font="DejaVu Sans", font_size=55)
        self.play(Write(outro_text))
        # Outro bekleme süresi
        self.wait(4.0)