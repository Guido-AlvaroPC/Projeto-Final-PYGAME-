import pygame
import random
pygame.init()


width,height = (800,600)
screen = pygame.display.set_mode((width,height))

def gera_palavra():
    global words
    wordStr = random.choice(words).strip()
    return DestroiPalavras(wordStr)

class DestroiPalavras(pygame.sprite.Sprite):
    def __init__(self, word):
        global width
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("assets/font/font.ttf",40) #escreve a fonte
        self.originalWord = word
        self.word = word
        self.image = self.font.render(self.word, True, (0,0,0))
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.centerx = random.uniform(self.rect.width/2,width-self.rect.width/2)
        
    def checa_letra(self, letter):
        #verifica uma letra que o jogador digitou
        if letter == self.word[0]:
            self.word = self.word[1:]
            self.atualiza_imagem()
        return self.word == ""

    def atualiza_imagem(self):
        self.image = self.font.render(self.word, True, (255,0,0))
        right = self.rect.right
        bottom = self.rect.bottom
        self.rect = self.image.get_rect()
        self.rect.right = right
        self.rect.bottom = bottom

    def atualiza(self):
        global height
        global speed, running, score, extra_words, currentword
        speedC = len(self.originalWord)
        if speedC < len(currentword.originalWord):
            speedC = len(currentword.originalWord)
        if speedC < 5:
            speedC = 5
        old_top = self.rect.top
        self.rect.top += speed / speedC
        if old_top < height/4 and self.rect.top >= height/4:
            extra_words.append(gera_palavra())
        if self.rect.bottom >= height:
            lose()
    def lose():
            print ("GAME OVER!"),score
            running = False

running = True
speed = 10
wordfile = open('words.txt', 'r')
words = wordfile.readlines()
currentword = gera_palavra()
extra_words = []
wordfile.close()
score = 0

score_font = pygame.font.Font("assets/font/score_font.ttf",60)
background = pygame.image.load("assets/img/praia.png").convert()

clock = pygame.time.Clock()
while running: #Loop Principal
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #Para o Jogo
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 
            else:
                if currentword.checa_letra(event.unicode):
                    speed += 3
                    score += 1
                    if len(extra_words) > 0:
                        lowestwordindex = 0
                        for i in range(len(extra_words)):
                            if extra_words[i].rect.bottom > extra_words[lowestwordindex].rect.bottom:
                                lowestwordindex = i
                        currentword = extra_words.pop(lowestwordindex)
                        
                    else:
                        currentword = gera_palavra()
    currentword.atualiza()
    for i in extra_words:
        i.update()

    score_surf = score_font.render("SCORE:"+str(score), True, (0,255,0))
    
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    screen.blit(score_surf,(0,530))
    for i in extra_words:
        screen.blit(i.image, i.rect)
    pygame.draw.line(screen,(0,255,0),(width/2, height),(currentword.rect.left+7, currentword.rect.bottom),14)
    screen.blit(currentword.image, currentword.rect)
    pygame.display.flip()
pygame.quit()
