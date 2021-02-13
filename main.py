from typing import Tuple
import pygame
from pygame.locals import *  
from sys import exit  
from random import randint 
from time import sleep

pygame.init()
pygame.mixer.init() 

pygame.mixer.music.set_volume(0.1)  
musica_de_fundo = pygame.mixer.music.load('sons/Tec-Pix.wav')  
pygame.mixer.music.play(-1) 

"""barulho_colisao = pygame.mixer.Sound('sons/smw_coin.wav')"""

largura = 640
altura = 480
x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

velocidade = 3
x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True) 

relogio = pygame.time.Clock() 
tela = pygame.display.set_mode((largura, altura))  
pygame.display.set_caption('Snake Game com estilo')  
lista_cobra = []
comprimento_inicial = 10
morreu = False
inicio = True


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 0, 255), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo() :
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cabeça, lista_cobra, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 10
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2) 
    lista_cobra = []
    lista_cabeça = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False
     

def mensagemInicial():
    msgInfo = 'Movimentação: W (cima), S (baixo), A (esquerda), D (direita)'
    txtInfo = fonte.render(msgInfo, True, (0,255,0))
    
    #pygame.display.update()

    fonte2 = pygame.font.SysFont('arial', 20, True, True )
    texto_formatado = fonte2.render(msgInfo, True, (84, 22, 180))
    ret_texto = texto_formatado.get_rect()
    ret_texto.center = (largura//2, altura//2)
    tela.blit(texto_formatado,ret_texto)
    pygame.display.update()
    sleep(5)
    
 
while True:  
    if inicio == True:
        mensagemInicial()
    inicio = False
    relogio.tick(90)  
    tela.fill((0,0,0)) 
    msg = f'Score: {pontos}' 
    txt = fonte.render(msg, True, (84, 22, 180))
    for event in pygame.event.get():  
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                exit()

            if event.key == K_a:  
                if x_controle == velocidade:
                    ...
                else:
                    x_controle = -velocidade
                    y_controle = 0

            if event.key == K_d:
                if x_controle == -velocidade:
                    ...
                else:
                    x_controle = velocidade
                    y_controle = 0

            if event.key == K_w:
                if y_controle == velocidade:
                    ...
                else:
                    y_controle = -velocidade
                    x_controle = 0

            if event.key == K_s:
                if y_controle == -velocidade:
                    ...
                else:
                    y_controle = velocidade
                    x_controle = 0
 

    x_cobra += x_controle
    y_cobra += y_controle

    cobra = pygame.draw.rect(tela, (128, 0, 128), (x_cobra, y_cobra, 20, 20))  
    maca = pygame.draw.rect(tela, (252,15,192), (x_maca, y_maca, 20, 20)) 

    if cobra.colliderect(maca):  
        x_maca = randint(40, 600)
        y_maca = randint(40, 430)
        pontos += 1
        #barulho_colisao.play() 
        comprimento_inicial +=1

    lista_cabeça = []  
    lista_cabeça.append(x_cobra)
    lista_cabeça.append(y_cobra)
    

    lista_cobra.append(lista_cabeça)

    
    
    if lista_cobra.count(lista_cabeça) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True )
        mensagem = 'Gamer Over? Prencione R'
        texto_formatado = fonte2.render(mensagem, True, (88,22,180))
        ret_texto = texto_formatado.get_rect()
        morreu = True
        while morreu:
            tela.fill((0,0,0))
            for event in pygame.event.get():
            
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado,ret_texto)
            pygame.display.update()
    
    if x_cobra > largura: 
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura

    if y_cobra > altura:
        y_cobra = 0
    

    if len(lista_cobra ) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
    tela.blit(txt, (450, 40))
    pygame.display.update() 
