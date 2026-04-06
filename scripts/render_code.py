from manim import *

config.background_color = WHITE

class KesirlerinMantigi(Scene):
    def construct(self):
        def get_text(text, color=DARK_GRAY, size=36, font="Montserrat"):
            return Text(text, color=color, font_size=size, font=font)

        # Giriş
        title = get_text("Kesirlerin Mantığı", color=BLUE, size=48)
        self.play(Write(title, run_time=2))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Şekil Çizimi (Bütün ve Parçalar)
        whole = Rectangle(width=6, height=1.5, color=DARK_GRAY)
        self.play(Create(whole, run_time=1.5))
        self.wait(0.5)

        lines = VGroup(
            Line(whole.get_corner(UL) + RIGHT*1.5, whole.get_corner(DL) + RIGHT*1.5, color=DARK_GRAY),
            Line(whole.get_corner(UL) + RIGHT*3.0, whole.get_corner(DL) + RIGHT*3.0, color=DARK_GRAY),
            Line(whole.get_corner(UL) + RIGHT*4.5, whole.get_corner(DL) + RIGHT*4.5, color=DARK_GRAY)
        )
        self.play(Create(lines, run_time=1.5))
        self.wait(0.5)

        # 3 Parçayı Vurgulama
        part1 = Rectangle(width=1.5, height=1.5, color=BLUE).set_fill(BLUE, opacity=0.6).move_to(whole.get_left() + RIGHT*0.75)
        part2 = Rectangle(width=1.5, height=1.5, color=BLUE).set_fill(BLUE, opacity=0.6).move_to(whole.get_left() + RIGHT*2.25)
        part3 = Rectangle(width=1.5, height=1.5, color=BLUE).set_fill(BLUE, opacity=0.6).move_to(whole.get_left() + RIGHT*3.75)
        
        self.play(FadeIn(part1, part2, part3, run_time=2))
        self.wait(1)

        # Kesir Gösterimi
        fraction = MathTex(r"\frac{3}{4}", color=GREEN, font_size=80)
        fraction.next_to(whole, DOWN, buff=1)
        self.play(Write(fraction, run_time=1.5))
        self.wait(1)

        # Okunuş Kuralları
        read1 = get_text("\"Dörtte üç\"\n(Parça-Bütün)", size=24).next_to(fraction, LEFT, buff=1)
        read2 = get_text("\"Üç bölü dört\"\n(İşlem)", size=24).next_to(fraction, RIGHT, buff=1)
        
        self.play(Write(read1, run_time=1.5))
        self.wait(1)
        self.play(Write(read2, run_time=1.5))
        self.wait(3)

        # Temizlik ve Uyarı
        self.play(FadeOut(whole, lines, part1, part2, part3, fraction, read1, read2))
        
        warning_title = get_text("Önemli Yazım Uyarısı", color=RED, size=40)
        warning_title.next_to(title, DOWN, buff=1)
        self.play(Write(warning_title, run_time=1.5))
        self.wait(1)

        rule1 = get_text("Okunuş: Dörtte biri  ->  Yazılış: 1/4'i", size=32)
        rule2 = get_text("Okunuş: Bir bölü dördü  ->  Yazılış: 1/4'ü", size=32)
        
        rules = VGroup(rule1, rule2).arrange(DOWN, buff=0.8)
        self.play(Write(rules, run_time=2))
        self.wait(3)

        # Kapanış
        self.play(FadeOut(rules, warning_title, title))
        outro = get_text("Maarif Matematik", color=BLUE, size=48)
        self.play(Write(outro, run_time=2))
        self.wait(2)