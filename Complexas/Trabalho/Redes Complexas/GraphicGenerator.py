import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker
import csv
import os
import calendar

inputFile = pd.read_csv(
    "./Output.csv", sep=';')
inputFile2 = pd.read_csv(
    "./Dist.csv", sep=';')

def plotGraph(title, yLabel, xLabel, values, xTicks):
    fig, ax = plt.subplots()
    #print(values)
    idx = pd.date_range('2017-01-01 01:00', '2017-01-01 21:48', freq = 'min')
    df = pd.Series(np.random.randn(len(idx)),  index = idx)

    hours = mdates.HourLocator(interval = 1)
    h_fmt = mdates.DateFormatter('%H:%M:%S')
    ax.plot(df.index, values, linestyle='-', linewidth='1')
    #plt.xticks(np.arange(24), rotation=20)    
    ax.xaxis.set_major_locator(hours)
    ax.xaxis.set_major_formatter(h_fmt)

    fig.autofmt_xdate()
    #plt.xticks([])

    ax.set_ylabel(yLabel)
    ax.set_xlabel(xLabel)
    ax.set_title(title)
    #plt.locator_params(axis='x', nbins=2)
    if(not xTicks):
        plt.tick_params(
                        axis='x',          # changes apply to the x-axis
                        which='both',      # both major and minor ticks are affected
                        bottom=False,      # ticks along the bottom edge are off
                        top=False,         # ticks along the top edge are off
                        labelbottom=False) 

    plt.show()    


def calculateFrequency(values, title):
    values2 = values.tolist()
    #print(values2)
    #frequency = {}
    #uniqueValues = np.unique(values).tolist()
    #for x in len(values2):
    #    frequency[x] = values2[x]


    print('Metricas',title,':')
    print('Média', np.mean(values))
    print('Mediana', np.median(values))
    print('Desvio Padrão', np.std(values))
    print('Máx:',np.max(values),'Min',np.min(values))
    print('-----------------------------------------------')

    #print(frequency)
    return values2


toPlotDegree = calculateFrequency(inputFile['Grau_medio'], 'Grau')
toPlotCluster = calculateFrequency(inputFile['Clusterizacao'], 'Clusterizacao')
toPlotDens = calculateFrequency(inputFile['Densidade'], 'Densidade')
toPlotAssor = calculateFrequency(inputFile['Assortatividade'], 'Assortatividade')
toPlotNa = calculateFrequency(inputFile['Numero_de_arestas'], 'Numero de arestas')
toPlotNv = calculateFrequency(inputFile['Numero_de_vertices'], 'Numero de vertices')

plotGraph('Densidade', 'Densidade(%)', 'Tempo', toPlotDens, True)
plotGraph('Grau médio', 'Grau médio', 'Tempo', toPlotDegree, True)
plotGraph('Clusterizacao', 'Clusterizacao', 'Tempo', toPlotCluster, True)
plotGraph('Assortatividade', 'Assortatividade', 'Tempo', toPlotAssor, True)
plotGraph('Numero de arestas', 'Numero de arestas', 'Tempo', toPlotNa, True)
plotGraph('Numero de vertices', 'Numero de vertices', 'Tempo', toPlotNv, True)




