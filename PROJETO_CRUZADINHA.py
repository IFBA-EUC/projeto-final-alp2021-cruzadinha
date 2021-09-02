import random

# Sugestão: Modo jogador 1

# Usar dicionários
lista_dicas_nivel1 = ["País onde Lionel Messi, jogador de futebol, nasceu.", "É feito de milho e cozido a vapor.", "Primeiro nome da atriz global e ex namorada do jogador de futebol Neymar Jr.", "Driblou, arremessou e é ponto!", "Animal doméstico que caça ratos.",
                      "Estrutura que permite a execução até uma determinada condição ser satisfeita (python)", "Profissional que cria, desenvolve e mantém diferentes tipos de softwares em sistemas amplos ou para uso em computadores pessoais.", "Festividade cristã que relembra o nascimento de Jesus Cristo."]
lista_dicas_nivel2 = ["Único país latino da América do Norte.", "Bolo de feijão, frito no azeite de dendê.", "Primeiro nome da Única atriz brasileira indicada ao prêmio Oscar.", "Jab, Jab, ele esquiva e finaliza com um gancho!", "Seu corpo é divido em cabeça, e tem transformação em quatro fases.",
                      "Estrutura lógica que precisa de todas entradas verdadeiras para seu resultado também ser verdadeiro.", "Profissional que zela pela segurança, conforto e tranquilidade dos passageiros do transporte aéreo", "Maior festa de rua da Bahia."]
lista_dicas_nivel3 = ["País europeu que possui o formato de uma bota.", "Feito de farinha de trigo, camarão e leite de coco.", "Primeiro nome do Cantor brasileiro de MPB, dono da música 'Apesar de você' escrita em 1970, como crítica a falta de liberdade durante a ditadura militar no Brasil", "Muita calma nessa hora! ele precisa estabilizar seu equilibrio...",
                      "Tem bico forte, língua carnosa e uma cauda longa em forma de espada.", "Fornece funções matématicas que para o seu uso é preciso ser chamada na biblioteca.", "Profissional responsável pelo estudo das mais variadas formas de vida existentes.", "Festa cristã que celebra o nascimento de João Batista."]
lista_numeros_disponiveis = [1, 2, 3, 4, 5, 6, 7, 8]
lista_pontos_jogador1 = []
lista_pontos_jogador2 = []
numero_escolhido = 1


def paisnivel1(numero_escolhido):
    print("\nA dica é:", lista_dicas_nivel1[0])
    if 5 not in lista_numeros_disponiveis and 6 in lista_numeros_disponiveis:
        print("\n",
              "-" * 37,
              "\n|   |   |   |   |   |   |   |   | A |"
              "\n-------------------------------------")
    elif 5 in lista_numeros_disponiveis and 6 not in lista_numeros_disponiveis:
        print("\n-------------------------------------"
              "\n|   |   |   |   |   |   | I |   |   |"
              "\n-------------------------------------")
    elif 5 not in lista_numeros_disponiveis and 6 not in lista_numeros_disponiveis:
        print("\n-------------------------------------"
              "\n|   |   |   |   |   |   | I |   | A |"
              "\n-------------------------------------")
    else:
        print("\n-------------------------------------"
              "\n|   |   |   |   |   |   |   |   |   |"
              "\n-------------------------------------")
    argentina = input("\nQual é o país? ")
    contador = 1
    while contador < 4:
        if argentina == "ARGENTINA":
            print("\n-------------------------------------"
                  "\n| A | R | G | E | N | T | I | N | A |"
                  "\n-------------------------------------"
                  "\nParabéns, você acertou! Ganhou +1 ponto:)")
            lista_numeros_disponiveis.remove(1)
            if jogador1 == True:
                lista_pontos_jogador1.append(1)
            else:
                lista_pontos_jogador2.append(1)
            break
        else:
            if contador == 1:
                argentina = input(
                    "\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
            if contador == 2:
                argentina = input(
                    "\nVixe, você errou. Tente novamente (última tentativa restante): ")
            if contador == 3:
                print("\nQue pena, não foi dessa vez! :(")
        contador = contador + 1


def comidanivel1(numero_escolhido):
    print("\nA dica é:", lista_dicas_nivel1[1])
    print("\n-------------------------"
          "\n|   |   |   |   |   |   |"
          "\n-------------------------")
    cuscuz = input("\nQual é a comida? ")
    contador = 1
    while contador < 4:
        if cuscuz == "CUSCUZ":
            print("\n-------------------------"
                  "\n| C | U | S | C | U | Z |"
                  "\n-------------------------"
                  "\nParabéns, você acertou! Ganhou +1 ponto:)")
            lista_numeros_disponiveis.remove(2)
            if jogador1 == True:
                lista_pontos_jogador1.append(1)
            else:
                lista_pontos_jogador2.append(1)
            break
        else:
            if contador == 1:
                cuscuz = input(
                    "\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
            if contador == 2:
                cuscuz = input(
                    "\nVixe, você errou. Tente novamente (última tentativa restante ): ")
            if contador == 3:
                print("\nQue pena, não foi dessa vez! :(")
        contador = contador + 1


def famosobrnivel1(numero_escolhido):
    print("\nA dica é:", lista_dicas_nivel1[2])
    print("\n-----")
    if 4 not in lista_numeros_disponiveis:
        print("| B |")
    else:
        print("|   |")
    print("|---|"
          "\n|   |"
          "\n|---|"
          "\n|   |"
          "\n|---|")
    if 8 not in lista_numeros_disponiveis:
        print("| N |")
    else:
        print("|   |")
    print("|---|")
    if 7 not in lista_numeros_disponiveis:
        print("| A |")
    else:
        print("|   |")
    print("-----")
    bruna = input("\nQual é o(a) famoso(a) brasileiro(a)? ")
    contador = 1
    while contador < 4:
        if bruna == "BRUNA":
            print("\n-----"
                  "\n| B |"
                  "\n|---|"
                  "\n| R |"
                  "\n|---|"
                  "\n| U |"
                  "\n|---|"
                  "\n| N |"
                  "\n|---|"
                  "\n| A |"
                  "\n-----"
                  "\nParabéns, você acertou! Ganhou +1 ponto:)")
            lista_numeros_disponiveis.remove(3)
            if jogador1 == True:
                lista_pontos_jogador1.append(1)
            else:
                lista_pontos_jogador2.append(1)
            break
        else:
            if contador == 1:
                bruna = input(
                    "\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
            if contador == 2:
                beruna = input(
                    "\nVixe, você errou. Tente novamente (última tentativa restante ): ")
            if contador == 3:
                print("\nQue pena, não foi dessa vez! :(")
        contador = contador + 1


def esportenivel1(numero_escolhido):
    print("\nA dica é:", lista_dicas_nivel1[3])
    if 3 not in lista_numeros_disponiveis and 6 in lista_numeros_disponiveis:
        print("\n--------------------------------"
              "\n| B |   |   |   |   |   |   |   |"
              "\n--------------------------------")
    elif 3 in lista_numeros_disponiveis and 6 not in lista_numeros_disponiveis:
        print("\n--------------------------------"
              "\n|   |   |   |   |   |   |   | E |"
              "\n--------------------------------")
    elif 3 not in lista_numeros_disponiveis and 6 not in lista_numeros_disponiveis:
        print("\n--------------------------------"
              "\n| B |   |   |   |   |   |   | E |"
              "\n--------------------------------")
    else:
        print("\n--------------------------------"
              "\n|   |   |   |   |   |   |   |   |"
              "\n--------------------------------")
    basquete = input("\nQual é o esporte? ")
    contador = 1
    while contador < 4:
        if basquete == "BASQUETE":
            print("\n--------------------------------"
                  "\n| B | A | S | Q | U | E | T | E |"
                  "\n--------------------------------"
                  "\nParabéns, você acertou! Ganhou +1 ponto:)")
            lista_numeros_disponiveis.remove(4)
            if jogador1 == True:
                lista_pontos_jogador1.append(1)
            else:
                lista_pontos_jogador2.append(1)
            break
        else:
            if contador == 1:
                basquete = input(
                    "\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
            if contador == 2:
                basquete = input(
                    "\nVixe, você errou. Tente novamente (última tentativa restante): ")
            if contador == 3:
                basquete = input("\nQue pena, não foi dessa vez! :(")
        contador = contador + 1


def animalnivel1(numero_escolhido):
    print("\nA dica é:", lista_dicas_nivel1[4])
    print("\n-----"
          "\n|   |"
          "\n|---|")
    if 1 not in lista_numeros_disponiveis:
        print("| A |")
    else:
        print("|   |")
    print("|---|"
          "\n|   |"
          "\n|---|"
          "\n|   |"
          "\n-----")
    gato = input("\nQual é o animal? ")
    contador = 1
    while contador < 4:
        if gato == "GATO":
            print("\n-----"
                  "\n| G |"
                  "\n|---|"
                  "\n| A |"
                  "\n|---|"
                  "\n| T |"
                  "\n|---|"
                  "\n| O |"
                  "\n-----"
                  "\nParabéns, você acertou! Ganhou +1 ponto:)")
            lista_numeros_disponiveis.remove(5)
            if jogador1 == True:
                lista_pontos_jogador1.append(1)
            else:
                lista_pontos_jogador2.append(1)
            break
        else:
            if contador == 1:
                gato = input(
                    "\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
            if contador == 2:
                gato = input(
                    "\nVixe, você errou. Tente novamente (última tentativa restante): ")
            if contador == 3:
                print("\nQue pena, não foi dessa vez! :(")
        contador = contador + 1


def repeticaonivel1(numero_escolhido):
    print("\nA dica é:", lista_dicas_nivel1[5])
    print("\n-----"
          "\n|   |"
          "\n|---|"
          "\n|   |"
          "\n|---|")
    if 1 not in lista_numeros_disponiveis:
        print("| I |")
    else:
        print("|   |")
    print("|---|"
          "\n|   |"
          "\n|---|")
    if 4 not in lista_numeros_disponiveis:
        print("| E |")
    else:
        print("|   |")
    print("-----")
    repeticao = input("\nQual é o comando na linguagem python? ")
    contador = 1
    while contador < 4:
        if repeticao == "WHILE":
            print("\n-----"
                  "\n| W |"
                  "\n|---|"
                  "\n| H |"
                  "\n|---|"
                  "\n| I |"
                  "\n|---|"
                  "\n| L |"
                  "\n|---|"
                  "\n| E |"
                  "\n-----"
                  "\nParabéns, você acertou! Ganhou +1 ponto:)")
            lista_numeros_disponiveis.remove(6)
            if jogador1 == True:
                lista_pontos_jogador1.append(1)
            else:
                lista_pontos_jogador2.append(1)
            break
        else:
            if contador == 1:
                repeticao = input(
                    "\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
            if contador == 2:
                repeticao = input(
                    "\nVixe, você errou. Tente novamente (última tentativa restante): ")
            if contador == 3:
                print("\nQue pena, não foi dessa vez! :(")
                acertou = 0
        contador = contador + 1


def profissaonivel1(numero_escolhido):
    print("\nA dica é:", lista_dicas_nivel1[6])
    if 3 not in lista_numeros_disponiveis:
        print("\n---------------------------------------------"
              "\n|   |   |   |   |   |   |   | A |   |   |   |"
              "\n---------------------------------------------")
    else:
        print("\n---------------------------------------------"
              "\n|   |   |   |   |   |   |   |   |   |   |   |"
              "\n---------------------------------------------")
    programador = input("\nQual é a profissão? ")
    contador = 1
    while contador < 4:
        if programador == "PROGRAMADOR":
            print("\n---------------------------------------------"
                  "\n| P | R | O | G | R | A | M | A | D | O | R |"
                  "\n---------------------------------------------"
                  "\nParabéns, você acertou! Ganhou +1 ponto:)")
            lista_numeros_disponiveis.remove(7)
            if jogador1 == True:
                lista_pontos_jogador1.append(1)
            else:
                lista_pontos_jogador2.append(1)
            break
        else:
            if contador == 1:
                programador = input(
                    "\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
            if contador == 2:
                programador = input(
                    "\nVixe, você errou. Tente novamente (última tentativa restante): ")
            if contador == 3:
                print("\nQue pena, não foi dessa vez! :(")
        contador = contador + 1


def datasnivel1(numero_escolhido):
    print("\nA dica é:", lista_dicas_nivel1[7])
    if 3 not in lista_numeros_disponiveis:
        print("\n---------------------"
              "\n| N |   |   |   |   |"
              "\n---------------------")
    else:
        print("\n---------------------"
              "\n|   |   |   |   |   |"
              "\n---------------------")
    natal = input("\nQual é a data comemorativa? ")
    contador = 1
    while contador < 4:
        if natal == "NATAL":
            print("\n---------------------"
                  "\n| N | A | T | A | L |"
                  "\n--------------------"
                  "\nParabéns, você acertou! Ganhou +1 ponto:)")
            lista_numeros_disponiveis.remove(8)
            if jogador1 == True:
                lista_pontos_jogador1.append(1)
            else:
                lista_pontos_jogador2.append(1)
            break
        else:
            if contador == 1:
                natal = input(
                    "\nVixe, você errou. Tente novamente (2 restantes): ")
            if contador == 2:
                natal = input(
                    "\nVixe, você errou. Tente novamente (última tentativa restante): ")
            if contador == 3:
                print("\nQue pena, não foi dessa vez! :(")
        contador = contador + 1

# Funções aplicadas a funções


def chamar_dica(numero_escolhido):
    if numero_escolhido == 1:
        paisnivel1(numero_escolhido)
    if numero_escolhido == 2:
        comidanivel1(numero_escolhido)
    if numero_escolhido == 3:
        famosobrnivel1(numero_escolhido)
    if numero_escolhido == 4:
        esportenivel1(numero_escolhido)
    if numero_escolhido == 5:
        animalnivel1(numero_escolhido)
    if numero_escolhido == 6:
        repeticaonivel1(numero_escolhido)
    if numero_escolhido == 7:
        profissaonivel1(numero_escolhido)
    if numero_escolhido == 8:
        datasnivel1(numero_escolhido)


# Maíscula pode ser resolvido com a função upper()
print("SEJAM BEM VINDOS AO JOGO CRUZADINHA!"
      "\n"
      "\nREGRAS:"
      "\n- O jogo precisa de 2 jogadores;"
      "\n- O primeiro a jogar será sorteado pelo computador;"
      "\n- Cada jogador terá a oportunidade de escolher um nome para adivinhar de acordo com o número correspondente;"
      "\n- Só será possível escolher uma palavra que ainda não foi descoberta;"
      "\n- A dica só aparecerá após a escolha do número;"
      "\n- Cada jogador possui 3 tentativas para descobrir cada palavra e em caso de acerto, ganhará 1 ponto;"
      "\n- O jogo possui 3 níveis e a dificuldade aumenta em cada um deles;"
      "\n- Todas as palavras devem ser escritas em letras MAIÚSCULAS, caso contrário, a mesma será considerada errada;"
      "\n- A vez é alternada em caso de acerto ou no fim da terceira tentativa;"
      "\n- Ganhará aquele que possuir mais pontos e em caso de empate, os dois jogadores serão os vencedores.")

retorno = 1
while retorno == 1:
    print("\nNÍVEL 1 = FÁCIL    NÍVEL 2 = MEDIANO   NÍVEL 3 = DIFÍCIL")
    nivel = int(input("\nQual nível vocês desejam jogar? (1, 2 ou 3): "))
    while nivel != 1 and nivel != 2 and nivel != 3:
        nivel = int(
            input("\nNível indisponível. Qual nível vocês desejam jogar? (1, 2 ou 3): "))
    if nivel == 1:
        player1 = input("\nDigite o nome do Player 1: ")
        player2 = input("Digite o nome do Player 2: ")

        sorteio = random.randint(1, 2)
        if sorteio == 1:
            jogador1 = True
        else:
            jogador1 = False

        print("\n                                                        -----"
              "\n                                                        | 6 |"
              "\n                            -------------------------   |---|   -----"
              "\n                            | 2 | 2 | 2 | 2 | 2 | 2 |   | 6 |   | 5 |"
              "\n                            ----|---|---|---|---|---|---|---|---|---|"
              "\n                                | 1 | 1 | 1 | 1 | 1 | 1 |1/6| 1 |1/5|         TEMAS:"
              "\n                                ------------------------|---|---|---|         1 -> PAÍSES"
              "\n                                                        | 6 |   | 5 |         2 -> COMIDAS"
              "\n                            ----------------------------|---|   |---|         3 -> FAMOSOS BRASILEIROS"
              "\n                            |3/4| 4 | 4 | 4 | 4 | 4 | 4 |4/6|   | 5 |         4 -> ESPORTES"
              "\n                            |---|----------------------------   -----         5 -> ANIMAIS"
              "\n                            | 3 |                                             6 -> CONTEÚDOS DE A.L.P.(PYTHON)"
              "\n                            |---|                                             7 -> PROFISSÕES"
              "\n                            | 3 |                                             8 -> DATAS COMEMORATIVAS"
              "\n                            |---|----------------"
              "\n                            |3/8| 8 | 8 | 8 | 8 |"
              "\n----------------------------|---|----------------"
              "\n| 7 | 7 | 7 | 7 | 7 | 7 | 7 |3/7| 7 | 7 | 7 |"
              "\n---------------------------------------------")

        while lista_numeros_disponiveis != []:
            if jogador1 == True:
                print(f"\n{player2}, agora é sua vez!")
                jogador1 = False
            else:
                print(f"\n{player1}, agora é sua vez!")
                jogador1 = True
            numero_escolhido = int(input("\nEscolha o número da palavra : "))
            while numero_escolhido not in lista_numeros_disponiveis:
                numero_escolhido = int(
                    input("\nO número escolhido é inválido. Tente novamente (de 1 a 8): "))
            chamar_dica(numero_escolhido)
        # Tentaria ajustar em matriz
        print("\nPARABÉNS, VOCÊS TERMINARAM O NÍVEL 1!"
              "\n                                                        -----"
              "\n                                                        | W |"
              "\n                            -------------------------   |---|   -----"
              "\n                            | C | U | S | C | U | Z |   | H |   | G |"
              "\n                            ----|---|---|---|---|---|---|---|---|---|"
              "\n                                | A | R | G | E | N | T | I | N | A |"
              "\n                                ------------------------|---|---|---|"
              "\n                                                        | L |   | T |"
              "\n                            ----------------------------|---|   |---|"
              "\n                            | B | A | S | Q | U | E | T | E |   | O |"
              "\n                            |---|----------------------------   -----"
              "\n                            | R |"
              "\n                            |---|"
              "\n                            | U |"
              "\n                            |---|----------------"
              "\n                            | N | A | T | A | L |"
              "\n----------------------------|---|----------------"
              "\n| P | R | O | G | R | A | M | A | D | O | R |"
              "\n---------------------------------------------")

        pontosjogador1 = lista_pontos_jogador1.count(1)
        pontosjogador2 = lista_pontos_jogador2.count(1)
        print(f"\n{player1}, você obteve {pontosjogador1} pontos."
              f"\n{player2}, você obteve {pontosjogador2} pontos.")
        if pontosjogador1 > pontosjogador2:
            print(f"\n{player1} foi o vencedor!!!")
        elif pontosjogador1 == pontosjogador2:
            print(f"\nDeu empate. {player1} e {player2} venceram!!!)")
        else:
            print(f"\n{player2} foi o vencedor!!!")
        retorno = input("Desejam jogar novamente? 1 para SIM, 2 para NÃO: ")
    elif nivel == 2:
        print("Ainda não criado")
    else:
        print("Ainda não criado")
print("\nEsperamos que tenham gostado do jogo. Até mais! <3")
