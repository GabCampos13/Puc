import numpy as np
inputFile = open('./Measures100Final.txt')
outputFile = open('Output.csv', 'w')

header = ['Tempo', 'Densidade', 'Assortatividade', 'Clusterizacao', 'Grau_medio', 'Numero_de_arestas', 'Numero_de_vertices']

def checkFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def checkValidLine(line):
    for value in line:
        result = checkFloat(value)
        print(value)
        if(not result): break

    return result

def writeLine(arrayValue):
    for index, value in enumerate(arrayValue):
        if index + 1 < len(arrayValue): outputFile.write(str(value) + ';')
        else: outputFile.write(str(value))
    outputFile.write('\n')

def run():
    writeLine(header)
    for line in inputFile:
        line = line.replace('\n','').split(';')
        if(checkValidLine(line)):
            writeLine(line)

    outputFile.close()
    inputFile.close()

if __name__ == "__main__":
    run()