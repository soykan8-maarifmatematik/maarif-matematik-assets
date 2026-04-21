from manim import *

class FractionLesson(Scene):
    def construct(self):
        # Intro (Merhaba, Maarif Matematik’e hoş geldiniz.)
        title = Text("Maarif Matematik", font_size=48, color=BLUE)
        self.play(Write(title), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), run_time=1)

        # Whole circle (Günlük hayatta bir bütünü parçalara ayırdığımızda, bu miktarları tam sayılarla ifade edemeyiz.)
        circle = Circle(radius=2, color=WHITE, stroke_width=4)
        self.play(Create(circle), run_time=2)
        self.wait(3.5)

        # Divide into 4 pieces (İşte burada devreye kesirler girer. Kesir, bir bütünün eş parçalarından birini veya birkaçını gösteren matematiksel bir modeldir.)
        colors = [RED, RED, RED, DARK_GRAY]
        sectors = VGroup()
        for i in range(4):
            sector = Sector(radius=2, angle=PI/2, start_angle=i*PI/2, color=colors[i], fill_opacity=0, stroke_width=2, stroke_color=WHITE)
            sectors.add(sector)

        self.play(FadeIn(sectors), FadeOut(circle), run_time=2)
        self.wait(4.5)

        # Fraction line (Ekranda gördüğünüz yatay çizgiye kesir çizgisi diyoruz.)
        frac_line = Line(LEFT, RIGHT, color=WHITE).scale(0.5)
        frac_line.shift(RIGHT * 4)
        self.play(sectors.animate.shift(LEFT * 3), Create(frac_line), run_time=2)
        self.wait(1)

        # Denominator (Bu çizginin altındaki sayıya 'payda' adı verilir. Payda, elimizdeki bütünün toplamda kaç eşit parçaya bölündüğünü gösterir.)
        denom = MathTex("4", font_size=64).next_to(frac_line, DOWN, buff=0.3)
        denom_text = Text("Payda", font_size=32, color=YELLOW).next_to(denom, RIGHT, buff=0.5)
        self.play(Write(denom), run_time=1)
        self.play(Write(denom_text), run_time=1)
        self.wait(4)

        # Highlight equal pieces (Burada en kritik nokta, parçaların kesinlikle birbirine eş olmasıdır; aksi takdirde kesir mantığı çöker.)
        self.play(sectors.animate.scale(1.05), run_time=1)
        self.play(sectors.animate.scale(1/1.05), run_time=1)
        self.wait(3)

        # Numerator (Çizginin üstündeki sayı ise 'pay' olarak adlandırılır. Böldüğümüz o eşit parçalardan kaç tanesini seçtiğimizi, kullandığımızı veya boyadığımızı belirtir.)
        self.play(
            sectors[0].animate.set_fill(opacity=0.7),
            sectors[1].animate.set_fill(opacity=0.7),
            sectors[2].animate.set_fill(opacity=0.7),
            run_time=2
        )
        num = MathTex("3", font_size=64).next_to(frac_line, UP, buff=0.3)
        num_text = Text("Pay", font_size=32, color=GREEN).next_to(num, RIGHT, buff=0.5)
        self.play(Write(num), run_time=1)
        self.play(Write(num_text), run_time=1)
        self.wait(4)

        # Clear texts for reading methods (Şimdi bu yapıyı nasıl seslendirdiğimize bakalım. Bir kesri okurken iki farklı yöntem kullanırız.)
        self.play(FadeOut(denom_text), FadeOut(num_text), run_time=1)
        self.wait(3.5)

        # Reading Method 1: Top to Bottom (Yukarıdan aşağıya doğru okumak istersek, matematiksel işlemi vurgularız. Önce payı söyler, aradaki çizgiyi 'bölü' kelimesiyle ifade eder ve paydayı okuruz.)
        arrow_down = Arrow(start=UP, end=DOWN, color=GREEN).next_to(num, LEFT, buff=0.5)
        read1_text = Text("Üç bölü dört", font_size=36, color=GREEN).next_to(frac_line, RIGHT, buff=1.5).shift(UP*1)
        self.play(GrowArrow(arrow_down), run_time=1.5)
        self.wait(5.5)
        
        # (Örneğin, üstte üç, altta dört varsa, bunu 'üç bölü dört' şeklinde seslendiririz.)
        self.play(Write(read1_text), run_time=2)
        self.wait(3)

        # Reading Method 2: Bottom to Top (İkinci yöntem ise aşağıdan yukarıya doğru okumaktır ve bu, oransal mantığı öne çıkarır. Önce paydayı söyler, bulunma hali eki olan 'de' veya 'da' ekler, ardından payı belirtiriz.)
        arrow_up = Arrow(start=DOWN, end=UP, color=YELLOW).next_to(denom, LEFT, buff=0.5)
        read2_text = Text("Dörtte üç", font_size=36, color=YELLOW).next_to(frac_line, RIGHT, buff=1.5).shift(DOWN*1)
        self.play(GrowArrow(arrow_up), run_time=1.5)
        self.wait(7.5)
        
        # (Aynı örneği bu kuralla 'dörtte üç' olarak okuruz.)
        self.play(Write(read2_text), run_time=1.5)
        self.wait(1.5)

        # Final grouping and highlight (Her iki okunuş da zihnimizde aynı resmi canlandırmalıdır: Dört eş dilime ayrılmış bir bütünün üç dilimi.)
        self.play(Circumscribe(VGroup(read1_text, read2_text), color=WHITE), run_time=1.5)
        self.wait(4.5)

        # Outro (Kesirlerin dünyasına sağlam bir adım attık. Bir sonraki derste görüşmek üzere, hoşça kalın.)
        self.play(
            FadeOut(sectors), FadeOut(frac_line), FadeOut(num), FadeOut(denom),
            FadeOut(arrow_down), FadeOut(arrow_up), FadeOut(read1_text), FadeOut(read2_text),
            run_time=2
        )
        self.wait(1)
        outro_text = Text("Maarif Matematik", font_size=48, color=BLUE)
        self.play(Write(outro_text), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(outro_text), run_time=1)
