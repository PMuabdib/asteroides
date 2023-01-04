import pygame

class Misil(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMisil = pygame.image.load("imagenes/misil01.png")
        self.rect = self.imagenMisil.get_rect()
        self.velocidadDisparo = 10
        self.rect.top = posY
        self.rect.left = posX
    def recorrido(self):
        self.rect.top -= self.velocidadDisparo
    def dibujar(self, superficie):
        superficie.blit(self.imagenMisil, self.rect)