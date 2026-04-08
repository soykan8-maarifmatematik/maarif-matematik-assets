from manim import *

class KesirlerinMantigi(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Giriş Bölümü
        title = Text('Maarif Matematik', font_size=60, color=BLUE).move_to(ORIGIN)
        self.play(Write(title))
        self.wait(8)
        self.play(FadeOut(title))
        
        sub_title = Text('Kesirlerin Mantığı', font_size=50, color=BLUE).move_to(UP*3)
        self.play(Write(sub_title))
        self.wait(22)
        
        # Pasta Dilimi Senaryosu
        cake = Circle(radius=2, color=DARK_GRAY, stroke_width=4)
        slices = VGroup(*[Sector(2.0, angle=TAU/9, start_angle=i*TAU/9, color=WHITE, stroke_color=DARK_GRAY, stroke_width=2, fill_opacity=1) for i in range(9)])
        self.play(Create(cake), FadeIn(slices))
        self.wait(28)
        self.play(slices[0].animate.set_fill(BLUE, opacity=0.5))
        self.wait(15)
        
        definition = Text('Bir bütünü eş parçalara ayırmak', color=DARK_GRAY, font_size=30).next_to(cake, DOWN)
        self.play(Write(definition))
        self.wait(45)
        
        self.play(FadeOut(cake), FadeOut(slices), FadeOut(definition))
        
        # Pay ve Payda Tanımı
        fraction_template = MathTex(r'\frac{\text{Pay}}{\text{Payda}}', color=DARK_GRAY, font_size=100)
        self.play(Write(fraction_template))
        self.wait(25)
        
        payda_label = Text('Payda: Bütünün kaç parçaya bölündüğü', color=GREEN, font_size=30).next_to(fraction_template, DOWN, buff=1)
        self.play(Write(payda_label))
        self.wait(30)
        
        pay_label = Text('Pay: Alınan parça sayısı', color=BLUE, font_size=30).next_to(fraction_template, UP, buff=1)
        self.play(Write(pay_label))
        self.wait(30)
        
        frac_example = MathTex(r'\frac{2}{9}', color=DARK_GRAY, font_size=100)
        self.play(Transform(fraction_template, frac_example))
        self.wait(15)
        
        reading = Text('dokuzda iki, yani iki bölü dokuz', color=DARK_GRAY, font_size=35).next_to(frac_example, RIGHT, buff=0.5)
        self.play(Write(reading))
        self.wait(45)
        
        self.play(FadeOut(fraction_template), FadeOut(payda_label), FadeOut(pay_label), FadeOut(reading))
        
        # İnteraktif Bölüm - Grid
        grid = VGroup(*[Rectangle(width=1, height=1, color=DARK_GRAY) for _ in range(10)]).arrange_in_grid(rows=2, cols=5, buff=0.1)
        self.play(Create(grid))
        self.wait(25)
        
        for i in range(7):
            grid[i].set_fill(BLUE, opacity=0.6)
        self.play(FadeIn(VGroup(*[grid[i] for i in range(7)])))
        self.wait(15)
        
        # Saat Animasyonu
        clock = Circle(radius=0.5, color=BLUE).to_corner(UR)
        hand = Line(clock.get_center(), clock.get_center() + UP*0.4, color=DARK_GRAY)
        self.play(Create(clock), Create(hand))
        self.play(Rotate(hand, angle=-TAU, about_point=clock.get_center(), rate_func=linear), run_time=10)
        self.wait(15)
        
        ans = MathTex(r'\frac{7}{10}', color=DARK_GRAY, font_size=80).next_to(grid, DOWN)
        self.play(Write(ans))
        self.wait(22)
        
        self.play(FadeOut(grid), FadeOut(ans), FadeOut(clock), FadeOut(hand))
        
        # Pizza ve Sayı Doğrusu
        pizza = Circle(radius=1.5, color=DARK_GRAY)
        pizza_slices = VGroup(*[Sector(1.5, angle=TAU/4, start_angle=i*TAU/4, color=WHITE, stroke_color=DARK_GRAY, stroke_width=2) for i in range(4)])
        pizza_slices[0].set_fill(BLUE, opacity=0.5)
        pizza_group = VGroup(pizza, pizza_slices).move_to(LEFT*3)
        self.play(FadeIn(pizza_group))
        self.wait(35)
        
        number_line = NumberLine(x_range=[0, 1, 0.25], length=5, color=DARK_GRAY, include_ticks=True).move_to(RIGHT*3)
        self.play(Create(number_line))
        dot = Dot(number_line.n2p(0.25), color=BLUE)
        self.play(Create(dot))
        self.wait(35)
        
        # Özet ve Outro
        summary_title = Text('Özet', color=BLUE, font_size=45).to_edge(UP)
        self.play(Transform(sub_title, summary_title))
        summary_text = Text('Pay: Alınan, Payda: Bölünen', color=DARK_GRAY, font_size=35)
        self.play(Write(summary_text))
        self.wait(30)
        
        self.play(FadeOut(pizza_group), FadeOut(number_line), FadeOut(dot), FadeOut(summary_text))
        
        question = Text('12 parça çikolatanın 5ini yedin. Kalan nedir?', color=DARK_GRAY, font_size=30)
        self.play(Write(question))
        self.wait(22)
        
        self.play(FadeOut(question), FadeOut(sub_title))
        
        outro = Text('Bir sonraki derste görüşmek üzere, hoşça kalın.', color=BLUE, font_size=40)
        self.play(Write(outro))
        self.wait(6)