import pygame
from clases import disparo

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave = pygame.image.load("imagenes/Nave.png") # Cargamos la imagen
        self.imagenExplota = pygame.image.load("imagenes/explosion.png")
        self.rect = self.imagenNave.get_rect() # Calculamos el rectángulo de la imagen
        # Posición inicial de la nave
        self.rect.centerx = 200
        self.rect.centery = 750
        # Otros atributos
        self.velocidad = 10
        self.vida = True
        self.listaDisparo = []
        self. sonidoDisparo = pygame.mixer.Sound("sonidos/458669.ogg")
    def mover(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 364:
                self.rect.right = 364
    def disparar(self, x, y):
        if self.vida == True:
            misil = disparo.Misil(x, y)
            self.listaDisparo.append(misil)
            self.sonidoDisparo.play()
    def dibujar(self, superficie):
        if self.vida == True:
            superficie.blit(self.imagenNave, self.rect)
        else:
            superficie.blit(self.imagenExplota, self.rect)