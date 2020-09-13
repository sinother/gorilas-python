import pygame, sys, random
pygame.init()

# Definir colores
BLACK   = (0,0,0)
WHITE   = (255,255,255)
GREEN   = (0,255,0)
RED     = (255,0,0)
BLUE    = (0,0,255)

size = (800, 500)

# crear ventana

screen = pygame.display.set_mode(size)

PrimerEdificio = random.randint (50, 450)
SegundoEdificio = random.randint (50, 450)
TercerEdificio = random.randint (50, 450)
CuartoEdificio = random.randint (50, 450)
QuintoEdificio = random.randint (50, 450)
SextoEdificio = random.randint (50, 450)
SeptimoEdificio = random.randint (50, 450)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #Color de fondo
    screen.fill(WHITE)

    #ZONA DE DIBUJO
    pygame.draw.rect(screen, BLACK, (25, 500, 80, -PrimerEdificio))
    pygame.draw.rect(screen, BLACK, (130, 500, 80, -SegundoEdificio))
    pygame.draw.rect(screen, BLACK, (235, 500, 80, -TercerEdificio))
    pygame.draw.rect(screen, BLACK, (340, 500, 80, -CuartoEdificio))
    pygame.draw.rect(screen, BLACK, (445, 500, 80, -QuintoEdificio))
    pygame.draw.rect(screen, BLACK, (550, 500, 80, -SextoEdificio))
    pygame.draw.rect(screen, BLACK, (655, 500, 80, -SeptimoEdificio))

    #ZONA DE DIBUJO


    #actualizar pantalla
    pygame.display.flip()