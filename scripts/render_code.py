from manim import *

class BirimKesirler(Scene):
    def construct(self):
        # Arka plan rengi (Kural 4)
        self.camera.background_color = "#FFFFFF"
        
        # Başlık (Kural 4: UP, buff=2.0 ve scale(1.2))
        title = Text("Birim Kesirler", font_size=48, weight=BOLD, color=BLACK)
        title.to_edge(UP, buff=2.0).scale(1.2)
        
        radius = 1.2
        
        # 1/2 Modeli (Kural 1: Önce bütün ve gri çizgiler, sonra boyalı kısım)
        circle_half = Circle(radius=radius, color=LIGHT_GRAY, stroke_width=4)
        line_half = Line(circle_half.get_top(), circle_half.get_bottom(), color=LIGHT_GRAY, stroke_width=4)
        sector_half = Sector(outer_radius=radius, angle=PI, start_angle=PI/2, color=BLUE, fill_opacity=0.8)
        label_half = MathTex(r"\frac{1}{2}", font_size=72, color=BLACK)
        
        # 1/4 Modeli (Kural 1: Görsel ispat için 4 parçayı ayıran çizgiler)
        circle_quarter = Circle(radius=radius, color=LIGHT_GRAY, stroke_width=4)
        line_q1 = Line(circle_quarter.get_top(), circle_quarter.get_bottom(), color=LIGHT_GRAY, stroke_width=4)
        line_q2 = Line(circle_quarter.get_left(), circle_quarter.get_right(), color=LIGHT_GRAY, stroke_width=4)
        sector_quarter = Sector(outer_radius=radius, angle=PI/2, start_angle=PI/2, color=RED, fill_opacity=0.8)
        label_quarter = MathTex(r"\frac{1}{4}", font_size=72, color=BLACK)
        
        # Gruplama ve Yerleşim (Kural 4: Merkezi yerleşim ve arrange(DOWN, buff=2.5))
        group_half = VGroup(VGroup(circle_half, line_half, sector_half), label_half).arrange(RIGHT, buff=1.0)
        group_quarter = VGroup(VGroup(circle_quarter, line_q1, line_q2, sector_quarter), label_quarter).arrange(RIGHT, buff=1.0)
        
        content_group = VGroup(group_half, group_quarter).arrange(DOWN, buff=2.5)
        content_group.shift(UP * 0.5) # Başlık ve alt sınır arasında dengelemek için
        
        # Animasyonlar ve Senkronizasyon (Kural 5: Saniyede 3.0 kelime)
        
        # 1. "Merhaba, Maarif Matematik’e hoş geldiniz." (5 kelime -> 1.67s)
        self.play(Write(title), run_time=1.0)
        self.wait(0.67)
        
        # 2. "Birim kesirlerde payda büyüdükçe kesir neden küçülür, hiç düşündünüz mü?" (10 kelime -> 3.33s)
        self.wait(3.33)
        
        # 3. "Bir pastayı ikiye böldüğünüzde alacağınız dilim..." (6 kelime -> 2.0s)
        self.play(Create(circle_half), Create(line_half), run_time=1.0)
        self.play(FadeIn(sector_half), Write(label_half), run_time=1.0)
        
        # 4. "...dörde böldüğünüzde alacağınız dilimden daha büyüktür." (6 kelime -> 2.0s)
        self.play(Create(circle_quarter), Create(line_q1), Create(line_q2), run_time=1.0)
        self.play(FadeIn(sector_quarter), Write(label_quarter), run_time=1.0)
        
        # 5. "Yani, payda büyüdükçe parça küçülür. 1 bölü 2 büyüktür 1 bölü 4'ten." (12 kelime -> 4.0s)
        final_eq = MathTex(r"\frac{1}{2} > \frac{1}{4}", font_size=80, color=BLACK)
        final_eq.move_to(DOWN * 4.0) # Kural 4: Alt sınır y = -4.5'ten yukarıda
        self.play(Write(final_eq), run_time=1.0)
        self.wait(3.0)
        
        # 6. "Maarif Matematik ile mantığını kavra, takipte kal!" (7 kelime -> 2.33s)
        self.wait(2.33)