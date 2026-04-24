from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 1080 / 1920 * 14.22
config.frame_height = 14.22

class MaarifScene(Scene):
    def construct(self):
        # 1. GİRİŞ VE BAŞLIK (Güvenli Alan: buff=2.0)
        title = Text("Birim Kesirler", font="DejaVu Sans", color=WHITE).scale(1.5).to_edge(UP, buff=2.0)
        self.play(Write(title))
        self.wait(1.7) # Merhaba, Maarif Matematik’e hoş geldiniz.
        
        self.wait(2.3) # Birim kesirlerde payda büyüdükçe kesir neden küçülür?
        self.wait(2.0) # Gelin mantığını bir pasta üzerinden anlayalım.
        
        # 2. PASTALAR (Merkez 6x10 alanına mıhlanmış)
        cake1_base = Circle(radius=1.5, color=WHITE).shift(UP*1.5 + LEFT*2.2)
        cake2_base = Circle(radius=1.5, color=WHITE).shift(UP*1.5 + RIGHT*2.2)
        
        self.play(Create(cake1_base), Create(cake2_base))
        self.wait(2.3) # Elimizde aynı boyutta iki nefis pasta var.
        
        # 3. DİLİMLER VE KESİRLER (outer_radius KESİNLİKLE YOK, sadece radius)
        slice1 = Sector(radius=1.5, angle=PI, color=ORANGE, fill_opacity=0.8).move_arc_center_to(cake1_base.get_center())
        frac1 = MathTex(r"\frac{1}{2}").scale(2.5).next_to(cake1_base, DOWN, buff=0.5)
        
        self.play(Create(slice1), Write(frac1))
        self.wait(3.0) # İlk pastayı iki kişiye paylaştıralım, yani bir bölü iki.
        
        slice2 = Sector(radius=1.5, angle=PI/2, color=BLUE, fill_opacity=0.8).move_arc_center_to(cake2_base.get_center())
        frac2 = MathTex(r"\frac{1}{4}").scale(2.5).next_to(cake2_base, DOWN, buff=0.5)
        
        self.play(Create(slice2), Write(frac2))
        self.wait(3.3) # İkinci pastayı ise dört kişiye paylaştıralım, yani bir bölü dört.
        
        self.wait(2.3) # Hangisinde tabağınıza daha büyük bir dilim düşer?
        
        self.play(Indicate(slice1, scale_factor=1.2, color=YELLOW))
        self.wait(2.0) # Tabii ki iki kişiye bölünen pastada!
        
        # 4. PEDAGOJİK AÇIKLAMA (Yazılar KESİNLİKLE scale(1.5) ve alignment parametresi YOK)
        exp_text1 = Text("Payda = Kisi Sayisi", font="DejaVu Sans", color=YELLOW).scale(1.5).shift(DOWN*2.5)
        self.play(Write(exp_text1))
        self.wait(2.0) # Payda, pastayı kaç kişiye böldüğümüzü gösterir.
        
        exp_text2 = Text("Kisi artarsa\ndilim kuculur", font="DejaVu Sans", color=RED_B).scale(1.5).next_to(exp_text1, DOWN, buff=0.8)
        self.play(Write(exp_text2))
        self.wait(2.3) # Kişi sayısı artarsa, sana düşen dilim küçülür.
        
        # 5. BÜYÜKTÜR SEMBOLÜ (Devasa ve YELLOW)
        comp_sign = Text(">", font="DejaVu Sans", color=YELLOW).scale(4).move_to(UP*1.5)
        self.play(Write(comp_sign))
        self.wait(3.0) # Bu yüzden bir bölü iki, bir bölü dörtten büyüktür.
        
        # 6. KAPANIŞ VE TEMİZLİK
        self.wait(1.5) # Son cümle bittikten sonra 1.5 saniye bekle
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        cta = Text("Maarif Matematik ile\nmantigini kavra,\ntakipte kal", font="DejaVu Sans", color=BLUE).scale(1.5)
        self.play(Write(cta))
        self.wait(2.3) # Maarif Matematik ile mantığını kavra, takipte kal!
