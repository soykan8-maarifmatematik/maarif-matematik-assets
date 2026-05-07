from manim import *

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#000000"
        
        # Başlık
        header = VGroup(
            Text("İKİ BASAMAKLI SAYILARLA", weight=BOLD, color="#FFFFFF"),
            Text("ÇARPMA İŞLEMİ", weight=BOLD, color="#FFFFFF")
        ).arrange(DOWN, buff=0.2).scale_to_fit_width(7.5).to_edge(UP, buff=1.2)

        # Çarpanlar ve İşaretler
        n67 = MathTex("6", "7", color="#FFFFFF").scale(1.5)
        n89 = MathTex("8", "9", color="#FFFFFF").scale(1.5)
        sign = MathTex("\\times", color="#FFFFFF").scale(1.2)
        
        n67.move_to(UP * 1.5 + RIGHT * 0.5)
        n89.next_to(n67, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign.next_to(n89, LEFT, buff=0.8)
        
        line1 = Line(sign.get_left(), n89.get_right(), color="#FFFFFF").scale(1.1)
        line1.next_to(n89, DOWN, buff=0.2)
        
        # Eldeler
        carry_6 = MathTex("+6", color="#FFFF00").scale(0.8).next_to(n67[0], UP, buff=0.3)
        carry_5 = MathTex("+5", color="#00FFFF").scale(0.8).next_to(n67[0], UP, buff=0.3)

        # 1. Çarpım Sonucu (603)
        res1 = MathTex("6", "0", "3", color="#FFFFFF").scale(1.5)
        res1.next_to(line1, DOWN, buff=0.3)
        res1.align_to(n89, RIGHT)

        # 2. Çarpım Sonucu (536) - Sola kaydırılmış
        res2 = MathTex("5", "3", "6", color="#FFFFFF").scale(1.5)
        res2.next_to(res1, DOWN, buff=0.3)
        res2.align_to(res1[1], RIGHT)
        
        # Toplama İşareti ve Çizgisi
        plus_sign = MathTex("+", color="#FFFFFF").scale(1.2)
        plus_sign.next_to(res2, LEFT, buff=0.5)

        line2 = Line(plus_sign.get_left(), res1.get_right(), color="#FFFFFF").scale(1.1)
        line2.next_to(res2, DOWN, buff=0.2)

        # Final Sonucu (5963)
        final_res = MathTex("5", "9", "6", "3", color="#FFFF00").scale(1.7)
        final_res.next_to(line2, DOWN, buff=0.3)
        final_res.align_to(res1, RIGHT)

        # Açıklama Metni
        desc = VGroup(
            Text("Eldeleri eklemeyi ve ikinci satırı", color="#FFFFFF"),
            Text("sola kaydırmayı unutma!", color="#FFFFFF")
        ).arrange(DOWN, buff=0.2).scale_to_fit_width(7.5).move_to(DOWN * 4.5)

        # ANİMASYON AKIŞI
        self.play(Write(header))
        self.wait(0.5)
        self.play(Write(n67), Write(n89), Write(sign))
        self.play(Create(line1))
        self.wait(1)

        # Adım 1: 9 * 7 = 63
        self.play(n89[1].animate.set_color("#FFFF00"), n67[1].animate.set_color("#FFFF00"))
        self.play(Write(res1[2]))
        self.play(Write(carry_6))
        self.wait(0.5)
        self.play(n67[1].animate.set_color("#FFFFFF"))

        # Adım 2: 9 * 6 = 54 + 6 = 60
        self.play(n67[0].animate.set_color("#FFFF00"))
        self.play(Write(res1[0:2]))
        self.play(FadeOut(carry_6))
        self.wait(0.5)
        self.play(n67[0].animate.set_color("#FFFFFF"), n89[1].animate.set_color("#FFFFFF"))

        # Adım 3: 8 * 7 = 56
        self.play(n89[0].animate.set_color("#00FFFF"), n67[1].animate.set_color("#00FFFF"))
        self.play(Write(res2[2]))
        self.play(Write(carry_5))
        self.wait(0.5)
        self.play(n67[1].animate.set_color("#FFFFFF"))

        # Adım 4: 8 * 6 = 48 + 5 = 53
        self.play(n67[0].animate.set_color("#00FFFF"))
        self.play(Write(res2[0:2]))
        self.play(FadeOut(carry_5))
        self.wait(0.5)
        self.play(n67[0].animate.set_color("#FFFFFF"), n89[0].animate.set_color("#FFFFFF"))

        # Adım 5: Toplama İşlemi
        self.play(Write(plus_sign), Create(line2))
        self.wait(0.5)
        self.play(Write(final_res))
        self.wait(0.5)
        self.play(Write(desc))
        
        self.wait(3)