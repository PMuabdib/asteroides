import pygame, sys
from pygame.locals import *
from random import randint
from time import time
from clases import jugador
from clases import asteroide

# DEFINICIÓN DE VALRIABLES Y CONSTANTES
#######################################
ALTO_VENTANA = 800 # Alto de la ventana donde cargaremos el juego
ANCHO_VENTANA = 400 # Ancho de la ventana donde cargaremos el juego
colorFuente = (255,255,255) # Color para la fuente del marcador

listaAsteroides = []

puntos = 0 # Variable para la puntuación del juego


jugando = True


# FUNCIÓN DE CARGA DE ASTEROIDES
################################
def cargarAsteroides(x, y):
    meteoro = asteroide.Asteroide(x, y)
    listaAsteroides.append(meteoro)


# FUNCIÓN PRINCIPAL
###################
def gameOver():
    global jugando
    jugando = False
    for asteroide in listaAsteroides:
        listaAsteroides.remove(asteroide)


def meteoritos():
    pygame.init()
    # Cargamos la ventana
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    # Cargamos el fondo
    fondo = pygame.image.load("imagenes/FondoAsteroides.png")
    # Titulo
    pygame.display.set_caption('Asteroides')
    # Música de fondo
    pygame.mixer.music.load("sonidos/388880.wav")
    pygame.mixer.music.play(-1) # Reproducir en bucle infinito '-1'
    # Sonido Colisión
    sonidoColision =  pygame.mixer.Sound("sonidos/394128.wav")
    # Sonido destruccion asteroide
    sonidoDestruccion = pygame.mixer.Sound("sonidos/472061.wav")
    # Fuente para el marcador
    fuenteMarcador = pygame.font.SysFont("Arial", 20)
    fuenteGameOver = pygame.font.SysFont("Arial", 40)
    # Creamos objeto jugador
    nave = jugador.Nave()
    # Variable contador de tiempo
    contador = 0

    # Ciclo del juego
    while True:
        ventana.blit(fondo, (0, 0)) # Dibujamos fondo
        nave.dibujar(ventana)  # Dibujamos nave
        # Marcador
        global puntos
        textoMarcador = fuenteMarcador.render(f'Puntos: {str(puntos)}',0,colorFuente)
        ventana.blit(textoMarcador, (5,5))
        # Dibujamos Meteoritos cada cierto tiempo
        tiempo = time()
        if (tiempo - contador > 1) and (nave.vida == True):
            contador = tiempo
            posX = randint(10, 380)
            posY = -20
            cargarAsteroides(posX, posY)
        # Comprobamos lista Asteroides
        if len(listaAsteroides)>0:
            for asteroide in listaAsteroides:
                asteroide.dibujar(ventana)
                asteroide.recorrido()
                if asteroide.rect.top > 800:
                    listaAsteroides.remove(asteroide)
                else:
                    if asteroide.rect.colliderect(nave.rect):
                        listaAsteroides.remove(asteroide)
                        sonidoColision.play()
                        nave.vida = False
                        gameOver()

        # Disparos/proyectiles
        if len(nave.listaDisparo) > 0:
            for disparo in nave.listaDisparo:
                disparo.dibujar(ventana)
                disparo.recorrido()
                if disparo.rect.top < -10:
                    nave.listaDisparo.remove(disparo)
                else:
                    for asteroide in listaAsteroides:
                        if disparo.rect.colliderect(asteroide):
                            listaAsteroides.remove(asteroide)
                            nave.listaDisparo.remove(disparo)
                            sonidoDestruccion.play()
                            puntos += 1
        nave.mover()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if nave.vida == True:
                    if evento.key == K_LEFT:
                        nave.rect.left -= nave.velocidad
                    elif evento.key == K_RIGHT:
                        nave.rect.right += nave.velocidad
                    elif evento.key == K_SPACE:
                        x, y = nave.rect.center
                        nave.disparar(x, y)
        if jugando == False:
            textoGameOver = fuenteGameOver.render("Game Over", 0, colorFuente)
            ventana.blit(textoGameOver, (100, 300))
            pygame.mixer.music.fadeout(3000)
        pygame.display.update()



if __name__ == '__main__':
    meteoritos()