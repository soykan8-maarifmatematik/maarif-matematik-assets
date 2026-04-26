from manim import *

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = '#FFFFFF'
        Text.set_default(color='#333333')
        MathTex.set_default(color='#333333')
        Tex.set_default(color='#333333')

        intro_text = Tex(r'Maarif Matematik: Kesirler').scale(1.5)
        self.play(Write(intro_text))
        self.wait(19)
        self.play(FadeOut(Group(*self.mobjects)))

        basit_title = Tex(r'Basit Kesir').to_edge(UP)
        basit_pie = VGroup(*[Sector(radius=2, angle=PI/2, start_angle=i*PI/2, color=BLUE, fill_opacity=0.8, stroke_width=2, stroke_color='#FFFFFF') for i in range(3)])
        basit_label = MathTex(r'\frac{3}{4}').scale(1.5).next_to(basit_pie, DOWN)
        self.play(Write(basit_title))
        self.play(Create(basit_pie), Write(basit_label))
        self.wait(25)
        self.play(FadeOut(Group(*self.mobjects)))

        bilesik_title = Tex(r'Bileşik Kesir').to_edge(UP)
        bilesik_pie1 = VGroup(*[Sector(radius=2, angle=PI/2, start_angle=i*PI/2, color=RED, fill_opacity=0.8, stroke_width=2, stroke_color='#FFFFFF') for i in range(4)]).shift(LEFT*2.5)
        bilesik_pie2 = Sector(radius=2, angle=PI/2, start_angle=0, color=RED, fill_opacity=0.8, stroke_width=2, stroke_color='#FFFFFF').shift(RIGHT*2.5)
        bilesik_label = MathTex(r'\frac{5}{4}').scale(1.5).next_to(VGroup(bilesik_pie1, bilesik_pie2), DOWN)
        self.play(Write(bilesik_title))
        self.play(Create(bilesik_pie1), Create(bilesik_pie2), Write(bilesik_label))
        self.wait(25)
        self.play(FadeOut(Group(*self.mobjects)))

        tam_title = Tex(r'Tam Sayılı Kesir').to_edge(UP)
        tam_pie1 = VGroup(*[Sector(radius=2, angle=PI/2, start_angle=i*PI/2, color=GREEN, fill_opacity=0.8, stroke_width=2, stroke_color='#FFFFFF') for i in range(4)]).shift(LEFT*2.5)
        tam_pie2 = Sector(radius=2, angle=PI/2, start_angle=0, color=GREEN, fill_opacity=0.8, stroke_width=2, stroke_color='#FFFFFF').shift(RIGHT*2.5)
        tam_label = MathTex(r'1 \frac{1}{4}').scale(1.5).next_to(VGroup(tam_pie1, tam_pie2), DOWN)
        self.play(Write(tam_title))
        self.play(Create(tam_pie1), Create(tam_pie2), Write(tam_label))
        self.wait(27)
        self.play(FadeOut(Group(*self.mobjects)))

        donusum1_title = Tex(r'Bileşik $\rightarrow$ Tam Sayılı').to_edge(UP)
        donusum1_label = MathTex(r'\frac{5}{4}').scale(1.5).move_to(LEFT*4)
        
        dividend = MathTex('5').move_to(LEFT*0.5 + UP*0.5)
        divisor = MathTex('4').move_to(RIGHT*0.5 + UP*0.5)
        v_line = Line(UP*1, DOWN*0.2, color='#333333').move_to(ORIGIN + UP*0.5)
        h_line = Line(ORIGIN, RIGHT*1, color='#333333').move_to(RIGHT*0.5 + UP*0.2)
        quotient = MathTex('1').move_to(RIGHT*0.5 + DOWN*0.2)
        sub_val = MathTex('4').move_to(LEFT*0.5 + DOWN*0.2)
        minus = MathTex('-').next_to(sub_val, LEFT, buff=0.1)
        sub_line = Line(LEFT*1, ORIGIN, color='#333333').move_to(LEFT*0.5 + DOWN*0.5)
        remainder = MathTex('1').move_to(LEFT*0.5 + DOWN*0.9)
        
        bolme_evi = VGroup(dividend, divisor, v_line, h_line, quotient, sub_val, minus, sub_line, remainder).shift(RIGHT*1)
        result_label = MathTex(r'= 1 \frac{1}{4}').scale(1.5).next_to(bolme_evi, RIGHT, buff=1)

        self.play(Write(donusum1_title), Write(donusum1_label))
        self.wait(5)
        self.play(Write(dividend), Write(divisor), Create(v_line), Create(h_line))
        self.wait(5)
        self.play(Write(quotient))
        self.wait(3)
        self.play(Write(sub_val), Write(minus), Create(sub_line))
        self.wait(3)
        self.play(Write(remainder))
        self.wait(5)
        self.play(Write(result_label))
        self.wait(5)
        self.play(FadeOut(Group(*self.mobjects)))

        donusum2_title = Tex(r'Tam Sayılı $\rightarrow$ Bileşik').to_edge(UP)
        donusum2_label = MathTex(r'1 \frac{1}{4}').scale(1.5).move_to(LEFT*3)
        
        calc_text = MathTex(r'= \frac{(1 \times 4) + 1}{4}').scale(1.2).next_to(donusum2_label, RIGHT, buff=0.5)
        final_text = MathTex(r'= \frac{5}{4}').scale(1.5).next_to(calc_text, RIGHT, buff=0.5)

        self.play(Write(donusum2_title), Write(donusum2_label))
        self.wait(6)
        self.play(Write(calc_text))
        self.wait(8)
        self.play(Write(final_text))
        self.wait(8)
        self.play(FadeOut(Group(*self.mobjects)))

        outro_text = Tex(r'Hoşça kalın!').scale(1.5)
        self.play(Write(outro_text))
        self.wait(16)
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)
