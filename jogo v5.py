import pygame
import random
pygame.init()


width,height = (800,600)
screen = pygame.display.set_mode((width,height))

def gera_palavra():
    global words
    wordStr = random.choice(words).strip()
    return TypingGameWord(wordStr)

class TypingGameWord(pygame.sprite.Sprite):
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