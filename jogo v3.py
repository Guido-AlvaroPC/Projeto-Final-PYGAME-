# ===== Inicialização =====
# ----- Importa e inicia pacotes

import pygame
import random
pygame.init()

# ----- Gera tela principal
WIDTH = 920
HEIGHT = 690
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Teste')

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
    def __init__(self,palavra):
        pygame.sprite.Sprite.__init__(self,img)
        


        

# ----- Inicia assets
fundo = pygame.image.load('assets/img/praia.png').convert()
fonte = pygame.font.SysFont('arial',30,True,True)

#------ Inicia Musicas

musica = pygame.mixer.music.load('assets/snd/theme.mp3')
volume = pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

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


    # ----- Gera saídas
    #window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(fundo, (0, 0))
    

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizado