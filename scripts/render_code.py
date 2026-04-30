from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        # BAŞLIK
        title = Text("BİRİM KESİRLER", color=BLACK, weight=BOLD).scale(1.2)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(2.6) # Birim kesirlerde payda büyüdükçe kesrin değeri küçülür.
        
        # MODELLER (shift(UP * 1.5) kuralına uygun yan yana yerleşim)
        circle_half = Circle(radius=1.5, color=BLACK, stroke_width=2)
        sector_half = Sector(radius=1.5, angle=PI, start_angle=PI/2, color=BLUE, fill_opacity=0.8, stroke_width=2)
        model_half = VGroup(circle_half, sector_half).shift(UP * 1.5 + LEFT * 2)
        
        circle_quarter = Circle(radius=1.5, color=BLACK, stroke_width=2)
        sector_quarter = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color=RED, fill_opacity=0.8, stroke_width=2)
        model_quarter = VGroup(circle_quarter, sector_quarter).shift(UP * 1.5 + RIGHT * 2)
        
        self.play(FadeIn(model_half), FadeIn(model_quarter))
        self.wait(3.6) # Mesela bir pastayı ikiye böldüğümüzde mi daha büyük bir dilim alırız,
        
        # KESİR SAYILARI (Modellerin hemen altına)
        frac_half = MathTex(r"\frac{1}{2}", color=BLACK).scale(1.5)
        frac_half.next_to(model_half, DOWN, buff=0.8)
        
        frac_quarter = MathTex(r"\frac{1}{4}", color=BLACK).scale(1.5)
        frac_quarter.next_to(model_quarter, DOWN, buff=0.8)
        
        self.play(Write(frac_half), Write(frac_quarter))
        self.wait(1.3) # yoksa dörde böldüğümüzde mi?
        
        # VURGU
        self.play(Indicate(sector_half, color=YELLOW, scale_factor=1.1))
        self.wait(1.3) # Tabii ki ikiye böldüğümüzde!
        
        # BÜYÜKTÜR İŞARETİ
        greater_sign = MathTex(">", color=BLACK).scale(2.0)
        greater_sign.move_to((frac_half.get_center() + frac_quarter.get_center()) / 2)
        self.play(Write(greater_sign))
        
        # ALT SONUÇ METNİ (YouTube UI'dan kaçmak için to_edge(DOWN, buff=4.5))
        bottom_text = Text("Payda büyüdükçe değer küçülür!", color=BLACK, weight=BOLD).scale(0.8)
        bottom_text.to_edge(DOWN, buff=4.5)
        self.play(Write(bottom_text))
        self.wait(3.0) # Yani 1 bölü 2, 1 bölü 4'ten daha büyüktür.
        
        self.wait(1.0)
