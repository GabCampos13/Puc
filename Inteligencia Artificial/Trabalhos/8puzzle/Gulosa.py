from queue import PriorityQueue #Coloca na fila o menor valor de caminho
from puzzle2 import puzzle2


def Gulosa(Inicial):
    contador=0
    explorados=[]
    no_inicial=puzzle2(Inicial,None,None,0,True)
    q = PriorityQueue()
    q.put((no_inicial.avaliacao,contador,no_inicial))

    while not q.empty():
        vertice=q.get()
        vertice=vertice[2]
        explorados.append(vertice.posicao)
        if vertice.resposta():
            return vertice.busca_solucao()

        total_filhos=vertice.gera_filho()
        for filho in total_filhos:
            if filho.posicao not in explorados:
                contador += 1
                q.put((filho.avaliacao,contador,filho))
    return

