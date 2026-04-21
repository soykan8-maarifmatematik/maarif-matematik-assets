from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi
        self.camera.background_color = "#FFFFFF"

        # BÖLÜM 1: Giriş (95 kelime -> 32 saniye)
        title = Text("KESİRLER", color="#333333", font_size=72)
        self.play(Write(title)) # 1s
        self.wait(1)
        self.play(title.animate.to_edge(UP)) # 1s
        
        frac = MathTex(r"\frac{1}{2}", color="#333333", font_size=96)
        self.play(FadeIn(frac)) # 1s
        self.wait(28) # Toplam 32s

        # BÖLÜM 2: Pay, Payda ve Kesir Çizgisi (92 kelime -> 31 saniye)
        self.play(FadeOut(frac)) # 1s
        
        line = Line(LEFT, RIGHT, color="#333333").scale(1.5)
        pay_text = Text("PAY", color="#1976D2", font_size=48).next_to(line, UP, buff=0.5)
        payda_text = Text("PAYDA", color="#D32F2F", font_size=48).next_to(line, DOWN, buff=0.5)
        
        self.play(Create(line)) # 1s
        self.play(Write(payda_text)) # 1s
        self.play(Write(pay_text)) # 1s
        self.wait(27) # Toplam 31s

        # BÖLÜM 3: Görsel Örnek - Daire (84 kelime -> 28 saniye)
        self.play(FadeOut(VGroup(line, pay_text, payda_text, title))) # 1s
        
        circle = Circle(radius=2, color="#333333", stroke_width=4)
        circle.to_edge(LEFT, buff=2)
        self.play(Create(circle)) # 1s
        
        line_v = Line(circle.get_top(), circle.get_bottom(), color="#333333")
        line_h = Line(circle.get_left(), circle.get_right(), color="#333333")
        self.play(Create(line_v), Create(line_h)) # 1s
        self.wait(5)
        
        sector1 = Sector(arc_center=circle.get_center(), radius=2, angle=PI/2, start_angle=0, color="#1976D2", fill_opacity=0.7)
        sector2 = Sector(arc_center=circle.get_center(), radius=2, angle=PI/2, start_angle=PI/2, color="#1976D2", fill_opacity=0.7)
        sector3 = Sector(arc_center=circle.get_center(), radius=2, angle=PI/2, start_angle=PI, color="#1976D2", fill_opacity=0.7)
        self.play(FadeIn(sector1), FadeIn(sector2), FadeIn(sector3)) # 1s
        
        frac34 = MathTex(r"\frac{3}{4}", font_size=96)
        frac34[0][0].set_color("#1976D2") # Pay
        frac34[0][1].set_color("#333333") # Çizgi
        frac34[0][2].set_color("#D32F2F") # Payda
        frac34.to_edge(RIGHT, buff=3)
        self.play(Write(frac34)) # 1s
        self.wait(18) # Toplam 28s

        # BÖLÜM 4: 1. Okuma Yöntemi (86 kelime -> 29 saniye)
        okunus1 = Text("Üç bölü Dört", color="#333333", font_size=48, t2c={"Üç": "#1976D2", "Dört": "#D32F2F"})
        okunus1.next_to(frac34, DOWN, buff=1)
        self.play(Write(okunus1)) # 1s
        self.wait(28) # Toplam 29s

        # BÖLÜM 5: 2. Okuma Yöntemi (82 kelime -> 27 saniye)
        okunus2 = Text("Dörtte Üç", color="#333333", font_size=48, t2c={"Dörtte": "#D32F2F", "Üç": "#1976D2"})
        okunus2.next_to(okunus1, DOWN, buff=0.5)
        self.play(Write(okunus2)) # 1s
        self.wait(26) # Toplam 27s

        # BÖLÜM 6: Görsel Örnek - Dikdörtgen (76 kelime -> 25 saniye)
        self.play(FadeOut(VGroup(circle, line_v, line_h, sector1, sector2, sector3, frac34, okunus1, okunus2))) # 1s
        
        rect = Rectangle(width=5, height=2, color="#333333", stroke_width=4)
        rect.to_edge(LEFT, buff=1.5)
        self.play(Create(rect)) # 1s
        
        lines = VGroup(*[Line(rect.get_corner(UL) + RIGHT * i, rect.get_corner(DL) + RIGHT * i, color="#333333") for i in range(1, 5)])
        self.play(Create(lines)) # 1s
        self.wait(4)
        
        rect_fill1 = Rectangle(width=1, height=2, color="#1976D2", fill_opacity=0.7).set_stroke(width=0).move_to(rect.get_left() + RIGHT*0.5)
        rect_fill2 = Rectangle(width=1, height=2, color="#1976D2", fill_opacity=0.7).set_stroke(width=0).move_to(rect.get_left() + RIGHT*1.5)
        self.play(FadeIn(rect_fill1), FadeIn(rect_fill2)) # 1s
        
        frac25 = MathTex(r"\frac{2}{5}", font_size=96)
        frac25[0][0].set_color("#1976D2")
        frac25[0][1].set_color("#333333")
        frac25[0][2].set_color("#D32F2F")
        frac25.to_edge(RIGHT, buff=3)
        self.play(Write(frac25)) # 1s
        self.wait(16) # Toplam 25s

        # BÖLÜM 7: 2. Örnek Okunuşu (63 kelime -> 21 saniye)
        okunus3 = Text("İki bölü Beş", color="#333333", font_size=48, t2c={"İki": "#1976D2", "Beş": "#D32F2F"})
        okunus3.next_to(frac25, DOWN, buff=1)
        self.play(Write(okunus3)) # 1s
        
        okunus4 = Text("Beşte İki", color="#333333", font_size=48, t2c={"Beşte": "#D32F2F", "İki": "#1976D2"})
        okunus4.next_to(okunus3, DOWN, buff=0.5)
        self.play(Write(okunus4)) # 1s
        self.wait(19) # Toplam 21s

        # BÖLÜM 8: Kapanış (58 kelime -> 19 saniye)
        self.play(FadeOut(VGroup(rect, lines, rect_fill1, rect_fill2, frac25, okunus3, okunus4))) # 1s
        
        logo = Text("Maarif Matematik", color="#1976D2", font_size=60)
        self.play(Write(logo)) # 1s
        self.wait(17) # Toplam 19s
