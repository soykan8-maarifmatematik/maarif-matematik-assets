from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0
config.background_color = "#FFFFFF"

class MaarifScene(Scene):
    def construct(self):
        # Başlık
        title = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", font="Montserrat", weight=BOLD, color="#212121")
        title.scale_to_fit_width(7.0)
        title.to_edge(np.array([0, 1, 0]), buff=1.0)
        self.play(Write(title))

        # Kesirler
        frac1 = MathTex(r"\frac{1}{3}", color="#212121").scale(2.5)
        frac2 = MathTex(r"\frac{1}{5}", color="#212121").scale(2.5)

        # 1/3 Modeli
        circle1 = Circle(radius=0.9, color="#212121")
        slice1 = Sector(radius=0.9, angle=TAU/3, color=BLUE, fill_opacity=0.7)
        lines1 = VGroup(*[Line(ORIGIN, np.array([0.9*np.cos(i*TAU/3), 0.9*np.sin(i*TAU/3), 0]), color="#212121") for i in range(3)])
        model1 = VGroup(circle1, slice1, lines1)

        # 1/5 Modeli
        circle2 = Circle(radius=0.9, color="#212121")
        slice2 = Sector(radius=0.9, angle=TAU/5, color=RED, fill_opacity=0.7)
        lines2 = VGroup(*[Line(ORIGIN, np.array([0.9*np.cos(i*TAU/5), 0.9*np.sin(i*TAU/5), 0]), color="#212121") for i in range(5)])
        model2 = VGroup(circle2, slice2, lines2)

        # Gruplama ve Yerleşim
        group1 = VGroup(frac1, model1).arrange(np.array([0, -1, 0]), buff=0.8)
        group2 = VGroup(frac2, model2).arrange(np.array([0, -1, 0]), buff=0.8)

        comparison_group = VGroup(group1, group2).arrange(np.array([1, 0, 0]), buff=1.5)
        comparison_group.scale(0.8).shift(np.array([0, 1.0, 0]))
        
        self.play(Create(comparison_group))

        # Sembol
        symbol = MathTex(">", color="#212121").scale(3)
        symbol.move_to(comparison_group.get_center())
        self.play(Write(symbol))

        # Sonuç Metni
        result_text = Text("Payda küçüldükçe parça büyür!", font="Montserrat", weight=BOLD, color="#212121")
        result_text.scale_to_fit_width(6.0)
        result_text.to_edge(np.array([0, -1, 0]), buff=4.8)
        self.play(Write(result_text))
        
        self.wait(2)