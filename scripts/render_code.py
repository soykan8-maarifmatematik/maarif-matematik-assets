from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        # Arka plan Maarif Laciverti
        self.camera.background_color = "#002B4D"

        # KANCA (Hook)
        title = Text("BİRİM KESİRLER", font_size=72, color="#FFD700", weight=BOLD).to_edge(UP, buff=1.5)
        self.play(Write(title), run_time=1)
        self.wait(1.5)

        def_text = Text("Payı 1 olan kesirler", font_size=48, color="#FFFFFF").next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(def_text, shift=DOWN), run_time=1)
        self.wait(2)

        # GÖVDE (Body) - Görselleştirme
        # 1/2 Çemberi
        circle_half = Circle(radius=1.5, color="#FFFFFF", stroke_width=4).move_to(UP * 1.5)
        line_half = Line(circle_half.get_top(), circle_half.get_bottom(), color="#FFFFFF")
        fill_half = AnnularSector(inner_radius=0, outer_radius=1.5, angle=PI, start_angle=PI/2, color="#D32F2F", fill_opacity=0.9).move_to(circle_half.get_center())
        frac_half = MathTex(r"\frac{1}{2}", font_size=96, color="#FFD700").next_to(circle_half, LEFT, buff=1)

        # 1/4 Çemberi
        circle_quarter = Circle(radius=1.5, color="#FFFFFF", stroke_width=4).move_to(DOWN * 2.5)
        lines_quarter = VGroup(
            Line(circle_quarter.get_top(), circle_quarter.get_bottom(), color="#FFFFFF"),
            Line(circle_quarter.get_left(), circle_quarter.get_right(), color="#FFFFFF")
        )
        fill_quarter = AnnularSector(inner_radius=0, outer_radius=1.5, angle=PI/2, start_angle=PI/2, color="#D32F2F", fill_opacity=0.9).move_to(circle_quarter.get_center())
        frac_quarter = MathTex(r"\frac{1}{4}", font_size=96, color="#FFD700").next_to(circle_quarter, LEFT, buff=1)

        self.play(FadeOut(def_text), run_time=0.5)
        
        # 1/2 Animasyonu
        self.play(Create(circle_half), Create(line_half), Write(frac_half), run_time=1)
        self.play(FadeIn(fill_half), run_time=0.5)
        self.wait(1.5)

        # 1/4 Animasyonu
        self.play(Create(circle_quarter), Create(lines_quarter), Write(frac_quarter), run_time=1)
        self.play(FadeIn(fill_quarter), run_time=0.5)
        self.wait(2)

        # Kural Metni
        self.play(FadeOut(circle_half, line_half, fill_half, frac_half, circle_quarter, lines_quarter, fill_quarter, frac_quarter), run_time=1)

        rule1 = Text("Payda Büyüdükçe", font_size=60, color="#FFFFFF").move_to(UP * 1)
        rule2 = Text("Değer KÜÇÜLÜR!", font_size=80, color="#D32F2F", weight=BOLD).next_to(rule1, DOWN, buff=0.5)

        self.play(Write(rule1), run_time=1)
        self.play(FadeIn(rule2, scale=1.5), run_time=1)
        self.wait(2.5)

        self.play(FadeOut(rule1, rule2), run_time=0.5)

        # Örnek
        ex_text = MathTex(r"\frac{1}{10} > \frac{1}{100}", font_size=120, color="#FFD700").move_to(CENTER)
        self.play(Write(ex_text), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(ex_text, title), run_time=0.5)

        # KAPANIŞ (CTA)
        cta = Text("Daha fazlası için\nTAKİP ET!", font_size=64, color="#FFFFFF", text_alignment="CENTER", weight=BOLD).move_to(CENTER)
        logo_text = Text("Maarif Matematik", font_size=48, color="#FFD700").next_to(cta, DOWN, buff=1)
        
        self.play(FadeIn(cta, shift=UP), Write(logo_text), run_time=1)
        self.wait(3)