import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

states = [1,2]

def graphicGeneratorV001(noDrepression, depression):
    statesNoDepression = noDrepression['Q110'].tolist()
    statesDepression = depression['Q110'].tolist()
    objects = ('MG', 'ES', 'RJ', 'SP', 'PA', 'SC', 'RS', 'MS', 'MT', 'GO', 'DF')

    noDepressionValues = []
    depressionValues = []
    for state in states:
        noDepressionValues.append(statesNoDepression.count(state))
        depressionValues.append(statesDepression.count(state))


    plotGraphic(noDepressionValues, 'Ñ Depressão', depressionValues, 'Depressão', '# Pessoas', 'Diagnosticado com doenca mental', objects)

def plotGraphic(valuesA, labelA, valuesB, labelB, yLabel, title, objects):
    ind = np.arange(len(valuesA))  # the x locations for the groups
    std = [10] * len(valuesA)
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width/2, valuesA, width,  yerr=std,
                    label=labelA)
    rects2 = ax.bar(ind + width/2, valuesB, width, yerr=std,
                    label=labelB)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(yLabel)
    ax.set_title(title)
    ax.set_xticks(ind)
    ax.set_xticklabels(objects)
    # ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
    ax.legend()

    autolabel(rects1, ax, "left",)
    autolabel(rects2, ax, "right")

    fig.tight_layout()

    plt.show()


def autolabel(rects, ax, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')

if __name__ == "__main__":
    dataNoDepressionPIB = pd.read_csv("TableNoDepressionPib.csv", sep=',')
    dataDepressionPIB = pd.read_csv("TableDepressionPib.csv", sep=',')

    graphicGeneratorV001(dataNoDepressionPIB, dataDepressionPIB)