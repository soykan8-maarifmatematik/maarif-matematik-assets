from manim import *

class UnitFractionLogic(Scene):
    def construct(self):
        # --- AYARLAR ---
        # Maarif Matematik Estetiği: Beyaz Arka Plan
        self.camera.background_color = "#FFFFFF"
        dark_grey = "#333333"
        maarif_blue = "#87CEEB" # Görseldeki yumuşak mavi tonu

        # 1. Başlık Oluşturma
        title = Text("Birim Kesir Mantığı", font="Oswald", color=dark_grey).scale(1.2)
        title.to_edge(UP, buff=0.5)

        # 2. Bütün Daireyi Oluşturma
        whole_circle = Circle(radius=2, color=dark_grey, stroke_width=2)
        whole_circle.shift(DOWN * 0.5)

        # 3. Bölme Çizgileri (4 eş parça için)
        horizontal_line = Line(
            whole_circle.get_left(), whole_circle.get_right(), 
            color=dark_grey, stroke_width=2
        )
        vertical_line = Line(
            whole_circle.get_top(), whole_circle.get_bottom(), 
            color=dark_grey, stroke_width=2
        )
        lines = VGroup(horizontal_line, vertical_line)

        # 4. Birim Kesir Dilimi (Hata Buradaydı: Tam Hizalama)
        # Sector kullanarak tam merkezi ve açıyı belirliyoruz
        unit_slice = Sector(
            inner_radius=0,
            outer_radius=2,
            angle=90 * DEGREES,      # 4'te 1 olduğu için 90 derece
            start_angle=90 * DEGREES, # Sol üst kadrana yerleştir (90'dan başla)
            color=maarif_blue,
            fill_opacity=0.8,
            stroke_width=0
        )
        unit_slice.move_to(whole_circle.get_center(), aligned_edge=ORIGIN)
        # Not: move_to ve aligned_edge kullanımı dilimin ucunun tam merkezde kalmasını sağlar.

        # 5. Alt Bilgi Metni (Altyazı Kutusu)
        subtitle_box = Rectangle(
            width=8, height=1, 
            fill_color=dark_grey, fill_opacity=0.7, 
            stroke_width=0
        ).to_edge(DOWN, buff=1)
        
        subtitle_text = Text(
            "Bir bütünü eş parçalara ayırdığımızda\no parçalardan sadece bir tanesine...",
            font="Montserrat", color=WHITE
        ).scale(0.5)
        subtitle_text.move_to(subtitle_box.get_center())
        
        caption_group = VGroup(subtitle_box, subtitle_text)

        # --- ANİMASYON AKIŞI ---
        self.play(Write(title))
        self.wait(0.5)
        
        self.play(Create(whole_circle))
        self.play(Create(lines))
        self.wait(1)

        # Dilimin belirmesi (Tam yerine oturacak şekilde)
        self.play(FadeIn(unit_slice, scale=0.5))
        self.play(unit_slice.animate.set_stroke(dark_grey, 1))
        
        self.play(FadeIn(caption_group, shift=UP))
        self.wait(3)

        # Kapanış
        self.play(FadeOut(VGroup(title, whole_circle, lines, unit_slice, caption_group)))
        self.wait(1)
