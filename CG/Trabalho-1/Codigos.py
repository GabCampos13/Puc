import sys, os, math
from PyQt5.QtGui import (QIcon, QPainter, QPen)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication, QDesktopWidget, QToolButton, QPushButton, QInputDialog, QLineEdit)
from implementacoes import (dda, bresenhan, bresenhan_Circunferencia,cohenSutherland,liangBarsky,bezier)

class CG(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.retas_dda = []
        self.retas_bre = []
        self.Brecirculos = []
        self.recorte = []
        self.BezCur  = []
        #self.recorteIni = []
        #self.recorteFim = []
        self.comando    = '' 
        self.initUI()  

        self.BezierPtsControle = -1
        self.BezierVarControle  = 0
        self.getATrans_dda = 0
        self.getBTrans_dda = 0
        self.getATrans_bre = 0
        self.getBTrans_bre = 0
        self.getATrans_breCirc = 0
        self.getBTrans_breCirc = 0

        self.getAEscala_dda = 0
        self.getAEscala_bre = 0
        self.getAEscala_breCirc = 0
        self.getBEscala_dda = 0
        self.getBEscala_bre = 0
        self.getBEscala_breCirc = 0

        self.getRota_dda = 0
        self.getRota_bre = 0
        self.getRota_breCirc = 0

        self.reflex_dda = 0
        self.reflex_bre = 0
        self.reflex_breCirc = 0

        self.getACisa_dda = 0
        self.getACisa_bre = 0
        self.getACisa_breCirc = 0
        self.getBCisa_dda = 0
        self.getBCisa_bre = 0
        self.getBCisa_breCirc = 0

    def ClearScreen(self):
        self.BezCur  = []
        self.Brecirculos   = []
        self.retas_bre = []
        self.retas_dda = []

        self.BezierPtsControle = -1
        self.BezierVarControle  = 0
        self.getATrans_dda = 0
        self.getBTrans_dda = 0
        self.getATrans_bre = 0
        self.getBTrans_bre = 0
        self.getATrans_breCirc = 0
        self.getBTrans_breCirc = 0

        self.getAEscala_dda = 0
        self.getAEscala_bre = 0
        self.getAEscala_breCirc = 0
        self.getBEscala_dda = 0
        self.getBEscala_bre = 0
        self.getBEscala_breCirc = 0

        self.getRota_dda = 0
        self.getRota_bre = 0
        self.getRota_breCirc = 0

        self.reflex_dda = 0
        self.reflex_bre = 0
        self.reflex_breCirc = 0

        self.getACisa_dda = 0
        self.getACisa_bre = 0
        self.getACisa_breCirc = 0
        self.getBCisa_dda = 0
        self.getBCisa_bre = 0
        self.getBCisa_breCirc = 0

        self.update()

    def DDA(self):
        self.comando = 'dda'
    
    def Bre(self):
        self.comando = 'bre'

    def BreCirc(self):
        self.comando = 'breCirc'
    
    def CohenSutherland(self):
        self.comando = 'cohenSutherland'

    def LiangBarsky(self):
        self.comando = 'liangBarsky'

    def Bezier(self):
        self.comando = 'bezier'

    def Escala(self):
        valorA, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Digite o valor A')
        valorB, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Digite o valor B')

        self.getAEscala_dda = int(valorA)
        self.getAEscala_bre = int(valorA)
        self.getAEscala_breCirc = int(valorA)
        self.getBEscala_dda = int(valorB)
        self.getBEscala_bre = int(valorB)
        self.getBEscala_breCirc = int(valorB)
        
        #ALTERA ESCALA DDA
        if(len(self.retas_dda) > 0):
            x1 = self.retas_dda[len(self.retas_dda)-1][0] 
            y1 = self.retas_dda[len(self.retas_dda)-1][1] 
            x2 = self.retas_dda[len(self.retas_dda)-1][2] 
            y2 = self.retas_dda[len(self.retas_dda)-1][3] 

            self.retas_dda[len(self.retas_dda)-1][2]  = ((x2 - x1) * int(self.getAEscala_dda)) + x1
            self.retas_dda[len(self.retas_dda)-1][3]  = ((y2 - y1) * int(self.getBEscala_dda)) + y1

        #ALTERA ESCALA BRESENHAN RETA
        if(len(self.retas_bre) > 0):
            x1 = self.retas_bre[len(self.retas_bre)-1][0] 
            y1 = self.retas_bre[len(self.retas_bre)-1][1] 
            x2 = self.retas_bre[len(self.retas_bre)-1][2] 
            y2 = self.retas_bre[len(self.retas_bre)-1][3] 

            self.retas_bre[len(self.retas_bre)-1][2]  = ((x2 - x1) * int(self.getAEscala_bre)) + x1
            self.retas_bre[len(self.retas_bre)-1][3]  = ((y2 - y1) * int(self.getBEscala_bre)) + y1

        #ALTERA ESCALA BRESENHAN CIRCULO
        if(len(self.Brecirculos) > 0):
            x1 = self.Brecirculos[len(self.Brecirculos)-1][0] 
            y1 = self.Brecirculos[len(self.Brecirculos)-1][1] 
            x2 = self.Brecirculos[len(self.Brecirculos)-1][2] 
            y2 = self.Brecirculos[len(self.Brecirculos)-1][3] 

            self.Brecirculos[len(self.Brecirculos)-1][2]  = ((x2 - x1) * int(self.getAEscala_breCirc)) + x1
            self.Brecirculos[len(self.Brecirculos)-1][3]  = ((y2 - y1) * int(self.getBEscala_breCirc)) + y1
 
    def Rota(self):
        valorA, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Digite o valor de rotação:')

        self.getRota_dda = abs(360 - int(valorA))
        self.getRota_bre = abs(360 - int(valorA))
        self.getRota_breCirc = abs(360 - int(valorA))

        #ALTERA ROTACAO DDA
        if(len(self.retas_dda) > 0):
            x1 = self.retas_dda[len(self.retas_dda)-1][0] 
            y1 = self.retas_dda[len(self.retas_dda)-1][1]
            x2 = self.retas_dda[len(self.retas_dda)-1][2] 
            y2 = self.retas_dda[len(self.retas_dda)-1][3]

            self.retas_dda[len(self.retas_dda)-1][2] =  ((x2-x1)*math.cos(math.radians(int(self.getRota_dda))) - (y2-y1)*math.sin(math.radians(int(self.getRota_dda))) + x1)
            self.retas_dda[len(self.retas_dda)-1][3] =  ((x2-x1)*math.sin(math.radians(int(self.getRota_dda))) + (y2-y1)*math.cos(math.radians(int(self.getRota_dda))) + y1)

        #ALTERA ROTACAO BRESENHAN RETA       
        if(len(self.retas_bre) > 0):
            x1 = self.retas_bre[len(self.retas_bre)-1][0] 
            y1 = self.retas_bre[len(self.retas_bre)-1][1]
            x2 = self.retas_bre[len(self.retas_bre)-1][2] 
            y2 = self.retas_bre[len(self.retas_bre)-1][3]
            
            self.retas_bre[len(self.retas_bre)-1][2] =  ((x2-x1)*math.cos(math.radians(int(self.getRota_bre))) - (y2-y1)*math.sin(math.radians(int(self.getRota_bre))) + x1)
            self.retas_bre[len(self.retas_bre)-1][3] =  ((x2-x1)*math.sin(math.radians(int(self.getRota_bre))) + (y2-y1)*math.cos(math.radians(int(self.getRota_bre))) + y1)

        #ALTERA ROTACAO BRESENHAN CIRCULO
        if(len(self.Brecirculos) > 0):
            x1 = self.Brecirculos[len(self.Brecirculos)-1][0] 
            y1 = self.Brecirculos[len(self.Brecirculos)-1][1]
            x2 = self.Brecirculos[len(self.Brecirculos)-1][2] 
            y2 = self.Brecirculos[len(self.Brecirculos)-1][3]
            
            self.Brecirculos[len(self.Brecirculos)-1][2] =  ((x2-x1)*math.cos(math.radians(int(self.getRota_breCirc))) - (y2-y1)*math.sin(math.radians(int(self.getRota_breCirc))) + x1)
            self.Brecirculos[len(self.Brecirculos)-1][3] =  ((x2-x1)*math.sin(math.radians(int(self.getRota_breCirc))) + (y2-y1)*math.cos(math.radians(int(self.getRota_breCirc))) + y1)

    def Translacao(self):
        valorA, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Digite o valor de A (translação em X)')
        valorB, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Digite o valor de B (translação em Y)')

        self.getATrans_dda = int(valorA)
        self.getBTrans_dda = int(valorB)
        self.getATrans_bre = int(valorA)
        self.getBTrans_bre = int(valorB)
        self.getATrans_breCirc = int(valorA)
        self.getBTrans_breCirc = int(valorB)

        #ALTERA RETA DDA
        if(len(self.retas_dda) > 0):
            x1 = self.retas_dda[len(self.retas_dda)-1][0]
            y1 = self.retas_dda[len(self.retas_dda)-1][1] 
            x2 = self.retas_dda[len(self.retas_dda)-1][2] 
            y2 = self.retas_dda[len(self.retas_dda)-1][3] 

            self.retas_dda[len(self.retas_dda)-1][0] = x1 + int(self.getATrans_dda)           
            self.retas_dda[len(self.retas_dda)-1][1] = y1 - int(self.getBTrans_dda)    
            self.retas_dda[len(self.retas_dda)-1][2] = x2 + int(self.getATrans_dda)    
            self.retas_dda[len(self.retas_dda)-1][3] = y2 - int(self.getBTrans_dda)   
        
        #ALTERA RETA BRESENHAN
        if(len(self.retas_bre) > 0):
            x1 = self.retas_bre[len(self.retas_bre)-1][0]
            y1 = self.retas_bre[len(self.retas_bre)-1][1] 
            x2 = self.retas_bre[len(self.retas_bre)-1][2] 
            y2 = self.retas_bre[len(self.retas_bre)-1][3] 

            self.retas_bre[len(self.retas_bre)-1][0] = x1 + int(self.getATrans_bre)           
            self.retas_bre[len(self.retas_bre)-1][1] = y1 - int(self.getBTrans_bre)    
            self.retas_bre[len(self.retas_bre)-1][2] = x2 + int(self.getATrans_bre)    
            self.retas_bre[len(self.retas_bre)-1][3] = y2 - int(self.getBTrans_bre)                   

        #ALTERA CIRCULO BRESENHAN
        if(len(self.Brecirculos) > 0):
            x1 = self.Brecirculos[len(self.Brecirculos)-1][0]
            y1 = self.Brecirculos[len(self.Brecirculos)-1][1] 
            x2 = self.Brecirculos[len(self.Brecirculos)-1][2] 
            y2 = self.Brecirculos[len(self.Brecirculos)-1][3] 

            self.Brecirculos[len(self.Brecirculos)-1][0] = x1 + int(self.getATrans_breCirc)           
            self.Brecirculos[len(self.Brecirculos)-1][1] = y1 - int(self.getBTrans_breCirc)    
            self.Brecirculos[len(self.Brecirculos)-1][2] = x2 + int(self.getATrans_breCirc)    
            self.Brecirculos[len(self.Brecirculos)-1][3] = y2 - int(self.getBTrans_breCirc)     

    def RefleteCentro(self):
        #REFLETE NA ORIGEM DDA
        if(len(self.retas_dda) > 0):
            self.reflex_dda = 1
            x1 = self.retas_dda[len(self.retas_dda)-1][0]
            y1 = self.retas_dda[len(self.retas_dda)-1][1] 
            x2 = self.retas_dda[len(self.retas_dda)-1][2] 
            y2 = self.retas_dda[len(self.retas_dda)-1][3] 

            self.retas_dda[len(self.retas_dda)-1][2] = ((x2-x1)*-1) + x1
            self.retas_dda[len(self.retas_dda)-1][3] = ((y2-y1)*-1) + y1   
            self.update()  

        #REFLETE NA ORIGEM DO BRESENHAN
        if(len(self.retas_bre) > 0):
            self.reflex_bre = 1
            x1 = self.retas_bre[len(self.retas_bre)-1][0]
            y1 = self.retas_bre[len(self.retas_bre)-1][1] 
            x2 = self.retas_bre[len(self.retas_bre)-1][2] 
            y2 = self.retas_bre[len(self.retas_bre)-1][3] 

            self.retas_bre[len(self.retas_bre)-1][2] = ((x2-x1)*-1) + x1
            self.retas_bre[len(self.retas_bre)-1][3] = ((y2-y1)*-1) + y1   
            self.update()     

        #REFLETE NA ORIGEM DO BRESENHAN CIRCULO
        if(len(self.Brecirculos) > 0):
            self.reflex_breCirc = 1
            x1 = self.Brecirculos[len(self.Brecirculos)-1][0]
            y1 = self.Brecirculos[len(self.Brecirculos)-1][1] 
            x2 = self.Brecirculos[len(self.Brecirculos)-1][2] 
            y2 = self.Brecirculos[len(self.Brecirculos)-1][3] 

            self.Brecirculos[len(self.Brecirculos)-1][2] = ((x2-x1)*-1) + x1
            self.Brecirculos[len(self.Brecirculos)-1][3] = ((y2-y1)*-1) + y1   
            self.update()       

    def RefleteX(self):
        #REFLETE NA ORIGEM DDA
        if(len(self.retas_dda) > 0):
            self.reflex_dda = 1
            x1 = self.retas_dda[len(self.retas_dda)-1][0]
            y1 = self.retas_dda[len(self.retas_dda)-1][1] 
            x2 = self.retas_dda[len(self.retas_dda)-1][2] 
            y2 = self.retas_dda[len(self.retas_dda)-1][3] 

            self.retas_dda[len(self.retas_dda)-1][3] = ((y2-y1)*-1) + y1   
            self.update()  

        #REFLETE NA ORIGEM DO BRESENHAN
        if(len(self.retas_bre) > 0):
            self.reflex_bre = 1
            x1 = self.retas_bre[len(self.retas_bre)-1][0]
            y1 = self.retas_bre[len(self.retas_bre)-1][1] 
            x2 = self.retas_bre[len(self.retas_bre)-1][2] 
            y2 = self.retas_bre[len(self.retas_bre)-1][3] 

            self.retas_bre[len(self.retas_bre)-1][3] = ((y2-y1)*-1) + y1   
            self.update()     

        #REFLETE NA ORIGEM DO BRESENHAN CIRCULO
        if(len(self.Brecirculos) > 0):
            self.reflex_breCirc = 1
            x1 = self.Brecirculos[len(self.Brecirculos)-1][0]
            y1 = self.Brecirculos[len(self.Brecirculos)-1][1] 
            x2 = self.Brecirculos[len(self.Brecirculos)-1][2] 
            y2 = self.Brecirculos[len(self.Brecirculos)-1][3] 

            self.Brecirculos[len(self.Brecirculos)-1][3] = ((y2-y1)*-1) + y1   
            self.update()       


    def RefleteY(self):
        #REFLETE NA ORIGEM DDA
        if(len(self.retas_dda) > 0):
            self.reflex_dda = 1
            x1 = self.retas_dda[len(self.retas_dda)-1][0]
            y1 = self.retas_dda[len(self.retas_dda)-1][1] 
            x2 = self.retas_dda[len(self.retas_dda)-1][2] 
            y2 = self.retas_dda[len(self.retas_dda)-1][3] 

            self.retas_dda[len(self.retas_dda)-1][2] = ((x2-x1)*-1) + x1
            self.update()  

        #REFLETE NA ORIGEM DO BRESENHAN
        if(len(self.retas_bre) > 0):
            self.reflex_bre = 1
            x1 = self.retas_bre[len(self.retas_bre)-1][0]
            y1 = self.retas_bre[len(self.retas_bre)-1][1] 
            x2 = self.retas_bre[len(self.retas_bre)-1][2] 
            y2 = self.retas_bre[len(self.retas_bre)-1][3] 

            self.retas_bre[len(self.retas_bre)-1][2] = ((x2-x1)*-1) + x1 
            self.update()     

        #REFLETE NA ORIGEM DO BRESENHAN CIRCULO
        if(len(self.Brecirculos) > 0):
            self.reflex_breCirc = 1
            x1 = self.Brecirculos[len(self.Brecirculos)-1][0]
            y1 = self.Brecirculos[len(self.Brecirculos)-1][1] 
            x2 = self.Brecirculos[len(self.Brecirculos)-1][2] 
            y2 = self.Brecirculos[len(self.Brecirculos)-1][3] 

            self.Brecirculos[len(self.Brecirculos)-1][2] = ((x2-x1)*-1) + x1
            self.update()      

    def CisalhamentoX(self):
        valorA, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Digite o valor de A')

        if(len(self.retas_dda) > 0):

            self.getACisa_dda = int(valorA)        
            x1 = self.retas_dda[len(self.retas_dda)-1][0]
            y1 = self.retas_dda[len(self.retas_dda)-1][1] 
            x2 = self.retas_dda[len(self.retas_dda)-1][2] 
            y2 = self.retas_dda[len(self.retas_dda)-1][3] 

            self.retas_dda[len(self.retas_dda)-1][2] = ((x2-x1) + self.getACisa_dda*(y2-y1)) + x1

        if(len(self.retas_bre) > 0):
            self.getACisa_bre = int(valorA)
            x1 = self.retas_bre[len(self.retas_bre)-1][0]
            y1 = self.retas_bre[len(self.retas_bre)-1][1] 
            x2 = self.retas_bre[len(self.retas_bre)-1][2] 
            y2 = self.retas_bre[len(self.retas_bre)-1][3] 

            self.retas_bre[len(self.retas_bre)-1][2] = ((x2-x1) + self.getACisa_bre*(y2-y1)) + x1

        if(len(self.Brecirculos) > 0):
            self.getACisa_breCirc = int(valorA)
            x1 = self.Brecirculos[len(self.Brecirculos)-1][0]
            y1 = self.Brecirculos[len(self.Brecirculos)-1][1] 
            x2 = self.Brecirculos[len(self.Brecirculos)-1][2] 
            y2 = self.Brecirculos[len(self.Brecirculos)-1][3] 

            self.Brecirculos[len(self.Brecirculos)-1][2] = ((x2-x1) + self.getACisa_breCirc*(y2-y1)) + x1      
    
    def CisalhamentoY(self):
        valorB, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Digite o valor de B')

        if(len(self.retas_dda) > 0):
            self.getBCisa_dda = int(valorB)        
            x1 = self.retas_dda[len(self.retas_dda)-1][0]
            y1 = self.retas_dda[len(self.retas_dda)-1][1] 
            x2 = self.retas_dda[len(self.retas_dda)-1][2] 
            y2 = self.retas_dda[len(self.retas_dda)-1][3] 

            self.retas_dda[len(self.retas_dda)-1][3] = ((y2-y1) + self.getBCisa_dda*(x2-x1)) - y1
            self.update()

        if(len(self.retas_bre) > 0):
            self.getBCisa_bre = int(valorB)
            x1 = self.retas_bre[len(self.retas_bre)-1][0]
            y1 = self.retas_bre[len(self.retas_bre)-1][1] 
            x2 = self.retas_bre[len(self.retas_bre)-1][2] 
            y2 = self.retas_bre[len(self.retas_bre)-1][3] 

            self.retas_bre[len(self.retas_bre)-1][3] = ((y2-y1) + self.getBCisa_bre*(x2-x1)) - y1
            self.update() 

        if(len(self.Brecirculos) > 0):
            self.getBCisa_breCirc = int(valorB)
            x1 = self.Brecirculos[len(self.Brecirculos)-1][0]
            y1 = self.Brecirculos[len(self.Brecirculos)-1][1] 
            x2 = self.Brecirculos[len(self.Brecirculos)-1][2] 
            y2 = self.Brecirculos[len(self.Brecirculos)-1][3] 

            self.Brecirculos[len(self.Brecirculos)-1][3] = ((y2-y1) + self.getBCisa_breCirc*(x2-x1)) - y1
            self.update()   
        


    def initUI(self):               
        self.setGeometry(300, 300, 1024, 738)
        self.setWindowTitle('Computação Gráfica')        
        self.setWindowIcon(QIcon('GotenSSJDragonFist.jpg'))   

        menubar  = self.menuBar()  
        #Menu Retas
        retaMenu = menubar.addMenu('&Retas')

        ddaAction = retaMenu.addAction('DDA')
        ddaAction.triggered.connect(self.DDA)

        breAction = retaMenu.addAction('Bresenhan')
        breAction.triggered.connect(self.Bre)

        #Menu Circulo
        circMenu = menubar.addMenu('&Circulo')

        breCircAction = circMenu.addAction('Bresenhan')
        breCircAction.triggered.connect(self.BreCirc)

        #Menu Translação  
        transfMenu = menubar.addMenu('&Transformações') 

        traAction = transfMenu.addAction('Translação')  
        traAction.triggered.connect(self.Translacao)

        EscAction = transfMenu.addAction('Escala')  
        EscAction.triggered.connect(self.Escala)     

        RotaAction = transfMenu.addAction('Rotação')
        RotaAction.triggered.connect(self.Rota)

        #Menu Reflexão
        ReflexAction = transfMenu.addMenu('Reflexão') 

        CenterAction = ReflexAction.addAction('Refleto no Centro')
        CenterAction.triggered.connect(self.RefleteCentro)

        XAction = ReflexAction.addAction('Reflete em X')
        XAction.triggered.connect(self.RefleteX)

        YAction = ReflexAction.addAction('Reflete em Y')
        YAction.triggered.connect(self.RefleteY)

        #Menu cisalhamento
        CisaAction = transfMenu.addMenu('Cisalhamento')

        CisaXAction = CisaAction.addAction('Cisalhamento em X')
        CisaXAction.triggered.connect(self.CisalhamentoX)

        CisaYAction = CisaAction.addAction('Cisalhamento em Y')
        CisaYAction.triggered.connect(self.CisalhamentoY)

        #Menu recorte
        RecorteMenu = menubar.addMenu('&Recorte')

        CohenAction = RecorteMenu.addAction('Cohen-Sutherland')
        CohenAction.triggered.connect(self.CohenSutherland)

        LiangAction = RecorteMenu.addAction('Liang-Barsky')
        LiangAction.triggered.connect(self.LiangBarsky)

        #Menu Bezier
        BezierMenu = menubar.addMenu('&Bezier')

        BezierAction = BezierMenu.addAction('Bezier')
        BezierAction.triggered.connect(self.Bezier)

        #Menu Limpar Tela
        clearMenu = menubar.addMenu('&Clear')

        clearAction = clearMenu.addAction('Limpar tela')
        clearAction.triggered.connect(self.ClearScreen)
        self.show()     
        
    #Clicou em algum ponto do grafico    
    def mousePressEvent(self, event): 
        if event.button() == Qt.LeftButton :
            if self.comando == 'dda':
                self.retas_dda = []
                x1 = event.pos().x()
                y1 = event.pos().y()
                self.retas_dda.append([x1,y1,0,0])
                #print(self.retas_dda)

        if event.button() == Qt.LeftButton :
            if self.comando == 'bre':
                self.retas_bre = []         
                x1 = event.pos().x()
                y1 = event.pos().y()
                self.retas_bre.append([x1,y1,0,0])
                #print(self.retas_bre)

        if event.button() == Qt.LeftButton :
            if self.comando == 'breCirc':
                self.Brecirculos = []
                x1 = event.pos().x()
                y1 = event.pos().y()
                self.Brecirculos.append([x1,y1,0,0])
                #print(self.Brecirculos)

        if event.button() == Qt.LeftButton :
            if self.comando == 'cohenSutherland':
                self.recorte = []
                x1 = event.pos().x()
                y1 = event.pos().y()
                self.recorte.append([x1,y1,0,0])     
       
        if event.button() == Qt.LeftButton :
            if self.comando == 'liangBarsky':
                self.recorte = []
                x1 = event.pos().x()
                y1 = event.pos().y()
                self.recorte.append([x1,y1,0,0])  

        if event.button() == Qt.LeftButton :
            if self.comando == 'bezier':                
                x, y = event.pos().x(), event.pos().y()
            if self.BezierVarControle < self.BezierPtsControle:
                self.BezierVarControle += 1
                self.BezCur.append(tuple((x,y)))
            print("comando: {}, Valor de x:{}, valor de y:{}, qt pontos Controle:{}, qt pontos Aux: {}"
                .format(self.comando, x, y, self.BezierPtsControle, self.BezierVarControle))  

    #Mover o mouse segurando o botão esquerdo
    def mouseMoveEvent(self, event):
        if self.comando == 'dda':
            x2 = event.pos().x()
            y2 = event.pos().y()
            self.retas_dda[len(self.retas_dda)-1][2] = x2
            self.retas_dda[len(self.retas_dda)-1][3] = y2
            self.update()
            print(self.retas_dda)

        if self.comando == 'bre':
            x2 = event.pos().x()
            y2 = event.pos().y()
            self.retas_bre[len(self.retas_bre)-1][2] = x2
            self.retas_bre[len(self.retas_bre)-1][3] = y2
            self.update()
            #print(self.retas_bre)

        if self.comando == 'breCirc':
            x2 = event.pos().x()
            y2 = event.pos().y()
            self.Brecirculos[len(self.Brecirculos)-1][2] = x2
            self.Brecirculos[len(self.Brecirculos)-1][3] = y2
            self.update()
            #print(self.Brecirculos)

        if self.comando == 'cohenSutherland':
            x2 = event.pos().x()
            y2 = event.pos().y()
            self.recorte[len(self.recorte)-1][2] = x2
            self.recorte[len(self.recorte)-1][3] = y2 
            self.update()

        if self.comando == 'liangBarsky':
            x2 = event.pos().x()
            y2 = event.pos().y()
            self.recorte[len(self.recorte)-1][2] = x2
            self.recorte[len(self.recorte)-1][3] = y2 
            self.update()


    def paintEvent(self, e):
        cor = Qt.black    
        pen = QPen(cor, 3, Qt.SolidLine)                    
        painter = QPainter(self)

        #RECORTE COHENSUTHERLAND
        if self.comando == 'cohenSutherland':
            if self.recorte:
                self.simplificaRecorteInicial = {'x': self.recorte[len(self.recorte)-1][0],'y': self.recorte[len(self.recorte)-1][1]}
                self.simplificaRecorteFinal = {'x': self.recorte[len(self.recorte)-1][2],'y': self.recorte[len(self.recorte)-1][3]}
                pen = QPen(cor, 2, Qt.DashLine)
                painter.setPen(pen)
                painter.drawLine(self.recorte[len(self.recorte)-1][0], self.recorte[len(self.recorte)-1][1], self.recorte[len(self.recorte)-1][2], self.recorte[len(self.recorte)-1][1]) 
                painter.drawLine(self.recorte[len(self.recorte)-1][0], self.recorte[len(self.recorte)-1][1], self.recorte[len(self.recorte)-1][0], self.recorte[len(self.recorte)-1][3]) 
                painter.drawLine(self.recorte[len(self.recorte)-1][0], self.recorte[len(self.recorte)-1][3], self.recorte[len(self.recorte)-1][2], self.recorte[len(self.recorte)-1][3]) 
                painter.drawLine(self.recorte[len(self.recorte)-1][2], self.recorte[len(self.recorte)-1][3], self.recorte[len(self.recorte)-1][2], self.recorte[len(self.recorte)-1][1]) 
                for px1,py1,px2,py2 in self.retas_dda:
                    valores = cohenSutherland(self.simplificaRecorteInicial, self.simplificaRecorteFinal, px1, py1, px2, py2)
                    if not valores:
                        continue
                    (x1, y1, x2, y2) = valores
                    px1 = x1
                    py1 = y1
                    px2 = x2
                    py2 = y2
                    for result in bresenhan(px1,py1,px2,py2, cor):
                        painter.drawPoint(result['x'], result['y'])

                for px1,py1,px2,py2 in self.retas_bre:
                    valores = cohenSutherland(self.simplificaRecorteInicial, self.simplificaRecorteFinal, px1, py1, px2, py2)
                    if not valores:
                        continue
                    (x1, y1, x2, y2) = valores
                    px1 = x1
                    py1 = y1
                    px2 = x2
                    py2 = y2
                    for result in bresenhan(px1,py1,px2,py2, cor):
                        painter.drawPoint(result['x'], result['y'])
            self.update()
        
        elif self.comando == 'liangBarsky':
            if self.recorte:
                self.simplificaRecorteInicial = {'x': self.recorte[len(self.recorte)-1][0],'y': self.recorte[len(self.recorte)-1][1]}
                self.simplificaRecorteFinal = {'x': self.recorte[len(self.recorte)-1][2],'y': self.recorte[len(self.recorte)-1][3]}
                pen = QPen(cor, 2, Qt.DashLine)
                painter.setPen(pen)
                painter.drawLine(self.recorte[len(self.recorte)-1][0], self.recorte[len(self.recorte)-1][1], self.recorte[len(self.recorte)-1][2], self.recorte[len(self.recorte)-1][1]) 
                painter.drawLine(self.recorte[len(self.recorte)-1][0], self.recorte[len(self.recorte)-1][1], self.recorte[len(self.recorte)-1][0], self.recorte[len(self.recorte)-1][3]) 
                painter.drawLine(self.recorte[len(self.recorte)-1][0], self.recorte[len(self.recorte)-1][3], self.recorte[len(self.recorte)-1][2], self.recorte[len(self.recorte)-1][3]) 
                painter.drawLine(self.recorte[len(self.recorte)-1][2], self.recorte[len(self.recorte)-1][3], self.recorte[len(self.recorte)-1][2], self.recorte[len(self.recorte)-1][1]) 
                for px1,py1,px2,py2 in self.retas_dda:
                    valores = liangBarsky(self.simplificaRecorteInicial, self.simplificaRecorteFinal, px1, py1, px2, py2)
                    if not valores:
                        continue
                    (x1, y1, x2, y2) = valores
                    px1 = x1
                    py1 = y1
                    px2 = x2
                    py2 = y2
                    for result in bresenhan(px1,py1,px2,py2, cor):
                        painter.drawPoint(result['x'], result['y'])

                for px1,py1,px2,py2 in self.retas_bre:
                    valores = liangBarsky(self.simplificaRecorteInicial, self.simplificaRecorteFinal, px1, py1, px2, py2)
                    if not valores:
                        continue
                    (x1, y1, x2, y2) = valores
                    px1 = x1
                    py1 = y1
                    px2 = x2
                    py2 = y2
                    for result in bresenhan(px1,py1,px2,py2, cor):
                        painter.drawPoint(result['x'], result['y'])
            self.update()
        else:

            pen = QPen(Qt.red, 10, Qt.SolidLine)
            painter.setPen(pen)   
            for p in self.BezCur:
                painter.drawPoint(p[0], p[1])

            if self.BezierPtsControle == self.BezierVarControle:                             
                    pen = QPen(Qt.blue, 3, Qt.SolidLine)
                    painter.setPen(pen) 
                    aux = bezier(500, self.BezCur)

                    for pontos in aux:
                        painter.drawPoint(pontos['x'], pontos['y'])

            self.update()   
            #DDA
                #TRANSLAÇÃO
            if (self.getATrans_dda != 0 or self.getBTrans_dda != 0):
                for x1,y1,x2,y2 in self.retas_dda:
                    for result in dda(x1, y1, x2, y2, cor):
                        painter.drawPoint(result['x'],result['y'])

                #ROTAÇÃO
            elif (self.getRota_dda != 0):
                for x1,y1,x2,y2 in self.retas_dda:
                    for result in dda(x1, y1, x2, y2 , cor):
                        painter.drawPoint(result['x'],result['y'])

                #ESCALA
            elif (self.getAEscala_dda != 0 or self.getBEscala_dda != 0):
                for x1,y1,x2,y2 in self.retas_dda:
                    for result in dda(x1, y1, x2, y2, cor):
                        painter.drawPoint(result['x'],result['y'])

                #CISALHAMENTO
            elif (self.getACisa_dda != 0 or self.getBCisa_dda != 0):
                for x1,y1,x2,y2 in self.retas_dda:
                    for result in dda(x1, y1, x2, y2, cor):
                        painter.drawPoint(result['x'],result['y'])

                #REFLEXÃO
            elif(self.reflex_dda != 0):
                for x1,y1,x2,y2 in self.retas_dda:
                    for result in dda(x1, y1, x2, y2, cor):
                        painter.drawPoint(result['x'],result['y'])

                #RETA PADRÃO
            elif (self.getACisa_dda == 0 and self.getBCisa_dda == 0 and self.getATrans_dda == 0 and self.getBTrans_dda == 0 and self.getAEscala_dda == 0 and self.getBEscala_dda == 0 and self.getRota_dda == 0 and self.reflex_dda == 0):
                for x1,y1,x2,y2 in self.retas_dda:
                    for result in dda(x1,y1,x2,y2,cor):
                        painter.drawPoint(result['x'],result['y'])

            #Brensenham
                #TRANSLAÇÃO
            if (self.getATrans_bre != 0 or self.getBTrans_bre != 0):
                for x1,y1,x2,y2 in self.retas_bre:
                    for result in bresenhan(x1, y1, x2, y2, cor):
                        painter.drawPoint(result['x'],result['y'])

                #ROTAÇÃO
            elif (self.getRota_bre != 0):
                for x1,y1,x2,y2 in self.retas_bre:
                    for result in bresenhan(x1, y1, x2, y2, cor):
                        painter.drawPoint(result['x'],result['y']) 

                #CISALHAMENTO
            elif (self.getACisa_bre != 0 or self.getBCisa_bre != 0):
                for x1,y1,x2,y2 in self.retas_bre:
                    for result in bresenhan(x1, y1, x2, y2, cor):
                        painter.drawPoint(result['x'],result['y'])                   

                #ESCALA
            elif (self.getAEscala_bre != 0 or self.getBEscala_bre != 0):
                for x1,y1,x2,y2 in self.retas_bre:
                    for result in bresenhan(x1, y1, x2, y2,cor):
                        painter.drawPoint(result['x'],result['y'])

                #RETA PADRÃO
            elif(self.getACisa_bre == 0 and self.getBCisa_bre == 0 and self.getATrans_bre == 0 and self.getBTrans_bre == 0 and self.getAEscala_bre == 0 and self.getBEscala_bre == 0 and self.getRota_bre == 0):                    
                for x1,y1,x2,y2 in self.retas_bre:
                    for result in bresenhan(x1,y1,x2,y2,cor):
                        painter.drawPoint(result['x'],result['y'])  

            #Brensenham Circulo
                #TRANSLAÇÃO
            if (self.getATrans_breCirc != 0 or self.getBTrans_breCirc != 0):        
                for x1,y1,x2,y2 in self.Brecirculos:
                    for result in bresenhan_Circunferencia(x1, y1, x2, y2, cor):
                        painter.drawPoint(result['x'],result['y'])

                #ROTAÇÃO
            elif (self.getRota_breCirc != 0):
                for x1,y1,x2,y2 in self.Brecirculos:
                    for result in bresenhan_Circunferencia(x1, y1, x2, y2, cor):
                        painter.drawPoint(result['x'],result['y'])       

                #CISALHAMENTO A
            elif (self.getACisa_breCirc != 0 or self.getBCisa_breCirc != 0):
                for x1,y1,x2,y2 in self.Brecirculos:
                    for result in bresenhan_Circunferencia(x1, y1, x2, y2, cor):
                        painter.drawPoint(result['x'],result['y'])             

                #ESCALA
            elif (self.getAEscala_breCirc != 0 or self.getBEscala_breCirc != 0):
                for x1,y1,x2,y2 in self.Brecirculos:
                    for result in bresenhan_Circunferencia(x1, y1, x2, y2,cor):
                        painter.drawPoint(result['x'],result['y'])

                #CIRCULO PADRÃO
            elif(self.getACisa_breCirc == 0 and self.getBCisa_breCirc == 0 and self.getATrans_breCirc == 0 and self.getBTrans_breCirc == 0 and self.getAEscala_breCirc == 0 and self.getBEscala_breCirc == 0 and self.getRota_breCirc == 0): 
                for x1,y1,x2,y2 in self.Brecirculos:
                    for result in bresenhan_Circunferencia(x1,y1,x2,y2,cor):
                        painter.drawPoint(result['x'],result['y'])     


    
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = CG()
    sys.exit(app.exec_())
