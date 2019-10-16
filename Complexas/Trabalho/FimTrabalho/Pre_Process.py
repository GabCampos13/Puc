import numpy as np
inputFile = open('./Measures.txt')
outputFile = open('Output.csv', 'w')

terms = ['Tempododia:', 'Densidade:', 'Assortatividade:', 'Clusterizacao:', 'Graumedio:']
header = ['TempoDoDia', 'Densidade', 'Assortatividade', 'Clusterizacao', 'GrauMedio']

def checkValidLine(line):
    result = True
    for term in terms:
        if(not result): break
        result = line.count(term) == 1
    return result

def writeLine(arrayValue):
    for index, value in enumerate(arrayValue):
        if index + 1 < len(arrayValue): outputFile.write(str(value) + ';')
        else: outputFile.write(str(value))
    outputFile.write('\n')

def getTermsIndex(line):
    termsIndex = []
    for index, term in enumerate(terms):
        if(index + 1 < len(terms)):
            end = line.index(terms[index + 1])
        else:
            end = -1
        termsIndex.append([line.index(term) + len(term),end])
    return termsIndex

def getValues(line, termsIndex):
    lineResults = []
    for index, valRange in enumerate(termsIndex):
        if len(valRange) > 1:
            val = line[valRange[0]:valRange[1]]
        else: val = line[valRange[0]:]
        try:
            if(index > 0):
                val = float(val)
                lineResults.append(val)
            else:
                lineResults.append(val)
        except Exception as e:
            lineResults = []
    return lineResults

def run():
    writeLine(header)
    for line in inputFile:
        line = line.replace(' ', '')
        if(checkValidLine(line)):
            termsIndex = getTermsIndex(line)
            lineResults = getValues(line, termsIndex)
            if len(lineResults) == 5 : writeLine(lineResults)

    outputFile.close()
    inputFile.close()

if __name__ == "__main__":
    run()