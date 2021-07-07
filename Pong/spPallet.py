#-*- encoding: utf-8 -*-
import config as cfg
import graphics as gfx
import pygame

class Pallet(pygame.sprite.Sprite):
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        self.image = gfx.LoadImage(cfg.sprites + "pala.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = cfg.height/2
        self.speed = 0.5

    def Update (self, drctr, time):
        if drctr == 1:
            if self.rect.top >= 0:
                self.rect.centery -= self.speed * time
        elif drctr == 2:
            if self.rect.bottom <= cfg.height:
                self.rect.centery += self.speed * time

    def IA (self, ball, time):
        if ball.speed[0] >= 0.0 and ball.rect.centerx >= float(cfg.width/2):
            if self.rect.centery < ball.rect.centery:
                self.rect.centery += self.speed * time
            if self.rect.centery > ball.rect.centery:
                self.rect.centery -= self.speed * time

    def draw(self, screen):
        screen.blit(self.image, self.rect)
