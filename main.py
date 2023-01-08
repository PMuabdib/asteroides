import pygame, sys
from pygame.locals import *
from random import randint
from time import time
from clases import jugador
from clases import asteroide
from clases import fondo
# DEFINICIÓN DE VALRIABLES Y CONSTANTES
#######################################
ALTO_VENTANA = 800                                              # Alto de la ventana donde cargaremos el juego
ANCHO_VENTANA = 400                                             # Ancho de la ventana donde cargaremos el juego
colorFuente = (255,255,255)                                     # Color para la fuente del marcador
listaAsteroides = []                                            # Lista de los asteroides que están activos
puntos = 0                                                      # Variable para la puntuación del juego
jugando = True                                                  # Bandera que nos permite saber si el juego a acabado

# FUNCIÓN DE CARGA DE ASTEROIDES
################################
def cargarAsteroides(x, y):
    meteoro = asteroide.Asteroide(x, y)
    listaAsteroides.append(meteoro)

# FUNCIÓN FIN DE JUEGO
######################
def gameOver():
    global jugando
    jugando = False
    for asteroide in listaAsteroides:
        listaAsteroides.remove(asteroide)

# FUNCIÓN PRINCIPAL
###################
def meteoritos():
    # INICIALIZAMOS VARIABLES Y CONFIGURACIONES
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))                        # Cargamos la ventana
    # fondo = pygame.image.load("imagenes/FondoAsteroides.png")                               # Cargamos el fondo
    pygame.display.set_caption('Asteroides')                                                # Titulo
    sonidoColision =  pygame.mixer.Sound("sonidos/394128.wav")                              # Sonido Colisión nave
    sonidoDestruccion = pygame.mixer.Sound("sonidos/472061.wav")                            # Sonido destruccion asteroide
    fuenteMarcador = pygame.font.SysFont("Arial", 20)                                       # Fuente para el marcador
    fuenteGameOver = pygame.font.SysFont("Arial", 40)                                       # Fuente para el GameOver
    fuenteSeguir = pygame.font.SysFont("Arial", 15)                                         # Fuente para el GameOver
    fondoJuego = fondo.Fondo()                                                              # Creamos el objeto fondo
    nave = jugador.Nave()                                                                   # Creamos objeto jugador
    contador = 0                                                                            # Variable contador de tiempo
    fondoJuego.musica()                                                                     # Música de fondo
    # CICLO DEL JUEGO
    while True:
        fondoJuego.cargar(ventana)                                                          # Dibujamos fondo
        nave.dibujar(ventana)                                                               # Dibujamos nave
        global puntos                                                                       # Globalizamos Marcador
        global jugando
        # MOSTRAMOS EL MARCADOR
        textoMarcador = fuenteMarcador.render(f'Puntos: {str(puntos)}',0,colorFuente)
        ventana.blit(textoMarcador, (5,5))
        # CREAMOS NUEVO METEORITOS CADA CIERTO TIEMPO
        tiempo = time()
        if (tiempo - contador > 1) and (nave.vida == True):
            contador = tiempo
            posX = randint(10, 380)
            posY = -20
            cargarAsteroides(posX, posY)
        # COMPROBAMOS LA LISTA DE ASTEROIDES
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
        # COMPROBAMOS DISPAROS/PROYECTILES
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
        # COMPROBACIÓN DE LOS EVENTOS (Teclado, raton,..)
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
                else:
                    if evento.key == K_F1:
                        jugando = True
                        puntos = 0
                        meteoritos()
                    elif evento.key == K_F2:
                        pygame.quit()
                        sys.exit()

        # FIN DE LA PARTIDA
        if jugando == False:
            textoGameOver = fuenteGameOver.render("Game Over", 0, colorFuente)
            ventana.blit(textoGameOver, (100, 300))
            textoSeguir = fuenteSeguir.render("F1 para nueva partida, F2 para salir", 0, colorFuente)
            ventana.blit(textoSeguir, (75, 350))
            pygame.mixer.music.fadeout(3000)
        pygame.display.update()

# MAIN - LANZADOR
###################
if __name__ == '__main__':
    meteoritos()