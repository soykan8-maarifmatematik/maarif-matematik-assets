from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        # BAŞLIK
        title = Text("BİRİM KESİRLERİ KARŞILAŞTIRMA", font="Montserrat", weight=BOLD, color="#212121")
        title.scale_to_fit_width(7.0)
        title.to_edge(np.array([0, 1, 0]), buff=1.0)
        self.play(Write(title))

        # MODELLER
        # Sol Model: 1/2
        left_circle = Circle(radius=0.9, color="#212121")
        left_filled = Sector(radius=0.9, angle=PI, start_angle=PI/2, color="#FF5722", fill_opacity=0.8)
        left_line = Line(start=np.array([0, 0.9, 0]), end=np.array([0, -0.9, 0]), color="#212121")
        left_label = Text("1/2", font="Montserrat", color="#212121")
        left_label.next_to(left_circle, np.array([0, -1, 0]))
        left_group = VGroup(left_filled, left_circle, left_line, left_label)
        left_group.move_to(np.array([-2.5, 0, 0]))

        # Sağ Model: 1/4
        right_circle = Circle(radius=0.9, color="#212121")
        right_filled = Sector(radius=0.9, angle=PI/2, start_angle=PI/2, color="#2196F3", fill_opacity=0.8)
        right_line1 = Line(start=np.array([0, 0.9, 0]), end=np.array([0, -0.9, 0]), color="#212121")
        right_line2 = Line(start=np.array([-0.9, 0, 0]), end=np.array([0.9, 0, 0]), color="#212121")
        right_label = Text("1/4", font="Montserrat", color="#212121")
        right_label.next_to(right_circle, np.array([0, -1, 0]))
        right_group = VGroup(right_filled, right_circle, right_line1, right_line2, right_label)
        right_group.move_to(np.array([2.5, 0, 0]))

        # Sembol
        symbol = Text(">", font="Montserrat", color="#212121").scale(2.0)
        symbol.move_to(ORIGIN)

        # Model ve Sembol Gruplaması (Ölçek ve Konumlandırma)
        models_group = VGroup(left_group, symbol, right_group)
        models_group.scale(0.8)
        models_group.shift(np.array([0, 1.5, 0]))

        self.play(Create(left_group))
        self.play(Create(right_group))
        self.play(Write(symbol))

        # SONUÇ METNİ
        result_text = Text("Payda büyüdükçe, dilim küçülür!", font="Montserrat", weight=BOLD, color="#212121")
        result_text.scale_to_fit_width(6.0)
        result_text.to_edge(np.array([0, -1, 0]), buff=4.8)
        self.play(Write(result_text))

        self.wait(2)
