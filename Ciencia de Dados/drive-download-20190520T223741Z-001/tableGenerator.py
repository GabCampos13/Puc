import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import os

dfDepression = pd.read_csv(
    "tableDepressionPib.csv", sep=',')
dfNoDepression = pd.read_csv(
    "TableNoDepressionPibAleatorio.csv", sep=',')

# ------------------------------------------------------------------------------------------------------------
# Substituir os valores das variáveis
#- Juntar desmotivado N016
#- Juntar lentidao N015
#- Juntar pouco interesse N012
#- Juntar concentração N013

# não teve pouco interesse(1) teve pouco interesse(2) N012
dfDepression['N012'].replace([2, 3, 4], 2)
dfNoDepression['N012'].replace([2, 3, 4], 2)

#Nas duas últimas semanas, com que frequência o(a) Sr(a) teve problemas para se concentrar nas suas atividades habituais? (1 nenhum 2 alguma) N013

dfDepression['N013'].replace([2, 3, 4], 2)
dfNoDepression['N013'].replace([2, 3, 4], 2)

#Nas duas últimas semanas, com que frequência o(a) sr(a) teve lentidão para se movimentar ou falar, ou ao contrário, ficou muito agitado(a) ou inquieto(a)?
#1 alguma 2 nenhuma

dfDepression['N015'].replace([2, 3, 4], 2)
dfNoDepression['N015'].replace([2, 3, 4], 2)

#Nas duas últimas semanas, com que frequência o(a) Sr(a) se sentiu deprimido(a), “pra baixo” ou sem perspectiva?
#1 alguma 2 nenhuma

dfDepression['N016'].replace([2, 3, 4], 2)
dfNoDepression['N016'].replace([2, 3, 4], 2)

# ------------------------------------------------------------------------------------------------------------

dfDepression.to_csv(os.path.join(
    os.getcwd(), 'ReducedTableDepression.csv'))
dfNoDepression.to_csv(os.path.join(
    os.getcwd(), 'ReducedTableNoDepression.csv'))
