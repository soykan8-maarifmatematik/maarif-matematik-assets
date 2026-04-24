from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # Objelerin Oluşturulması
        title = Text("Birim Kesirler", font="DejaVu Sans", font_size=56).move_to(UP * 3.5)

        # 1/2 Görseli
        circle_half = Circle(radius=1.3, color=WHITE)
        line_half = Line(circle_half.get_top(), circle_half.get_bottom(), color=WHITE)
        sector_half = Sector(radius=1.3, angle=PI, start_angle=PI/2, color=BLUE, fill_opacity=0.7)
        frac_half = MathTex(r"\frac{1}{2}", font_size=72)
        group_half = VGroup(VGroup(circle_half, line_half, sector_half), frac_half).arrange(DOWN, buff=0.5)

        # 1/4 Görseli
        circle_quarter = Circle(radius=1.3, color=WHITE)
        line_q1 = Line(circle_quarter.get_top(), circle_quarter.get_bottom(), color=WHITE)
        line_q2 = Line(circle_quarter.get_left(), circle_quarter.get_right(), color=WHITE)
        sector_quarter = Sector(radius=1.3, angle=PI/2, start_angle=PI/2, color=RED, fill_opacity=0.7)
        frac_quarter = MathTex(r"\frac{1}{4}", font_size=72)
        group_quarter = VGroup(VGroup(circle_quarter, line_q1, line_q2, sector_quarter), frac_quarter).arrange(DOWN, buff=0.5)

        # Yan yana dizilim
        circles_group = VGroup(group_half, group_quarter).arrange(RIGHT, buff=1.2)
        
        # Karşılaştırma
        comparison = MathTex(r"\frac{1}{2} > \frac{1}{4}", font_size=88)

        # KESİN KURAL: VGroup(...).arrange(DOWN, buff=1.6)
        content = VGroup(circles_group, comparison).arrange(DOWN, buff=1.6)
        content.move_to(DOWN * 0.5) # Güvenli alan hizalaması (UP * 3.5 ile DOWN * 4 arası)

        # Animasyonlar ve Senkronizasyon (Hız: 3.0 kelime/saniye)
        
        # 1. "Merhaba, Maarif Matematik’e hoş geldiniz." (5 kelime -> 1.67s)
        self.play(Write(title), run_time=0.67)
        self.wait(1.0)

        # 2. "Birim kesirlerde payda büyüdükçe kesrin değeri neden küçülür?" (8 kelime -> 2.67s)
        self.wait(2.67)

        # 3. "Bir pastayı iki kişiye bölersek her birimize yarım pasta düşer." (10 kelime -> 3.33s)
        self.play(FadeIn(group_half), run_time=1.0)
        self.wait(2.33)

        # 4. "Aynı pastayı dört kişiye bölersek dilimler küçülür ve çeyrek pasta düşer." (11 kelime -> 3.67s)
        self.play(FadeIn(group_quarter), run_time=1.0)
        self.wait(2.67)

        # 5. "Yani payda parça sayısını gösterir parça sayısı artarsa dilimler ufalır." (10 kelime)
        self.play(Write(comparison), run_time=1.0)
        
        # MÜHÜR KURALI: Son matematiksel animasyon bittikten sonra, o cümledeki kelime sayısını (10) 3.0'a böl ve bekle.
        self.wait(3.33)

        # 6. ÇIKIŞ MÜHRÜ: "Maarif Matematik ile mantığını kavra, takipte kal!" (7 kelime -> 2.33s)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.5)
        outro_text = Text("Maarif Matematik ile\nmantığını kavra,\ntakipte kal!", font="DejaVu Sans", font_size=56)
        self.play(Write(outro_text), run_time=0.83)
        self.wait(1.5)
