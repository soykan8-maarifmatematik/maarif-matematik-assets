from manim import *

class BirimKesirler(Scene):
    def construct(self):
        # BAŞLIK STİLİ KURALI
        title = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", weight=BOLD).scale_to_fit_width(7.0).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        # KESİR FORMATI KURALI (Daima 1/n)
        frac1 = MathTex(r"\frac{1}{3}").scale(2.5)
        frac2 = MathTex(r"\frac{1}{6}").scale(2.5)
        
        # Modelleri oluşturan fonksiyon
        def create_pie(denominator, color):
            pie = VGroup()
            for i in range(denominator):
                sector = Sector(
                    outer_radius=1.2, 
                    angle=TAU/denominator, 
                    start_angle=i*TAU/denominator, 
                    color=WHITE, 
                    stroke_width=2
                )
                if i == 0:
                    sector.set_fill(color, opacity=0.9)
                else:
                    sector.set_fill(DARK_GRAY, opacity=0.4)
                pie.add(sector)
            return pie
            
        model1 = create_pie(3, BLUE)
        model2 = create_pie(6, RED)
        
        # KESİR VE MODEL GRUPLAMA KURALI
        left_group = VGroup(frac1, model1).arrange(DOWN, buff=0.8)
        right_group = VGroup(frac2, model2).arrange(DOWN, buff=0.8)
        
        # SİMETRİK YERLEŞTİRME KURALI
        left_group.move_to(LEFT * 3.5)
        right_group.move_to(RIGHT * 3.5)
        
        # İŞARET KONUMU KURALI (DAİMA ORIGIN)
        sign = MathTex(">").scale(3.5).move_to(ORIGIN)
        
        # Animasyonlar
        self.play(FadeIn(left_group, shift=RIGHT))
        self.wait(1)
        self.play(FadeIn(right_group, shift=LEFT))
        self.wait(1)
        
        # Dilimlerin büyüklüğünü vurgulama
        self.play(Indicate(model1[0], color=YELLOW, scale_factor=1.1))
        self.play(Indicate(model2[0], color=YELLOW, scale_factor=1.1))
        self.wait(1)
        
        # İşaretin belirmesi
        self.play(GrowFromCenter(sign))
        self.wait(1)
        
        # Sonuç metni
        conclusion = Text("Payda küçüldükçe, dilim BÜYÜR!", color=YELLOW).scale(0.8).to_edge(DOWN, buff=0.5)
        self.play(Write(conclusion))
        self.wait(2)