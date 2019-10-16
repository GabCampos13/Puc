import pandas as pd
import numpy as np

filePath = './dotaMatchPos.csv'
newFile = './dotaMatchParsed.csv'


file = pd.read_csv(filePath)
originalHeader = file.columns.tolist()
newHeader = []
nTotalChamps = 121

for head in originalHeader:
    if 'Hero' not in head and 'Winner Team' not in head:
        newHeader.append(head)

for x in range(1, nTotalChamps + 1):
    newHeader.append('Hero'+str(x))

newHeader.append('Winner Team')

new_df = pd.DataFrame(index = np.arange(len(file.index)), columns = newHeader)

for index, row in file.iterrows():
    newData = []
    champsRow = [0] * nTotalChamps

    for i in range(1,11):
        champTeam = 1
        if(i > 5): champTeam = 2
        champsRow[row['Hero'+str(i)] - 1] = champTeam

    for head in originalHeader:
        if 'Hero' in head or 'Winner Team' in head:
            continue
        newData.append(row[head])
    newData.extend(champsRow)
    newData.append(row['Winner Team'])
    new_df.iloc[index] = newData
    # print('Done index: ' + str(index) + '/' + str(len(file.index)))
    
        


new_df.to_csv(newFile, sep=',')