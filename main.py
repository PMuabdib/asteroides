import pygame, sys
from pygame.locals import *

# DEFINICIÓN DE VALRIABLES Y CONSTANTES
#######################################
ALTO_VENTANA = 800 # Alto de la ventana donde cargaremos el juego
ANCHO_VENTANA = 400 # Ancho de la ventana donde cargaremos el juego

# FUNCIÓN PRINCIPAL
###################
def meteoritos():
    pygame.init()
    # Cargamos la ventana
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    # Cargamos el fondo
    fondo = pygame.image.load("imagenes/FondoAsteroides.png")
    ventana.blit(fondo,(0,0))
    # Titulo
    pygame.display.set_caption('Asteroides')
    # Ciclo del juego
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()



if __name__ == '__main__':
    meteoritos()