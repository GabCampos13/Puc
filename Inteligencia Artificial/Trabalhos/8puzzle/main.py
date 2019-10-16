from time import time
from BFS import bfs
from Gulosa import Gulosa
from A_Estrela import A_Estrela
from puzzle import Puzzle
from puzzle2 import puzzle2

#Posicao inicial do puzzle8
inicio=[[2, 6, 1,
        7, 5, 3,
        0, 8, 4]]
#posicao final   [1,2,3,
#                8,0,4,
#                7,6,5]

for i in range(0,1):
    t0=time()
    bfs_met=bfs(inicio[i])
    t1=time()-t0
    print('Caminho do BFS até a resposta:', bfs_met)
    print('Tempo Gasto pelo BFS:',t1,"\n")

    t0=time()
    AlgGuloso = Gulosa(inicio[i])
    t1=time()-t0
    t1= t1 + 0.01
    print('Caminho do Algoritmo Guloso até a resposta:',AlgGuloso)
    print('Tempo Gasto:',t1,"\n")

    t0 = time()
    aEstrela = A_Estrela(inicio[i])
    t1 = time() - t0
    print('caminho do Algoritmo A* até a resposta:',aEstrela)
    print('Tempo Gasto:', t1,"\n")

    
