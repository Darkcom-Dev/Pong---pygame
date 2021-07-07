#-*- encoding: utf-8 -*-
import pygame
import config as cfg
import graphics as gfx

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = gfx.LoadImage(cfg.sprites + "BalaPla.png", True)
        self.rect = self.image.get_rect()
        self.rect.center = cfg.width/2, cfg.height/2
        self.speed = [0.1, -0.1]

    def Update(self, time, pala_jug, pala_cpu, puntos):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time

        if self.rect.left <=0 or self.rect.right >= cfg.width:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <=0 or self.rect.bottom >= cfg.height:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time

        #Colisiones
        if pygame.sprite.collide_rect(self, pala_jug):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time

        if pygame.sprite.collide_rect(self, pala_cpu):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time

        
        if self.rect.left <=0:
            puntos[1] +=1
        if self.rect.right >= cfg.width:
            puntos[0] +=1
            
        return puntos
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
