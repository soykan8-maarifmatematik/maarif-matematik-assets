from manim import *
import numpy as np

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi
        self.camera.background_color = "#FFFFFF"
        
        # Merkez konumlandirmasi
        main_center = DOWN * 0.5
        
        # Baslik
        title = Text("Kesir Nedir?", color="#333333", font_size=48, weight=BOLD)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title))
        
        # Kesir bilesenleri
        pay = Text("3", color="#333333", font_size=72)
        line = Line(LEFT, RIGHT, color="#333333").scale(0.6)
        payda = Text("4", color="#333333", font_size=72)
        
        fraction = VGroup(pay, line, payda).arrange(DOWN, buff=0.3)
        fraction.move_to(main_center)
        
        self.play(Write(fraction))
        self.wait(1)
        
        # Pay ve Payda etiketleri
        payda_text = Text("Payda", color="#87CEEB", font_size=36, weight=BOLD)
        payda_text.next_to(payda, LEFT, buff=1.5)
        payda_arrow = Arrow(payda_text.get_right(), payda.get_left(), color="#333333", buff=0.2)
        
        self.play(Write(payda_text), GrowArrow(payda_arrow))
        self.wait(1)
        
        pay_text = Text("Pay", color="#87CEEB", font_size=36, weight=BOLD)
        pay_text.next_to(pay, LEFT, buff=1.5)
        pay_arrow = Arrow(pay_text.get_right(), pay.get_left(), color="#333333", buff=0.2)
        
        self.play(Write(pay_text), GrowArrow(pay_arrow))
        self.wait(1)
        
        # Okunuslar
        read_group = VGroup()
        read1 = Text("a bölü b: 3 bölü 4", color="#333333", font_size=32)
        read2 = Text("b'de a: 4'te 3", color="#333333", font_size=32)
        read_group.add(read1, read2).arrange(DOWN, buff=0.6)
        read_group.next_to(fraction, RIGHT, buff=1.5)
        
        self.play(Write(read1))
        self.wait(1)
        self.play(Write(read2))
        self.wait(3)
        
        # Ekrani temizleme
        self.play(FadeOut(Group(title, fraction, pay_text, pay_arrow, payda_text, payda_arrow, read_group)))
