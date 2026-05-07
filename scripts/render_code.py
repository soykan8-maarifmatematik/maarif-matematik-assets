config.pixel_height, config.pixel_width = 1920, 1080
from manim import *

class Multiplication(Scene):
    def construct(self):
        # Başlık ve Alt Metin
        title = Text("İki Basamaklı Çarpma İşlemi").to_edge(UP, buff=0.8).scale_to_fit_width(8.5)
        bottom_text = Text("Adım adım çarpmayı öğreniyoruz!").move_to(DOWN * 3.5).scale_to_fit_width(7.5)
        
        # Sayılar ve İşaretler
        num1 = MathTex("6", "7").scale(2)
        num2 = MathTex("8", "9").scale(2)
        num2.next_to(num1, DOWN, buff=0.2, aligned_edge=RIGHT)
        
        times = MathTex("\\times").scale(2).next_to(num2, LEFT, buff=0.5)
        line1 = Line(LEFT, RIGHT).scale(1.5).next_to(num2, DOWN, buff=0.2).align_to(times, LEFT)
        
        # Adım 1: 9 x 67
        res1_3 = MathTex("3").scale(2).next_to(line1, DOWN, buff=0.3)
        res1_3.set_x(num2[1].get_x())
        
        res1_0 = MathTex("0").scale(2).set_y(res1_3.get_y())
        res1_0.set_x(num2[0].get_x())
        
        res1_6 = MathTex("6").scale(2).set_y(res1_3.get_y())
        res1_6.next_to(res1_0, LEFT, buff=0.3)
        
        carry6 = MathTex("+6").scale(0.8).next_to(num1[0], UP, buff=0.2).set_color(YELLOW)
        
        # Adım 2: 8 x 67
        res2_6 = MathTex("6").scale(2).next_to(res1_3, DOWN, buff=0.3)
        res2_6.set_x(res1_0.get_x())
        
        res2_3 = MathTex("3").scale(2).set_y(res2_6.get_y())
        res2_3.set_x(res1_6.get_x())
        
        res2_5 = MathTex("5").scale(2).set_y(res2_6.get_y())
        res2_5.next_to(res2_3, LEFT, buff=0.3)
        
        carry5 = MathTex("+5").scale(0.8).next_to(carry6, UP, buff=0.1).set_color(ORANGE)
        
        # Toplama İşlemi
        line2 = Line(LEFT, RIGHT).scale(2.2).next_to(res2_6, DOWN, buff=0.2)
        line2.set_x(res2_3.get_x())
        plus = MathTex("+").scale(1.5).next_to(line2, LEFT, buff=0.2)
        
        # Sonuç: 5963
        fin_3 = MathTex("3").scale(2).next_to(line2, DOWN, buff=0.3)
        fin_3.set_x(res1_3.get_x())
        
        fin_6 = MathTex("6").scale(2).set_y(fin_3.get_y())
        fin_6.set_x(res2_6.get_x())
        
        fin_9 = MathTex("9").scale(2).set_y(fin_3.get_y())
        fin_9.set_x(res2_3.get_x())
        
        fin_5 = MathTex("5").scale(2).set_y(fin_3.get_y())
        fin_5.set_x(res2_5.get_x())
        
        # Tüm matematiksel ifadeleri grupla ve konumlandır
        math_group = VGroup(
            num1, num2, times, line1,
            res1_3, res1_0, res1_6, carry6,
            res2_6, res2_3, res2_5, carry5,
            line2, plus,
            fin_3, fin_6, fin_9, fin_5
        )
        math_group.move_to(UP * 1.2)
        
        # Animasyonlar
        self.play(Write(title), Write(bottom_text))
        self.play(Write(num1), Write(num2), Write(times), Create(line1))
        
        # 9 x 7
        self.play(num2[1].animate.set_color(YELLOW), num1[1].animate.set_color(YELLOW))
        self.wait(0.3)
        self.play(Write(res1_3))
        self.play(Write(carry6))
        self.play(num1[1].animate.set_color(WHITE))
        
        # 9 x 6
        self.play(num1[0].animate.set_color(YELLOW))
        self.wait(0.3)
        self.play(Write(res1_0), Write(res1_6))
        self.play(carry6.animate.set_opacity(0.3))
        self.play(num2[1].animate.set_color(WHITE), num1[0].animate.set_color(WHITE))
        
        # 8 x 7
        self.play(num2[0].animate.set_color(ORANGE), num1[1].animate.set_color(ORANGE))
        self.wait(0.3)
        self.play(Write(res2_6))
        self.play(Write(carry5))
        self.play(num1[1].animate.set_color(WHITE))
        
        # 8 x 6
        self.play(num1[0].animate.set_color(ORANGE))
        self.wait(0.3)
        self.play(Write(res2_3), Write(res2_5))
        self.play(carry5.animate.set_opacity(0.3))
        self.play(num2[0].animate.set_color(WHITE), num1[0].animate.set_color(WHITE))
        
        # Toplama
        self.play(Create(line2), Write(plus))
        self.play(Write(fin_3))
        self.play(Write(fin_6))
        self.play(Write(fin_9))
        self.play(Write(fin_5))
        
        self.wait(2)