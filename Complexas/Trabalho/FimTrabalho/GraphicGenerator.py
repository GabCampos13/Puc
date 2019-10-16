import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import csv
import os

inputFile = pd.read_csv(
    "./Output.csv", sep=';')

sortedDF = pd.DataFrame(inputFile)

def plotGraph(title, xLabel, yLabel, values, legend):
    fig, ax = plt.subplots()

    values = np.array(values, dtype=np.float32)
    plt.plot(values)

    ax.set_ylabel(yLabel)
    ax.set_xlabel(xLabel)
    ax.set_title(title)
    ax.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=False)

    plt.show()    

plotGraph('Densidade', "Tempo", 'Valor da densindade', sortedDF['Densidade'].tolist(), sortedDF['TempoDoDia'].tolist())
plotGraph('Assortatividade', 'Tempo', 'Valor da assortatividade', sortedDF['Assortatividade'].tolist(), sortedDF['TempoDoDia'].tolist())
plotGraph('Clusterizacao', 'Tempo', 'Valor da clusterização', sortedDF['Clusterizacao'].tolist(), sortedDF['TempoDoDia'].tolist())
plotGraph('Grau Medio', 'Tempo', 'Valor do grau médio', sortedDF['GrauMedio'].tolist(), sortedDF['TempoDoDia'].tolist())



