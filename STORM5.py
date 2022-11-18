import pygame
import random
import time
pygame.init()
pygameDisplay = pygame.display
pygameDisplay.set_caption("STORM 5")
altura = 560
largura = 1000
tamanho = (largura, altura)
gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
gameEvents = pygame.event
branco = (255,255,255)
vermelho=(255,100,100)
preto=(0,0,0)
fundo = pygame.image.load("assets2/fundo2.jpg")
iron = pygame.image.load("assets2/naruto.png")
missile = pygame.image.load("assets2/s1.png")




def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",15)
    textoDisplay = fonte.render(texto,True,preto)
    gameDisplay.blit(textoDisplay, (880,100))
    pygameDisplay.update()

def morreu():
    fonte  = pygame.font.Font("freesansbold.ttf",95)
    fonte2  = pygame.font.Font("freesansbold.ttf",45)
    textoDisplay = fonte.render("GAME OVER ",True,vermelho)
    textoDisplay2 = fonte2.render("press enter to continue ",True,preto)
    gameDisplay.blit(textoDisplay, (150,150))
    gameDisplay.blit(textoDisplay2, (150,350))
    pygameDisplay.update()

def jogar():
    jogando = True
    ironX = 500
    ironY = 400
    movimentoIronX = 0
    movimentoIrony = 0
    larguraIron = 110
    alturaIron = 156
    alturaMissile =60
    larguraMissile =60
    posicaoMissileX = 400
    posicaoMissileY = -240
    velocidadeMissile = 1
    pontos = 0
    pygame.mixer.music.load("assets2/passaro azul.mp3")
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(1)

    missileSound = pygame.mixer.Sound("assets2/shu3.mp3")
    missileSound.set_volume(+2)
    pygame.mixer.Sound.play(missileSound)

    explosaoSound = pygame.mixer.Sound("assets2/kill.mp3")
    explosaoSound.set_volume(1)
    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoIronX = -15
                elif event.key == pygame.K_RIGHT:
                    movimentoIronX = 15
                elif event.key == pygame.K_RETURN:
                    jogar()
            elif event.type == pygame.KEYUP:
                movimentoIronX = 0
            
             
        if jogando:
            if posicaoMissileY > altura:
                posicaoMissileY = -240
                posicaoMissileX = random.randint(0,largura)
                velocidadeMissile = velocidadeMissile + 1
                pontos = pontos + 1
                pygame.mixer.Sound.play(missileSound)
            else:
                posicaoMissileY =posicaoMissileY + velocidadeMissile

            if ironX + movimentoIronX >0 and ironX + movimentoIronX< largura-larguraIron:
                ironX = ironX + movimentoIronX
            gameDisplay.fill(branco)
            gameDisplay.blit(fundo,(0,0))
            gameDisplay.blit(iron, (ironX,ironY))
            
            gameDisplay.blit(missile, (posicaoMissileX,posicaoMissileY))
            escreverTexto ("Pontos: "+str(pontos))

            pixelsXIron = list(range(ironX, ironX+larguraIron))
            pixelsYIron = list(range(ironY, ironY+alturaIron))

            pixelXMissile = list(range(posicaoMissileX, posicaoMissileX+larguraMissile))
            pixelYMissile = list(range(posicaoMissileY, posicaoMissileY+alturaMissile))

            colisaoY = len(list(set(pixelYMissile) & set(pixelsYIron) ))
            if colisaoY > 0:
                colisaoX = len(list(set(pixelXMissile) & set(pixelsXIron) ))
                print(colisaoX)
                if colisaoX > 45:
                    morreu()
                    jogando=False
                    pygame.mixer.music.stop()
                          
                    
                    pygame.mixer.Sound.play(explosaoSound)


        pygameDisplay.update()
        clock.tick(120)

jogar()