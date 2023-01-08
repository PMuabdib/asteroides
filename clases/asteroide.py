import pygame

class Asteroide (pygame.sprite.Sprite):
    def __init__(self, posX, posY, velocidad):
        pygame.sprite.Sprite.__init__(self)
        self.imagenAsteroide = pygame.image.load("imagenes/asteroide.png")
        self.rect = self.imagenAsteroide.get_rect()
        self.velocidad = velocidad
        self.rect.top = posY
        self.rect.left = posX


    def recorrido(self):
        self.rect.top += self.velocidad

    def dibujar(self, superficie):
        superficie.blit(self.imagenAsteroide, self.rect)

    def aumentarVelocidad(self):
        self.velocidad += 10
