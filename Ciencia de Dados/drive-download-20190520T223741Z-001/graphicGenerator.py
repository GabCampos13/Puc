import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import numbers
import decimal
from math import isnan

fields = ['N012','N013','N015', 'N016']
#- Juntar desmotivado
#- Juntar lentidao N015
#- Juntar pouco interesse N012
#- Juntar concentração N013

mapping = {}
def setup_mapping():

    mapping["N012"] = {
        "title": "Nas duas últimas semanas, com que frequência o(a) Sr(a) se sentiu incomodado por ter pouco interesse ou não sentiu prazer em fazer as coisas?",
        '1': "Nenhuma vez",
        '2': "1 ou mais vezes"
    }
    mapping["N013"] = {
        "title": "Nas duas últimas semanas, com que frequência o(a) Sr(a) teve problemas para se concentrar nas suas atividades habituais?",
        '1': "Nenhuma vez",
        '2': "1 ou mais vezes"
    }
    mapping["N015"] = {
        "title": "Nas duas últimas semanas, com que frequência o(a) sr(a) teve lentidão para se movimentar ou falar, ou ao contrário, ficou muito agitado(a) ou inquieto(a)?",
        '1': "Nenhuma vez",
        '2': "1 ou mais vezes"
    }
    mapping["N016"] = {
        "title": "Nas duas últimas semanas, com que frequência o(a) Sr(a) se sentiu deprimido(a), “pra baixo” ou sem perspectiva?",
        '1': "Nenhuma vez",
        '2': "1 ou mais vezes"
    }        


def treatInput(input):
    if isinstance(input, numbers.Number) and not isnan(input) :
        return str(int(input))
    return str(input)

def graphicGenerator(noDrepression, depression, field):
    if field not in mapping:
        return
    values = mapping[field]

    statesNoDepression = [treatInput(x) for x in noDrepression[field].tolist()]
    statesDepression = [treatInput(x) for x in depression[field].tolist()]
    
    noDepressionValues = []
    depressionValues = []
    usefulValues = []
    for key, value in values.items():
        noDepressionCount = statesNoDepression.count(key)
        depressionCount = statesDepression.count(key)
        if noDepressionCount > 0 or depressionCount > 0:
            noDepressionValues.append(noDepressionCount)
            depressionValues.append(depressionCount)
            usefulValues.append(value)

    plotGraphic(depressionValues, 'Com Depressão', noDepressionValues, 'Sem Depressão', '# Pessoas', values['title'], field, usefulValues)

def plotGraphic(valuesA, labelA, valuesB, labelB, yLabel, title, other, objects):
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

    # autolabel(rects1, ax, "left",)
    # autolabel(rects2, ax, "right")

    # fig.tight_layout()
    fig.autofmt_xdate()
    # plt.savefig(other+'.png', figsize=(30.0, 20), dpi = 300)
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
    dataNoDepressionPIB = pd.read_csv("TableNoDepressionPibAleatorio.csv", sep=',')
    dataDepressionPIB = pd.read_csv("TableDepressionPib.csv", sep=',')
    setup_mapping()

    for field in fields:
        graphicGenerator(dataNoDepressionPIB, dataDepressionPIB, field)
    # graphicGenerator(dataNoDepressionPIB, dataDepressionPIB, 'M016')
