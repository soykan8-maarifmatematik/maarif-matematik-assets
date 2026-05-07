from manim import *
config.pixel_height, config.pixel_width = 1920, 1080

class Multiplication(Scene):
    def construct(self):
        self.camera.frame_width = 9
        self.camera.frame_height = 16
        
        # Başlık
        title = Text("İki Basamaklı Sayılarla Çarpma", font_size=48, weight=BOLD, color=YELLOW)
        title.to_edge(UP, buff=0.8)
        self.play(Write(title))
        
        # Koordinat ve Grid Ayarları (Orta-Üst UP * 1.2 civarına merkezlenmiş)
        y_r1 = 3.5
        y_r2 = 2.5
        y_l1 = 1.9
        y_r3 = 1.1
        y_r4 = 0.1
        y_l2 = -0.6
        y_r5 = -1.4
        
        step_x = 0.8
        x0 = 1.2  # Birler basamağı
        x1 = x0 - step_x  # Onlar basamağı
        x2 = x0 - 2 * step_x  # Yüzler basamağı
        x3 = x0 - 3 * step_x  # Binler basamağı
        x4 = x0 - 4 * step_x  # İşaret konumu
        
        # 67 ve 89 Sayıları
        d7_top = MathTex("7", font_size=80).move_to(RIGHT * x0 + UP * y_r1)
        d6_top = MathTex("6", font_size=80).move_to(RIGHT * x1 + UP * y_r1)
        
        d9_bot = MathTex("9", font_size=80).move_to(RIGHT * x0 + UP * y_r2)
        d8_bot = MathTex("8", font_size=80).move_to(RIGHT * x1 + UP * y_r2)
        mul_sign = MathTex("\\times", font_size=80).move_to(RIGHT * x2 + UP * y_r2)
        
        line1 = Line(RIGHT * (x2 - 0.5) + UP * y_l1, RIGHT * (x0 + 0.5) + UP * y_l1, stroke_width=4)
        
        # Başlangıç animasyonu
        self.play(Write(d6_top), Write(d7_top))
        self.play(Write(d8_bot), Write(d9_bot), Write(mul_sign), Create(line1))
        self.wait(0.5)
        
        # Adım 1: 9 x 67
        res1_3 = MathTex("3", font_size=80).move_to(RIGHT * x0 + UP * y_r3)
        res1_0 = MathTex("0", font_size=80).move_to(RIGHT * x1 + UP * y_r3)
        res1_6 = MathTex("6", font_size=80).move_to(RIGHT * x2 + UP * y_r3)
        carry6 = MathTex("+6", font_size=40, color=RED).move_to(RIGHT * x1 + UP * (y_r1 + 0.8))
        
        # 9 x 7
        self.play(d9_bot.animate.set_color(YELLOW), d7_top.animate.set_color(YELLOW))
        self.play(Write(res1_3), Write(carry6))
        self.play(d7_top.animate.set_color(WHITE))
        
        # 9 x 6
        self.play(d6_top.animate.set_color(YELLOW))
        self.play(Indicate(carry6, color=RED, scale_factor=1.3))
        self.play(Write(res1_0), Write(res1_6))
        self.play(d9_bot.animate.set_color(WHITE), d6_top.animate.set_color(WHITE), FadeOut(carry6))
        self.wait(0.5)
        
        # Adım 2: 8 x 67
        res2_6 = MathTex("6", font_size=80).move_to(RIGHT * x1 + UP * y_r4)
        res2_3 = MathTex("3", font_size=80).move_to(RIGHT * x2 + UP * y_r4)
        res2_5 = MathTex("5", font_size=80).move_to(RIGHT * x3 + UP * y_r4)
        carry5 = MathTex("+5", font_size=40, color=ORANGE).move_to(RIGHT * x1 + UP * (y_r1 + 0.8))
        
        # 8 x 7
        self.play(d8_bot.animate.set_color(GREEN), d7_top.animate.set_color(GREEN))
        self.play(Write(res2_6), Write(carry5))
        self.play(d7_top.animate.set_color(WHITE))
        
        # 8 x 6
        self.play(d6_top.animate.set_color(GREEN))
        self.play(Indicate(carry5, color=ORANGE, scale_factor=1.3))
        self.play(Write(res2_3), Write(res2_5))
        self.play(d8_bot.animate.set_color(WHITE), d6_top.animate.set_color(WHITE), FadeOut(carry5))
        self.wait(0.5)
        
        # Adım 3: Toplama İşlemi
        plus_sign = MathTex("+", font_size=80).move_to(RIGHT * x4 + UP * y_r4)
        line2 = Line(RIGHT * (x4 - 0.5) + UP * y_l2, RIGHT * (x0 + 0.5) + UP * y_l2, stroke_width=4)
        
        self.play(Write(plus_sign), Create(line2))
        self.wait(0.5)
        
        fin_3 = MathTex("3", font_size=80).move_to(RIGHT * x0 + UP * y_r5)
        fin_6 = MathTex("6", font_size=80).move_to(RIGHT * x1 + UP * y_r5)
        fin_9 = MathTex("9", font_size=80).move_to(RIGHT * x2 + UP * y_r5)
        fin_5 = MathTex("5", font_size=80).move_to(RIGHT * x3 + UP * y_r5)
        
        self.play(Write(fin_3))
        self.play(Write(fin_6))
        self.play(Write(fin_9))
        self.play(Write(fin_5))
        self.wait(0.5)
        
        # Sonucu Vurgulama
        final_box = SurroundingRectangle(VGroup(fin_5, fin_9, fin_6, fin_3), color=YELLOW, buff=0.2)
        self.play(Create(final_box))
        self.wait(1)
        
        # Alt Açıklama Metni (DOWN * 3.5)
        desc = Text("Çarpma işleminde eldeleri unutma!\nİkinci satıra geçerken bir basamak\nsola kaydırmayı hatırla.", font_size=36, text_alignment=CENTER)
        desc.move_to(DOWN * 3.5)
        self.play(Write(desc))
        self.wait(2)