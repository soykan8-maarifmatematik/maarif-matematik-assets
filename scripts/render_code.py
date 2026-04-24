from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # 1. Cümle: "Merhaba, Maarif Matematik’e hoş geldiniz." (5 kelime -> 5/3 + 1.5 = 3.16s)
        self.wait(3.16)

        # 2. Cümle: "Birim kesirlerde payda büyüdükçe kesrin değeri neden küçülür?" (8 kelime -> 8/3 + 1.5 = 4.16s)
        title = Text("BİRİM KESİRLER", font="DejaVu Sans", color=YELLOW).to_edge(UP, buff=0.8)
        self.play(Write(title))
        self.wait(4.16)

        # 3. Cümle: "Bir bütün pizzayı ikiye böldüğümüzde elde ettiğimiz dilim, bir bölü ikidir." (11 kelime -> 11/3 + 1.5 = 5.16s)
        pizza1 = Circle(radius=1.5, color=WHITE)
        slice1 = Sector(radius=1.5, angle=PI, color=YELLOW, fill_opacity=0.7)
        label1 = MathTex(r"\frac{1}{2}").scale(2)
        group1 = VGroup(VGroup(pizza1, slice1), label1).arrange(RIGHT, buff=1.0)
        group1.scale_to_fit_width(6.0)
        group1.move_to(UP * 2.5)

        self.play(Create(pizza1))
        self.play(Create(slice1), Write(label1))
        self.wait(5.16)

        # 4. Cümle: "Aynı pizzayı dörde bölersek, bir dilim bir bölü dört olur." (10 kelime -> 10/3 + 1.5 = 4.83s)
        pizza2 = Circle(radius=1.5, color=WHITE)
        slice2 = Sector(radius=1.5, angle=PI/2, color=ORANGE, fill_opacity=0.7)
        label2 = MathTex(r"\frac{1}{4}").scale(2)
        group2 = VGroup(VGroup(pizza2, slice2), label2).arrange(RIGHT, buff=1.0)
        group2.scale_to_fit_width(6.0)
        group2.next_to(group1, DOWN, buff=2.0)

        self.play(Create(pizza2))
        self.play(Create(slice2), Write(label2))
        self.wait(4.83)

        # 5. Cümle: "Gördüğünüz gibi, payda arttıkça dilimler küçülüyor." (6 kelime -> 6/3 + 1.5 = 3.5s)
        comp_text = Text("Payda büyüdükçe değer küçülür!", font="DejaVu Sans", color=GREEN)
        comp_text.scale_to_fit_width(6.5)
        comp_text.next_to(group2, DOWN, buff=1.5)
        
        self.play(Write(comp_text))
        self.wait(3.5)

        # Ekranı Temizleme (Kapanış yazısı tertemiz ekrana gelmelidir)
        self.play(FadeOut(title), FadeOut(group1), FadeOut(group2), FadeOut(comp_text))

        # 6. Cümle (ÇIKIŞ): "Maarif Matematik ile mantığını kavra, takipte kal!" (7 kelime -> 7/3 + 1.5 = 3.83s)
        outro = Text("Maarif Matematik ile\nmantığını kavra,\ntakipte kal!", font="DejaVu Sans", color=BLUE)
        outro.scale_to_fit_width(6.5)
        
        self.play(Write(outro))
        self.wait(3.83)

        # Final Mührü
        self.wait(4)
