from manim import *

class MaarifScene(Scene):
    def construct(self):
        # Arka plan rengi
        self.camera.background_color = "#FFFFFF"
        
        # Maarif Matematik Renk Paleti
        dark_gray = "#333333"
        navy_blue = "#002B4D"
        maarif_red = "#D32F2F"

        # --- BÖLÜM 1: GİRİŞ VE TANIM ---
        # "Merhaba, Maarif Matematik’e hoş geldiniz." (5 kelime = 2.77s)
        title = Text("Birim Kesir", color=navy_blue, font_size=48).to_edge(UP)
        self.play(Write(title), run_time=1)
        self.wait(1.77)

        # "Bugün sizlerle kesirlerin en temel yapı taşı olan birim kesirleri öğreneceğiz." (11 kelime = 6.11s)
        subtitle = Text("Payı 1 olan kesirler", color=dark_gray, font_size=36).next_to(title, DOWN)
        self.play(Write(subtitle), run_time=1)
        self.wait(5.11)

        # "Bir bütünü eş parçalara ayırdığımızda, bu eş parçalardan sadece bir tanesini ifade eden kesre birim kesir diyoruz." (17 kelime = 9.44s)
        circle = Circle(radius=1.5, color=navy_blue, stroke_width=4)
        lines = VGroup(*[Line(circle.get_center(), circle.point_at_angle(i * PI / 2), color=navy_blue) for i in range(4)])
        self.play(Create(circle), Create(lines), run_time=2)
        self.wait(7.44)

        # "Yani payı her zaman bir olan kesirlerdir." (7 kelime = 3.88s)
        fraction = MathTex(r"\frac{1}{4}", color=dark_gray, font_size=64).next_to(circle, RIGHT, buff=1)
        fraction[0][0].set_color(maarif_red) # Pay kısmını kırmızı yap
        self.play(Write(fraction), run_time=1)
        self.wait(2.88)

        # "Örneğin, bir bütünü dört eş parçaya bölerseniz, her bir parça dörtte bir kesrini ifade eder." (15 kelime = 8.33s)
        slice_1 = Sector(radius=1.5, angle=PI/2, start_angle=0, color=maarif_red, fill_opacity=0.5)
        self.play(FadeIn(slice_1), run_time=1)
        self.wait(7.33)

        # --- BÖLÜM 2: SAYI DOĞRUSU ---
        # "Peki, birim kesirleri sayı doğrusunda nasıl gösteririz?" (7 kelime = 3.88s)
        self.play(FadeOut(Group(title, subtitle, circle, lines, fraction, slice_1)), run_time=0.5)
        title2 = Text("Sayı Doğrusunda Gösterim", color=navy_blue, font_size=48).to_edge(UP)
        self.play(Write(title2), run_time=0.5)
        self.wait(2.88)

        # "Birim kesirler her zaman sıfır ile bir tam sayıları arasında yer alır." (12 kelime = 6.66s)
        nl = NumberLine(x_range=[0, 1, 0.25], length=8, color=dark_gray, include_numbers=False)
        nl_labels = VGroup(
            MathTex("0", color=dark_gray).next_to(nl.n2p(0), DOWN),
            MathTex("1", color=dark_gray).next_to(nl.n2p(1), DOWN)
        )
        self.play(Create(nl), Write(nl_labels), run_time=2)
        self.wait(4.66)

        # "Çünkü bir bütünden daha küçüktürler." (5 kelime = 2.77s)
        self.wait(2.77)

        # "Sayı doğrusunda sıfır ile bir arasını, kesrimizin paydası kadar eş parçaya böleriz." (12 kelime = 6.66s)
        ticks = VGroup(*[Line(UP*0.2, DOWN*0.2, color=navy_blue).move_to(nl.n2p(i*0.25)) for i in range(1,4)])
        self.play(Create(ticks), run_time=2)
        self.wait(4.66)

        # "Sıfırdan sonraki ilk adımımız, bize birim kesrimizin yerini gösterir." (9 kelime = 5.00s)
        dot = Dot(nl.n2p(0.25), color=maarif_red, radius=0.15)
        label_14 = MathTex(r"\frac{1}{4}", color=maarif_red).next_to(dot, UP)
        self.play(FadeIn(dot), Write(label_14), run_time=1)
        self.wait(4.00)

        # --- BÖLÜM 3: KARŞILAŞTIRMA ---
        # "Şimdi en kritik noktaya gelelim." (5 kelime = 2.77s)
        self.play(FadeOut(Group(title2, nl, nl_labels, ticks, dot, label_14)), run_time=1)
        self.wait(1.77)

        # "Birim kesirleri nasıl karşılaştırırız?" (4 kelime = 2.22s)
        title3 = Text("Birim Kesirleri Karşılaştırma", color=navy_blue, font_size=48).to_edge(UP)
        self.play(Write(title3), run_time=1)
        self.wait(1.22)

        # "Ezberlemek yerine mantığını düşünelim." (4 kelime = 2.22s)
        self.wait(2.22)

        # "Bir bütünü iki parçaya böldüğünüzde mi daha büyük bir parça elde edersiniz, yoksa on parçaya böldüğünüzde mi?" (17 kelime = 9.44s)
        rect1 = Rectangle(width=4, height=1, color=navy_blue).shift(LEFT*3 + UP)
        rect2 = Rectangle(width=4, height=1, color=navy_blue).shift(RIGHT*3 + UP)
        
        line1 = Line(rect1.get_top(), rect1.get_bottom(), color=navy_blue)
        fill1 = Rectangle(width=2, height=1, color=maarif_red, fill_opacity=0.5).align_to(rect1, LEFT).align_to(rect1, UP)
        
        lines2 = VGroup(*[Line(rect2.get_corner(UL) + RIGHT*(i*0.4), rect2.get_corner(DL) + RIGHT*(i*0.4), color=navy_blue) for i in range(1,10)])
        fill2 = Rectangle(width=0.4, height=1, color=maarif_red, fill_opacity=0.5).align_to(rect2, LEFT).align_to(rect2, UP)
        
        self.play(Create(rect1), Create(line1), Create(rect2), Create(lines2), run_time=2)
        self.wait(7.44)

        # "Elbette iki parçaya böldüğünüzde." (4 kelime = 2.22s)
        self.play(FadeIn(fill1), FadeIn(fill2), run_time=1)
        self.wait(1.22)

        # "Bu yüzden payda büyüdükçe, yani parça sayısı arttıkça, birim kesrin değeri küçülür." (12 kelime = 6.66s)
        comp_text = MathTex(r"\frac{1}{2}", ">", r"\frac{1}{10}", color=dark_gray, font_size=64).shift(DOWN*1.5)
        comp_text[0].set_color(maarif_red)
        comp_text[2].set_color(maarif_red)
        self.play(Write(comp_text), run_time=1)
        self.wait(5.66)

        # "İkide bir, onda birden her zaman daha büyüktür." (8 kelime = 4.44s)
        self.play(comp_text[1].animate.scale(1.5).set_color(navy_blue), run_time=0.5)
        self.play(comp_text[1].animate.scale(1/1.5), run_time=0.5)
        self.wait(3.44)

        # "Bir sonraki derste görüşmek üzere, hoşça kalın." (7 kelime = 3.88s)
        outro = Text("Maarif Matematik", color=maarif_red, font_size=48).shift(DOWN*3)
        self.play(Write(outro), run_time=1)
        self.wait(2.88)
