from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = '#FFFFFF'
        
        # Part 1: Basit Kesir
        intro_text = Text('Basit Kesirler', color=BLACK, font_size=48).to_edge(UP)
        self.play(Write(intro_text), run_time=2.0)
        
        c_outline = Circle(radius=1.5, color=BLACK).move_to(LEFT * 2)
        self.play(Create(c_outline), run_time=1.0)
        
        l1 = Line(c_outline.get_top(), c_outline.get_bottom(), color=BLACK)
        l2 = Line(c_outline.get_left(), c_outline.get_right(), color=BLACK)
        self.play(Create(VGroup(l1, l2)), run_time=1.0)
        
        s1 = Sector(radius=1.5, angle=PI/2, start_angle=0, color=BLUE, fill_opacity=0.7).move_to(LEFT * 2)
        s2 = Sector(radius=1.5, angle=PI/2, start_angle=PI/2, color=BLUE, fill_opacity=0.7).move_to(LEFT * 2)
        s3 = Sector(radius=1.5, angle=PI/2, start_angle=PI, color=BLUE, fill_opacity=0.7).move_to(LEFT * 2)
        
        self.play(Create(VGroup(s1, s2, s3)), run_time=2.0)
        
        frac1 = MathTex(r'\frac{3}{4}', color=BLACK, font_size=72).next_to(c_outline, RIGHT, buff=1.0)
        self.play(Write(frac1), run_time=2.0)
        
        self.wait(20.23)
        
        part1_group = VGroup(intro_text, c_outline, l1, l2, s1, s2, s3, frac1)
        
        # Part 2: Bilesik Kesir
        self.play(FadeOut(part1_group), run_time=1.0)
        
        c1 = Circle(radius=1.2, color=BLACK).move_to(LEFT * 3)
        c2 = Circle(radius=1.2, color=BLACK).move_to(ORIGIN)
        self.play(Create(VGroup(c1, c2)), run_time=2.0)
        
        sectors = VGroup()
        for i in range(4):
            sectors.add(Sector(radius=1.2, angle=PI/2, start_angle=i*PI/2, color=RED, fill_opacity=0.7).move_to(LEFT * 3))
        for i in range(3):
            sectors.add(Sector(radius=1.2, angle=PI/2, start_angle=i*PI/2, color=RED, fill_opacity=0.7).move_to(ORIGIN))
            
        self.play(Create(sectors), run_time=2.0)
        
        frac2 = MathTex(r'\frac{7}{4}', color=BLACK, font_size=72).next_to(c2, RIGHT, buff=1.0)
        self.play(Write(frac2), run_time=2.0)
        
        self.wait(19.47)
        
        part2_group = VGroup(c1, c2, sectors, frac2)
        
        # Part 3: Tam Sayili Kesir
        self.play(part2_group.animate.shift(LEFT * 2), run_time=2.0)
        
        frac3 = MathTex(r'1 \frac{3}{4}', color=BLACK, font_size=72).next_to(frac2, RIGHT, buff=1.0)
        self.play(Write(frac3), run_time=2.0)
        
        self.wait(21.88)
        
        part3_group = VGroup(part2_group, frac3)
        
        # Part 4: Cevirme ve Bolme Evi
        self.play(FadeOut(part3_group), run_time=1.0)
        
        dividend = MathTex('7', color=BLACK, font_size=72).move_to(LEFT * 0.5 + UP * 0.5)
        divisor = MathTex('4', color=BLACK, font_size=72).move_to(RIGHT * 0.5 + UP * 0.5)
        self.play(Write(VGroup(dividend, divisor)), run_time=2.0)
        
        v_line = Line(UP * 1.2, DOWN * 0.2, color=BLACK)
        h_line = Line(ORIGIN, RIGHT * 1.2, color=BLACK)
        self.play(Create(VGroup(v_line, h_line)), run_time=2.0)
        
        quotient = MathTex('1', color=BLACK, font_size=72).next_to(h_line, DOWN, buff=0.3)
        self.play(Write(quotient), run_time=1.0)
        
        remainder = MathTex('3', color=BLACK, font_size=72).next_to(dividend, DOWN, buff=0.8)
        self.play(Write(remainder), run_time=1.0)
        
        final_frac = MathTex(r'1 \frac{3}{4}', color=BLACK, font_size=72).move_to(RIGHT * 3 + DOWN * 1)
        self.play(Write(final_frac), run_time=2.0)
        
        self.wait(16.29)
        
        part4_group = VGroup(dividend, divisor, v_line, h_line, quotient, remainder, final_frac)
        
        # Part 5: Kapanis
        self.play(FadeOut(part4_group), run_time=1.0)
        
        outro_text = Text('Maarif Matematik', color=BLACK, font_size=60)
        self.play(Write(outro_text), run_time=2.0)
        
        self.wait(5.41)
        self.wait(1.0)