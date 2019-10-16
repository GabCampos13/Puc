Created By: Gabriel Oliveira Campos

Como funciona a execução do código do trabalho de computação gráfica:

---------------------------CRIAÇÃO DE RETAS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Para criar uma reta DDA, vá ao menu e selecione RETAS, depois selecione DDA, clique e segure no ponto inicial da reta e arraste até o final desejado da reta.
Para criar uma reta Bresenhan, vá ao menu e selecione RETAS, depois selecione Bresenhan, clique e segure no ponto inicial da reta e arraste até o final desejado da reta.


---------------------------CRIAÇÃO DE CIRCULOS-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Para criar um circulo, vá ao menu e selecione Circulo e depois selecione Bresenhan, clique e segure no ponto inicial do circulo e arraste até o final desejado do raio desse circulo.


---------------------------TRANSFORMAÇÕES(TRANSLAÇÃO)------------------------------------------------------------------------------------------------------------------------------------------------------------------
Para aplicar qualquer transformações nas retas e/ou no circulo, va ao menu e selecione Transformações e depois selecione qual transformação você quer realizar,
se for uma translação, selecione a mesma no menu de transformações e digite os valores desejados para X e Y;


---------------------------TRANSFORMAÇÕES(ESCALA)----------------------------------------------------------------------------------------------------------------------------------------------------------------------
se for uma escala, digite o valor para as variáveis A e B, sendo A a escala de X e B a escala de Y;


---------------------------TRANSFORMAÇÕES(ROTAÇÃO)---------------------------------------------------------------------------------------------------------------------------------------------------------------------
se for uma rotação, digite o angulo desejado para a rotação da reta/circulo;


---------------------------TRANSFORMAÇÕES(REFLEXÃO)--------------------------------------------------------------------------------------------------------------------------------------------------------------------
se for uma reflexão, selecione a opção reflexão, se for uma reflexão do centro, selecione a opção "Reflete no centro", 
se for uma reflexão ao eixo X, selecione a opção "Reflete em X", 
se for uma reflexão ao eixo Y, selecione a Opção "Reflete em Y";


---------------------------TRANSFORMAÇÕES(CISALHAMENTO)----------------------------------------------------------------------------------------------------------------------------------------------------------------
se for um cisalhamento, selecione a opção cisalhamento, se quiser fazer um cisalhamento no eixo X, selecione "cisalhamento em X" e digite o valor de A desejado para o cisalhamento,
se quiser fazer um cisalhamento no eixo Y, selecione "cisalhamento em Y" e digite o valor de B desejado para o cisalhamento;


---------------------------RECORTE---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
se quiser fazer um recorte nas retas usando Cohen-Sutherland, selecione a opção recorte e depois a opção "Cohen-Sutherland", depois crie um quadro(segure e arraste do início até o final desejado do quadro),
se quiser fazer um recorte nas retas usando Liang-Barsky, selecione a opção recorte e depois a opção "Liang-Barsky", depois crie um quadro(segure e arraste do início até o final desejado do quadro),

para desativar os quadros do recorte, selecione qualquer outra opção sem ser "Recorte" no menu.


---------------------------CONSIDERAÇÕES FINAIS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Infelizmente os algoritmos de preenchimento em python tem uma biblioteca muito mais complicada que o esperado, por isso não foram implementados.