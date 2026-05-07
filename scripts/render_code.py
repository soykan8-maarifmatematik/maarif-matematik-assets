from manim import *

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_width = 9
config.frame_height = 16

class MultiplicationStepByStep(Scene):
    def construct(self):
        # 1. BAŞLIK (Sabit Kadraj ve Boyutlandırma)
        header = Text("ÇARPMA İŞLEMİ", weight=BOLD, color=YELLOW)
        header.to_edge(UP, buff=0.8).scale_to_fit_width(8.5)
        self.play(Write(header))

        # 2. MODELLER (Matematiksel İşlem)
        num1_tens = MathTex("1").scale(3)
        num1_units = MathTex("5").scale(3)
        num2_units = MathTex("3").scale(3)
        
        sym = MathTex("\\times").scale(2.5)
        line = Line(LEFT, RIGHT).scale(2).set_stroke(width=6, color=WHITE)
        
        res_tens = MathTex("4").scale(3)
        res_units = MathTex("5").scale(3)
        
        carry = MathTex("1").scale(1.5).set_color(YELLOW)
        
        # Hizalama İşlemleri
        num1_units.move_to(RIGHT * 0.8 + UP * 0.5)
        num1_tens.move_to(LEFT * 0.8 + UP * 0.5)
        
        num2_units.next_to(num1_units, DOWN, buff=0.5)
        sym.next_to(num2_units, LEFT, buff=1)
        
        line.next_to(num2_units, DOWN, buff=0.4)
        line.set_x(0)
        
        res_units.next_to(line, DOWN, buff=0.5)
        res_units.set_x(num1_units.get_x())
        
        res_tens.next_to(line, DOWN, buff=0.5)
        res_tens.set_x(num1_tens.get_x())
        
        carry.next_to(num1_tens, UP, buff=0.3)
        
        # Grubu oluştur ve kurala göre taşı
        math_group = VGroup(num1_tens, num1_units, num2_units, sym, line, res_tens, res_units, carry)
        math_group.move_to(UP * 1.2)
        
        # Animasyonlar (Aniden ekrana gelme yok, sırayla çizim)
        self.play(Write(num1_tens), Write(num1_units))
        self.wait(0.5)
        self.play(Write(num2_units))
        self.wait(0.5)
        self.play(Write(sym), Create(line))
        self.wait(1)
        
        # 3. AÇIKLAMA (Adım 1)
        desc1 = Text("Adım 1: 3 x 5 = 15\n5'i yaz, elde var 1.", weight=BOLD, color=WHITE)
        desc1.move_to(DOWN * 3.5).scale_to_fit_width(7.5)
        
        self.play(Write(desc1))
        self.play(num1_units.animate.set_color(GREEN), num2_units.animate.set_color(GREEN))
        self.wait(1)
        
        self.play(Write(res_units))
        self.play(Write(carry))
        self.wait(1)
        
        # 3. AÇIKLAMA (Adım 2)
        desc2 = Text("Adım 2: 3 x 1 = 3\nEldeki 1'i ekle, sonuç 4.", weight=BOLD, color=WHITE)
        desc2.move_to(DOWN * 3.5).scale_to_fit_width(7.5)
        
        self.play(Transform(desc1, desc2))
        self.play(num1_units.animate.set_color(WHITE), num2_units.animate.set_color(GREEN))
        self.play(num1_tens.animate.set_color(GREEN))
        self.wait(1)
        
        self.play(carry.animate.scale(1.2).set_color(RED))
        self.play(Write(res_tens))
        self.wait(1)
        
        # Final Görünümü
        self.play(
            num1_tens.animate.set_color(WHITE),
            num2_units.animate.set_color(WHITE),
            carry.animate.scale(1/1.2).set_color(YELLOW),
            res_tens.animate.set_color(YELLOW),
            res_units.animate.set_color(YELLOW)
        )
        self.wait(2)