from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi beyaz
        self.camera.background_color = "#FFFFFF"
        
        # 1. GİRİŞ
        intro_text = Text("Maarif Matematik", color="#333333", font_size=48)
        self.play(Write(intro_text))
        self.wait(4) # Merhaba, Maarif Matematik’e hoş geldiniz.
        self.play(FadeOut(intro_text))
        
        # 2. KESİR NEDİR?
        title1 = Text("Kesir Nedir?", color="#333333", font_size=40).to_edge(UP)
        self.play(Write(title1))
        self.wait(5) # Bugün sizlerle matematiğin en temel ve en önemli konularından biri olan kesirleri öğreneceğiz.
        
        circle = Circle(radius=1.5, color="#333333", stroke_width=4)
        self.play(Create(circle))
        self.wait(6) # Kesir, bir bütünün eş parçalarından birini veya birkaçını gösteren sayıdır.
        self.wait(6) # Düşünün ki elinizde nefis bir pizza var ve bunu arkadaşlarınızla eşit olarak paylaşmak istiyorsunuz.
        self.wait(4) # İşte tam bu noktada kesirler devreye girer.
        self.play(FadeOut(circle), FadeOut(title1))
        
        # 3. PAY VE PAYDA İLİŞKİSİ
        kesir_cizgisi = Line(LEFT, RIGHT, color="#333333").scale(1.5)
        pay_text = Text("Pay", color="#1976D2", font_size=48).next_to(kesir_cizgisi, UP, buff=0.5)
        payda_text = Text("Payda", color="#D32F2F", font_size=48).next_to(kesir_cizgisi, DOWN, buff=0.5)
        
        self.play(Create(kesir_cizgisi))
        self.wait(4) # Bir kesir yazarken ortada bir kesir çizgisi bulunur.
        self.play(Write(pay_text))
        self.wait(3) # Üstteki sayıya 'pay',
        self.play(Write(payda_text))
        self.wait(3) # alttaki sayıya ise 'payda' deriz.
        
        self.play(Indicate(payda_text, color="#D32F2F"))
        self.wait(5) # Payda, bütünü kaç eşit parçaya böldüğümüzü gösterir.
        self.play(Indicate(pay_text, color="#1976D2"))
        self.wait(5) # Pay ise bu eşit parçalardan kaç tanesini aldığımızı ifade eder.
        
        self.play(FadeOut(pay_text), FadeOut(payda_text), FadeOut(kesir_cizgisi))
        
        # 4. ÖRNEK: 3/4
        ex_line = Line(LEFT, RIGHT, color="#333333").scale(0.5).shift(RIGHT*3)
        ex_pay = Text("3", color="#1976D2", font_size=48).next_to(ex_line, UP, buff=0.3)
        ex_payda = Text("4", color="#D32F2F", font_size=48).next_to(ex_line, DOWN, buff=0.3)
        
        self.play(Create(ex_line), Write(ex_pay), Write(ex_payda))
        self.wait(4) # Örneğin, 3/4 kesrini ele alalım.
        
        # Animasyonlu Pizza (Sector kullanımı)
        pizza = VGroup()
        for i in range(4):
            slice_color = "#1976D2" if i < 3 else "#FFFFFF"
            fill_op = 0.8 if i < 3 else 0.1
            # KURAL: outer_radius KESİNLİKLE KULLANILMADI, sadece radius kullanıldı.
            pizza_slice = Sector(radius=1.5, angle=PI/2, start_angle=i*PI/2, color=slice_color, fill_opacity=fill_op, stroke_color="#333333", stroke_width=2)
            pizza.add(pizza_slice)
        
        pizza.shift(LEFT*2)
        self.play(Create(pizza[0]), Create(pizza[1]), Create(pizza[2]), Create(pizza[3]))
        self.wait(6) # Burada payda 4'tür, yani bütünümüz 4 eşit parçaya bölünmüştür.
        
        self.play(pizza[0].animate.scale(1.1), pizza[1].animate.scale(1.1), pizza[2].animate.scale(1.1))
        self.wait(5) # Pay ise 3'tür, yani bu parçalardan 3 tanesini alıyoruz.
        self.play(pizza[0].animate.scale(1/1.1), pizza[1].animate.scale(1/1.1), pizza[2].animate.scale(1/1.1))
        
        self.play(FadeOut(pizza))
        self.play(VGroup(ex_line, ex_pay, ex_payda).animate.move_to(ORIGIN).scale(1.5))
        self.wait(3) # Peki bu kesri nasıl okuruz?
        
        # 5. KESİRLERİN OKUNUŞU
        read1 = Text("Üç bölü Dört", color="#333333", font_size=36).next_to(ex_line, RIGHT, buff=2).shift(UP*1)
        read2 = Text("Dörtte Üç", color="#333333", font_size=36).next_to(ex_line, RIGHT, buff=2).shift(DOWN*1)
        
        arrow1 = Arrow(start=ex_pay.get_right(), end=read1.get_left(), color="#1976D2", buff=0.2)
        arrow2 = Arrow(start=ex_payda.get_right(), end=read2.get_left(), color="#D32F2F", buff=0.2)
        
        self.wait(4) # Kesirleri okumanın iki farklı yolu vardır.
        self.play(Write(read1), GrowArrow(arrow1))
        self.wait(5) # Birincisi yukarıdan aşağıya doğru okumaktır: 'Üç bölü Dört'.
        
        self.play(Write(read2), GrowArrow(arrow2))
        self.wait(5) # İkincisi ise aşağıdan yukarıya doğru okumaktır: 'Dörtte Üç'.
        
        self.wait(5) # İkisi de aynı anlama gelir ve günlük hayatta sıkça kullanılır.
        
        self.play(FadeOut(VGroup(ex_line, ex_pay, ex_payda, read1, read2, arrow1, arrow2)))
        
        # 6. ÇIKIŞ
        outro_text = Text("Maarif Matematik", color="#333333", font_size=48)
        self.play(Write(outro_text))
        self.wait(6) # Kesirlerin temel mantığı işte bu kadar basittir. Bir sonraki derste görüşmek üzere, hoşça kalın.
        self.play(FadeOut(outro_text))
