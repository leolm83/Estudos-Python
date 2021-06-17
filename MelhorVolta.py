class Jogador:
  def __init__(self,nome):
    self.nome = nome
    self.tempo = []
  def getNome(self):
      return self.nome
  def setTempo(self,posicao,tempo):
      self.tempo.insert(posicao,tempo)
listaJogadores=[]
melhorVolta=999999999
ganhador=999999999
nomeGanhador=""
nomeMelhorVolta=""
for x in range(3):
    nomeJogador=input("Digite o nome do jogador : ")
    jogador= Jogador(nomeJogador)
    listaJogadores.append(jogador)
    for y in range(3):
        tempo=int(input("Digite o "+str(y+1)+" Tempo : "))
        listaJogadores[x].setTempo(y,tempo)
for x in range(3):
    print(listaJogadores[x].nome)
    mediaJogador=0
    for y in range(3):
        print(listaJogadores[x].tempo[y])
        if(listaJogadores[x].tempo[y]<melhorVolta):
            melhorVolta=listaJogadores[x].tempo[y]
            nomeMelhorVolta=listaJogadores[x].nome
        mediaJogador+=listaJogadores[x].tempo[y]
    mediaJogador=mediaJogador/3
    if(mediaJogador<ganhador):    
        ganhador=mediaJogador
        nomeGanhador=listaJogadores[x].nome
print("A melhor Volta foi de "+nomeMelhorVolta+" com : "+str(melhorVolta))
print("O ganhador foi "+nomeGanhador+" com a média de :"+str(ganhador))
