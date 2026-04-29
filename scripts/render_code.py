from manim import *
config.pixel_height = 1920
config.pixel_width = 1080

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # Başlık
        title = Text("BİRİM KESİRLER", color=BLACK, weight=BOLD, font_size=72)
        title.to_edge(UP, buff=1.0)
        
        # 1/2 Pizza Modeli
        pizza1_group = VGroup()
        circle1 = Circle(radius=1.5, color=BLACK, stroke_width=6)
        slice1 = Sector(radius=1.5, angle=PI, start_angle=0, color=ORANGE, fill_opacity=0.8)
        line1 = Line(circle1.get_top(), circle1.get_bottom(), color=BLACK, stroke_width=6)
        label1 = MathTex(r"\frac{1}{2}", color=BLACK, font_size=72).move_to(slice1.get_center())
        pizza1_group.add(circle1, slice1, line1, label1).move_to(UP * 2.5)
        
        # 1/4 Pizza Modeli
        pizza2_group = VGroup()
        circle2 = Circle(radius=1.5, color=BLACK, stroke_width=6)
        slice2 = Sector(radius=1.5, angle=PI/2, start_angle=0, color=RED, fill_opacity=0.8)
        line2_1 = Line(circle2.get_top(), circle2.get_bottom(), color=BLACK, stroke_width=6)
        line2_2 = Line(circle2.get_left(), circle2.get_right(), color=BLACK, stroke_width=6)
        label2 = MathTex(r"\frac{1}{4}", color=BLACK, font_size=72).move_to(slice2.get_center())
        pizza2_group.add(circle2, slice2, line2_1, line2_2, label2).move_to(DOWN * 1.5)
        
        # Alt Metin
        result_text = Text("Payda Büyüdükçe Değer Küçülür!", color=BLUE, weight=BOLD, font_size=48)
        result_text.to_edge(DOWN, buff=2.0)
        
        # Animasyonlar ve Senkronizasyon (Saniyede 3 kelime)
        
        # Cümle 1: Birim kesirleri karşılaştırırken kafan mı karışıyor? (7 kelime -> 2.33s)
        self.play(Write(title))
        self.wait(1.33)
        
        # Cümle 2: Gel, pizzalarla çok kolay bir şekilde öğrenelim! (7 kelime -> 2.33s)
        self.wait(2.33)
        
        # Cümle 3: Bir pizzayı ikiye bölersek, bir dilimi yarım pizza eder. Bu bir bölü ikidir. (13 kelime -> 4.33s)
        self.play(Create(circle1), Create(line1))
        self.play(FadeIn(slice1), Write(label1))
        self.wait(2.33)
        
        # Cümle 4: Aynı pizzayı dörde bölersek, dilimler küçülür. Bu da bir bölü dörttür. (11 kelime -> 3.66s)
        self.play(Create(circle2), Create(line2_1), Create(line2_2))
        self.play(FadeIn(slice2), Write(label2))
        self.wait(1.66)
        
        # Cümle 5: Yani payda büyüdükçe, dilim küçülür, kesrin değeri azalır! (8 kelime -> 2.66s)
        self.play(Write(result_text))
        self.wait(1.66)
        
        # Cümle 6: Maarif Matematik ile matematiği görerek anla! (6 kelime -> 2.0s)
        self.wait(2.0)