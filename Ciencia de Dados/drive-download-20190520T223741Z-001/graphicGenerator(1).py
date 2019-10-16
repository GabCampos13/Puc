import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import numbers
import decimal

fields = ['Q101', 'Q102', 'Q106', 'Q107', 'Q110', 'Q11001',
         'Q11002', 'Q11003', 'Q11004', 'X001', 'X002', 'X004', 'X005']

mapping = {}

def setup_mapping():
    
    mapping["X004"] = {
        "title": "Na primeira vez que procurou atendimento médico por este motivo, o(a) Sr(a) conseguiu ser atendido?",
        '1': "Sim",
        '2': "Não"
    }
        
    mapping["X002"] = {
        'title': "Por qual motivo o(a) Sr(a) precisou consultar um médico?",
        '1': "Acidente ou lesão",
        '2': "Continuação de tratamento ou terapia",
        '3': "Consulta pré-natal",
        '4': "Exame médico periódico",
        '5': "Outro exame médico (admissional, para carteira de motorista, etc.)",
        '6': "Problema de saúde mental",
        '7': "Doença ou outro problema de saúde ",
        '8': "Outro",
    }

    mapping["X001"] = {
        'title': "Quando foi a última vez que o(a) Sr(a) consultou um médico?",
        '1': "Há menos de 2 semanas",
        '2': "Entre 15 dias e um mês",
        '3': "Entre um mês e 3 meses atrás",
        '4': "Entre três meses e um ano",
        '5': "Há mais de um ano",
        '6': "Nunca foi ao médico"
    }

    mapping["Q11004"] = {
        'title': "Algum médico ou profissional de saúde mental (como psiquiatra ou psicólogo) já lhe deu o diagnóstico de outra doença mental?",
        '1': "Sim",
        '2': "Não",

    }

    mapping["Q11003"] = {
        'title': "Algum médico ou profissional de saúde mental já lhe deu o diagnóstico de outra doença mental, como psicose ou TOC?",
        '1': "Sim",
        '2': "Não",

    }
    mapping["Q11002"] = {
        'title': "Algum médico ou profissional de saúde mental (como psiquiatra ou psicólogo) já lhe deu o diagnóstico de outra doença mental, como transtorno bipolar?",
        '1': "Sim",
        '2': "Não",

    }
    mapping["Q11001"] = {
        'title': "Algum médico ou profissional de saúde mental (como psiquiatra ou psicólogo) já lhe deu o diagnóstico de outra doença mental, como esquizofrenia?",
        '1': "Sim",
        '2': "Não",

    }

    mapping["Q110"] = {
        'title': "Algum médico ou profissional de saúde mental já lhe deu o diagnóstico de outra doença mental, como esquizofrenia, transtorno bipolar, psicose ou TOC?",
        '1': "Sim",
        '2': "Não",

    }

    mapping["Q107"] = {
        'title': "O(a) Sr(a) conseguiu ir a todas as consultas com profissional especialista de saúde mental?",
        '1': "Sim",
        '2': "Não",

    }

    mapping["Q106"] = {
        'title': "Em algum dos atendimentos para depressão, houve encaminhamento para algum acompanhamento com profissional de saúde mental, como psiquiatra ou psicólogo?",
        '1': "Sim",
        '2': "Não",
        '3': "Não houve encaminhamento, pois todas as consultas para depressão foram com profissional de saúde mental"

    }
    mapping["Q102"] = {
        'title': "Na última vez que recebeu assistência médica para depressão, onde o(a) Sr(a) foi atendido?",
        '1': "Unidade básica de saúde (posto ou centro de saúde ou unidade de saúde da família)",
        '2': "Centro de Especialidades, Policlínica pública ou PAM  - Posto de Assistência Médica",
        '3': "UPA (Unidade de pronto Atendimento)",
        '4': "CAPS – Centro de Atenção Psicossocial",
        '5': "Outro tipo de Pronto Atendimento Público (24 horas)",
        '6': "Pronto-socorro ou emergência de hospital público",
        '7': "Hospital público/ambulatório",
        '8': "Consultório particular ou Clínica privada",
        '9': "Ambulatório ou consultório de empresa ou sindicato",
        '10': "Pronto-atendimento ou emergência de hospital privado",
        '11': "No domicílio, com médico da equipe de saúde da família",
        '12': "No domicílio, com médico particular",
        '13': "Outro",
    }

    mapping["Q101"] = {
        'title': "Quando foi a última vez que o(a) Sr(a) recebeu assistência médica por causa da depressão?",
        '1': "Há menos de 6 meses",
        '2': "Entre 6 meses e menos de 1 ano",
        '3': "Entre 1 ano e menos de 2 anos",
        '4': "Entre 2 anos e menos de 3 anos",
        '5': "Há 3 anos ou mais",
        '6': "Nunca recebeu"
    }

def treatInput(input):
    if isinstance(input, numbers.Number):
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

    plotGraphic(noDepressionValues, 'Ñ Depressão', depressionValues, 'Depressão', '# Pessoas', values['title'], usefulValues)

def graphicGeneratorV001(noDrepression, depression):
    statesNoDepression = noDrepression['V0001'].tolist()
    statesDepression = depression['V0001'].tolist()
    objects = ('MG', 'ES', 'RJ', 'SP', 'PA', 'SC', 'RS', 'MS', 'MT', 'GO', 'DF')

    noDepressionValues = []
    depressionValues = []
    for state in states:
        noDepressionValues.append(statesNoDepression.count(state))
        depressionValues.append(statesDepression.count(state))


    plotGraphic(noDepressionValues, 'Ñ Depressão', depressionValues, 'Depressão', '# Pessoas', 'Depressão', objects)

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

    # autolabel(rects1, ax, "left",)
    # autolabel(rects2, ax, "right")

    # fig.tight_layout()
    fig.autofmt_xdate()
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
