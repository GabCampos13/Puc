Created By: Gabriel Oliveira Campos

Como funciona a execu��o do c�digo do trabalho de computa��o gr�fica:

---------------------------CRIA��O DE RETAS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Para criar uma reta DDA, v� ao menu e selecione RETAS, depois selecione DDA, clique e segure no ponto inicial da reta e arraste at� o final desejado da reta.
Para criar uma reta Bresenhan, v� ao menu e selecione RETAS, depois selecione Bresenhan, clique e segure no ponto inicial da reta e arraste at� o final desejado da reta.


---------------------------CRIA��O DE CIRCULOS-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Para criar um circulo, v� ao menu e selecione Circulo e depois selecione Bresenhan, clique e segure no ponto inicial do circulo e arraste at� o final desejado do raio desse circulo.


---------------------------TRANSFORMA��ES(TRANSLA��O)------------------------------------------------------------------------------------------------------------------------------------------------------------------
Para aplicar qualquer transforma��es nas retas e/ou no circulo, va ao menu e selecione Transforma��es e depois selecione qual transforma��o voc� quer realizar,
se for uma transla��o, selecione a mesma no menu de transforma��es e digite os valores desejados para X e Y;


---------------------------TRANSFORMA��ES(ESCALA)----------------------------------------------------------------------------------------------------------------------------------------------------------------------
se for uma escala, digite o valor para as vari�veis A e B, sendo A a escala de X e B a escala de Y;


---------------------------TRANSFORMA��ES(ROTA��O)---------------------------------------------------------------------------------------------------------------------------------------------------------------------
se for uma rota��o, digite o angulo desejado para a rota��o da reta/circulo;


---------------------------TRANSFORMA��ES(REFLEX�O)--------------------------------------------------------------------------------------------------------------------------------------------------------------------
se for uma reflex�o, selecione a op��o reflex�o, se for uma reflex�o do centro, selecione a op��o "Reflete no centro", 
se for uma reflex�o ao eixo X, selecione a op��o "Reflete em X", 
se for uma reflex�o ao eixo Y, selecione a Op��o "Reflete em Y";


---------------------------TRANSFORMA��ES(CISALHAMENTO)----------------------------------------------------------------------------------------------------------------------------------------------------------------
se for um cisalhamento, selecione a op��o cisalhamento, se quiser fazer um cisalhamento no eixo X, selecione "cisalhamento em X" e digite o valor de A desejado para o cisalhamento,
se quiser fazer um cisalhamento no eixo Y, selecione "cisalhamento em Y" e digite o valor de B desejado para o cisalhamento;


---------------------------RECORTE---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
se quiser fazer um recorte nas retas usando Cohen-Sutherland, selecione a op��o recorte e depois a op��o "Cohen-Sutherland", depois crie um quadro(segure e arraste do in�cio at� o final desejado do quadro),
se quiser fazer um recorte nas retas usando Liang-Barsky, selecione a op��o recorte e depois a op��o "Liang-Barsky", depois crie um quadro(segure e arraste do in�cio at� o final desejado do quadro),

para desativar os quadros do recorte, selecione qualquer outra op��o sem ser "Recorte" no menu.


---------------------------CONSIDERA��ES FINAIS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Infelizmente os algoritmos de preenchimento em python tem uma biblioteca muito mais complicada que o esperado, por isso n�o foram implementados.