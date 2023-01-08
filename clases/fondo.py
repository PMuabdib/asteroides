import pygame
class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenFondo = pygame.image.load("imagenes/FondoAsteroides.png")
        self.rect = self.imagenFondo.get_rect()
    def cargar(self, superficie):
        superficie.blit(self.imagenFondo, self.rect)
    def musica(self):
        pygame.mixer.music.load("sonidos/388880.wav")  # Música de fondo
        pygame.mixer.music.play(-1)