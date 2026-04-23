from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class UnitFractions(Scene):
    def construct(self):
        # KAPANIŞ MÜHRÜ (CTA) - Başlangıçta gizli
        cta_text = Text("Maarif Matematik ile mantığını kavra, takipte kal!", font="sans-serif")
        cta_text.scale_to_fit_width(7.2)
        cta_text.move_to(ORIGIN)
        cta_text.set_opacity(0)
        self.add(cta_text)

        def create_sub(text_str):
            t = Text(text_str, font="sans-serif")
            t.scale_to_fit_width(7.2)
            t.move_to(UP * 5)
            return t

        # KANCA [0-5 sn]
        sub = create_sub("Pastayı 2'ye mi bölsen daha büyük dilim yersin, 10'a mı?")
        self.play(FadeIn(sub))
        self.wait(4.0) # 10 kelime / 2.5 = 4.0 sn

        sub_next = create_sub("İşte birim kesirler!")
        self.play(ReplacementTransform(sub, sub_next))
        sub = sub_next
        self.wait(1.2) # 3 kelime / 2.5 = 1.2 sn

        # GÖVDE [5-55 sn]
        sub_next = create_sub("Birim kesir, payı 1 olan kesirdir.")
        self.play(ReplacementTransform(sub, sub_next))
        sub = sub_next
        
        formula = MathTex(r"\frac{1}{x}").scale(3).move_to(ORIGIN)
        self.play(Write(formula))
        self.wait(2.4) # 6 kelime / 2.5 = 2.4 sn

        sub_next = create_sub("Yani bir bütünün sadece bir parçasıdır.")
        self.play(ReplacementTransform(sub, sub_next))
        sub = sub_next
        
        box = SurroundingRectangle(formula[0][0], color=YELLOW)
        self.play(Create(box))
        self.wait(2.4) # 6 kelime / 2.5 = 2.4 sn

        sub_next = create_sub("Örneğin, 1/2 ve 1/4 kesirlerini düşünelim.")
        self.play(ReplacementTransform(sub, sub_next))
        sub = sub_next
        self.play(FadeOut(formula), FadeOut(box))
        self.wait(2.4) # 6 kelime / 2.5 = 2.4 sn

        sub_next = create_sub("İki tane aynı boyutta pizza hayal edelim.")
        self.play(ReplacementTransform(sub, sub_next))
        sub = sub_next
        
        circle1 = Circle(radius=1.8, color=WHITE).move_to(UP * 1.8)
        circle2 = Circle(radius=1.8, color=WHITE).move_to(DOWN * 2.2)
        self.play(Create(circle1), Create(circle2))
        self.wait(2.8) # 7 kelime / 2.5 = 2.8 sn

        sub_next = create_sub("İlk pizzayı 2 eşit parçaya bölelim...")
        self.play(ReplacementTransform(sub, sub_next))
        sub = sub_next
        
        line1 = Line(circle1.get_top(), circle1.get_bottom(), color=WHITE)
        self.play(Create(line1))
        self.wait(2.4) # 6 kelime / 2.5 = 2.4 sn

        sub_next = create_sub("...ve birini alalım. Bu 1/2'dir.")
        self.play(ReplacementTransform(sub, sub_next))
        sub = sub_next
        
        sector1 = Sector(radius=1.8, angle=PI, start_angle=PI/2, arc_center=circle1.get_center(), color=YELLOW, fill_opacity=0.8)
        label1 = MathTex(r"\frac{1}{2}").scale(1.5).move_to(circle1.get_center() + LEFT * 0.9)
        self.play(Create(sector1), Write(label1))
        self.wait(2.0) # 5 kelime / 2.5 = 2.0 sn

        sub_next = create_sub("İkinci pizzayı ise 4 eşit parçaya bölelim...")
        self.play(ReplacementTransform(sub, sub_next))
        sub = sub_next
        
        line2_v = Line(circle2.get_top(), circle2.get_bottom(), color=WHITE)
        line2_h = Line(circle2.get_left(), circle2.get_right(), color=WHITE)
        self.play(Create(line2_v), Create(line2_h))
        self.wait(2.8) # 7 kelime / 2.5 = 2.8 sn

        sub_next = create_sub("...ve yine birini alalım. Bu da 1/4'tür.")
        self.play(ReplacementTransform(sub, sub_next))
        sub = sub_next
        
        sector2 = Sector(radius=1.8, angle=PI/2, start_angle=PI/2, arc_center=circle2.get_center(), color=ORANGE, fill_opacity=0.8)
        label2 = MathTex(r"\frac{1}{4}").scale(1.2).move_to(circle2.get_center() + LEFT * 0.6 + UP * 0.6)
        self.play(Create(sector2), Write(label2))
        self.wait(2.8) # 7 kelime / 2.5 = 2.8 sn

        sub_next = create_sub("Gördüğünüz gibi, 1/2 dilimi, 1/4 diliminden çok daha büyüktür.")
        self.play(ReplacementTransform(sub, sub_next))
        sub = sub_next
        
        self.play(Indicate(sector1, color=YELLOW, scale_factor=1.1))
        self.wait(3.6) # 9 kelime / 2.5 = 3.6 sn

        sub_next = create_sub("Kural çok basit: Payda büyüdükçe, bütün daha fazla parçaya bölünür.")
        self.play(ReplacementTransform(sub, sub_next))
        sub = sub_next
        
        self.play(FadeOut(circle1), FadeOut(line1), FadeOut(sector1), FadeOut(label1),
                  FadeOut(circle2), FadeOut(line2_v), FadeOut(line2_h), FadeOut(sector2), FadeOut(label2))
        
        rule_text = MathTex(r"\text{Payda } \uparrow \implies \text{Parça Sayısı } \uparrow").scale(1.2).move_to(UP * 1)
        self.play(Write(rule_text))
        self.wait(4.0) # 10 kelime / 2.5 = 4.0 sn

        sub_next = create_sub("Bu yüzden parça küçülür. Yani payda büyüdükçe, birim kesrin değeri küçülür.")
        self.play(ReplacementTransform(sub, sub_next))
        sub = sub_next
        
        rule_text2 = MathTex(r"\implies \text{Kesrin Değeri } \downarrow").scale(1.2).next_to(rule_text, DOWN * 2)
        self.play(Write(rule_text2))
        self.wait(4.4) # 11 kelime / 2.5 = 4.4 sn

        sub_next = create_sub("1/2 büyüktür 1/3, o da büyüktür 1/4!")
        self.play(ReplacementTransform(sub, sub_next))
        sub = sub_next
        
        self.play(FadeOut(rule_text), FadeOut(rule_text2))
        ineq = MathTex(r"\frac{1}{2} > \frac{1}{3} > \frac{1}{4}").scale(2.0).move_to(ORIGIN)
        self.play(Write(ineq))
        self.wait(2.8) # 7 kelime / 2.5 = 2.8 sn

        # KAPANIŞ [55-60 sn]
        sub_next = create_sub("Artık payda büyüdükçe kesrin küçüldüğünü biliyorsun.")
        self.play(ReplacementTransform(sub, sub_next))
        sub = sub_next
        
        box2 = SurroundingRectangle(ineq, color=GREEN)
        self.play(Create(box2))
        self.wait(2.4) # 6 kelime / 2.5 = 2.4 sn

        self.play(FadeOut(sub), FadeOut(ineq), FadeOut(box2))
        
        # MÜHRÜ GÖSTER
        self.play(cta_text.animate.set_opacity(1))
        self.wait(2.0)
