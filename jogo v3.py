# ===== Inicialização =====
# ----- Importa e inicia pacotes

import pygame
import random
from assets import CANHAO_IMG

from config import IMG_DIR
pygame.init()

# ----- Gera tela principal
WIDTH = 920
HEIGHT = 690
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Teste')

# ----- Inicia assets
fundo = pygame.image.load('assets/img/praia.png').convert()
fonte = pygame.font.SysFont('arial',30,True,True)

#------ Inicia Musicas

musica = pygame.mixer.music.load('assets/snd/theme.mp3')
volume = pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

# ----- Inicia estruturas de dados
game = True
lista_palavras = ['Bola', 'Areia', 'Sol', 'Água', 'Vento', 'Churrasco', 'Carangueijo']
#palavras = random.choice(lista_palavras)
palavra_x = random.randint(0,500)
palavra_y = random.randint(-100,0)
palavra_velocidadex = random.randint(-3,3)
palavra_velocidadey = random.randint(2,9)
clock = pygame.time.Clock()
FPS = 60

class PALAVRA(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets/img/canhão.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        #self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(-100,HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)
    def uptade (self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

game = True
Clock = pygame.time.Clock()
FPS = 60

pal = PALAVRA(CANHAO_IMG)

todas_palavras = pygame.sprite.Group()
todas_sprites = pygame.sprite.Group()


# ===== Loop principal =====
while game:
    clock.tick(FPS)


    # ----- Trata eventos

    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False


    while len(todas_palavras) < 10:
        palavra = PALAVRA(random.choice(lista_palavras))
        todas_palavras.add(palavra)
        todas_sprites.add(palavra)

    todas_sprites.update()
    pal.update(

    window.blit(pal.image, pal.rect)
    )


    # ----- Gera saídas
    #window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(fundo, (0, 0))
    

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizado