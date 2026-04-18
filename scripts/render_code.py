from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        main_center = DOWN * 0.5

        # Title
        title = Text("Kesir Nedir?", color=BLACK, font_size=48)
        title.to_edge(UP)
        self.play(Write(title))

        # Fraction Structure
        pay_text = Text("Pay", color=BLUE, font_size=48)
        line = Line(LEFT, RIGHT, color=BLACK).scale(1.2)
        payda_text = Text("Payda", color=RED, font_size=48)
        frac_group = VGroup(pay_text, line, payda_text).arrange(DOWN, buff=0.3)
        
        # Visual (Circle)
        sectors = VGroup()
        for i in range(5):
            sector = Sector(outer_radius=1.5, angle=TAU/5, start_angle=i*TAU/5, color=BLACK, fill_opacity=0, stroke_width=2)
            sectors.add(sector)
        
        visual_group = VGroup(frac_group, sectors).arrange(RIGHT, buff=2)
        visual_group.move_to(main_center)

        self.play(Write(frac_group))
        self.wait(2)

        self.play(Create(sectors))
        self.wait(2)

        # Highlight Pay
        filled_sectors = VGroup()
        for i in range(3):
            filled_sector = Sector(outer_radius=1.5, angle=TAU/5, start_angle=i*TAU/5, color=GREEN, fill_opacity=0.6, stroke_width=2)
            filled_sectors.add(filled_sector)
        filled_sectors.move_to(sectors.get_center())
        
        self.play(FadeIn(filled_sectors))
        self.wait(2)

        # Transform to 3/5
        num_3 = Text("3", color=BLUE, font_size=48)
        num_5 = Text("5", color=RED, font_size=48)
        frac_35 = VGroup(num_3, line.copy(), num_5).arrange(DOWN, buff=0.3)
        frac_35.move_to(frac_group.get_center())

        self.play(Transform(frac_group, frac_35))
        self.wait(2)

        # Readings
        read_1 = Text("3 bölü 5", color=BLACK, font_size=36)
        read_1.next_to(frac_35, DOWN, buff=0.5)
        
        arrow_down = Arrow(start=frac_35.get_top() + UP*0.2 + LEFT*0.8, end=frac_35.get_bottom() + DOWN*0.2 + LEFT*0.8, color=BLUE)
        
        self.play(Write(read_1), GrowArrow(arrow_down))
        self.wait(2)

        read_2 = Text("5'te 3", color=BLACK, font_size=36)
        read_2.next_to(frac_35, DOWN, buff=0.5)
        
        arrow_up = Arrow(start=frac_35.get_bottom() + DOWN*0.2 + LEFT*0.8, end=frac_35.get_top() + UP*0.2 + LEFT*0.8, color=RED)

        self.play(Transform(read_1, read_2), Transform(arrow_down, arrow_up))
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)