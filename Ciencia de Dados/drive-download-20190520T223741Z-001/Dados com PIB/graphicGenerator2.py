import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import numbers
import decimal
from math import isnan

states = [31, 32, 33, 35, 41, 42, 43, 50, 51, 52, 53]

fields = ['V0001', 'C006', 'C009', 'C011', 'J001', 'J002', 'J004', 'M009', 'M01106', 'M01301', 'M014', 'M015', 'M016',
         'M018', 'M019', 'N001', 'N010', 'N011', 'N012', 'N013', 'N014', 'N015', 'N016', 'N017', 'N018', 'O025',
         'O027', 'O028', 'O029', 'O030', 'O031', 'O032', 'P025', 'P026', 'P02601', 'P027', 'P028', 'P029', 'Q092',
         'Q093', 'Q094', 'Q095', 'Q09601', 'Q09602', 'Q097', 'Q098', 'Q101', 'Q102', 'Q106', 'Q107', 'Q110', 'Q11001',
         'Q11002', 'Q11003', 'Q11004', 'X001', 'X002', 'X004', 'X005']

mapping = {}
def stats(noDrepression, depression, field):
    if field not in mapping:
        return
    title = mapping[field]['title']
    print(title + ": desvio padrão= " +  str(noDrepression.loc[:, field].std()))
    print(title + ": media= " +  str(noDrepression.loc[:, field].mean()))

def setup_mapping():
    mapping["Q11004"] = {#5 ok
        'title': "Algum médico ou profissional de saúde mental (como psiquiatra ou psicólogo) já lhe deu o diagnóstico de outra doença mental?",
        '1': "Com depressão",
        '2': "Sem Depressão"
    }

    mapping["Q11003"] = {#6 ok
        'title': "Algum médico ou profissional de saúde mental (como psiquiatra ou psicólogo) já lhe deu o diagnóstico de outra doença mental, como psicose ou TOC (Transtorno obsessivo compulsivo)?",
        '1': "Com depressão",
        '2': "Sem Depressão"
    }
    
    mapping["Q11002"] = {#7 ok
        'title': "Algum médico ou profissional de saúde mental (como psiquiatra ou psicólogo) já lhe deu o diagnóstico de outra doença mental, como transtorno bipolar?",
        '1': "Com depressão",
        '2': "Sem Depressão"
    }

    mapping["Q11001"] = {#8
        'title': "Algum médico ou profissional de saúde mental (como psiquiatra ou psicólogo) já lhe deu o diagnóstico de outra doença mental, como esquizofrenia?",
        '1': "Com depressão",
        '2': "Sem Depressão"
    }

    mapping["Q110"] = {#10 ok
        'title': "Algum médico ou profissional de saúde mental (como psiquiatra ou psicólogo) já lhe deu o diagnóstico de outra doença mental, como esquizofrenia, transtorno bipolar, psicose ou TOC (Transtorno obsessivo compulsivo)?",
        '1': "Com depressão",
        '2': "Sem Depressão"
    }

    mapping["Q107"] = {#11 ok
        'title': "O(a) Sr(a) conseguiu ir a todas as consultas com profissional especialista de saúde mental?",
        '1': "Com depressão",
        '2': "Sem Depressão"
    }

    mapping["Q106"] = {#12 ok
        'title': "Em algum dos atendimentos para depressão, houve encaminhamento para algum acompanhamento com profissional de saúde mental, como psiquiatra ou psicólogo?",
        '1': "Com depressão",
        '2': "Sem Depressão"
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

    plotGraphic(noDepressionValues, 'Não', depressionValues, 'Sim', '# Pessoas', values['title'], field, usefulValues)

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
    dataNoDepressionPIB = pd.read_csv("TableNoDepressionPib.csv", sep=',')
    dataDepressionPIB = pd.read_csv("TableDepressionPib.csv", sep=',')
    setup_mapping()

    for field in fields:
        #graphicGenerator(dataNoDepressionPIB, dataDepressionPIB, field)
        stats(dataNoDepressionPIB, dataDepressionPIB, field)
    # graphicGenerator(dataNoDepressionPIB, dataDepressionPIB, 'M016')
