from queue import Queue #FIFO
from puzzle import Puzzle


def bfs(Inicial): #Best First Search, busca em largura, olha todos os filhos primeiro antes de descer pros filhos dos filhos...
    no_inicial = Puzzle(Inicial, None, None, 0)
    if no_inicial.resposta():
        return no_inicial.busca_solucao()
    q = Queue()
    q.put(no_inicial)
    explorados=[]
    while not(q.empty()):
        no=q.get()
        explorados.append(no.posicao)
        total_filhos=no.gera_filho()
        for filho in total_filhos:
            if filho.posicao not in explorados:
                if filho.resposta():
                    return filho.busca_solucao()
                q.put(filho)
    return
