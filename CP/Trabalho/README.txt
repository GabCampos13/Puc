Tenha certeza de que todos os arquivo est�o na mesma pasta, tanto os arquivos de teste e execu��o

------------------------------------------------------------------

O codigo deve ser compilado com o comando:

g++ -sdt=c++11 dtc_paralelo.cpp -o resp -fopenmp

O c�digo deve ser executado com o comando:

./resp
------------------------------------------------------------------
	O c�digo � uma t�cnica de intelig�ncia artificial de �vore de decis�o(ID3) que foi implementada de forma recursiva e pode ser encontrada no link:

https://github.com/hafeezali/Parallel-Decision-Tree-Classifier/blob/master/dtc_seq.cpp

	Por�m, nosso c�digo teve uma altera��o da vers�o original pois acrescentamos o hit mark(quantos acertos teve)e o accuracy(quantos acertos teve dividido pelo total), alem de quantos valores positivos(Vitoria do time Radiant) e valores negativos(Vitoria do time Dire), que ja continham no c�digo original, separamos tamb�m o Ground truth test do arquivo original, onde ocorre a verifica��o de acertos do treinamento do algoritmo com a resposta original do dataset.

	O dataset utilizado foi de um jogo online do estilo MOBA, chamado dota2,o jogo consistem e uma batalha de 5 herois de cada time tentando destruir a base do outro(Radiant e Dire), onde, no arquivo de entrada csv, a primeira coluna est� descrevendo a regi�o aonde o jogo foi jogado, a segunda � o estilo de jogo, a terceira � o tipo de jogo, e da quarta at� a penultima os herois escolhidos no jogo, j� o ultimo � o Ground Truth test, onde demonstra qual time ganhou a partida.


Link do Data set:
https://archive.ics.uci.edu/ml/datasets/Dota2+Games+Results






