# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha')

# ----- Inicia assets
PALAVRA_WIDTH = 50
PALAVRA_HEIGHT = 38
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('assets/img/praia.png').convert()
palavra_img = pygame.image.load('assets/img/teste.png').convert_alpha()
palavra_img = pygame.transform.scale(palavra_img, (150, 50))
# ----- Inicia estruturas de dados
# Definindo os novos tipos
class PALAVRA(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-PALAVRA_WIDTH)
        self.rect.y = random.randint(-100, -PALAVRA_HEIGHT)
        self.speedx = random.randint(-1, 1)
        self.speedy = random.randint(2, 3)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-PALAVRA_WIDTH)
            self.rect.y = random.randint(-100, -PALAVRA_HEIGHT)
            self.speedx = random.randint(-1, 1)
            self.speedy = random.randint(2, 3)

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 60

# Criando dois meteoros
#palavra1 = PALAVRA(palavra_img)
#palavra2 = PALAVRA(palavra_img)
all_palavras = pygame.sprite.Group()
for i in range(8):
    palavra = PALAVRA(palavra_img)
    all_palavras.add(palavra)
# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    #palavra1.update()
    #palavra2.update()
    all_palavras.update()
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando meteoros
    #window.blit(palavra1.image, palavra1.rect)
    #window.blit(palavra2.image, palavra2.rect)
    all_palavras.draw(window)
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
