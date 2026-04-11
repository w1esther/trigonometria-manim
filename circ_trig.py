from manim import *
import numpy as np
import pdb


class CirculoTrigonometrico(MovingCameraScene):
    def construct(self):

        plano = NumberPlane()
        self.add(plano)



        circulo = Circle(radius=1, color=BLUE)
        self.play(Create(circulo))

        # guarda um número que pode mudar durante a animação

        angulo = ValueTracker(3.14)
        # pdb.set_trace()
        # "sempre que for desenhar o ponto use o valor atual do ângulo"
        
        # ponto = always_redraw(lambda: Dot(circulo.point_at_angle(angulo.get_value()),color=YELLOW))
        
        def teste():
            return Dot(circulo.point_at_angle(angulo.get_value()),color=YELLOW)
        
        ponto = always_redraw(teste())
                              
        # ponto_no_circulo = Dot(circulo.point_at_angle(angulo.get_value()),color=YELLOW)
                              
        # always_redraw(ponto_no_circulo)
        
        
        # self.add(ponto_no_circulo)
        # ponto = always_redraw(Dot(circulo.point_at_angle(angulo.get_value()),color=YELLOW))


        # raio = always_redraw(lambda: Line(ORIGIN, ponto.get_center(), color=WHITE))

        # proj_x = always_redraw(lambda: Dot([ponto.get_x(), 0, 0],color=GREEN))

        # linha_cosseno = always_redraw(lambda: Line(ORIGIN, [ponto.get_x(), 0, 0], color=GREEN))

        # # projeção no eixo y (seno)
        # proj_y = always_redraw(lambda: Dot([0, ponto.get_y(), 0],color=RED))

        # linha_seno = always_redraw( lambda: Line([ponto.get_x(), 0, 0] ,ponto.get_center(), color=RED))

        # self.add(ponto, raio, proj_x, proj_y, linha_cosseno, linha_seno)

        # self.play(
        #     angulo.animate.set_value(TAU), #TAU = 2PI
        #     run_time=6,
        #     rate_func=linear
        # )

        self.wait(2)