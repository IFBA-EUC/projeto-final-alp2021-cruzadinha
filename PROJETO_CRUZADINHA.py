import random
 
lista_dicas_nivel1 = ["País onde Lionel Messi, jogador de futebol, nasceu.","É feito de milho e cozido a vapor.", "Primeiro nome da atriz global e ex namorada do jogador de futebol Neymar Jr.", "Driblou, arremessou e é ponto!", "Animal doméstico que caça ratos.", "Estrutura que permite a execução até uma determinada condição ser satisfeita (python)", "Profissional que cria, desenvolve e mantém diferentes tipos de softwares em sistemas amplos ou para uso em computadores pessoais.", "Festividade cristã que relembra o nascimento de Jesus Cristo."]
lista_dicas_nivel2 = ["Único país latino da América do Norte.", "Bolo de feijão, frito no azeite de dendê.", "Primeiro nome da Única atriz brasileira indicada ao prêmio Oscar.", "Jab, Jab, ele esquiva e finaliza com um gancho!", "Seu corpo é divido em cabeça, e tem transformação em quatro fases.", "Estrutura lógica que precisa de todas entradas verdadeiras para seu resultado também ser verdadeiro.", "Profissional que zela pela segurança, conforto e tranquilidade dos passageiros do transporte aéreo", "Maior festa de rua da Bahia."]
lista_dicas_nivel3 = ["País europeu que possui o formato de uma bota.", "Feito de farinha de trigo, camarão e leite de coco.", "Primeiro nome do Cantor brasileiro de MPB, dono da música 'Apesar de você' escrita em 1970, como crítica a falta de liberdade durante a ditadura militar no Brasil", "Muita calma nessa hora! ele precisa estabilizar seu equilibrio...", "Tem bico forte, língua carnosa e uma cauda longa em forma de espada.", "Fornece funções matématicas que para o seu uso é preciso ser chamada na biblioteca.", "Profissional responsável pelo estudo das mais variadas formas de vida existentes.", "Festa cristã que celebra o nascimento de João Batista."]  

def paisnivel1(numero_escolhido):
  if numero_escolhido == 1:
    print("\nA dica é:", lista_dicas_nivel1[0])
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
      "\n"
      "\nParabéns, você acertou! :)")
      break
    else:
      if contador == 1:
        argentina = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
      if contador == 2:
        argentina = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
      if contador == 3:
        print("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def comidanivel1 (numero_escolhido): 
  if numero_escolhido == 2:
    print("\nA dica é:", lista_dicas_nivel1[1])
  print ("\n-------------------------"
  "\n|   |   |   |   |   |   |"
  "\n-------------------------" )
  cuscuz = input ("\nQual é a comida? ")
  contador = 1 
  while contador < 4 :
    if cuscuz == "CUSCUZ" : 
      print ("\n-------------------------"
      "\n| C | U | S | C | U | Z |"
      "\n-------------------------"
      "\n" 
      "\nParabéns, você acertou! :)")
      break
    else: 
      if contador == 1 :
        cuscuz = input ("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
      if contador == 2 :
        cuscuz = input ("\nVixe, você errou. Tente novamente (última tentativa restante ): ")
      if contador == 3 : 
        print ("\nQue pena, não foi dessa vez! :(")  
    contador = contador + 1

def famosobrnivel1 (numero_escolhido):
  if numero_escolhido == 3:
    print("\nA dica é:", lista_dicas_nivel1[2]) 
  print("\n-----"
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
  bruna = input ("\nQual é o(a) famoso(a) brasileiro(a)? ")
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
      "\nParabéns, você acertou! :)")
      break
    else: 
      if contador == 1 :
        bruna = input ("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
      if contador == 2 :
        beruna = input ("\nVixe, você errou. Tente novamente (última tentativa restante ): ")
      if contador == 3 : 
        print ("\nQue pena, não foi dessa vez! :(")  
    contador = contador + 1

def esportenivel1 (numero_escolhido): 
  if numero_escolhido == 4:
    print("\nA dica é:", lista_dicas_nivel1[3])
  print("\n--------------------------------"
  "\n|   |   |   |   |   |   |   |   |"
  "\n-------------------------------"
  "\n")
  basquete = input ("\nQual é o esporte? ")
  contador = 1 
  while contador < 4 :
    if basquete == "BASQUETE" : 
      print("\n--------------------------------"
      "\n| B | A | S | Q | U | E | T | E |"
      "\n-------------------------------"
      "\n" 
      "\nParabéns, você acertou! :)")
      break
    else: 
      if contador == 1:
        basquete = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
      if contador == 2:
        basquete = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
      if contador == 3:
        basquete = input("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def animalnivel1(numero_escolhido):
  if numero_escolhido == 5:
    print("\nA dica é:", lista_dicas_nivel1[4])
  print("\n-----"
  "\n|   |"
  "\n|---|"
  "\n|   |"
  "\n|---|"
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
      "\nParabéns, você acertou! :)")
      break
    else:
      if contador == 1:
        gato = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
      if contador == 2:
        gato = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
      if contador == 3:
        print("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def repeticaonivel1 (numero_escolhido): 
  if numero_escolhido == 6:
    print("\nA dica é:", lista_dicas_nivel1[5])
  print("\n-----"
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
  repeticao = input ("\nQual é o comando na linguagem python? ")
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
      "\nParabéns, você acertou! :)")
      break
    else: 
      if contador == 1 :
        repeticao = input ("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
      if contador == 2 :
        repeticao = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
      if contador == 3:
        print("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

def profissaonivel1(numero_escolhido):
  if numero_escolhido == 7:
    print("\nA dica é:", lista_dicas_nivel1[6])
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
      "\nParabéns, você acertou! :)")
      break
    else:
      if contador == 1:
        programador = input("\nVixe, você errou. Tente novamente (2 tentativas restantes): ")
      if contador == 2:
        programador = input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
      if contador == 3:
        print("\nQue pena, não foi dessa vez! :(")
    contador = contador + 1

    def datasnivel1 (numero_escolhido):
  if numero_escolhido == 8:
    print("\nA dica é:", lista_dicas_nivel1[7])
  print ("\n-------------------"
  "\n|   |   |   |   |   |"
  "\n---------------------")
  natal = input ("\nQual é a data comemorativa?")
  contador = 1
  while contador  <  4 :
    if natal  ==  "NATAL" :
      print("\n---------------------"
      "\n| N | A | T | A | L |"
      "\n--------------------"
      "\n"
      "\nParabéns, você acertou! :)")
      break
    else:
      if contador  ==  1 :
        natal  =  input("\nVixe, você errou. Tente novamente (2 restantes): ")
      if contador  ==  2 :
        natal =  input("\nVixe, você errou. Tente novamente (última tentativa restante): ")
      if contador  ==  3 :
        print("\nQue pena, não foi dessa vez! :(")
    contador  =  contador  +  1
 
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
 
player1 = input("\nDigite o nome do Player 1: ") 
player2 = input("Digite o nome do Player 2: ") 
 
sorteio = random.randint(1,2)
if sorteio == 1:
  print(f"\nO primeiro a jogar é {player1}!")
  jogador1 = True
  jogador2 = False
else:
  print(f"\nO primeiro a jogar é {player2}!")
  jogador1 = False
  jogador2 = True
 
contador = 1
while contador < 100000000:
  numero_escolhido = int(input("\nEscolha o número da palavra (de 1 a 8): "))
  while numero_escolhido > 8 or numero_escolhido < 1:
    numero_escolhido = int(input("\nO número escolhido é inválido. Tente novamente (de 1 a 8): "))
  chamar_dica(numero_escolhido)
  if jogador1 == True:
    print(f"\nO próximo a jogar é {player2}!")
    jogador2 = True
    jogador1 = False
  else:
    print(f"\nO próximo a jogar é {player1}!")
    jogador1 = True
    jogador2 = False
  contador = contador + 1
