#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import pygame
import director
import sceneGame

def main():
    drctr = director.Director()
    scene = sceneGame.SceneGame(drctr)
    drctr.change_scene(scene)
    drctr.loop()

if __name__ == '__main__':
    pygame.init()
    main()

