from manim import *

config.pixel_height, config.pixel_width = 1920, 1080
config.frame_height, config.frame_width = 16.0, 9.0

class MaarifScene(Scene):
    def construct(self):
        self.camera.background_color = "#000000"
        
        header = Paragraph(
            "İKİ BASAMAKLI SAYILARLA\nÇARPMA İŞLEMİ",
            alignment="center",
            line_spacing=0.8,
            color="#FFFFFF",
            weight=BOLD
        ).scale_to_fit_width(7.2).to_edge(UP, buff=1.0)

        n67 = MathTex("6", "7", color="#FFFFFF").scale(1.7)
        n89 = MathTex("8", "9", color="#FFFFFF").scale(1.7)
        sign = MathTex("\\times", color="#FFFFFF").scale(1.7)
        line1 = Line(LEFT, RIGHT, color="#FFFFFF", stroke_width=6).scale(1.7)

        n89.next_to(n67, DOWN, aligned_edge=RIGHT, buff=0.5)
        sign.next_to(n89, LEFT, buff=0.8)
        line1.next_to(n89, DOWN, buff=0.2)
        
        res1 = MathTex("6", "0", "3", color="#FFFFFF").scale(1.7).next_to(line1, DOWN, aligned_edge=RIGHT, buff=0.3)
        res2 = MathTex("5", "3", "6", color="#FFFFFF").scale(1.7).next_to(res1, DOWN, aligned_edge=RIGHT, buff=0.3)
        res2.shift(LEFT * 0.85)
        
        line2 = Line(LEFT, RIGHT, color="#FFFFFF", stroke_width=6).scale(2.2).next_to(res2, DOWN, buff=0.2)
        final_res = MathTex("5", "9", "6", "3", color="#FFFF00").scale(1.7).next_to(line2, DOWN, aligned_edge=RIGHT, buff=0.3)

        carry_6 = MathTex("+6", color="#FFFF00").scale(0.8).next_to(n67[0], UP, buff=0.2)
        carry_5 = MathTex("+5", color="#00FFFF").scale(0.8).next_to(n67[0], UP, buff=0.2)

        math_group = VGroup(n67, n89, sign, line1, res1, res2, line2, final_res, carry_6, carry_5)
        math_group.move_to(UP * 0.8)

        desc = Paragraph(
            "Eldeleri eklemeyi ve ikinci satırı\nsola kaydırmayı unutma!",
            alignment="center",
            color="#FFFFFF"
        ).scale_to_fit_width(7.5).move_to(DOWN * 4.5)

        self.play(Write(header))
        self.play(Write(n67, run_time=0.5), Write(n89, run_time=0.5), Write(sign, run_time=0.5))
        self.play(Create(line1))
        self.wait(0.5)

        self.play(n89[1].animate.set_color("#FFFF00"))
        self.play(Write(carry_6, run_time=0.5))
        self.play(Write(res1, run_time=0.5))
        self.wait(1.85)
        self.play(FadeOut(carry_6), n89[1].animate.set_color("#FFFFFF"))

        self.play(n89[0].animate.set_color("#00FFFF"))
        self.play(Write(carry_5, run_time=0.5))
        self.play(Write(res2, run_time=0.5))
        self.wait(1.85)
        self.play(FadeOut(carry_5), n89[0].animate.set_color("#FFFFFF"))

        self.play(Create(line2))
        self.play(Write(final_res, run_time=0.5))
        self.play(Write(desc))
        self.wait(3)