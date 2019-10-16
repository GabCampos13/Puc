import networkx as nx
import pandas as pd 
import csv
import matplotlib.pyplot as plt
import numpy as npy
from PIL import Image

G=nx.Graph()
x = True
data = pd.read_csv("pathPuc.csv",sep=';')
existentes = []
with open("pathPuc.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    for i, line in enumerate(reader):
        if(line[0] not in existentes):
            G.add_node(line[0])
            existentes.append(line[0])

with open("pathPuc.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    for i, line in enumerate(reader):
        G.add_edge(line[0],line[1],weight = line[2])

#nx.draw(G,with_labels = True)
#plt.show()       
while(x == True):
    print(" Digite 1 para abrir o mapa com os vertices (recomendado, se escolhido deixe o mapa aberto) ou digite 0 para calcular o caminho sem abrir o mapa")
    opcao = input()

    if(opcao == "1"):
        Image.open("pucmap.jpeg").show()
    else:
        opcao = 0

    print("De qual vértice você deseja sair?")
    verticeInicial = input()


    print("A qual vértice deseja chegar?")
    #Image.open("pucmap.jpeg").show()
    verticeFinal = input()

    path = nx.dijkstra_path(G,verticeInicial,verticeFinal,weight = "")
    print("O melhor caminho a ser feito é, no mapa: ")
    print(*path,sep = "-")
    cont = 0
    distancia = 0

    while cont < len(path)-1 :
        for y in G.edges.data("weight"):
            if((path[cont] == y[0] and path[cont+1] == y[1])or(path[cont] == y[1] and path[cont+1] == y[0])):
                distancia = distancia + float(y[2]) 
                break  
        cont = cont + 1
    print("Com distância: ","%.2f" % round(distancia,2),"metros")     
    print("Deseja finalizar o programa? (1 para sim e 0 para nao)") 
    opcao2 = input()      
    if(opcao2 == "1"):
        break
    else:
        x = True