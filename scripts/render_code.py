from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        # Başlık (Text komutu Türkçe karakterler için daha güvenlidir)
        title = Text("Kesirlerin Mantığı", color=BLACK).scale(0.8).to_edge(UP)
        self.play(Write(title))

        # Kesir Bileşenleri
        line = Line(LEFT, RIGHT, color=BLACK).scale(0.8)
        num = MathTex("3", color="#1976D2").scale(1.5).next_to(line, UP, buff=0.3)
        den = MathTex("4", color="#D32F2F").scale(1.5).next_to(line, DOWN, buff=0.3)
        fraction = VGroup(num, line, den)

        # Etiketler
        num_label = Text("Pay (Alınan Parça)", color="#1976D2", font_size=24).next_to(num, RIGHT, buff=0.5)
        den_label = Text("Payda (Bütün Parçalar)", color="#D32F2F", font_size=24).next_to(den, RIGHT, buff=0.5)
        
        # Gruplama ve Merkezleme
        read_1 = Text("- Üç bölü dört", color=BLACK, font_size=28)
        read_2 = Text("- Dörtte üç", color=BLACK, font_size=28)
        readings = VGroup(read_1, read_2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        main_group = VGroup(VGroup(fraction, num_label, den_label), readings).arrange(DOWN, buff=1)
        main_group.move_to(main_center)

        # Animasyon Akışı
        self.play(Create(line))
        self.play(Write(den), FadeIn(den_label))
        self.wait(1)
        self.play(Write(num), FadeIn(num_label))
        self.wait(1)
        self.play(Write(readings))
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))
