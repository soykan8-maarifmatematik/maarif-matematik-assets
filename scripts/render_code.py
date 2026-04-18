from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengini beyaz yapıyoruz
        self.camera.background_color = "#FFFFFF"
        
        # Merkez konumlandırma kuralı
        main_center = DOWN * 0.5
        
        # Kesir elemanlarını oluşturma
        pay = MathTex("3", color="#00529B").scale(3)
        cizgi = Line(LEFT, RIGHT, color=BLACK).scale(1.2)
        payda = MathTex("4", color="#D32F2F").scale(3)
        
        # Kesri VGroup ile birleştirip merkeze sabitliyoruz
        kesir_grubu = VGroup(pay, cizgi, payda).arrange(DOWN, buff=0.3)
        kesir_grubu.move_to(main_center)
        
        # Kavram etiketleri
        pay_etiket = Text("Pay (Alınan Parça)", color="#00529B", font_size=28)
        pay_etiket.next_to(pay, RIGHT, buff=1)
        
        payda_etiket = Text("Payda (Toplam Eşit Parça)", color="#D32F2F", font_size=28)
        payda_etiket.next_to(payda, RIGHT, buff=1)
        
        cizgi_etiket = Text("Kesir Çizgisi", color=BLACK, font_size=24)
        cizgi_etiket.next_to(cizgi, LEFT, buff=1)
        
        # Okunuş metinleri (Üst kısma yerleştiriliyor)
        okunus_baslik = Text("Kesrin Okunuşu", color=BLACK, font_size=36, weight=BOLD)
        okunus_baslik.to_edge(UP).shift(DOWN * 0.2)
        
        okunus1 = Text("1) Yukarıdan Aşağıya: \"3 bölü 4\"", color="#00529B", font_size=28)
        okunus1.next_to(okunus_baslik, DOWN, buff=0.3)
        
        okunus2 = Text("2) Aşağıdan Yukarıya: \"4'te 3\"", color="#D32F2F", font_size=28)
        okunus2.next_to(okunus1, DOWN, buff=0.2)
        
        # Animasyon sırası
        self.play(Write(kesir_grubu), run_time=2)
        self.wait(1)
        
        self.play(
            Write(pay_etiket),
            Write(payda_etiket),
            Write(cizgi_etiket)
        )
        self.wait(2)
        
        self.play(Write(okunus_baslik))
        self.play(Write(okunus1))
        self.wait(1)
        self.play(Write(okunus2))
        self.wait(3)
        
        # Sahne kapanışı
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)