import pygame, sys
from pygame.locals import *

from clases import jugador

# DEFINICIÓN DE VALRIABLES Y CONSTANTES
#######################################
ALTO_VENTANA = 800 # Alto de la ventana donde cargaremos el juego
ANCHO_VENTANA = 400 # Ancho de la ventana donde cargaremos el juego

jugando = True


# FUNCIÓN PRINCIPAL
###################
def meteoritos():
    pygame.init()
    # Cargamos la ventana
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    # Cargamos el fondo
    fondo = pygame.image.load("imagenes/FondoAsteroides.png")
    # Titulo
    pygame.display.set_caption('Asteroides')
    # Creamos objeto jugador
    nave = jugador.Nave()

    # Ciclo del juego
    while True:
        ventana.blit(fondo, (0, 0)) # Dibujamos fondo
        nave.dibujar(ventana)  # Dibujamos nave
        # Disparos/proyectiles
        if len(nave.listaDisparo) > 0:
            for disparo in nave.listaDisparo:
                disparo.dibujar(ventana)
                disparo.recorrido()
                if disparo.rect.top < -10:
                    nave.listaDisparo.remove(disparo)
        nave.mover()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    nave.rect.left -= nave.velocidad
                elif evento.key == K_RIGHT:
                    nave.rect.right += nave.velocidad
                elif evento.key == K_SPACE:
                    x, y = nave.rect.center
                    nave.disparar(x, y)
        pygame.display.update()



if __name__ == '__main__':
    meteoritos()