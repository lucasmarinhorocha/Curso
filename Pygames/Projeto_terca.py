import pygame
import random
import sys

pygame.init()

L = 600
A = 400

# Botões
botao_jogar = pygame.Rect(200, 100, 200, 50)
botao_opcoes = pygame.Rect(200, 180, 200, 50)
botao_sair = pygame.Rect(200, 260, 200, 50)

# Tela
tela = pygame.display.set_mode((L, A))
pygame.display.set_caption("Desvie do Bloco!")

# CORES
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (200, 0, 0)
azul = (0, 80, 200)
amarelo = (255, 255, 0)
azul_claro = (38, 170, 182)

# Fonte
fonte = pygame.font.SysFont(None, 40)

# Objetos
player = {"x": L // 2, "y": A - 50, "vel": 5, "tam": 40}
obstaculo = {"x": random.randint(0, L - 40), "y": -50, "vel": 5, "tam": 40}
bonus = {"x": random.randint(0, L - 40), "y": -50, "vel": 5, "tam": 40}
projetil = {"x": 0, "y": 0, "vel": 50, "tam": 10}


ponto = 0


def alterar_tela(cor):
    tela.fill(cor)


def menu():
    rodando = True
    while rodando:
        alterar_tela(branco)

        # Desenhar botões
        pygame.draw.rect(tela, azul, botao_jogar)
        pygame.draw.rect(tela, azul, botao_opcoes)
        pygame.draw.rect(tela, vermelho, botao_sair)

        # Texto nos botões
        texto_jogar = fonte.render("Jogar", True, branco)
        texto_opcoes = fonte.render("Opções", True, branco)
        texto_sair = fonte.render("Sair", True, branco)

        tela.blit(texto_jogar, (botao_jogar.x + 60, botao_jogar.y + 10))
        tela.blit(texto_opcoes, (botao_opcoes.x + 50, botao_opcoes.y + 10))
        tela.blit(texto_sair, (botao_sair.x + 70, botao_sair.y + 10))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar.collidepoint(evento.pos):
                    jogo()
                elif botao_opcoes.collidepoint(evento.pos):
                    print("Tela de opções ainda não implementada")
                elif botao_sair.collidepoint(evento.pos):
                    rodando = False


def jogo():
    global ponto
    rodando = True
    relogio = pygame.time.Clock()

    while rodando:
        relogio.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # CONTROLE DO JOGADOR
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and player["x"] > 0:
            player["x"] -= player["vel"]
        if teclas[pygame.K_RIGHT] and player["x"] < L - player["tam"]:
            player["x"] += player["vel"]

       
       # if projetil["x"] < player["x"]:
        #    projetil["x"] += player["vel"]
        #if projetil["x"] > player["x"]:
        #    projetil["x"] -= player["vel"]



        # MOVIMENTO DOS OBJETOS
        obstaculo["y"] += obstaculo["vel"]
        bonus["y"] += bonus["vel"]

        # RESETAR OBSTÁCULO
        if obstaculo["y"] > A:
            obstaculo["y"] = -obstaculo["tam"]
            obstaculo["x"] = random.randint(0, L - obstaculo["tam"])
            ponto += 1
            obstaculo["vel"] += 0.2

        # RESETAR BÔNUS
        if bonus["y"] > A:
            bonus["y"] = -bonus["tam"]
            bonus["x"] = random.randint(0, L - bonus["tam"])

        # TRANSFORMAR EM RECT
        rect_projetil = pygame.Rect(projetil["x"],projetil["y"],projetil["tam"],projetil["tam"])
        rect_player = pygame.Rect(player["x"], player["y"], player["tam"], player["tam"])
        rect_obs = pygame.Rect(obstaculo["x"], obstaculo["y"], obstaculo["tam"], obstaculo["tam"])
        rect_bonus = pygame.Rect(bonus["x"], bonus["y"], bonus["tam"], bonus["tam"])

        # COLISÃO COM OBSTÁCULO
        if rect_player.colliderect(rect_obs):
            print("Game Over!")
            rodando = False

        # COLISÃO COM BÔNUS
        if rect_player.colliderect(rect_bonus):
            ponto += 2
            bonus["vel"] += 0.5
            bonus["y"] = -bonus["tam"]
            bonus["x"] = random.randint(0, L - bonus["tam"])

        # DESENHO
        alterar_tela(preto)

        pygame.draw.rect(tela, azul, rect_player)
        pygame.draw.rect(tela, vermelho, rect_obs)
        pygame.draw.circle(tela, amarelo, rect_bonus.center, rect_bonus.width // 2)
        pygame.draw.rect(tela,azul_claro,rect_projetil)
        texto = fonte.render(f"Pontos: {ponto}", True, branco)
        tela.blit(texto, (10, 10))

        pygame.display.update()


# Inicia pelo menu
menu()

pygame.quit()
sys.exit()
