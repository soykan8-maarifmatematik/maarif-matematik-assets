from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class BirimKesir(Scene):
    def construct(self):
        # Kanca [0-5 sn]
        hook_text = Text("1/3 mü daha büyük, 1/5 mi?", font="sans-serif").move_to(UP * 5).scale_to_fit_width(7.2)
        self.play(Write(hook_text))
        self.wait(2.8) # 7 kelime / 2.5 = 2.8 sn

        # Gövde 1 [5-25 sn]
        body1_text = Text("Bir pizzayı 3 eş parçaya bölelim.", font="sans-serif").move_to(UP * 5).scale_to_fit_width(7.2)
        self.play(Transform(hook_text, body1_text))
        
        circle1 = Circle(radius=2.0, color=ORANGE, fill_opacity=0.2)
        slice1 = Sector(radius=2.0, angle=TAU/3, color=ORANGE, fill_opacity=0.8, arc_center=circle1.get_center())
        circle_group1 = VGroup(circle1, slice1)
        frac1 = MathTex(r"\frac{1}{3}", font_size=120)
        
        visual1 = VGroup(circle_group1, frac1).arrange(DOWN, buff=1.0).move_to(ORIGIN)
        self.play(FadeIn(visual1))
        self.wait(2.4) # 6 kelime / 2.5 = 2.4 sn

        body1_text_b = Text("Her bir dilim oldukça doyurucu olur.", font="sans-serif").move_to(UP * 5).scale_to_fit_width(7.2)
        self.play(Transform(hook_text, body1_text_b))
        self.wait(2.4) # 6 kelime / 2.5 = 2.4 sn

        # Gövde 2 [25-40 sn]
        body2_text = Text("Aynı pizzayı 5 eş parçaya bölersek...", font="sans-serif").move_to(UP * 5).scale_to_fit_width(7.2)
        self.play(Transform(hook_text, body2_text))
        
        circle2 = Circle(radius=2.0, color=BLUE, fill_opacity=0.2)
        slice2 = Sector(radius=2.0, angle=TAU/5, color=BLUE, fill_opacity=0.8, arc_center=circle2.get_center())
        circle_group2 = VGroup(circle2, slice2)
        frac2 = MathTex(r"\frac{1}{5}", font_size=120)
        
        visual2 = VGroup(circle_group2, frac2).arrange(DOWN, buff=1.0).move_to(ORIGIN)
        self.play(Transform(visual1, visual2))
        self.wait(2.4) # 6 kelime / 2.5 = 2.4 sn

        body2_text_b = Text("Dilimler küçülür, çünkü çok kişiye paylaştırıyorsun.", font="sans-serif").move_to(UP * 5).scale_to_fit_width(7.2)
        self.play(Transform(hook_text, body2_text_b))
        self.wait(2.4) # 6 kelime / 2.5 = 2.4 sn

        # Gövde 3 [40-55 sn]
        body3_text = Text("Yani, birim kesirlerde payda büyüdükçe...", font="sans-serif").move_to(UP * 5).scale_to_fit_width(7.2)
        self.play(Transform(hook_text, body3_text))
        
        final_math = MathTex(r"\frac{1}{3} > \frac{1}{5}", font_size=120).move_to(ORIGIN)
        self.play(Transform(visual1, final_math))
        self.wait(2.0) # 5 kelime / 2.5 = 2.0 sn

        body3_text_b = Text("Parça küçülür. Mantık çok basit!", font="sans-serif").move_to(UP * 5).scale_to_fit_width(7.2)
        self.play(Transform(hook_text, body3_text_b))
        self.wait(2.0) # 5 kelime / 2.5 = 2.0 sn

        # Kapanış (CTA) [55-60 sn]
        self.play(FadeOut(visual1), FadeOut(hook_text))
        cta_text = Text("Maarif Matematik ile mantığını kavra, takipte kal!", font="sans-serif").move_to(UP * 5).scale_to_fit_width(7.2)
        self.play(Write(cta_text))
        self.wait(2.8) # 7 kelime / 2.5 = 2.8 sn