# coding: utf8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import os

dfDepression = pd.read_csv(
    "/home/carlos/Documents/graduacao/Data_Science/Dados Juntados/TableDepressionPib.csv", sep=',')
dfNoDepression = pd.read_csv(
    "/home/carlos/Documents/graduacao/Data_Science/Dados Juntados/TableNoDepressionPibAleatorio.csv", sep=',')

# ------------------------------------------------------------------------------------------------------------
# Substituir os valores das variáveis

# Não pensou em se ferir(1) ou pensou em se ferir(2)
dfDepression['N018'].replace([2, 3, 4], 2)
dfNoDepression['N018'].replace([2, 3, 4], 2)

# Consumo de sal adequado(1) ou não adequado(2)
dfDepression['P02601'].replace([1, 4, 5], 2)
dfNoDepression['P02601'].replace([1, 4, 5], 2)
dfDepression['P02601'].replace([3], 1)
dfNoDepression['P02601'].replace([3], 1)

# ------------------------------------------------------------------------------------------------------------

dfDepression.to_csv(os.path.join(
    os.getcwd(), 'ReducedTableDepression.csv'))
dfNoDepression.to_csv(os.path.join(
    os.getcwd(), 'ReducedTableNoDepression.csv'))
