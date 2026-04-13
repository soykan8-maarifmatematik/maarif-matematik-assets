```python
from manim import *

class UnitFractionLogic(Scene):
    def construct(self):
        # --- TASARIM STANDARTLARI ---
        self.camera.background_color = "#FFFFFF"
        dark_grey = "#333333"
        maarif_blue = "#87CEEB"
        
        # 1. MERKEZ NOKTASI (Tüm objeler buraya kilitlenecek)
        main_center = DOWN * 0.5 

        # 2. Başlık
        title = Text("Birim Kesir Mantığı", font="Oswald", color=dark_grey).scale(1.1)
        title.to_edge(UP, buff=0.7)

        # 3. Ana Daire
        # arc_center kullanarak merkezi en baştan tanımlıyoruz
        whole_circle = Circle(radius=2.2, color=dark_grey, stroke_width=2)
        whole_circle.move_to(main_center)

        # 4. Eşit Bölme Çizgileri
        # Çizgilerin merkezini dairenin merkezine göre hesaplıyoruz
        h_line = Line(
            whole_circle.get_left(), whole_circle.get_right(), 
            color=dark_grey, stroke_width=2
        )
        v_line = Line(
            whole_circle.get_top(), whole_circle.get_bottom(), 
            color=dark_grey, stroke_width=2
        )
        lines = VGroup(h_line, v_line)

        # 5. Birim Kesir Dilimi (KRİTİK DÜZELTME)
        # arc_center=main_center diyerek dilimin "sivri ucunu" dairenin merkezine çiviliyoruz
        unit_slice = Sector(
            arc_center=main_center, # Tam merkezde olması için kilit nokta
            inner_radius=0,
            outer_radius=2.2,
            angle=90 * DEGREES,
            start_angle=90 * DEGREES, # Sol üst kadran
            color=maarif_blue,
            fill_opacity=0.8,
            stroke_width=1,
            stroke_color=dark_grey
        )

        # 6. Altyazı Kutusu ve Metni
        subtitle_box = Rectangle(
            width=8.5, height=1, 
            fill_color=dark_grey, fill_opacity=0.8, 
            stroke_width=0
        ).to_edge(DOWN, buff=0.8)
        
        caption = Text(
            "Bir pastayı kaç eş parçaya bölerseniz\nbölün o parçalardan sadece bir tanesine...",
            font="Montserrat", color=WHITE
        ).scale(0.45)
        caption.move_to(subtitle_box.get_center())

        # --- ANİMASYON ---
        self.play(Write(title))
        self.wait(0.3)
        
        self.play(Create(whole_circle), Create(lines))
        self.wait(0.5)

        # Dilimin merkezden dışarı doğru zarifçe gelmesi
        self.play(FadeIn(unit_slice, shift=RIGHT*0.2 + DOWN*0.2)) 
        self.wait(0.2)
        
        # Altyazı
        self.play(FadeIn(subtitle_box, shift=UP), Write(caption))
        self.wait(4)

        # Temizlik
        self.play(
            FadeOut(VGroup(whole_circle, lines, unit_slice, title, subtitle_box, caption))
        )
        self.wait(1)

```
