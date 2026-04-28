from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan beyaz
        self.camera.background_color = "#FFFFFF"

        # Başlık (Çentik güvenli alan)
        title = Text("Birim Kesirler", color=BLACK, weight=BOLD).scale(1.2)
        title.to_edge(UP, buff=2.8)
        self.play(Write(title))
        self.wait(1.5)

        # 1/2 Kesri
        c2 = Circle(radius=0.9, color=BLACK).move_to(UP * 1.5 + LEFT * 1.5)
        s2 = Sector(radius=0.9, angle=PI, color=RED, fill_opacity=0.8).move_to(c2.get_center())
        t2 = MathTex(r"\frac{1}{2}", color=BLACK).scale(1.5).next_to(c2, RIGHT, buff=1.5)
        
        self.play(Create(c2))
        self.play(Create(s2), Write(t2))
        self.wait(1.5)

        # 1/3 Kesri
        c3 = Circle(radius=0.9, color=BLACK).move_to(DOWN * 0.5 + LEFT * 1.5)
        s3 = Sector(radius=0.9, angle=2*PI/3, color=BLUE, fill_opacity=0.8).move_to(c3.get_center())
        t3 = MathTex(r"\frac{1}{3}", color=BLACK).scale(1.5).next_to(c3, RIGHT, buff=1.5)
        
        self.play(Create(c3))
        self.play(Create(s3), Write(t3))
        self.wait(1.5)

        # 1/4 Kesri
        c4 = Circle(radius=0.9, color=BLACK).move_to(DOWN * 2.5 + LEFT * 1.5)
        s4 = Sector(radius=0.9, angle=PI/2, color=GREEN, fill_opacity=0.8).move_to(c4.get_center())
        t4 = MathTex(r"\frac{1}{4}", color=BLACK).scale(1.5).next_to(c4, RIGHT, buff=1.5)
        
        self.play(Create(c4))
        self.play(Create(s4), Write(t4))
        self.wait(1.5)

        # Paydaları vurgulama
        self.play(
            Indicate(t2[0][2], color=RED, scale_factor=1.5),
            Indicate(t3[0][2], color=BLUE, scale_factor=1.5),
            Indicate(t4[0][2], color=GREEN, scale_factor=1.5)
        )
        self.wait(2.0)

        # Alt özet metni (Alt güvenli alan sınırı y = -4.2, biz -4.0 kullanıyoruz)
        summary = Text("Payda Buyurse Kesir Kuculur", color=BLACK, weight=BOLD).scale(0.65).move_to(DOWN * 4.0)
        self.play(Write(summary))
        
        # Kapanış beklemesi (11 kelime / 3.0 + 2 = ~5.6 saniye)
        self.wait(5.6)
