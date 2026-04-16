from manim import *
import numpy as np

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi (Beyaz)
        self.camera.background_color = "#FFFFFF"
        
        # Ana merkez noktasi
        main_center = DOWN * 0.5

        # Baslik
        title = Text("Kesirler: Pay ve Payda", font="Sans", color="#333333")
        title.to_edge(UP, buff=0.7)
        self.play(Write(title))

        # Altyazi kutusu (Gorunmez referans alani)
        subtitle_box = Rectangle(width=10, height=1, fill_opacity=0, stroke_opacity=0)
        subtitle_box.to_edge(DOWN, buff=0.8)
        self.add(subtitle_box)

        # 1. Gorsel: 4 es parcaya bolunmus sekil (3'u boyali)
        squares = VGroup(*[Square(side_length=1, color="#333333") for _ in range(4)])
        squares.arrange(RIGHT, buff=0)
        
        for i in range(3):
            squares[i].set_fill("#2ECC71", opacity=0.8)
        squares[3].set_fill("#FFFFFF", opacity=1)

        # 2. Kesir Ifadesi
        num = Text("3", font="Sans", color="#2ECC71")
        frac_line = Line(LEFT, RIGHT, color="#333333").scale(0.5)
        den = Text("4", font="Sans", color="#E74C3C")
        
        fraction = VGroup(num, frac_line, den).arrange(DOWN, buff=0.2)
        
        # Etiketler
        pay_label = Text("Pay (Alinan Parca)", font="Sans", color="#2ECC71", font_size=24)
        pay_label.next_to(num, RIGHT, buff=0.5)
        pay_arrow = Arrow(pay_label.get_left(), num.get_right(), buff=0.1, color="#2ECC71")
        
        payda_label = Text("Payda (Toplam Parca)", font="Sans", color="#E74C3C", font_size=24)
        payda_label.next_to(den, RIGHT, buff=0.5)
        payda_arrow = Arrow(payda_label.get_left(), den.get_right(), buff=0.1, color="#E74C3C")

        cizgi_label = Text("Kesir Cizgisi", font="Sans", color="#333333", font_size=24)
        cizgi_label.next_to(frac_line, LEFT, buff=0.5)
        cizgi_arrow = Arrow(cizgi_label.get_right(), frac_line.get_left(), buff=0.1, color="#333333")

        fraction_group = VGroup(fraction, pay_label, pay_arrow, payda_label, payda_arrow, cizgi_label, cizgi_arrow)

        # 3. Okunuslar
        read_1 = Text("1. Okunus (a bolu b): Uc bolu dort", font="Sans", color="#333333", font_size=28)
        read_2 = Text("2. Okunus (b'de a): Dortte uc", font="Sans", color="#87CEEB", font_size=28)
        readings = VGroup(read_1, read_2).arrange(DOWN, buff=0.3)

        # Duzen ve Konumlandirma
        top_group = VGroup(squares, fraction_group).arrange(RIGHT, buff=1.5)
        all_content = VGroup(top_group, readings).arrange(DOWN, buff=1)
        
        # Tum objeleri main_center'a kilitleme
        all_content.move_to(main_center)

        # Animasyonlar
        self.play(FadeIn(squares), run_time=2)
        self.wait(1)
        
        self.play(Write(fraction), run_time=2)
        self.wait(1)

        self.play(Write(payda_label), GrowArrow(payda_arrow))
        self.wait(1)
        
        self.play(Write(pay_label), GrowArrow(pay_arrow))
        self.wait(1)

        self.play(Write(cizgi_label), GrowArrow(cizgi_arrow))
        self.wait(2)

        self.play(Write(read_1))
        self.wait(1)
        
        self.play(Write(read_2))
        self.wait(2)
