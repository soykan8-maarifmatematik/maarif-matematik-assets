from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class BirimKesirler(Scene):
    def construct(self):
        # 1. ARKA PLAN VE RENK MÜHRÜ
        self.camera.background_color = "#FFFFFF"
        koyu_gri = "#333333"
        maarif_mavisi = "#007BFF"
        kirmizi = "#FF0000"
        
        # 3. KADRAJ VE YERLEŞİM (Güvenli Alan)
        baslik = Tex("Birim Kesirler", color=koyu_gri, font_size=72).to_edge(UP, buff=2.0)
        
        # 2. MODERN İNŞA - 1/2 Modeli
        cember_yarim = Circle(radius=1.5, color=koyu_gri, stroke_width=4)
        cizgi_yarim = Line(cember_yarim.get_top(), cember_yarim.get_bottom(), color=koyu_gri, stroke_width=2)
        dilim_yarim = Sector(outer_radius=1.5, angle=PI, start_angle=PI/2, color=maarif_mavisi, fill_opacity=0.8)
        yazi_yarim = MathTex(r"\frac{1}{2}", color=koyu_gri, font_size=80)
        grup_yarim = VGroup(VGroup(cember_yarim, cizgi_yarim, dilim_yarim), yazi_yarim).arrange(RIGHT, buff=1.0)
        
        # 2. MODERN İNŞA - 1/4 Modeli
        cember_ceyrek = Circle(radius=1.5, color=koyu_gri, stroke_width=4)
        cizgi_c1 = Line(cember_ceyrek.get_top(), cember_ceyrek.get_bottom(), color=koyu_gri, stroke_width=2)
        cizgi_c2 = Line(cember_ceyrek.get_left(), cember_ceyrek.get_right(), color=koyu_gri, stroke_width=2)
        dilim_ceyrek = Sector(outer_radius=1.5, angle=PI/2, start_angle=PI/2, color=kirmizi, fill_opacity=0.8)
        yazi_ceyrek = MathTex(r"\frac{1}{4}", color=koyu_gri, font_size=80)
        grup_ceyrek = VGroup(VGroup(cember_ceyrek, cizgi_c1, cizgi_c2, dilim_ceyrek), yazi_ceyrek).arrange(RIGHT, buff=1.0)
        
        # 2. SEMBOLİK KARŞILAŞTIRMA
        sembol = MathTex(">", color=koyu_gri, font_size=120)
        
        # 3. HİZALAMA VE MERKEZLEME
        ana_grup = VGroup(grup_yarim, sembol, grup_ceyrek).arrange(DOWN, buff=1.8)
        ana_grup.move_to(ORIGIN)
        
        # --- ANİMASYONLAR VE 4. MİLİMETRİK SENKRON ---
        self.play(Write(baslik), run_time=1)
        
        # "Bir pastayı iki kişiye mi bölersen daha çok yersin, yoksa dört kişiye mi?" (13 kelime -> ~4.3 sn)
        self.play(Create(cember_yarim), Create(cizgi_yarim), run_time=1.5)
        self.play(FadeIn(dilim_yarim), Write(yazi_yarim), run_time=1.5)
        self.wait(1.3)
        
        # "İşte birim kesirlerin sırrı budur! Payda büyüdükçe, dilim küçülür." (9 kelime -> 3.0 sn)
        self.play(Create(cember_ceyrek), Create(cizgi_c1), Create(cizgi_c2), run_time=1.5)
        self.play(FadeIn(dilim_ceyrek), Write(yazi_ceyrek), run_time=1.5)
        
        # "Gelin bunu matematikle ispatlayalım. Bir bölü iki, büyüktür, bir bölü dört." (11 kelime -> ~3.6 sn)
        self.play(Write(sembol), run_time=1)
        self.play(Circumscribe(sembol, color=maarif_mavisi, time_width=2, stroke_width=8), run_time=1.5)
        self.wait(1.1)
        
        # "Matematik ezber değil, mantıktır. Maarif Matematik ile keşfet!" (8 kelime)
        # 4. BİTİŞ KURALI: 8 kelime / 3.0 + 2 saniye = 4.66 saniye bekleme. Ekran temizlenmez.
        self.wait(4.66)
