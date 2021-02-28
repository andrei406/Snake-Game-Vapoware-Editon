import pygame


largura = 640
altura = 480

pygame.init()
sprite_sheet = pygame.image.load('snake spritesheet calciumtrice - vapowave.png').convert_alpha()

class cobra(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_cobra = []

        for i in range(4): # Se almentar um aqui, almente mais um na def update na primeira condição  
            tamanho = 5
            img = sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32*tamanho, 32*tamanho))
            self.imagens_cobra.append(img)

        self.index_lista = 0
        self.image = self.imagens_cobra[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (largura//2, altura//2)

    def update(self):
        if self.index_lista > 3:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_cobra[int(self.index_lista)]

