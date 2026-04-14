from manim import *
import numpy as np

class CirculoTrigonometrico(MovingCameraScene):
    def construct(self):

        axes = Axes(
            x_range=[-5, 5, 5],
            y_range=[-5, 5, 5],
        ).scale(0.5)

        self.add(axes)

        circulo = Circle(radius=1, color=BLUE)
        self.play(Create(circulo))

        label_eixo_senos = Text('Eixo dos \n  Senos').shift(1.8*UP).scale(0.2)
        label_eixo_cossenos = Text('Eixo dos \nCossenos').shift(2*RIGHT + 0.3*DOWN).scale(0.2)

        noventa = MathTex(r"\frac{\pi}{2}").scale(0.3).shift(1.3*UP + 0.2*RIGHT)

        cento_e_oitenta = MathTex(r"\pi").shift(1.2*LEFT + 0.1*UP).scale(0.3)

        duzentos_e_setenta = MathTex(r"\frac{3\pi}{2}").scale(0.3).shift(1.3*DOWN + 0.2* RIGHT)

        trezentos_e_setenta = MathTex(r"2\pi").scale(0.3).shift(1.2*RIGHT + 0.1*UP)

        self.play(Write(label_eixo_cossenos), Write(label_eixo_senos), FadeIn(noventa), FadeIn(cento_e_oitenta), FadeIn(duzentos_e_setenta), FadeIn(trezentos_e_setenta))


        self.play(self.camera.frame.animate.scale(0.5).shift(0.2*UP))

        angulo = angulo = ValueTracker(0.001) #em radianos

        ponto = always_redraw(lambda: Dot(circulo.point_at_angle(angulo.get_value()),color=YELLOW))

        raio = always_redraw(lambda: Line(ORIGIN, ponto.get_center(), color=WHITE))

        proj_x = always_redraw(lambda: Dot([ponto.get_x(), 0, 0],color=GREEN))

        linha_cosseno = always_redraw(lambda: Line(ORIGIN, [ponto.get_x(), 0, 0], color=GREEN))

        # linha_cosseno = always_redraw(lambda: Line([0, ponto.get_y(), 0], ponto.get_center(), color=GREEN))

        proj_y = always_redraw(lambda: Dot([0, ponto.get_y(), 0],color=RED))

        linha_seno = always_redraw(lambda: Line([ponto.get_x(), 0, 0] ,ponto.get_center(), color=RED))

        valor_seno = always_redraw(lambda: DecimalNumber( ponto.get_y(), num_decimal_places=2, color=RED ).next_to(proj_y, RIGHT, buff=0.1).scale(0.4)) 

        valor_cosseno = always_redraw(lambda: DecimalNumber( ponto.get_x(), num_decimal_places=2, color=GREEN ).next_to(proj_x, DOWN, buff=0.1).scale(0.4))

        angulo_texto = always_redraw(lambda: MathTex( f"\\theta = {angulo.get_value():.2f}" ).to_corner(UL).scale(0.5)) 
        
        caminho_seno = TracedPath( proj_y.get_center, stroke_color=RED, stroke_width=2 ) 
        # caminho_cosseno = TracedPath(proj_x.get_center, stroke_color=GREEN, stroke_width=4)

        linha_cosseno_topo = always_redraw(lambda: Line([0, ponto.get_y(), 0],ponto.get_center(),color=GREEN))

        linha_base = Line(ORIGIN, RIGHT, color=WHITE)

        angulo_visual = always_redraw(lambda: Angle(
        linha_base,
        raio,
        radius=0.3,
        color=YELLOW,
        stroke_width = 2
        ))

        theta_simbolo = always_redraw(lambda: MathTex(r"\theta")
        .move_to(angulo_visual.get_center())
        .scale(0.3)
        )

        self.add(linha_base,angulo_visual, theta_simbolo)

        self.add( ponto, raio, proj_x, proj_y, linha_cosseno, linha_seno, valor_seno, valor_cosseno, angulo_texto, caminho_seno, linha_cosseno_topo)

        self.play( angulo.animate.set_value(TAU - 0.001), run_time=10, rate_func=linear )

        self.wait(2)