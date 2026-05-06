from manim import *

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height = 16
config.frame_width = 9

class Multiplication(Scene):
    def construct(self):
        # 1. BAŞLIK (En Üst)
        header = Text("ÇARPMA İŞLEMİ", weight=BOLD, color=YELLOW)
        header.scale_to_fit_width(8.5)
        header.to_edge(UP, buff=0.8)
        self.play(Write(header))

        # 2. MODELLER (Orta-Üst)
        num1_tens = Text("1", weight=BOLD).scale(3)
        num1_ones = Text("5", weight=BOLD).scale(3)
        num2_ones = Text("3", weight=BOLD).scale(3)
        multiply_sign = Text("x", weight=BOLD).scale(2.5)
        
        # Hizalama işlemleri
        num1_ones.move_to(ORIGIN)
        num1_tens.next_to(num1_ones, LEFT, buff=0.8)
        num2_ones.next_to(num1_ones, DOWN, buff=0.5)
        multiply_sign.next_to(num1_tens, DOWN, buff=0.5)
        
        line = Line(LEFT * 2, RIGHT * 2).set_stroke(width=6)
        line.next_to(num2_ones, DOWN, buff=0.4)
        line.align_to(multiply_sign, LEFT).shift(LEFT * 0.3)
        
        # VGroup ile gruplayıp kurala uygun konuma taşıma
        math_group = VGroup(num1_tens, num1_ones, num2_ones, multiply_sign, line)
        math_group.move_to(UP * 1.2)
        
        self.play(Write(math_group))
        self.wait(0.5)

        # Adım 1: Birler basamağını çarpma
        self.play(num2_ones.animate.set_color(YELLOW), num1_ones.animate.set_color(YELLOW))
        self.wait(0.5)
        
        res_ones = Text("5", weight=BOLD).scale(3).set_color(YELLOW)
        res_ones.next_to(line, DOWN, buff=0.5)
        res_ones.set_x(num1_ones.get_x())
        
        carry_1 = Text("+1", weight=BOLD, color=RED).scale(1.5)
        carry_1.next_to(num1_tens, UP, buff=0.3)
        
        self.play(Write(res_ones))
        self.play(Write(carry_1))
        self.wait(0.5)
        
        self.play(num2_ones.animate.set_color(WHITE), num1_ones.animate.set_color(WHITE))

        # Adım 2: Onlar basamağını çarpma
        self.play(num2_ones.animate.set_color(GREEN), num1_tens.animate.set_color(GREEN))
        self.wait(0.5)
        
        self.play(Indicate(carry_1, color=RED, scale_factor=1.5))
        
        res_tens = Text("4", weight=BOLD).scale(3).set_color(GREEN)
        res_tens.next_to(line, DOWN, buff=0.5)
        res_tens.set_x(num1_tens.get_x())
        
        self.play(Write(res_tens))
        
        # Elde kullanıldı çizimi
        cross_line = Line(carry_1.get_corner(DL), carry_1.get_corner(UR), color=RED, stroke_width=6)
        self.play(Create(cross_line))
        self.wait(0.5)
        
        self.play(
            num2_ones.animate.set_color(WHITE), 
            num1_tens.animate.set_color(WHITE),
            res_ones.animate.set_color(WHITE),
            res_tens.animate.set_color(WHITE)
        )

        # 3. AÇIKLAMA (En Alt)
        exp_text = Paragraph(
            "Adım 1: 3 x 5 = 15 (5'i yaz, elde var 1)",
            "Adım 2: 3 x 1 = 3 (Eldeyi ekle: 3+1=4)",
            "Sonuç: 45",
            weight=BOLD
        )
        exp_text.scale_to_fit_width(7.5)
        exp_text.move_to(DOWN * 3.5)
        
        self.play(Write(exp_text))
        self.wait(2)