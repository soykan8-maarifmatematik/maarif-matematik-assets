from manim import *

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class MultiplicationShort(Scene):
    def construct(self):
        # 3. DİKEY EKOSİSTEM: Arka plan siyah
        self.camera.background_color = "#000000"

        # 1. AKILLI BAŞLIK YASASI
        title = Paragraph(
            "İki Basamaklı Sayılarla",
            "Çarpma İşlemi",
            alignment="center"
        ).scale_to_fit_width(7.5).to_edge(UP, buff=1.1)
        self.play(Write(title))

        # Izgara Ayarları
        step_x = 1.0
        step_y = 1.2
        
        # Satır 1: 67
        num1_7 = MathTex("7").scale(1.8).move_to(RIGHT * step_x * 0.5 + UP * step_y * 2)
        num1_6 = MathTex("6").scale(1.8).move_to(LEFT * step_x * 0.5 + UP * step_y * 2)
        
        # Satır 2: x 89
        num2_9 = MathTex("9").scale(1.8).move_to(RIGHT * step_x * 0.5 + UP * step_y * 1)
        num2_8 = MathTex("8").scale(1.8).move_to(LEFT * step_x * 0.5 + UP * step_y * 1)
        sym_mul = MathTex("\\times").scale(1.8).move_to(LEFT * step_x * 1.5 + UP * step_y * 1)
        
        line1 = Line(LEFT * step_x * 2.2, RIGHT * step_x * 1.2).move_to(UP * step_y * 0.4)
        
        # Satır 3: 603
        res1_3 = MathTex("3").scale(1.8).move_to(RIGHT * step_x * 0.5 + UP * step_y * 0)
        res1_0 = MathTex("0").scale(1.8).move_to(LEFT * step_x * 0.5 + UP * step_y * 0)
        res1_6 = MathTex("6").scale(1.8).move_to(LEFT * step_x * 1.5 + UP * step_y * 0)
        
        # Satır 4: + 536
        res2_6 = MathTex("6").scale(1.8).move_to(LEFT * step_x * 0.5 + UP * step_y * -1)
        res2_3 = MathTex("3").scale(1.8).move_to(LEFT * step_x * 1.5 + UP * step_y * -1)
        res2_5 = MathTex("5").scale(1.8).move_to(LEFT * step_x * 2.5 + UP * step_y * -1)
        sym_add = MathTex("+").scale(1.8).move_to(LEFT * step_x * 3.5 + UP * step_y * -1)
        
        line2 = Line(LEFT * step_x * 4.2, RIGHT * step_x * 1.2).move_to(UP * step_y * -1.6)
        
        # Satır 5: 5963
        fin_3 = MathTex("3").scale(1.8).move_to(RIGHT * step_x * 0.5 + UP * step_y * -2)
        fin_6 = MathTex("6").scale(1.8).move_to(LEFT * step_x * 0.5 + UP * step_y * -2)
        fin_9 = MathTex("9").scale(1.8).move_to(LEFT * step_x * 1.5 + UP * step_y * -2)
        fin_5 = MathTex("5").scale(1.8).move_to(LEFT * step_x * 2.5 + UP * step_y * -2)
        
        # Eldeler
        carry1 = MathTex("+6").scale(0.9).set_color(YELLOW).next_to(num1_6, UP, buff=0.2).shift(RIGHT * 0.2)
        carry2 = MathTex("+5").scale(0.9).set_color(ORANGE).next_to(num1_6, UP, buff=0.8).shift(RIGHT * 0.2)
        
        # 3. DİKEY EKOSİSTEM: İşlem Grubunu Sabitleme
        math_group = VGroup(
            num1_7, num1_6, num2_9, num2_8, sym_mul, line1,
            res1_3, res1_0, res1_6,
            res2_6, res2_3, res2_5, sym_add, line2,
            fin_3, fin_6, fin_9, fin_5,
            carry1, carry2
        )
        math_group.move_to(UP * 1.5)
        
        # Animasyonlar Başlıyor
        self.play(
            Write(num1_6), Write(num1_7),
            Write(num2_8), Write(num2_9),
            Write(sym_mul), Create(line1)
        )
        self.wait(0.5)

        # Adım 1: 9 x 67
        self.play(num2_9.animate.set_color(YELLOW), num1_7.animate.set_color(YELLOW))
        self.play(Write(res1_3))
        self.play(Write(carry1))
        self.play(num1_7.animate.set_color(WHITE))
        
        self.play(num1_6.animate.set_color(YELLOW))
        self.play(Write(res1_0), Write(res1_6))
        self.play(carry1.animate.set_opacity(0.3), num2_9.animate.set_color(WHITE), num1_6.animate.set_color(WHITE))
        self.wait(0.5)

        # Adım 2: 8 x 67
        self.play(num2_8.animate.set_color(ORANGE), num1_7.animate.set_color(ORANGE))
        self.play(Write(res2_6))
        self.play(Write(carry2))
        self.play(num1_7.animate.set_color(WHITE))
        
        self.play(num1_6.animate.set_color(ORANGE))
        self.play(Write(res2_3), Write(res2_5))
        self.play(carry2.animate.set_opacity(0.3), num2_8.animate.set_color(WHITE), num1_6.animate.set_color(WHITE))
        self.wait(0.5)

        # Adım 3: Toplama İşlemi
        self.play(Write(sym_add), Create(line2))
        self.play(Write(fin_3))
        self.play(Write(fin_6))
        self.play(Write(fin_9))
        self.play(Write(fin_5))
        
        self.wait(0.5)
        
        # Sonucu Vurgulama
        final_result = VGroup(fin_5, fin_9, fin_6, fin_3)
        box = SurroundingRectangle(final_result, color=GREEN, buff=0.2)
        self.play(Create(box))
        self.play(final_result.animate.set_color(GREEN))
        
        self.wait(2)
