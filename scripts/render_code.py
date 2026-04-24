from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0

class BirimKesirler(Scene):
    def construct(self):
        # 1. GİRİŞ VE BAŞLIK (iPHONE 16 ZIRHI)
        title = Text("Birim Kesirlerin Büyüklüğü", font="DejaVu Sans", font_size=42).to_edge(UP, buff=2.0)
        self.play(Write(title))
        self.wait(5 / 3.0) # Merhaba, Maarif Matematik’e hoş geldiniz.

        concept = Text("Payda Büyüdükçe Değer Küçülür", font="DejaVu Sans", font_size=32, color=YELLOW).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(concept))
        self.wait(7 / 3.0) # Birim kesirlerde payda büyüdükçe kesrin değeri küçülür.

        # 2. MODEL 1: 1/2 (İLK MODEL KESİNLİKLE UP * 2.0)
        rect1 = Rectangle(width=6, height=1.5, color=WHITE)
        line1 = Line(rect1.get_top(), rect1.get_bottom(), color=WHITE)
        fill1 = Rectangle(width=3, height=1.5, color=BLUE).set_fill(BLUE, 0.8).align_to(rect1, LEFT)
        label1 = MathTex(r"\frac{1}{2}", font_size=72).next_to(rect1, RIGHT, buff=0.5)
        
        group1 = VGroup(rect1, line1, fill1, label1).move_to(UP * 2.0)
        
        self.play(Create(rect1), Create(line1))
        self.play(FadeIn(fill1), Write(label1))
        self.wait(7 / 3.0) # Örneğin, bir bütünü iki eş parçaya bölelim.

        # 3. MODEL 2: 1/4 (DOWN, buff=1.8 KURALI)
        rect2 = Rectangle(width=6, height=1.5, color=WHITE)
        lines2 = VGroup(*[
            Line(rect2.get_top() + LEFT * (3 - i*1.5), rect2.get_bottom() + LEFT * (3 - i*1.5), color=WHITE)
            for i in range(1, 4)
        ])
        fill2 = Rectangle(width=1.5, height=1.5, color=RED).set_fill(RED, 0.8).align_to(rect2, LEFT)
        label2 = MathTex(r"\frac{1}{4}", font_size=72).next_to(rect2, RIGHT, buff=0.5)
        
        group2 = VGroup(rect2, lines2, fill2, label2).next_to(group1, DOWN, buff=1.8)
        
        self.play(Create(rect2), Create(lines2))
        self.play(FadeIn(fill2), Write(label2))
        self.wait(8 / 3.0) # Aynı bütünü dört eş parçaya bölersek dilimler küçülür.

        # 4. MODEL 3: 1/8 (DOWN, buff=1.8 KURALI)
        rect3 = Rectangle(width=6, height=1.5, color=WHITE)
        lines3 = VGroup(*[
            Line(rect3.get_top() + LEFT * (3 - i*0.75), rect3.get_bottom() + LEFT * (3 - i*0.75), color=WHITE)
            for i in range(1, 8)
        ])
        fill3 = Rectangle(width=0.75, height=1.5, color=GREEN).set_fill(GREEN, 0.8).align_to(rect3, LEFT)
        label3 = MathTex(r"\frac{1}{8}", font_size=72).next_to(rect3, RIGHT, buff=0.5)
        
        group3 = VGroup(rect3, lines3, fill3, label3).next_to(group2, DOWN, buff=1.8)
        
        self.play(Create(rect3), Create(lines3))
        self.play(FadeIn(fill3), Write(label3))
        self.wait(9 / 3.0) # Sekiz eş parçaya böldüğümüzde ise dilimler daha da küçülür.

        # 5. SONUÇ VE VURGU
        box = SurroundingRectangle(VGroup(label1, label2, label3), color=YELLOW, buff=0.2)
        self.play(Create(box))
        self.wait(6 / 3.0) # Yani payda büyüdükçe, birim kesir küçülür.

        # 6. OUTRO KİLİDİ (MUTLAK SENKRONİZASYON)
        self.wait(2.0)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        outro = Text("Maarif Matematik ile\nmantığını kavra,\ntakipte kal!", font="DejaVu Sans", font_size=48, color=WHITE)
        self.play(Write(outro))
        self.wait(4.0)