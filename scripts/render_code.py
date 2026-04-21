from manim import *

class KesirMantigi(Scene):
    def construct(self):
        # Intro
        intro_text = Text("Maarif Matematik", font_size=54, color=BLUE)
        self.play(Write(intro_text), run_time=2)
        self.wait(2) # Merhaba, Maarif Matematik'e...
        self.play(FadeOut(intro_text))
        self.wait(6) # Bugün matematiğin en temel...
        self.wait(6) # Günlük hayatta bir bütünün...
        
        # Pizza (Bütün)
        pizza_group = VGroup()
        for i in range(4):
            # KESİN KURAL: outer_radius kullanılmadı, sadece radius kullanıldı.
            sector = Sector(radius=2.5, angle=PI/2, start_angle=i*PI/2, color=ORANGE, fill_opacity=0.4, stroke_width=3, stroke_color=WHITE)
            pizza_group.add(sector)
            
        self.play(Create(pizza_group), run_time=3)
        self.wait(4) # Örneğin, masanızda duran...
        
        # Dilimlere ayırma ve vurgulama
        self.play(pizza_group.animate.arrange_in_grid(rows=2, buff=0.1), run_time=2)
        self.wait(6) # Bu pizzayı tam ortadan...
        
        self.play(pizza_group[0].animate.set_fill(color=RED, opacity=0.9).shift(UP*0.2 + RIGHT*0.2), run_time=2)
        self.wait(6) # İçlerinden sadece bir dilimini...
        self.wait(5) # İşte bu durumu sayılarla...
        
        # Pizzayı sola kaydır, kesri sağa yaz
        self.play(pizza_group.animate.scale(0.5).to_edge(LEFT, buff=1.5), run_time=2)
        
        # Kesir Çizgisi
        frac_line = Line(LEFT, RIGHT, color=WHITE, stroke_width=6).scale(1.2).move_to(RIGHT*2)
        self.play(Create(frac_line), run_time=2)
        self.wait(5) # Ekranda beliren yatay çizgiye...
        self.wait(5) # Bu çizgi, bütünü parçalara...
        
        # Payda
        denom = MathTex("4", font_size=96).next_to(frac_line, DOWN, buff=0.5)
        denom_label = Text("Payda", font_size=40, color=YELLOW).next_to(denom, RIGHT, buff=0.8)
        self.play(Write(denom), run_time=1.5)
        self.wait(5) # Çizginin hemen altına yazdığımız...
        self.play(Write(denom_label), run_time=1)
        self.wait(7) # Payda kelimesi, elimizdeki nesnenin...
        self.wait(5) # Eğer parçalar eşit değilse...
        
        # Pay
        num = MathTex("1", font_size=96).next_to(frac_line, UP, buff=0.5)
        num_label = Text("Pay", font_size=40, color=GREEN).next_to(num, RIGHT, buff=0.8)
        self.play(Write(num), run_time=1.5)
        self.wait(5) # Çizginin üst kısmına yerleştirdiğimiz...
        self.play(Write(num_label), run_time=1)
        self.wait(7) # Pay, oluşturduğumuz bu eşit...
        self.wait(5) # Şimdi ekrandaki pizzamızı sayılara...
        self.wait(4) # Karşımıza çıkan bu ifadenin...
        
        # Okunuşlar
        read_group = VGroup(num, frac_line, denom)
        self.play(FadeOut(num_label), FadeOut(denom_label), run_time=1)
        
        # 1. Okunuş (Yukarıdan Aşağıya)
        arrow_down = Arrow(start=UP*2, end=DOWN*2, color=BLUE, stroke_width=6).next_to(read_group, LEFT, buff=1)
        text_down = Text("Bir bölü dört", font_size=36, color=BLUE).next_to(arrow_down, LEFT, buff=0.5)
        self.play(GrowArrow(arrow_down), Write(text_down), run_time=2)
        self.wait(6) # Birinci yöntem, yukarıdan aşağıya...
        self.wait(6) # Buradaki 'bölü' ifadesi, kesir...
        
        # 2. Okunuş (Aşağıdan Yukarıya)
        arrow_up = Arrow(start=DOWN*2, end=UP*2, color=PURPLE, stroke_width=6).next_to(read_group, RIGHT, buff=1)
        text_up = Text("Dörtte bir", font_size=36, color=PURPLE).next_to(arrow_up, RIGHT, buff=0.5)
        self.play(GrowArrow(arrow_up), Write(text_up), run_time=2)
        self.wait(6) # İkinci yöntem ise aşağıdan...
        self.wait(7) # Bu okunuş tarzı, bütünün...
        self.wait(8) # Özellikle yeni nesil problemleri...
        
        # Kapanış
        self.play(FadeOut(Group(*self.mobjects)), run_time=2)
        outro_text = Text("Matematik Mantıktır", font_size=54, color=GOLD)
        self.play(Write(outro_text), run_time=2)
        self.wait(6) # Sayıların sadece birer sembol...
        self.wait(3) # Bir sonraki derste görüşmek...
        self.play(FadeOut(outro_text), run_time=1)