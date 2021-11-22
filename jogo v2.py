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
palavra_x = random.randint(0,500)
palavra_y = random.randint(-100,0)
palavra_velocidadex = random.randint(-3,3)
palavra_velocidadey = random.randint(2,9)
clock = pygame.time.Clock()
FPS = 60
# ----- Inicia assets
fundo = pygame.image.load('assets/img/praia.png').convert()
fonte = pygame.font.SysFont('arial',30,True,True)

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    texto = f'Bola'
    txt_tela = fonte.render(texto, True,(255,255,255))

    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    palavra_x += palavra_velocidadex
    palavra_y += palavra_velocidadey


    # ----- Gera saídas
    #window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(fundo, (0, 0))
    window.blit(txt_tela, (palavra_x,palavra_y))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizado