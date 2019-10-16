import numpy as np
import pandas as pd
import random
import csv

# Estado? Codigo domiciolio ? Upa ? Sexo? Cor/Raça? Estado civil? Qual seu estado de saúde ? Deixou de realizar tarefas habituais por motivo de saude
# Qual foi o principal motivo de saude que te afastou ? Trabalha ambiente aberto ou fechado ?
# No trabalho, nervosismo que pode afetar a saúde ? Anos no trabalho principal ?
# Quantos parentes se sente a vontade de falar sobre quase tudo ?
# Quantos amigos || - (tirando parentes) ? Últimos 12 meses, quantas vezes participou de esportes em grupo ?
# Últimos 12 meses, trabalho voluntário ou não remunerado ? Últimos 12 meses, atividades religiosas ?
# Como avalia sua saude ? Problemas com sono ? Cansado e não disposto ? Pouco interesse e prazer nas coisas ?
# Problema de concentração ? Problema de alimentação ? Comportamento agitado/quieto (anormal) ?
# Deprimido, p/ baixo sem perspectiva ? Se sentiu mal consigo mesmo, fracassado ? Pensou em suicídio ?
# Violencia fora de casa (polica, bandido, etc) ? Tipo de violência ? Ameaçado/ferido ?
# Local violência ? Autor violência ? Deixou de realizar atividade pela violência ? Lesão corporal ?
# Alimentos doces ? Junk food ? Consumeo de sal ? Álcool ? Frequencia Alcool ? Qtd alcool ?
# Diagnostico depressão ? Idade depressão ? Vai ao medico pela depressao ? Motivo para nao ir ao medico depressao ?
# Dieta por depressao ? Fisioterapia por depressao ? Medicamento depressao coberto pelo plano ?
# Medicamento em servico publico de saude ? Ultima assistencia medica por depressao ?
# Quando buscou assistencia, foi atendido ? Atendimento de depressao foi encaminhado para profissional ?
# Foi as consultas com especilista mental ? Diagnosticos de doencas mentais ? Diagnosticos de doencas mentais (similar ao anterior) ?
# Diagnosticos de doencas mentais (similar ao anterior) ? Diagnosticos de doencas mentais (similar ao anterior) ?
# Ultima vez que procurou medico ? Motivo medico ? Foi atendido ? Quantas vezes buscou novamente atendimento ?
fields = ['V0001', 'C006', 'C008', 'C009', 'C011', 'J001', 'J002', 'J004', 'M009', 'M01106', 'M01301', 'M014', 'M015', 'M016',
         'M018', 'M019', 'N001', 'N010', 'N011', 'N012', 'N013', 'N014', 'N015', 'N016', 'N017', 'N018', 'O025', 
         'O027', 'O028', 'O029', 'O030', 'O031', 'O032', 'P025', 'P026', 'P02601', 'P027', 'P028', 'P029', 'Q092',
         'Q093', 'Q094', 'Q095', 'Q09601', 'Q09602', 'Q097', 'Q098', 'Q101', 'Q102', 'Q106', 'Q107', 'Q110', 'Q11001',
         'Q11002', 'Q11003', 'Q11004', 'X001', 'X002', 'X004', 'X005']

data = pd.read_csv("Dados/PESPNS2013.csv", sep=';', usecols=fields)
dataDep = pd.read_csv("./TableDepression.csv", sep=',')
dataDep = data.loc[(data['Q092'] == 1)]

#PIB Per capta acima de 23.646
# MG, ES, RJ, SP, PA, SC, RS, MS, MT, GO, DF
withDepressionPib = dataDep.loc[(data['V0001'].isin([31, 32, 33, 35, 41, 42, 43, 50, 51, 52, 53]))]
# withNoDepressionPib = noDepression.loc[(data['V0001'].isin([31, 32, 33, 35, 41, 42, 43, 50, 51, 52, 53]))]

print(np.unique(withDepressionPib['V0001']))
print(np.unique(withDepressionPib['Q092']))
withDepressionPib.to_csv('TableDepressionPib.csv')
# withNoDepressionPib.to_csv('TableNoDepressionPib.csv')