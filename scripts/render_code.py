from manim import *

config.pixel_height=1920
config.pixel_width=1080
config.frame_height=14.22
config.frame_width=8.0

class MaarifScene(Scene):
    def construct(self):
        # Objeleri oluşturma
        title = Text("BİRİM KESİRLER", font="DejaVu Sans", color=YELLOW)
        
        circle_half = VGroup(Circle(radius=2, color=WHITE), Sector(radius=2, angle=PI, color=BLUE, fill_opacity=0.8))
        frac_half = VGroup(MathTex(r"\frac{1}{2}").scale(2), circle_half).arrange(DOWN, buff=0.5)
        
        circle_quarter = VGroup(Circle(radius=2, color=WHITE), Sector(radius=2, angle=PI/2, color=RED, fill_opacity=0.8))
        frac_quarter = VGroup(MathTex(r"\frac{1}{4}").scale(2), circle_quarter).arrange(DOWN, buff=0.5)
        
        comparison = Text("1/2 > 1/4", font="DejaVu Sans", color=GREEN)
        
        # Hizalama ve Ölçeklendirme (Zırh Kuralları)
        main_group = VGroup(title, frac_half, frac_quarter, comparison).arrange(DOWN, buff=2.2)
        main_group.scale_to_fit_width(6.2)
        
        # Animasyonlar ve Milimetrik Senkronizasyon
        # Giriş: 5 kelime -> 1.67 saniye
        self.play(Write(title), run_time=1.0)
        self.wait(0.67)
        
        # Cümle 2 (6 kelime -> 2.0s) ve Cümle 3 (7 kelime -> 2.33s) Toplam: 4.33s
        self.wait(4.33)
        
        # Cümle 4: 7 kelime -> 2.33 saniye
        self.play(FadeIn(frac_half), run_time=1.0)
        self.wait(1.33)
        
        # Cümle 5: 7 kelime -> 2.33 saniye
        self.play(FadeIn(frac_quarter), run_time=1.0)
        self.wait(1.33)
        
        # Cümle 6: 7 kelime -> 2.33 saniye
        self.play(Write(comparison), run_time=1.0)
        self.wait(1.33)
        
        # Çıkış: 7 kelime -> 2.33 saniye
        self.wait(2.33)
        
        # Kapanış Sabitleme
        self.wait(5)
