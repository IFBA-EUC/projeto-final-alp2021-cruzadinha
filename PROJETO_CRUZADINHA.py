import random
 
lista_dicas_nivel1 = ["País onde Lionel Messi, jogador de futebol, nasceu.","É feito de milho e cozido a vapor.", "Primeiro nome da atriz global e ex namorada do jogador de futebol Neymar Jr.", "Driblou, arremessou e é ponto!", "Animal doméstico que caça ratos.", "Estrutura que permite a execução até uma determinada condição ser satisfeita (python)", "Profissional que cria, desenvolve e mantém diferentes tipos de softwares em sistemas amplos ou para uso em computadores pessoais.", "Festividade cristã que relembra o nascimento de Jesus Cristo."]
lista_dicas_nivel2 = ["Único país latino da América do Norte.", "Bolo de feijão, frito no azeite de dendê.", "Primeiro nome da Única atriz brasileira indicada ao prêmio Oscar.", "Jab, Jab, ele esquiva e finaliza com um gancho!", "Seu corpo é dividido em cabeça, e tem transformação em quatro fases.", "Estrutura lógica que precisa de todas entradas verdadeiras para seu resultado também ser verdadeiro.", "Profissional que zela pela segurança, conforto e tranquilidade dos passageiros do transporte aéreo", "Maior festa de rua da Bahia."]
lista_dicas_nivel3 = ["País europeu que possui o formato de uma bota.", "Feito de farinha de trigo, camarão e leite de coco.", "Primeiro nome do Cantor brasileiro de MPB, dono da música 'Apesar de você' escrita em 1970, como crítica a falta de liberdade durante a ditadura militar no Brasil", "Muita calma nessa hora! ele precisa estabilizar seu equilibrio...", "Tem bico forte, língua carnosa e uma cauda longa em forma de espada.", "Fornece funções matématicas que para o seu uso é preciso ser chamada na biblioteca.", "Profissional responsável pelo estudo das mais variadas formas de vida existentes.", "Festa cristã que celebra o nascimento de João Batista."]  
lista_numeros_disponiveis = [1,2,3,4,5,6,7,8]
lista_pontos_jogador1 = []
lista_pontos_jogador2 = []

def paisnivel1(numero_escolhido):
  print("\nA dica é:", lista_dicas_nivel1[0])
  if 5 not in lista_numeros_disponiveis and 6 in lista_numeros_disponiveis:
    print("\n-------------------------------------"
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
  argentina = argentina.upper()
  contador = 1
  while contador < 4:
    if argentina == "ARGENTINA":
      print("\n-------------------------------------"
      "\n| A | R | G | E | N | T | I | N | A |"
      "\n-------------------------------------"
      "\nParabéns, você acertou! Ganhou +1 ponto:)")
      lista_numeros_disponiveis.remove(1)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else:
      if contador == 1:
        argentina = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        argentina = argentina.upper()
      if contador == 2:
        argentina = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
        argentina = argentina.upper()
      if contador == 3:
        print("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def paisnivel2 (numero_escolhido):
  print("\nA dica é:", lista_dicas_nivel2[0])
  print("\n-------------------------"
  "\n|   |   |   |   |   |   |"
  "\n-------------------------")
  mexico = input("\nQual é o país? ")
  mexico = mexico.upper()
  contador = 1
  while contador < 4:
    if mexico == "MEXICO" or mexico == "MÉXICO":
      print("\n-------------------------"
      "\n| M | É | X | I | C | O |"
      "\n-------------------------"
      "\nParabéns, você acertou! Ganhou +1 ponto:)")
      lista_numeros_disponiveis.remove(1)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else:
      if contador == 1:
        mexico = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        mexico = mexico.upper()
      if contador == 2:
        mexico = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
        mexico = mexico.upper()
      if contador == 3:
        print("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def paisnivel3 (numero_escolhido):
  print("\nA dica é:", lista_dicas_nivel3[0])
  print("\n-------------------------")
  if 2 not in lista_numeros_disponiveis:
    print("|   |   | Á |   |   |   |")
  else:
    print("|   |   |   |   |   |   |")
  print("-------------------------")
  italia = input("\nQual é o país? ")
  italia = italia.upper()
  contador = 1
  while contador < 4:
    if italia == "ITÁLIA" or italia == "ITALIA":
      print("\n-------------------------"
      "\n| I | T | Á | L | I | A |"
      "\n-------------------------"
      "\nParabéns, você acertou! Ganhou +1 ponto:)")
      lista_numeros_disponiveis.remove(1)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else:
      if contador == 1:
        italia = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        italia = italia.upper()
      if contador == 2:
        italia = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
        italia = italia.upper()
      if contador == 3:
        print("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def comidasnivel1 (numero_escolhido): 
  print("\nA dica é:", lista_dicas_nivel1[1])
  print("\n-------------------------"
  "\n|   |   |   |   |   |   |"
  "\n-------------------------" )
  cuscuz = input ("\nQual é a comida? ")
  cuscuz = cuscuz.upper()
  contador = 1 
  while contador < 4 :
    if cuscuz == "CUSCUZ" : 
      print ("\n-------------------------"
      "\n| C | U | S | C | U | Z |"
      "\n-------------------------" 
      "\nParabéns, você acertou! Ganhou +1 ponto:)")
      lista_numeros_disponiveis.remove(2)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else: 
      if contador == 1 :
        resposta = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        resposta = resposta.upper()
      if contador == 2 :
        resposta = input("\nVixe, você errou. Tente novamente (última tentativa restante ): ")
        resposta = resposta.upper()
      if contador == 3 : 
        print("\nQue pena, não foi dessa vez! :(")  
    contador = contador + 1

def comidasnivel2 (numero_escolhido): 
  print("\nA dica é:", lista_dicas_nivel2[1])
  print("\n-----------------------------")
  if 6 not in lista_numeros_disponiveis:
    print("| A |   |   |   |   |   |   |")
  else:
    print("|   |   |   |   |   |   |   |")
  print("----------------------------")
  acaraje = input("\nQual é a comida? ")
  acaraje = acaraje.upper()
  contador = 1 
  while contador < 4 :
    if acaraje == "ACARAJE" or acaraje == "ACARAJÉ": 
      print("\n-----------------------------"
      "\n| A | C | A | R | A | J | É |"
      "\n----------------------------"
      "\nParabéns, você acertou! Ganhou +1 ponto :)")
      lista_numeros_disponiveis.remove(2)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else: 
      if contador == 1 :
        acaraje = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        acaraje = acaraje.upper()
      if contador == 2 :
        acaraje = input ("\nVixe, você errou. Tente novamente (última tentativa restante ): ")
        acaraje = acaraje.upper()
      if contador == 3 : 
        print ("\nQue pena, não foi dessa vez! :(")  
    contador = contador + 1

def comidasnivel3 (numero_escolhido):
  print("\nA dica é:", lista_dicas_nivel3[1])
  print("\n-----" 
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n|---|")
  if 1 not in lista_numeros_disponiveis:
    print("| Á |")
  else:
    print("|   |")
  print("-----")
  vatapa = input("\nQual é a comida? ")
  vatapa = vatapa.upper()
  contador = 1
  while contador < 4:
    if vatapa == "VATAPA" or vatapa == "VATAPÁ":
      print("\n-----"
      "\n| V |"
      "\n|---|"
      "\n| A |"
      "\n|---|"
      "\n| A |"
      "\n|---|"
      "\n| A |"
      "\n|---|"
      "\n| A |"
      "\n|---|"
      "\n| A |"
      "\n-----"
      "\nParabéns, você acertou! Ganhou +1 ponto:)")
      lista_numeros_disponiveis.remove(2)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else: 
      if contador == 1 :
        vatapa = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        vatapa = vatapa.upper()
      if contador == 2 :
        vatapa = input ("\nVixe, você errou. Tente novamente (última tentativa restante ): ")
        vatapa = vatapa.upper()
      if contador == 3 : 
        print ("\nQue pena, não foi dessa vez! :(")  
    contador = contador + 1

def famosobrnivel1 (numero_escolhido):
  print("\nA dica é:", lista_dicas_nivel1[2]) 
  print("\n-----")
  if 4 not in lista_numeros_disponiveis:
    print( "| B |")
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
  bruna = input ("\nQual é o(a) famoso(a) brasileiro(a)? ")
  bruna = bruna.upper()
  contador = 1 
  while contador < 4 :
    if bruna == "BRUNA" : 
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
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else: 
      if contador == 1 :
        bruna = input ("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        bruna = bruna.upper()
      if contador == 2 :
        bruna = input ("\nVixe, você errou. Tente novamente (última tentativa restante ): ")
        bruna = bruna.upper()
      if contador == 3 : 
        print ("\nQue pena, não foi dessa vez! :(")  
    contador = contador + 1

def famosobrnivel2 (numero_escolhido):
  print("\nA dica é:", lista_dicas_nivel2[2]) 
  print("\n---------------------------------")
  if 5 not in lista_numeros_disponiveis:
    print("|   |   |   |   | A |   |   |   |")  
  else:
    print("|   |   |   |   |   |   |   |   |")
  print("---------------------------------")
  fernanda = input ("\nQual é o(a) famoso(a) brasileiro(a)? ")
  fernanda = fernanda.upper()
  contador = 1 
  while contador < 4 :
    if fernanda == "FERNANDA": 
      print("\n---------------------------------"
      "\n| F | E | R | N | A | N | D | A |"
      "\n---------------------------------"
      "\nParabéns, você acertou! Ganhou +1 ponto:)")
      lista_numeros_disponiveis.remove(3)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else: 
      if contador == 1 :
        fernanda = input ("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        fernanda = fernanda.upper()
      if contador == 2 :
        fernanda = input ("\nVixe, você errou. Tente novamente (última tentativa restante ): ")
        fernanda = fernanda.upper()
      if contador == 3 : 
        print ("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def famosobrnivel3 (numero_escolhido):
  print("\nA dica é:", lista_dicas_nivel3[2]) 
  print("\n-----"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n|---|")
  if 7 not in lista_numeros_disponiveis:
    print("| O |")  
  else:
    print("|   |")
  print("-----")
  chico = input ("\nQual é o(a) famoso(a) brasileiro(a)? ")
  chico = chico.upper()
  contador = 1 
  while contador < 4 :
    if chico == "CHICO": 
      print("\n-----"
      "\n| C |"
      "\n|---|"
      "\n| H |"
      "\n|---|"
      "\n| I |"
      "\n|---|"
      "\n| C |"
      "\n|---|"
      "\n| O |"
      "\n-----"
      "\nParabéns, você acertou! Ganhou +1 ponto:)")
      lista_numeros_disponiveis.remove(3)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else: 
      if contador == 1 :
        chico = input ("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        chico = chico.upper()
      if contador == 2 :
        chico = input ("\nVixe, você errou. Tente novamente (última tentativa restante ): ")
        chico = chico.upper()
      if contador == 3 : 
        print ("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def esportenivel1 (numero_escolhido): 
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
  basquete = input ("\nQual é o esporte? ")
  basquete = basquete.upper()
  contador = 1 
  while contador < 4 :
    if basquete == "BASQUETE" : 
      print("\n--------------------------------"
      "\n| B | A | S | Q | U | E | T | E |"
      "\n--------------------------------"
      "\nParabéns, você acertou! Ganhou +1 ponto:)")
      lista_numeros_disponiveis.remove(4)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else: 
      if contador == 1:
        basquete = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        basquete = basquete.upper()
      if contador == 2:
        basquete = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
        basquete = basquete.upper()
      if contador == 3:
        basquete = input("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def esportenivel2 (numero_escolhido):
  print("\nA dica é:", lista_dicas_nivel2[3])
  print("\n-----"
  "\n|   |"
  "\n|---|")
  if 7 not in lista_numeros_disponiveis: 
    print("| O |")
  else:
    print("| O |")
  print("|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n-----")
  boxe = input ("\nQual é o esporte? ")
  boxe = boxe.upper()
  contador = 1 
  while contador < 4:
    if boxe == "BOXE": 
      print("\n-----"
      "\n| B |"
      "\n|---|"
      "\n| O |"
      "\n|---|"
      "\n| X |"
      "\n|---|"
      "\n| E |"
      "\n-----"
      "\nParabéns, você acertou! Ganhou +1 ponto:)")
      lista_numeros_disponiveis.remove(4)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else: 
      if contador == 1:
        boxe = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        boxe = boxe.upper()
      if contador == 2:
        boxe = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
        boxe = boxe.upper()
      if contador == 3:
        print("\nQue pena, não foi dessa vez! :(")
      contador = contador + 1

def esportenivel3 (numero_escolhido):
  print("\nA dica é:", lista_dicas_nivel3[3]) 
  print("\n------------------------------------"
  "\n|   |   |   |   |   |   |   |   |   |"
  "\n------------------------------------")
  slackline = input ("\nQual é o esporte? ")
  slackline = slackline.upper()
  contador = 1 
  while contador < 4 :
    if slackline == "SLACKLINE": 
      print("\n------------------------------------"
      "\n| S | L | A | C | K | L | I | N | E |"
      "\n------------------------------------"
      "\nParabéns, você acertou! Ganhou +1 ponto:)")
      lista_numeros_disponiveis.remove(4)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else: 
      if contador == 1 :
        slackline = input ("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        slackline = slackline.upper()
      if contador == 2 :
        slackline = input ("\nVixe, você errou. Tente novamente (última tentativa restante ): ")
        slackline = slackline.upper()
      if contador == 3 : 
        print ("\nQue pena, não foi dessa vez! :(")  
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
  gato = gato.upper()
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
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else:
      if contador == 1:
        gato = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        gato = gato.upper()
      if contador == 2:
        gato = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
        gato = gato.upper()
      if contador == 3:
        print("\nQue pena, não foi dessa vez! :(")
      contador = contador + 1

def animaisnivel2 (numero_escolhido): 
  print("\nA dica é:", lista_dicas_nivel2[4])
  print("\n-----"
  "\n|   |"
  "\n|---|")
  if 7 not in lista_numeros_disponiveis:
    print("| O |")
  else:
    print("|   |")
  print("|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |")
  if 3 not in lista_numeros_disponiveis:
    print("| A |")
  else:
    print("|   |")
  print("-----")
  borboleta = input("\n Qual é o animal? ")
  borboleta = borboleta.upper()
  contador = 1 
  while contador < 4 :
    if borboleta == "BORBOLETA": 
      print("\n-----"
      "\n| B |"
      "\n|---|"
      "\n| O |"
      "\n|---|"
      "\n| R |"
      "\n|---|"
      "\n| B |"
      "\n|---|"
      "\n| O |"
      "\n|---|"
      "\n| E |"
      "\n|---|"
      "\n| T |"
      "\n|---|"
      "\n| A |"
      "\n-----"
      "\nParabéns, você acertou! :)")
      lista_numeros_disponiveis.remove(5)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else : 
      if contador == 1:
        borboleta = input ("\n Vixe, você errou. Tente novamente (2 tentativas restantes ):")
        borboleta = borboleta.upper()
      if contador == 2:
        borboleta = input ("\n Vixe, você errou. Tente novamente (última tentativa restante ):")
        borboleta = borboleta.upper()
      if contador == 3: 
        print ("\n Que pena, não foi dessa vez! :(") 
    contador = contador + 1

def animaisnivel3 (numero_escolhido): 
  print("\nA dica é:", lista_dicas_nivel3[4])
  print("\n-----------------------------------------"
  "\n|   |   |   |   |   | - |   |   |   |   |"
  "\n-----------------------------------------")
  araraazul = input("\nQual é o animal? ")
  araraazul = araraazul.upper()
  contador = 1
  while contador < 4:
    if araraazul == "ARARA-AZUL" or araraazul == "ARARA AZUL":
      print("\n-----------------------------------------"
      "\n| A | R | A | R | A | - | A | Z | U | L |"
      "\n----------------------------------------"
      "\nParabéns, você acertou! Ganhou +1 ponto:)")
      lista_numeros_disponiveis.remove(5)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
        lista_pontos_jogador1.append(1)
      break
    else:
      if contador == 1:
        araraazul = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        araraazul = araraazul.upper()
      if contador == 2:
        araraazul = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
        araraazul = araraazul.upper()
      if contador == 3:
        print("\nQue pena, não foi dessa vez! :(")
      contador = contador + 1

def repeticaonivel1 (numero_escolhido): 
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
  repeticao = input ("\nQual é o comando na linguagem python? ")
  repeticao = repeticao.upper()
  contador = 1 
  while contador < 4 :
    if repeticao == "WHILE" : 
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
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else: 
      if contador == 1 :
        repeticao = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        repeticao = repeticao.upper()
      if contador == 2 :
        repeticao = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
        repeticao = repeticao.upper()
      if contador == 3:
        print("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def repeticaonivel2 (numero_escolhido): 
  print("\nA dica é:", lista_dicas_nivel2[5])
  print("\n-----")
  if 2 not in lista_numeros_disponiveis:
    print("| A |")
  else:
    print("|   |")
  print("|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n-----")
  repeticao = input ("\nQual é o comando na linguagem python? ")
  repeticao = repeticao.upper()
  contador = 1 
  while contador < 4 :
    if repeticao == "AND": 
      print("\n-----"
      "\n| A |"
      "\n|---|"
      "\n| N |"
      "\n|---|"
      "\n| D |"
      "\n-----"
      "\nParabéns, você acertou! Ganhou +1 ponto:)")
      lista_numeros_disponiveis.remove(6)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else: 
      if contador == 1 :
        repeticao = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        repeticao = repeticao.upper()
      if contador == 2 :
        repeticao = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
        repeticao = repeticao.upper()
      if contador == 3:
        print("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def repeticaonivel3 (numero_escolhido): 
  print("\nA dica é:", lista_dicas_nivel2[5])
  print("\n-----------------"
  "\n|   |   |   |   |"
  "\n-----------------")
  repeticao = input ("\nQual é o comando na linguagem python? ")
  repeticao = repeticao.upper()
  contador = 1 
  while contador < 4 :
    if repeticao == "MATH": 
      print("\n-----------------"
      "\n| M | A | T | H |"
      "\n-----------------"
      "\nParabéns, você acertou! Ganhou +1 ponto:)")
      lista_numeros_disponiveis.remove(6)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else: 
      if contador == 1 :
        repeticao = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        repeticao = repeticao.upper()
      if contador == 2 :
        repeticao = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
        repeticao = repeticao.upper()
      if contador == 3:
        print("\nQue pena, não foi dessa vez! :(")
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
  programador = programador.upper()
  contador = 1
  while contador < 4:
    if programador == "PROGRAMADOR":
      print("\n---------------------------------------------"
      "\n| P | R | O | G | R | A | M | A | D | O | R |"
      "\n---------------------------------------------"
      "\nParabéns, você acertou! Ganhou +1 ponto:)")
      lista_numeros_disponiveis.remove(7)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else:
      if contador == 1:
        programador = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        programador = programador.upper()
      if contador == 2:
        programador = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
        programador = programador.upper()
      if contador == 3:
        print("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def profissaonivel2 (numero_escolhido): 
  print("\nA dica é:", lista_dicas_nivel2[6])
  print("\n---------------------------------"
  "\n|   |   |   ", end="")
  if 5 not in lista_numeros_disponiveis:
    print("| O ", end="")
  else:
    print("|   ", end="")
  print("|   ", end="")
  if 4 not in lista_numeros_disponiveis:
    print("| O ", end="")
  else:
    print("|   ", end="")
  print("|   ", end="")
  if 8 not in lista_numeros_disponiveis:
    print("| A |")
  else:
    print("|   |")
  print("---------------------------------")
  aeromoça = input ("\nQual  é a profissão? ")
  aeromoça = aeromoça.upper()
  contador = 1 
  while contador < 4 :
    if aeromoça == "AEROMOÇA": 
      print("\n---------------------------------"
      "\n| A | E | R | O | M | O | Ç | A |"
      "\n---------------------------------"
      "\nParabéns, você acertou! Ganhou +1 ponto :)" )
      lista_numeros_disponiveis.remove(7)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else: 
      if contador == 1 :
        aeromoça = input ("\nVixe, você errou. Tente novamente (2 tentativas restantes):" )
      if contador == 2 :
        aeromoça= input ("\nVixe, você errou. Tente novamente (última tentativa restante ):" )
      if contador == 3 : 
        print("\nQue pena, não foi dessa vez! :(")  
    contador = contador + 1

def profissaonivel3 (numero_escolhido): 
  print("\nA dica é:", lista_dicas_nivel3[6])
  print("\n-----------------------------"
  "\n|   |   |   |   |   |   |   |"
  "\n-----------------------------")
  biologo = input ("\nQual é a profissão? ")
  biologo = biologo.upper()
  contador = 1
  while contador < 4 :
    if biologo == "BIOLOGO" or biologo == "BIÓLOGO":
      print("\n-----------------------------"
      "\n| B | I | Ó | L | O | G | O |"
      "\n-----------------------------"
      "\nParabéns, você acertou! Ganhou +1 ponto :)")
      lista_numeros_disponiveis.remove(7)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else:
      if contador == 1 :
        biologo = input("\nVixe, você errou. Tente novamente (2 restantes): ")
        biologo = biologo.upper()
      if contador == 2 :
        biologo = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
        biologo = biologo.upper()
      if contador == 3 :
        print("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def datasnivel1 (numero_escolhido):
  print("\nA dica é:", lista_dicas_nivel1[7])
  if 3 not in lista_numeros_disponiveis:
    print("\n---------------------"
    "\n| N |   |   |   |   |"
    "\n---------------------")
  else:
    print("\n---------------------"
    "\n|   |   |   |   |   |"
    "\n---------------------")
  natal = input ("\nQual é a data comemorativa? ")
  natal = natal.upper()
  contador = 1
  while contador < 4 :
    if natal  ==  "NATAL" :
      print("\n---------------------"
      "\n| N | A | T | A | L |"
      "\n--------------------"
      "\nParabéns, você acertou! Ganhou +1 ponto :)")
      lista_numeros_disponiveis.remove(8)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else:
      if contador == 1 :
        natal = input("\nVixe, você errou. Tente novamente (2 restantes): ")
        natal = natal.upper()
      if contador == 2 :
        natal = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
        natal = natal.upper()
      if contador == 3 :
        print("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def datasnivel2 (numero_escolhido):
  print("\nA dica é:", lista_dicas_nivel2[7])
  print("\n-----"
  "\n|   |"
  "\n|---|")
  if 7 not in lista_numeros_disponiveis:
    print("| A |")
  else:
    print("|   |")
  print("|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n-----")
  carnaval = input("\nQual é a data comemorativa? ")
  carnaval = carnaval.upper()
  contador = 1
  while contador < 4:
    if carnaval == "CARNAVAL":
      print("\n -----"
      "\n| C |"
      "\n|---|"
      "\n| A |"
      "\n|---|"
      "\n| R |"
      "\n|---|"
      "\n| N |"
      "\n|---|"
      "\n| A |"
      "\n|---|"
      "\n| V |"
      "\n|---|"
      "\n| A |"
      "\n|---|"
      "\n| L |"
      "\n-----"
      "\nParabéns, você acertou! Ganhou +1 ponto:)")
      lista_numeros_disponiveis.remove(8)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
          lista_pontos_jogador1.append(1)
      break
    else:
      if contador == 1:
        carnaval = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        carnaval = carnaval.upper()
      if contador == 2:
        carnaval = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
        carnaval = carnaval.upper()
      if contador == 3:
        print("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def datasnivel3 (numero_escolhido):
  print("\nA dica é:", lista_dicas_nivel3[7]) 
  print("\n---------------------------------"
  "\n|   |   |   | - |   |   |   |   |"
  "\n---------------------------------")
  saojoao = input("\nQual é a data comemorativa? ")
  saojoao = saojoao.upper()
  contador = 1
  while contador < 4:
    if saojoao == "SAO JOAO" or saojoao == "SÃO JOÃO" or saojoao == "SAO JOÃO" or saojoao == "SÃO JOAO":
      print("\n---------------------------------"
      "\n| S | Ã | O | - | J | O | Ã | O |"
      "\n---------------------------------"
      "\nParabéns, você acertou! Ganhou +1 ponto:)")
      lista_numeros_disponiveis.remove(8)
      if quantidade_jogadores == 2:
        if jogador1 == True:
          lista_pontos_jogador1.append(1)
        else:
          lista_pontos_jogador2.append(1)
      else:
        lista_pontos_jogador1.append(1)
      break
    else:
      if contador == 1:
        saojoao = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
        saojoao = saojoao.upper()
      if contador == 2:
        saojoao = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
        saojoao = saojoao.upper()
      if contador == 3:
        print("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def chamar_dica(numero_escolhido):
  if numero_escolhido == 1:
    if nivel == 1:
      paisnivel1(numero_escolhido)
    elif nivel == 2:
      paisnivel2(numero_escolhido)
    else:
      paisnivel3(numero_escolhido)
  if numero_escolhido == 2:
    if nivel == 1:
      comidasnivel1(numero_escolhido)
    elif nivel == 2:
      comidasnivel2(numero_escolhido)
    else:
      comidasnivel3(numero_escolhido)
  if numero_escolhido == 3:
    if nivel == 1:
      famosobrnivel1(numero_escolhido)
    elif nivel == 2:
      famosobrnivel2(numero_escolhido)
    else:
      famosobrnivel3(numero_escolhido)
  if numero_escolhido == 4:
    if nivel == 1:
      esportenivel1(numero_escolhido)
    elif nivel == 2:
      esportenivel2(numero_escolhido)
    else:
      esportenivel3(numero_escolhido)
  if numero_escolhido == 5:
    if nivel == 1:
      animalnivel1(numero_escolhido) 
    elif nivel == 2:
      animaisnivel2(numero_escolhido) 
    else:
      animaisnivel3(numero_escolhido)    
  if numero_escolhido == 6:
    if nivel == 1:
      repeticaonivel1(numero_escolhido)
    elif nivel == 2:
      repeticaonivel2(numero_escolhido)
    else:
      repeticaonivel3(numero_escolhido)
  if numero_escolhido == 7:
    if nivel == 1:
      profissaonivel1(numero_escolhido)
    elif nivel == 2:
      profissaonivel2(numero_escolhido)
    else:
      profissaonivel3(numero_escolhido)
  if numero_escolhido == 8:
    if nivel == 1:
      datasnivel1(numero_escolhido)
    elif nivel == 2:
      datasnivel2(numero_escolhido)
    else:
      datasnivel3(numero_escolhido) 

print("SEJAM BEM VINDOS AO JOGO CRUZADINHA!"
"\n"
"\nREGRAS:"
"\n- O jogo pode ter 1 ou 2 jogadores;"
"\n- O primeiro a jogar será sorteado pelo computador;"
"\n- Cada jogador terá a oportunidade de escolher um nome para adivinhar de acordo com o número correspondente;"
"\n- Só será possível escolher uma palavra que ainda não foi descoberta;"
"\n- A dica só aparecerá após a escolha do número;"
"\n- Cada jogador possui 3 tentativas para descobrir cada palavra e em caso de acerto, ganhará 1 ponto;"
"\n- O jogo possui 3 níveis e a dificuldade aumenta em cada um deles;"
"\n- A vez é alternada em caso de acerto ou no fim da terceira tentativa;"
"\n- Ganhará aquele que possuir mais pontos e em caso de empate, os dois jogadores serão os vencedores.")

retorno = 1
while retorno == 1:
  quantidade_jogadores =  int(input("\nQuantos jogadores participarão? (1 ou 2): "))
  player1 = input("\nDigite o nome do Player 1: ")
  if quantidade_jogadores == 2: 
    player2 = input("Digite o nome do Player 2: ") 
    sorteio = random.randint(1,2)
    if sorteio == 1:
      jogador1 = True
    else:
      jogador1 = False
  print("\nNÍVEL 1 = FÁCIL    NÍVEL 2 = MEDIANO   NÍVEL 3 = DIFÍCIL")
  nivel = int(input("\nQual nível você(s) deseja(m) jogar? (1, 2 ou 3): "))
  while nivel != 1 and nivel != 2 and nivel != 3:
    nivel = int(input("\nNível indisponível. Qual nível você(s) deseja(m) jogar? (1, 2 ou 3): "))
  if nivel == 1:
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
  elif nivel == 2:
    print("\n    -------------------------"
    "\n    | 1 | 1 | 1 | 1 | 1 | 1 |"
    "\n----|---|---|---|---|---|----"
    "\n|2/6| 2 | 2 | 2 | 2 | 2 | 2 |"
    "\n|---|------------------------"
    "\n| 6 |"
    "\n|---|           -----   -----   -----"
    "\n| 6 |           | 5 |   | 4 |   | 8 |                TEMAS:"   
    "\n----|-----------|---|---|---|---|---|                1 -> PAÍSES"
    "\n    | 7 | 7 | 7 |5/7| 7 |4/7| 7 |7/8|                2 -> COMIDAS"
    "\n    ------------|---|---|---|---|---|                3 -> FAMOSOS BRASILEIROS"
    "\n                | 5 |   | 4 |   | 8 |                4 -> ESPORTES"
    "\n                |---|   |---|   |---|                5 -> ANIMAIS"
    "\n                | 5 |   | 4 |   | 8 |                6 -> CONTEÚDOS DE A.L.P.(PYTHON)"
    "\n                |---|   -----   |---|                7 -> PROFISSÕES"
    "\n                | 5 |           | 8 |                8 -> DATAS COMEMORATIVAS"
    "\n                |---|           |---|"
    "\n                | 5 |           | 8 |"
    "\n                |---|           |---|"
    "\n                | 5 |           | 8 |"
    "\n                |---|           |---|"
    "\n                | 5 |           | 8 |"
    "\n----------------|---|----------------"
    "\n| 3 | 3 | 3 | 3 |3/5| 3 | 3 | 3 |"
    "\n---------------------------------")
  else:
    print("\n        -----     -----------------------------------------"
    "\n        | 2 |     | 5 | 5 | 5 | 5 | 5 | - | 5 | 5 | 5 | 5 |"
    "\n        |---|     -----------------------------------------"
    "\n        | 2 |"
    "\n        |---|                           -----"
    "\n        | 2 |                           | 3 |"
    "\n        |---|                           |---|                          TEMAS:"                        
    "\n        | 2 |                           | 3 |                          1 -> PAÍSES"
    "\n        |---|                           |---|                          2 -> COMIDAS"
    "\n        | 2 |                           | 3 |                          3 -> FAMOSOS BRASILEIROS"
    "\n--------|---|------------               |---|                          4 -> ESPORTES"
    "\n| 1 | 1 |1/2| 1 | 1 | 1 |               | 3 |                          5 -> ANIMAIS"
    "\n----------------|---|---|---------------|---|                          6 -> CONTEÚDOS DE A.L.P.(PYTHON)"
    "\n                | 7 | 7 | 7 | 7 | 7 | 7 |3/7|                          7 -> PROFISSÕES"
    "\n    ------------|---|------------------------                          8 -> DATAS COMEMORATIVAS"
    "\n    | 6 | 6 | 6 | 6 |"
    "\n    ----------------|------------------------------------"
    "\n                    | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |"
    "\n            --------|---|---|---|---|---|---|------------"
    "\n            | 8 | 8 | 8 | - | 8 | 8 | 8 | 8 |"
    "\n            ---------------------------------")
  while lista_numeros_disponiveis != []:
    if quantidade_jogadores == 2:
      if jogador1 == True:
        print(f"\n{player2}, agora é sua vez!")
        jogador1 = False
      else:
        print(f"\n{player1}, agora é sua vez!")
        jogador1 = True
    numero_escolhido = int(input("\nEscolha o número da palavra : "))
    while numero_escolhido not in lista_numeros_disponiveis:
      numero_escolhido = int(input("\nO número escolhido é inválido. Tente novamente (de 1 a 8): "))
    chamar_dica(numero_escolhido)
  if nivel == 1:
    print("\nPARABÉNS, NÍVEL 1 FINALIZADO!"
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
  elif nivel == 2:
    print("\nPARABÉNS, NÍVEL 2 FINALIZADO!"
    "\n    -------------------------"
    "\n    | M | É | X | I | C | O |"
    "\n----|---|---|---|---|---|----"
    "\n| A | C | A | R | A | J | É |"
    "\n|---|------------------------"
    "\n| N |"
    "\n|---|           -----   -----   -----"
    "\n| D |           | B |   | B |   | C |"
    "\n----|-----------|---|---|---|---|---|"
    "\n    | A | E | R | O | M | O | Ç | A |"
    "\n    ------------|---|---|---|---|---|"
    "\n                | R |   | X |   | R |"
    "\n                |---|   |---|   |---|"
    "\n                | B |   | E |   | N |"
    "\n                |---|   -----   |---|"
    "\n                | O |           | A |"
    "\n                |---|           |---|"
    "\n                | L |           | V |"
    "\n                |---|           |---|"
    "\n                | E |           | A |"
    "\n                |---|           |---|"
    "\n                | T |           | L |"
    "\n----------------|---|----------------"
    "\n| F | E | R | N | A | N | D | A |"
    "\n---------------------------------")
  else: 
    print("\nPARABÉNS, NÍVEL 3 FINALIZADO!"
    "\n        -----     -----------------------------------------"
    "\n        | V |     | A | R | A | R | A | - | A | Z | U | L |"
    "\n        |---|     -----------------------------------------"
    "\n        | A |"
    "\n        |---|                           -----"
    "\n        | T |                           | C |"
    "\n        |---|                           |---|"
    "\n        | A |                           | H |"
    "\n        |---|                           |---|"
    "\n        | P |                           | I |"
    "\n--------|---|------------               |---|"
    "\n| I | T | Á | L | I | A |               | C |"
    "\n----------------|---|---|---------------|---|"
    "\n                | B | I | Ó | L | O | G | O |"
    "\n    ------------|---|------------------------"
    "\n    | M | A | T | H |"
    "\n    ----------------|------------------------------------"
    "\n                    | S | L | A | C | K | L | I | N | E |"
    "\n            --------|---|---|---|---|---|---|------------"
    "\n            | S | Ã | O | - | J | O | Ã | O |"
    "\n            ---------------------------------")
  pontosjogador1 = lista_pontos_jogador1.count(1)
  pontosjogador2 = lista_pontos_jogador2.count(1)
  print (f"\n{player1}, você obteve {pontosjogador1} pontos.")
  if quantidade_jogadores == 2:
    print (f"{player2}, você obteve {pontosjogador2} pontos.")
    if pontosjogador1 > pontosjogador2:
      print(f"\n{player1} foi o vencedor!!!")
    elif pontosjogador1 == pontosjogador2:
      print(f"\nDeu empate. {player1} e {player2} venceram!!!)")
    else:
      print(f"\n{player2} foi o vencedor!!!")
  lista_numeros_disponiveis = [1,2,3,4,5,6,7,8]
  retorno = int(input("\nDeseja(m) jogar novamente? 1 para SIM, 2 para NÃO: "))
print("\nEsperamos que tenham gostado do jogo. Até mais! <3")
