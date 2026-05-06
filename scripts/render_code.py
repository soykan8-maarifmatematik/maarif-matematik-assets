from manim import *
config.pixel_height, config.pixel_width = 1920, 1080
config.background_color = "#FFFFFF"

class MaarifScene(Scene):
    def construct(self):
        self.camera.frame_width = 9
        self.camera.frame_height = 16
        
        title = Text("Birim Kesirleri Karşılaştırma", color="#212121", weight="BOLD")
        title.scale_to_fit_width(7.0).to_edge(UP, buff=1.0)
        
        sectors_3 = VGroup()
        for i in range(3):
            sector = Sector(
                radius=0.9,
                angle=TAU/3,
                start_angle=i*TAU/3,
                color="#212121",
                stroke_width=2,
                fill_color=BLUE if i == 0 else "#FFFFFF",
                fill_opacity=0.5 if i == 0 else 0.0
            )
            sectors_3.add(sector)
            
        sectors_6 = VGroup()
        for i in range(6):
            sector = Sector(
                radius=0.9,
                angle=TAU/6,
                start_angle=i*TAU/6,
                color="#212121",
                stroke_width=2,
                fill_color=RED if i == 0 else "#FFFFFF",
                fill_opacity=0.5 if i == 0 else 0.0
            )
            sectors_6.add(sector)
            
        sectors_3.shift(LEFT * 2 + UP * 2.5)
        sectors_6.shift(RIGHT * 2 + UP * 2.5)
        
        label_3 = MathTex(r"\frac{1}{3}", color="#212121").next_to(sectors_3, DOWN)
        label_6 = MathTex(r"\frac{1}{6}", color="#212121").next_to(sectors_6, DOWN)
        
        greater_sign = MathTex(">", color="#212121").scale(2).move_to(UP * 2.5)
        
        explanation = Paragraph(
            "Bir pastayı 3'e bölersek mi",
            "daha büyük dilim yeriz,",
            "yoksa 6'ya bölersek mi?",
            "Payda büyüdükçe dilim küçülür!",
            alignment="center",
            color="#212121"
        )
        explanation.scale_to_fit_width(6.5).to_edge(DOWN, buff=3.5)
        
        self.play(Write(title))
        self.wait(0.5)
        
        self.play(Create(sectors_3), Write(label_3))
        self.wait(0.5)
        
        self.play(Create(sectors_6), Write(label_6))
        self.wait(0.5)
        
        self.play(Write(greater_sign))
        self.wait(1)
        
        self.play(Write(explanation))
        self.wait(2)