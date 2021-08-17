import random

def dica(numero_escolhido):
  while numero_escolhido > 8 or numero_escolhido < 1:
    numero_escolhido = int(input("\nO número escolhido é inválido. Tente novamente (de 1 a 8): "))
  if numero_escolhido == 1:
    print("\nA dica é:", lista_dicas_nivel1[0])
  if numero_escolhido == 2:
    print("\nA dica é:", lista_dicas_nivel1[1])
  if numero_escolhido == 3:
    print("\nA dica é:", lista_dicas_nivel1[2])
  if numero_escolhido == 4:
    print("\nA dica é:", lista_dicas_nivel1[3])
  if numero_escolhido == 5:
    print("\nA dica é:", lista_dicas_nivel1[4])
  if numero_escolhido == 6:
    print("\nA dica é:", lista_dicas_nivel1[5])
  if numero_escolhido == 7:
    print("\nA dica é:", lista_dicas_nivel1[6])
  if numero_escolhido == 8:
    print("\nA dica é:", lista_dicas_nivel1[7])

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

lista_dicas_nivel1 = ["País onde Lionel Messi, jogador de futebol, nasceu.","É feito de milho e cozido a vapor.", "Primeiro nome da atriz global e ex namorada do jogador de futebol Neymar Jr.", "Driblou, arremessou e é ponto!", "Animal doméstico que caça ratos.", "Estrutura que permite a execução até uma determinada condição ser satisfeita (python)", "Profissional que cria, desenvolve e mantém diferentes tipos de softwares em sistemas amplos ou para uso em computadores pessoais.", "Festividade cristã que relembra o nascimento de Jesus Cristo."]
lista_dicas_nivel2 = ["Único país latino da América do Norte.", "Bolo de feijão, frito no azeite de dendê.", "Primeiro nome da Única atriz brasileira indicada ao prêmio Oscar.", "Jab, Jab, ele esquiva e finaliza com um gancho!", "Seu corpo é divido em cabeça, e tem transformação em quatro fases.", "Estrutura lógica que precisa de todas entradas verdadeiras para seu resultado também ser verdadeiro.", "Profissional que zela pela segurança, conforto e tranquilidade dos passageiros do transporte aéreo", "Maior festa de rua da Bahia."]
lista_dicas_nivel3 = ["País europeu que possui o formato de uma bota.", "Feito de farinha de trigo, camarão e leite de coco.", "Primeiro nome do Cantor brasileiro de MPB, dono da música 'Apesar de você' escrita em 1970, como crítica a falta de liberdade durante a ditadura militar no Brasil", "Muita calma nessa hora! ele precisa estabilizar seu equilibrio...", "Tem bico forte, língua carnosa e uma cauda longa em forma de espada.", "Fornece funções matématicas que para o seu uso é preciso ser chamada na biblioteca.", "Profissional responsável pelo estudo das mais variadas formas de vida existentes.", "Festa cristã que celebra o nascimento de João Batista."]  
print("Olá Lara")
