class Puzzle: #Heuristica utilizada pelo A*, onde ele considera tanto H(n) quanto G(n)
    posicao_esperada=[1,2,3,
                      8,0,4,
                      7,6,5]
    heuristica=None
    avaliacao=None
    precisa=False
    def __init__(self,posicao,pai,movimento,custo,precisa=False):
        self.pai=pai
        self.posicao=posicao
        self.movimento=movimento
        if pai:
            self.custo = pai.custo + custo
        else:
            self.custo = custo
        if precisa:
            self.precisa=True
            self.gera_heuristica()
            self.avaliacao=self.heuristica+self.custo

    def __str__(self):
        return str(self.posicao[0:3])+'\n'+str(self.posicao[3:6])+'\n'+str(self.posicao[6:9])

    def gera_heuristica(self):
        self.heuristica=0
        for num in range(1,9):
            distancia=abs(self.posicao.index(num) - self.posicao_esperada.index(num))
            i=int(distancia/3)
            j=int(distancia%3)
            self.heuristica=self.heuristica+i+j

    def resposta(self):
        if self.posicao == self.posicao_esperada:
            return True
        return False

    @staticmethod
    def procura_movimento(i,j):
        movimentos_permitidos = ['Cima', 'Baixo', 'Esquerda', 'Direita']
        if i == 0: 
            movimentos_permitidos.remove('Cima')
        elif i == 2:  
            movimentos_permitidos.remove('Baixo')
        if j == 0:
            movimentos_permitidos.remove('Esquerda')
        elif j == 2:
            movimentos_permitidos.remove('Direita')
        return movimentos_permitidos

    def gera_filho(self):
        filho=[]
        x = self.posicao.index(0)
        i = int(x / 3)
        j = int(x % 3)
        movimentos_permitidos2=self.procura_movimento(i,j)

        for movimento in movimentos_permitidos2:
            new_posicao = self.posicao.copy()
            if movimento is 'Cima':
                new_posicao[x], new_posicao[x-3] = new_posicao[x-3], new_posicao[x]
            elif movimento is 'Baixo':
                new_posicao[x], new_posicao[x+3] = new_posicao[x+3], new_posicao[x]
            elif movimento is 'Esquerda':
                new_posicao[x], new_posicao[x-1] = new_posicao[x-1], new_posicao[x]
            elif movimento is 'Direita':
                new_posicao[x], new_posicao[x+1] = new_posicao[x+1], new_posicao[x]
            filho.append(Puzzle(new_posicao,self,movimento,1,self.precisa))
        return filho

    def busca_solucao(self):
        resp = []
        resp.append(self.movimento)
        caminho = self
        while caminho.pai != None:
            caminho = caminho.pai
            resp.append(caminho.movimento)
        resp = resp[:-1]
        resp.reverse()
        return resp
