# -*- encoding: utf-8 -*-
import scene as scn
import config as cfg
import graphics as gfx
import spPallet, spBall
import pygame

class SceneGame(scn.Scene):
    "Escena inicial del juego, esta es la primera que se carga cuando inicia"

    def __init__(self, director):
        scn.Scene.__init__(self, director)
        self.back = gfx.LoadImage(cfg.backgrounds + "fondo_pong.png")
        # Constructor
        self.palletPlayer = spPallet.Pallet(30)
        self.palletCPU = spPallet.Pallet(cfg.width - 30)
        self.ball = spBall.Ball()
        self.puntos = [0,0]
        self.p_jug = None
        self.p_cpu = None
        self.p_jug_rect = None
        self.p_cpu_rect = None

    def on_update(self):
        self.time = self.director.time
        self.puntos = self.ball.Update(self.time, self.palletPlayer, self.palletCPU, self.puntos)
                
        self.palletCPU.IA(self.ball, self.time)

        self.p_jug, self.p_jug_rect = gfx.Text(str(self.puntos[0]), (cfg.width / 4, 40), (234,234,0), 40)
        self.p_cpu, self.p_cpu_rect = gfx.Text(str(self.puntos[1]), (cfg.width - cfg.width / 4, 40), (123,123,255), 40)
                

    def on_event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.palletPlayer.Update(1, self.time)
        if keys[pygame.K_DOWN]:
            self.palletPlayer.Update(2, self.time)
    
    def on_draw(self, screen):
        screen.blit(self.back, (0,0))
        self.palletPlayer.draw(screen)
        self.palletCPU.draw(screen)
        self.ball.draw(screen)
        screen.blit(self.p_jug, self.p_jug_rect)
        screen.blit(self.p_cpu, self.p_cpu_rect)
