from manim import *

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class MultiplicationShorts(Scene):
    def construct(self):
        self.camera.frame_width = 9
        self.camera.frame_height = 16
        self.camera.background_color = "#000000"
        
        # Başlık
        header = Text("İKİ BASAMAKLI ÇARPMA", color="#00FFFF", weight=BOLD).scale(1.1)
        header.to_edge(UP, buff=1.1)
        self.play(Write(header))
        
        # Izgara Ayarları
        dx = 0.9
        dy = 1.2
        
        def make_digit(char, col, row, color="#FFFFFF"):
            d = MathTex(char, color=color).scale(2)
            d.move_to(RIGHT * col * dx + DOWN * row * dy)
            return d

        # Sayılar (Sütunlar sağdan sola: 3=Birler, 2=Onlar, 1=Yüzler, 0=Binler)
        d6 = make_digit("6", 2, 0)
        d7 = make_digit("7", 3, 0)
        d8 = make_digit("8", 2, 1)
        d9 = make_digit("9", 3, 1)
        
        times = MathTex("\\times", color="#FFFF00").scale(1.5).move_to(RIGHT * 1 * dx + DOWN * 1 * dy)
        line1 = Line(RIGHT * 0.5 * dx + DOWN * 1.5 * dy, RIGHT * 3.5 * dx + DOWN * 1.5 * dy, color="#FFFFFF")
        
        # İlk Çarpım (9 x 67 = 603)
        r1_6 = make_digit("6", 1, 2, "#00FFFF")
        r1_0 = make_digit("0", 2, 2, "#00FFFF")
        r1_3 = make_digit("3", 3, 2, "#00FFFF")
        
        # İkinci Çarpım (8 x 67 = 536)
        r2_5 = make_digit("5", 0, 3, "#FFFF00")
        r2_3 = make_digit("3", 1, 3, "#FFFF00")
        r2_6 = make_digit("6", 2, 3, "#FFFF00")
        
        plus = MathTex("+", color="#FFFFFF").scale(1.5).move_to(RIGHT * -0.5 * dx + DOWN * 3 * dy)
        line2 = Line(RIGHT * -0.5 * dx + DOWN * 3.5 * dy, RIGHT * 3.5 * dx + DOWN * 3.5 * dy, color="#FFFFFF")
        
        # Toplam (5963)
        f_5 = make_digit("5", 0, 4)
        f_9 = make_digit("9", 1, 4)
        f_6 = make_digit("6", 2, 4)
        f_3 = make_digit("3", 3, 4)
        
        # Eldeler
        c_6 = MathTex("+6", color="#00FFFF").scale(1.2).next_to(d6, UP, buff=0.3)
        c_5 = MathTex("+5", color="#FFFF00").scale(1.2).next_to(d6, UP, buff=0.3)

        # Tüm matematiksel ifadeleri grupla ve konumlandır
        math_group = VGroup(
            d6, d7, d8, d9, times, line1,
            r1_6, r1_0, r1_3,
            r2_5, r2_3, r2_6, plus, line2,
            f_5, f_9, f_6, f_3,
            c_6, c_5
        )
        math_group.move_to(UP * 1.5)
        
        # Açıklama Metni Yardımcısı
        def get_exp(text_str, color="#FFFFFF"):
            return Text(text_str, color=color, weight=BOLD).scale(0.65).move_to(DOWN * 4.0)

        # Başlangıç Görünümü
        self.play(Write(d6), Write(d7), Write(d8), Write(d9), Write(times), Create(line1))
        self.wait(0.5)
        
        # Adım 1: 9 x 67
        exp_text = get_exp("Önce 9 ile 67'yi çarpıyoruz.")
        self.play(Write(exp_text))
        self.wait(0.5)
        
        # 9 x 7
        self.play(d9.animate.set_color("#00FFFF"), d7.animate.set_color("#00FFFF"))
        new_exp = get_exp("9 x 7 = 63 (Elde var 6)")
        self.play(Transform(exp_text, new_exp))
        self.play(Write(r1_3))
        self.play(Write(c_6))
        self.wait(0.5)
        self.play(d7.animate.set_color("#FFFFFF"))
        
        # 9 x 6
        self.play(d6.animate.set_color("#00FFFF"))
        new_exp = get_exp("9 x 6 = 54, 6 da elde = 60")
        self.play(Transform(exp_text, new_exp))
        self.play(Write(r1_0), Write(r1_6))
        self.play(FadeOut(c_6))
        self.wait(0.5)
        self.play(d9.animate.set_color("#FFFFFF"), d6.animate.set_color("#FFFFFF"))
        
        # Adım 2: 8 x 67
        new_exp = get_exp("Şimdi 8 ile 67'yi çarpıyoruz.")
        self.play(Transform(exp_text, new_exp))
        self.wait(0.5)
        
        # 8 x 7
        self.play(d8.animate.set_color("#FFFF00"), d7.animate.set_color("#FFFF00"))
        new_exp = get_exp("8 x 7 = 56 (Elde var 5)")
        self.play(Transform(exp_text, new_exp))
        self.play(Write(r2_6))
        self.play(Write(c_5))
        self.wait(0.5)
        self.play(d7.animate.set_color("#FFFFFF"))
        
        # 8 x 6
        self.play(d6.animate.set_color("#FFFF00"))
        new_exp = get_exp("8 x 6 = 48, 5 de elde = 53")
        self.play(Transform(exp_text, new_exp))
        self.play(Write(r2_3), Write(r2_5))
        self.play(FadeOut(c_5))
        self.wait(0.5)
        self.play(d8.animate.set_color("#FFFFFF"), d6.animate.set_color("#FFFFFF"))
        
        # Adım 3: Toplama
        new_exp = get_exp("Sonuçları topluyoruz.")
        self.play(Transform(exp_text, new_exp))
        self.play(Write(plus), Create(line2))
        self.wait(0.5)
        
        self.play(Write(f_3))
        self.wait(0.2)
        self.play(Write(f_6))
        self.wait(0.2)
        self.play(Write(f_9))
        self.wait(0.2)
        self.play(Write(f_5))
        
        new_exp = get_exp("İşlem tamamlandı: 5963", color="#00FFFF")
        self.play(Transform(exp_text, new_exp))
        
        # Son Bekleme
        self.wait(3)
