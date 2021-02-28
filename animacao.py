import pygame
from pygame import locals
from sys import exit
from objetos import cobra

from pygame.constants import QUIT

largura = 640
altura = 480

cor_tela = (0, 0, 0)
fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game: vapowave edition')

x = 0 # variavel de contra


todas_sprites = pygame.sprite.Group()
snake = cobra()
todas_sprites.add(snake)

relogio = pygame.time.Clock()

def mensagemInicial():
    msgInfo = 'Snake Game: vapowave edition'
    txtInfo = fonte.render(msgInfo, True, (0,255,0))
    
    #pygame.display.update()

    fonte2 = pygame.font.SysFont('arial', 20, True, True )
    texto_formatado = fonte2.render(msgInfo, True, (84, 22, 180))
    ret_texto = texto_formatado.get_rect()
    ret_texto.center = (largura//2, altura//3)
    tela.blit(texto_formatado,ret_texto)
    pygame.display.update()

while True:
    relogio.tick(30)
    
    tela.fill(cor_tela)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    todas_sprites.draw(tela)
    todas_sprites.update()
    mensagemInicial()
    pygame.display.flip()