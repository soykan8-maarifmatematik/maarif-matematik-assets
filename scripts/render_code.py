from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi (Maarif Laciverti)
        self.camera.background_color = "#002B4D"
        
        # Başlık ve Kanca
        title = Text("BİRİM KESİRLER", color="#FFD700", font_size=64).to_edge(UP, buff=1.0)
        hook = Text("1/3 mü büyük,\nyoksa 1/10 mu?", color="#FFFFFF", font_size=48, text_alignment=CENTER).next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title), run_time=1)
        self.play(Write(hook), run_time=1.5)
        self.wait(2.5) # Kanca süresi (Toplam 5 sn)
        
        self.play(FadeOut(hook), run_time=0.5)
        
        # 1/3 Kesri ve Görseli
        frac_1_3 = MathTex(r"\frac{1}{3}", font_size=96, color="#FFD700").move_to(UP * 2.5)
        pizza_1_3 = Circle(radius=1.5, color="#FFFFFF").next_to(frac_1_3, DOWN, buff=0.5)
        slice_1_3 = Sector(radius=1.5, angle=TAU/3, start_angle=PI/2, color="#D32F2F", fill_opacity=0.9).move_to(pizza_1_3.get_center())
        
        self.play(Write(frac_1_3), run_time=1)
        self.wait(2)
        
        self.play(Create(pizza_1_3), run_time=1)
        self.play(Create(slice_1_3), run_time=1)
        self.wait(5) # 3 arkadaş paylaşımı anlatımı
        
        # 1/10 Kesri ve Görseli
        frac_1_10 = MathTex(r"\frac{1}{10}", font_size=96, color="#FFD700").move_to(DOWN * 1.5)
        pizza_1_10 = Circle(radius=1.5, color="#FFFFFF").next_to(frac_1_10, DOWN, buff=0.5)
        slice_1_10 = Sector(radius=1.5, angle=TAU/10, start_angle=PI/2, color="#D32F2F", fill_opacity=0.9).move_to(pizza_1_10.get_center())
        
        self.play(Write(frac_1_10), run_time=1)
        self.play(Create(pizza_1_10), run_time=1)
        self.play(Create(slice_1_10), run_time=1)
        self.wait(4) # 10 arkadaş paylaşımı anlatımı
        
        # Kural Metni
        rule = Text("Payda büyürse,\ndilim küçülür!", color="#FFD700", font_size=56, text_alignment=CENTER).move_to(DOWN * 5.5)
        self.play(Write(rule), run_time=1)
        self.wait(6) # Kuralın açıklanması
        
        # Sonuç ve Kapanış
        self.play(
            FadeOut(pizza_1_3), FadeOut(slice_1_3), 
            FadeOut(pizza_1_10), FadeOut(slice_1_10), 
            FadeOut(rule), run_time=1
        )
        
        final_math = MathTex(r"\frac{1}{3} > \frac{1}{10}", font_size=144, color="#FFFFFF").move_to(CENTER)
        self.play(Transform(frac_1_3, final_math), FadeOut(frac_1_10), run_time=1)
        self.wait(3) # Son kural vurgusu
        
        cta = Text("Daha fazlası için\ntakip et!", color="#FFD700", font_size=56, text_alignment=CENTER).next_to(final_math, DOWN, buff=1.5)
        self.play(Write(cta), run_time=1)
        self.wait(4) # Kapanış beklemesi