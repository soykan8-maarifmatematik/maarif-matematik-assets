from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class UnitFractions(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # BAŞLIK
        title = Text("BİRİM KESİRLER", color=BLACK, weight=BOLD).to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(3.3)
        
        # GİRİŞ METNİ
        intro_text = Text("Payı 1 olan kesir", color=BLUE, weight=BOLD).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(intro_text))
        self.wait(4.0)
        self.play(FadeOut(intro_text))
        
        # ANA ŞEKİLLER (Merkezde)
        pizza1 = Circle(radius=1.5, color=BLACK).shift(LEFT * 2.2)
        pizza2 = Circle(radius=1.5, color=BLACK).shift(RIGHT * 2.2)
        
        self.play(Create(pizza1), Create(pizza2))
        self.wait(2.3)
        
        # BÖLME ÇİZGİLERİ
        line1 = Line(pizza1.get_top(), pizza1.get_bottom(), color=BLACK)
        lines2 = VGroup(
            Line(pizza2.get_top(), pizza2.get_bottom(), color=BLACK),
            Line(pizza2.get_left(), pizza2.get_right(), color=BLACK)
        )
        self.play(Create(line1), Create(lines2))
        self.wait(2.3)
        
        # DİLİMLER (Sadece radius kullanıldı, move_to ile hizalandı)
        slice1 = Sector(radius=1.5, angle=PI, start_angle=PI/2, color=BLUE, fill_opacity=0.6).move_to(pizza1.get_center())
        slice2 = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color=RED, fill_opacity=0.6).move_to(pizza2.get_center())
        
        self.play(FadeIn(slice1), FadeIn(slice2))
        self.wait(4.3)
        
        # KESİR YAZILARI VE İŞARET
        label1 = MathTex("\\frac{1}{2}", color=BLACK, font_size=72).next_to(pizza1, DOWN, buff=0.5)
        label2 = MathTex("\\frac{1}{4}", color=BLACK, font_size=72).next_to(pizza2, DOWN, buff=0.5)
        sign = MathTex(">", color=BLACK, font_size=96).move_to(ORIGIN)
        
        self.play(Write(label1), Write(label2), Write(sign))
        self.wait(4.6)
        
        # ALT METİN (Sonuç)
        rule_text1 = Text("Payda Büyüdükçe", color=RED, weight=BOLD)
        rule_text2 = Text("Kesir KÜÇÜLÜR!", color=BLUE, weight=BOLD)
        rule_group = VGroup(rule_text1, rule_text2).arrange(DOWN, buff=0.3).to_edge(DOWN, buff=2.0)
        
        self.play(Write(rule_group))
        self.wait(2.6)
        
        # KAPANIŞ
        outro = Text("Maarif Matematik", color=DARK_GRAY, weight=BOLD).next_to(rule_group, UP, buff=1.0)
        self.play(FadeIn(outro))
        self.wait(2.3)
