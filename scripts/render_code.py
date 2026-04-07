from manim import *

class KesirlerinMantigi(Scene):
    def construct(self):
        # Arka plan rengi
        self.camera.background_color = WHITE
        
        # Başlık (Intro)
        title = Text("Kesirlerin Mantığı", color=BLUE, font_size=48, weight=BOLD)
        self.play(Write(title))
        # Merhaba, Maarif Matematik kanalına hoş geldiniz. (3 saniye)
        self.wait(3)
        
        # Bugün kesirlerin ne anlama geldiğini ve temel mantığını öğreneceğiz. (4.5 saniye)
        self.play(title.animate.to_edge(UP))
        self.wait(3.5) # Animasyon süresi 1s, toplam 4.5s
        
        # Öncelikle bir bütün düşünelim. (2 saniye)
        whole_rect = Rectangle(width=6, height=2, color=DARK_GRAY)
        self.play(Create(whole_rect))
        self.wait(1) # Animasyon 1s, toplam 2s
        
        # Mesela bir çikolata veya bir dikdörtgen. (3 saniye)
        self.wait(3)
        
        # Şimdi bu bütünü tam dört eş parçaya bölelim. (4 saniye)
        parts = VGroup(*[Rectangle(width=1.5, height=2, color=DARK_GRAY) for _ in range(4)])
        parts.arrange(RIGHT, buff=0)
        parts.move_to(whole_rect.get_center())
        self.play(FadeIn(parts), FadeOut(whole_rect))
        self.wait(3) # Animasyon 1s, toplam 4s
        
        # Bu dört eş parçadan üç tanesini alalım ve renklendirelim. (4.5 saniye)
        self.play(
            parts[0].animate.set_fill(GREEN, opacity=0.7),
            parts[1].animate.set_fill(GREEN, opacity=0.7),
            parts[2].animate.set_fill(GREEN, opacity=0.7)
        )
        self.wait(3.5) # Animasyon 1s, toplam 4.5s
        
        # Bunu matematik dilinde ifade etmek için kesirleri kullanırız. (4 saniye)
        self.play(parts.animate.shift(LEFT * 2.5))
        fraction = MathTex(r"\frac{3}{4}", color=DARK_GRAY, font_size=120)
        fraction.next_to(parts, RIGHT, buff=2)
        self.play(Write(fraction))
        self.wait(2) # Animasyon 2s (shift+write), toplam 4s
        
        # Kesrimiz dörtte üç, yani üç bölü dört olacaktır. (4 saniye)
        self.wait(4)
        
        # Buradaki alt kısma payda diyoruz. (2.5 saniye)
        payda_label = VGroup(
            Text("Payda", color=BLUE, font_size=28, weight=BOLD),
            Text("(Bütünün parça sayısı)", color=DARK_GRAY, font_size=20)
        ).arrange(DOWN, buff=0.1).next_to(fraction, DOWN, buff=1)
        arrow_payda = Arrow(payda_label.get_top(), fraction.get_bottom(), buff=0.1, color=DARK_GRAY)
        self.play(Write(payda_label), GrowArrow(arrow_payda))
        self.wait(1.5) # Animasyon 1s, toplam 2.5s
        
        # Payda, bütünü kaç eş parçaya böldüğümüzü gösterir. Burada dörde böldük. (5 saniye)
        self.wait(5)
        
        # Üst kısma ise pay diyoruz. (2.5 saniye)
        pay_label = VGroup(
            Text("Pay", color=GREEN, font_size=28, weight=BOLD),
            Text("(Alınan parça sayısı)", color=DARK_GRAY, font_size=20)
        ).arrange(DOWN, buff=0.1).next_to(fraction, UP, buff=1)
        arrow_pay = Arrow(pay_label.get_bottom(), fraction.get_top(), buff=0.1, color=DARK_GRAY)
        self.play(Write(pay_label), GrowArrow(arrow_pay))
        self.wait(1.5) # Animasyon 1s, toplam 2.5s
        
        # Pay, bu eş parçalardan kaç tanesini aldığımızı belirtir. Burada üç parça aldık. (6 saniye)
        self.wait(6)
        
        # Kesirler, bir bütünün eş parçalarından kaç tanesini aldığımızı anlatan harika bir yoldur. (6 saniye)
        self.wait(6)
        
        # Bir sonraki derste görüşmek üzere, hoşça kalın. (3.5 saniye)
        self.play(FadeOut(Group(title, parts, fraction, pay_label, arrow_pay, payda_label, arrow_payda)))
        logo = Text("Maarif Matematik", color=BLUE, font_size=48, weight=BOLD)
        self.play(Write(logo))
        self.wait(2.5) # Animasyon 1s, toplam 3.5s
        
        # Kural: Videonun son cümlesinden sonra mutlaka 4 saniye bekle.
        self.wait(4)
