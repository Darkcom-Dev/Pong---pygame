#!/usr/bin/env python
#-*- encoding: utf-8 -*-
#Linea anterior sirve para decirle al editor que la codificacion es utf8

#Módulos
import sys, pygame
from pygame.locals import*
#Constantes
import config as cfg
import graphics as gfx
import spPallet, spBall
        
#------------------------------------------------------------
#Funciones
#------------------------------------------------------------

def texto(texto, posx, posy, color =(255,255,255)):
    fuente = pygame.font.Font(cfg.fonts + "DroidSans.ttf",25)
    salida = pygame.font.Font.render(fuente, texto,1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect
#------------------------------------------------------------

"""
la funcion main sirve para indicarle al compilador que si este archivo es
importado desde otro script, no ejecute la funcion main
"""
def main():
    screen = pygame.display.set_mode((cfg.width,cfg.height))
    pygame.display.set_caption(cfg.projectName)
    
    puntos = [0,0]
    clock = pygame.time.Clock()
    
    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        
        screen.blit(p_jug, p_jug_rect)
        screen.blit(p_cpu, p_cpu_rect)
                
        pygame.display.flip()#Que hace esto?
    return 0
if __name__ == '__main__':
    pygame.init()
    main()
