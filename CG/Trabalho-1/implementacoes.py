from math import sqrt

def dda(x1,y1,x2,y2, cor): #Código passado em sala de aula

    x = x1
    y = y1
    dx = x2 - x
    dy = y2 - y
    colore = []

    if abs(dx) > abs(dy) :
        passos = abs(dx)
    else:
        passos = abs(dy)


    if passos == 0:
        return colore

    xincr = dx/passos
    yincr = dy/passos

    for _ in range(int(passos)):
        x += xincr
        y += yincr
        colore.append({'x': round(x),'y': round(y)})
    
    return colore



def bresenhan(x1,y1,x2,y2, cor): #Código passado em sala de aula
    x = x1
    y  = y1
    dx = x2 - x
    dy = y2 - y
    colore = []

    if dx < 0 :
        dx = -dx; 
        xincr = -1
    else: 
        xincr = 1

    if dy < 0 : 
        dy = -dy
        yincr = -1
    else: 
        yincr = 1
        
    if dx > dy : #1 caso
        p = 2 * dy-dx
        const1 = 2 * dy; 
        const2 = 2 * (dy-dx)
        for i in range(int(dx)):
            x += xincr  #sempre atualiza x
            if p < 0 :
                p += const1
            else:
                y += yincr
                p += const2
            colore.append({'x': x, 'y': y})

    else: #segundo caso
        p = 2 * dx-dy; const1 = 2 * dx; const2 = 2 * (dx-dy)
        for i in range(int(dy)):
            y += yincr #sempre atualiza y
            if p < 0 :
                p += const1
            else:
                p += const2
                x += xincr            
            colore.append({'x': x, 'y': y})
    return colore

def bresenhan_Circunferencia(x1,y1,x2,y2, cor): #Código passado em sala de aula
    raio = round(sqrt((x1 - x2)**2  + (y1 - y2)**2)) #sqrt{( xini - xfinal )^ 2 + ( yini + yfinal )^ 2}  TRINOMIO QUADRADO PERFEITO
    x = 0
    y = raio    
    p = 3 - (2 * raio)
    circulo = plotaSimetricos(x1,y1,x,y)
    while x < y:
        if p < 0:
            p += (4 * x) + 6
        else:
            p += 4 * (x - y) + 10
            y -= 1
        x += 1
        circulo += plotaSimetricos(x1,y1,x,y)
    return circulo

def plotaSimetricos(xcentro,ycentro,x,y): #Código passado em sala de aula
    pontos = []
    pontos.append({'x': xcentro + x, 'y': ycentro + y})
    pontos.append({'x': xcentro + x, 'y': ycentro - y})
    pontos.append({'x': xcentro - x, 'y': ycentro + y})
    pontos.append({'x': xcentro - x, 'y': ycentro - y})
    pontos.append({'x': xcentro + y, 'y': ycentro + x})
    pontos.append({'x': xcentro + y, 'y': ycentro - x})
    pontos.append({'x': xcentro - y, 'y': ycentro + x})
    pontos.append({'x': xcentro - y, 'y': ycentro - x})
    return pontos

def cohenSutherland(p1, p2, Tx1, Ty1, Tx2, Ty2):
    aceito = False
    feito = False
    (xmax, ymax, xmin, ymin) = limites(p1, p2)
    (x1, y1, x2, y2) = (Tx1, Ty1, Tx2, Ty2)
    
    while not feito:
        cod1 = calculaCodigo(p1, p2, x1, y1)
        cod2 = calculaCodigo(p1, p2, x2, y2)
        if cod1 == 0 and cod2 == 0:
            aceito = True
            feito  = True
        elif cod1 & cod2 != 0:
            feito  = True
        else:
            if cod1 != 0:
                cfora = cod1
            else:
                cfora = cod2

            if cfora & 1 == 1: #se bit 0 está setado
                xint = xmin
                yint = y1 + (y2-y1) * (xmin-x1)/ (x2-x1)
            elif cfora & 2 == 2: #se bit 1 está setado
                xint = xmax
                yint = y1 + (y2-y1) * (xmax-x1)/(x2-x1)
            elif cfora & 4 == 4: #se bit 2 está setado
                yint = ymin
                xint = x1 + (x2-x1) * (ymin-y1)/(y2-y1)
            elif cfora & 8 == 8: #se bit 3 está setado
                yint = ymax
                xint = x1 + (x2-x1) * (ymax-y1)/(y2-y1)

            if cfora == cod1: #atualiza ponto incial da reta
                x1 = xint
                y1 = yint
            else:             #atualiza ponto final da reta
                x2 = xint
                y2 = yint
    if(aceito):
        return (round(x1), round(y1), round(x2), round(y2))
    else:
        return ()

def calculaCodigo(p1, p2, x, y):
    cod = 0
    (xmax, ymax, xmin, ymin) = limites(p1, p2)
    if x < xmin:
        cod += 1
    elif x > xmax:
        cod += 2

    if y < ymin:
        cod += 4
    elif y > ymax:
        cod += 8

    return cod

def limites(p1, p2):
    if p1['x'] > p2['x']:
        xmax = p1['x']
        xmin = p2['x']
    else:
        xmax = p2['x']
        xmin = p1['x']

    if p1['y'] > p2['y']:
        ymax = p1['y']
        ymin = p2['y']
    else:
        ymax = p2['y']
        ymin = p1['y']
    
    return(xmax, ymax, xmin, ymin)

def liangBarsky(p1, p2,  Tx1, Ty1, Tx2, Ty2):
    u1 = 0
    u2 = 1

    (x1, y1, x2, y2) = (Tx1, Ty1, Tx2, Ty2)
    (xmax, ymax, xmin, ymin) = limites(p1, p2)

    dx = x2 - x1
    dy = y2 - y1
    
    u1, u2, result = cliptest(-dx, x1 - xmin, u1, u2)
    if result: #fronteira esquerda
        u1, u2, result = cliptest(dx, xmax - x1, u1, u2)
        if result: #fronteira direita
            u1, u2, result = cliptest(-dy, y1 - ymin, u1, u2)
            if result: #fronteira inferior
                u1, u2, result = cliptest(dy, ymax - y1, u1, u2)
                if result: #fronteira superior
                    if u2 < 1:
                        x2 = x1 + (dx * u2) # x1 = valor inicial antes do recorte
                        y2 = y1 + (dy * u2) # y1 = valor inicial antes do recorte
                    if u1 > 0:
                        x1 = x1 + (dx * u1)
                        y1 = y1 + (dy * u1)
                    return (round(x1), round(y1), round(x2), round(y2))

    return ()

def cliptest(p, q, u1, u2):
    result = True
    if p < 0:
        r = q/p
        if r > u2:
            result = False #fora da janela
        elif r > u1:
            u1 = r
    elif p > 0:
        r = q/p
        if r < u1:
            result = False #fora da janela
        elif r < u2:
            u2 = r
    elif q < 0:
        result = False
    return (u1, u2, result) #False = fora da janela, True = dentro da janela