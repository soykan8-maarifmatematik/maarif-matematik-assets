from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # 1. Başlık (Zırh kuralı: to_edge(UP, buff=0.8))
        title = Text("Birim Kesirler", font="DejaVu Sans", font_size=50, color=YELLOW).to_edge(UP, buff=0.8)
        self.play(Write(title))
        self.wait(0.66) # "Merhaba..." (5 kelime = 1.66s, 1s animasyon + 0.66s bekleme)
        
        self.wait(2.0) # "Birim kesirleri karşılaştırmak..." (6 kelime = 2.0s)

        # 2. Matematiksel Objeler
        # 1/2 Kesri Modeli
        circle1 = Circle(radius=1.2, color=WHITE)
        line1 = Line(circle1.get_top(), circle1.get_bottom())
        sector1 = Sector(radius=1.2, angle=PI, start_angle=PI/2, color=ORANGE, fill_opacity=0.7)
        label1 = MathTex(r"\frac{1}{2}", font_size=72)
        group1 = VGroup(circle1, line1, sector1)
        hgroup1 = VGroup(group1, label1).arrange(RIGHT, buff=1.0)

        # 1/4 Kesri Modeli
        circle2 = Circle(radius=1.2, color=WHITE)
        line2_v = Line(circle2.get_top(), circle2.get_bottom())
        line2_h = Line(circle2.get_left(), circle2.get_right())
        sector2 = Sector(radius=1.2, angle=PI/2, start_angle=PI/2, color=BLUE, fill_opacity=0.7)
        label2 = MathTex(r"\frac{1}{4}", font_size=72)
        group2 = VGroup(circle2, line2_v, line2_h, sector2)
        hgroup2 = VGroup(group2, label2).arrange(RIGHT, buff=1.0)

        # Zırh kuralı: İlk model KESİNLİKLE UP * 2.5 noktasından başlamalı
        hgroup1.move_to(UP * 2.5)
        # Zırh kuralı: arrange(DOWN, buff=2.0) mantığıyla ferah yerleşim
        hgroup2.next_to(hgroup1, DOWN, buff=2.0)

        # Animasyonlar ve Ses Senkronu
        self.play(Create(circle1), Create(circle2))
        self.wait(0.66) # "Aynı büyüklükte iki pizza..." (5 kelime = 1.66s)

        self.play(Create(line1), Create(line2_v), Create(line2_h))
        self.wait(1.33) # "İlkini iki dilime, ikincisini..." (7 kelime = 2.33s)

        self.play(FadeIn(sector1), FadeIn(sector2), Write(label1), Write(label2))
        self.wait(1.66) # "İki dilime bölünen pizzanın..." (8 kelime = 2.66s)

        # Sonuç Metni
        conclusion = Text("Payda büyüdükçe\ndeğer küçülür!", font="DejaVu Sans", font_size=42, color=GREEN_C)
        conclusion.next_to(hgroup2, DOWN, buff=1.5)
        self.play(Write(conclusion))

        # MUTLAK SENKRONİZASYON KURALI
        # Son cümle: "Yani payda büyüdükçe, birim kesrin değeri küçülür." (7 kelime)
        # Formül: (7 / 3.0) + 1.5 = 2.33 + 1.5 = 3.83 saniye
        self.wait(3.83)

        # Ekranı Temizleme
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Mühür (Çıkış)
        outro = Text("Maarif Matematik ile mantığını kavra,\ntakipte kal!", font="DejaVu Sans", font_size=38)
        self.play(Write(outro))
        self.wait(4.0)