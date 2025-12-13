import pygame
import random
import sys

pygame.init()

L = 600
A = 400

#imagens
nave = pygame.image.load("Nave_atari.png")
fundo = pygame.image.load("espaço.webp")
nave2 = pygame.image.load("nave2.png")
engrenagem = pygame.image.load("engrenagem.png")


def escala(imagem,escala):
    imagem = pygame.transform.scale(imagem, (escala, escala))
    return imagem

nave = escala(nave, 40)
nave2 = escala(nave2, 40)
engrenagem = escala(engrenagem, 40)
fundo = pygame.transform.scale(fundo, (L, A))

# Botões
botao_voltar = pygame.Rect(200,180,200,50)
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


def alterar_tela(cor):
    tela.fill(cor)


def criar_projetil(rect_player):
    return {
        "x": rect_player.centerx - 5,
        "y": rect_player.centery - 5,
        "tam": 10,
        "vel": 7
    }


def atualizar_projeteis(projeteis, rect_obs, obstaculo, ponto):
    for p in projeteis[:]:
        p["y"] -= p["vel"]
        rect_p = pygame.Rect(p["x"], p["y"], p["tam"], p["tam"])

        if rect_p.colliderect(rect_obs):
            projeteis.remove(p)
            obstaculo["y"] = -obstaculo["tam"]
            obstaculo["x"] = random.randint(0, L - obstaculo["tam"])
            ponto += 1
            obstaculo["vel"] += 0.2

        elif p["y"] < 0:
            projeteis.remove(p)

        else:
            pygame.draw.rect(tela, amarelo, rect_p)

    return projeteis, obstaculo, ponto


# ---------- GAME OVER ----------
def game_over():
    rodando = True

    # Criar dois botões centralizados
    largura_botao = 220
    altura_botao = 55

    botao_continue = pygame.Rect((L - largura_botao)//2, 130, largura_botao, altura_botao)
    botao_menu = pygame.Rect((L - largura_botao)//2, 210, largura_botao, altura_botao)

    while rodando:
        alterar_tela(preto)

        # --- DESENHAR BOTÕES ---
        pygame.draw.rect(tela, amarelo, botao_continue)
        pygame.draw.rect(tela, amarelo, botao_menu)

        # --- TEXTOS CENTRALIZADOS ---
        texto_continue = fonte.render("Continuar", True, vermelho)
        texto_menu = fonte.render("Voltar ao menu", True, azul_claro)

        tela.blit(texto_continue, (botao_continue.centerx - texto_continue.get_width()//2,
                                   botao_continue.centery - texto_continue.get_height()//2))

        tela.blit(texto_menu, (botao_menu.centerx - texto_menu.get_width()//2,
                               botao_menu.centery - texto_menu.get_height()//2))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_continue.collidepoint(evento.pos):
                    return "continue"
                if botao_menu.collidepoint(evento.pos):
                    return "menu"



def reiniciar():
    player = {"x": L // 2, "y": A - 50, "vel": 5, "tam": 40}
    obstaculo = {"x": random.randint(0, L - 40), "y": -50, "vel": 5, "tam": 40}
    bonus = {"x": random.randint(0, L - 40), "y": -50, "vel": 5, "tam": 40}
    projeteis = []
    ponto = 0
    return player, obstaculo, bonus, projeteis, ponto


# ---------- MENU ----------
def menu():
    rodando = True
    while rodando:
        alterar_tela(branco)

        pygame.draw.rect(tela, azul, botao_jogar)
        pygame.draw.rect(tela, azul, botao_opcoes)
        pygame.draw.rect(tela, vermelho, botao_sair)

        texto_jogar = fonte.render("Jogar", True, branco)
        texto_opcoes = fonte.render("Opções", True, branco)
        texto_sair = fonte.render("Sair", True, branco)

        tela.blit(texto_jogar, (botao_jogar.x + 60, botao_jogar.y + 10))
        tela.blit(texto_opcoes, (botao_opcoes.x + 50, botao_opcoes.y + 10))
        tela.blit(texto_sair, (botao_sair.x + 70, botao_sair.y + 10))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()     # ← ADICIONADO
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar.collidepoint(evento.pos):
                    return "jogo"
                elif botao_opcoes.collidepoint(evento.pos):
                    print("Tela de opções ainda não implementada")
                elif botao_sair.collidepoint(evento.pos):
                    return "sair"


# ---------- JOGO PRINCIPAL ----------
def jogo():
    player, obstaculo, bonus, projeteis, ponto = reiniciar()
    relogio = pygame.time.Clock()

    while True:
        relogio.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()      # ← ADICIONADO
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    projeteis.append(criar_projetil(rect_player))

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and player["x"] > 0:
            player["x"] -= player["vel"]
        if teclas[pygame.K_RIGHT] and player["x"] < L - player["tam"]:
            player["x"] += player["vel"]
        if teclas[pygame.K_UP] and player["y"] > 0:
            player["y"] -= player["vel"]
        if teclas[pygame.K_DOWN] and player["y"] < A - player["tam"]:
            player["y"] += player["vel"]

        obstaculo["y"] += obstaculo["vel"]
        bonus["y"] += bonus["vel"]

        if obstaculo["y"] > A:
            obstaculo["y"] = -obstaculo["tam"]
            obstaculo["x"] = random.randint(0, L - obstaculo["tam"])
            ponto += 1
            obstaculo["vel"] += 0.2

        if bonus["y"] > A:
            bonus["y"] = -bonus["tam"]
            bonus["x"] = random.randint(0, L - bonus["tam"])

        rect_player = pygame.Rect(player["x"], player["y"], player["tam"], player["tam"])
        rect_obs = pygame.Rect(obstaculo["x"], obstaculo["y"], obstaculo["tam"], obstaculo["tam"])
        rect_bonus = pygame.Rect(bonus["x"], bonus["y"], bonus["tam"], bonus["tam"])

        if rect_player.colliderect(rect_obs):
            escolha = game_over()
            if escolha == "menu":
                return
            elif escolha == "continue":
                player, obstaculo, bonus, projeteis, ponto = reiniciar()
                continue

        if rect_player.colliderect(rect_bonus):
            ponto += 2
            bonus["vel"] += 0.5
            bonus["y"] = -bonus["tam"]
            bonus["x"] = random.randint(0, L - bonus["tam"])

        alterar_tela(preto)
        pygame.draw.rect(tela, azul, rect_player)
        pygame.draw.rect(tela, vermelho, rect_obs)
        pygame.draw.circle(tela, amarelo, rect_bonus.center, rect_bonus.width // 2)
        tela.blit(fundo, (0,0))

        projeteis, obstaculo, ponto = atualizar_projeteis(projeteis, rect_obs, obstaculo, ponto)

        texto = fonte.render(f"Pontos: {ponto}", True, branco)
        tela.blit(texto, (10, 10))

        tela.blit(nave, (player["x"], player["y"]))
        tela.blit(nave2, (obstaculo["x"], obstaculo["y"]))
        tela.blit(engrenagem, (bonus["x"], bonus["y"]))

        pygame.display.update()


# ---------- LOOP PRINCIPAL ----------
while True:
    acionamento = menu()

    if acionamento == "jogo":
        jogo()
    elif acionamento == "sair":
        pygame.quit()    # ← ADICIONADO
        sys.exit()