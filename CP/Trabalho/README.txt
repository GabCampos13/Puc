Tenha certeza de que todos os arquivo estão na mesma pasta, tanto os arquivos de teste e execução

------------------------------------------------------------------

O codigo deve ser compilado com o comando:

g++ -sdt=c++11 dtc_paralelo.cpp -o resp -fopenmp

O código deve ser executado com o comando:

./resp
------------------------------------------------------------------
	O código é uma técnica de inteligência artificial de ávore de decisão(ID3) que foi implementada de forma recursiva e pode ser encontrada no link:

https://github.com/hafeezali/Parallel-Decision-Tree-Classifier/blob/master/dtc_seq.cpp

	Porém, nosso código teve uma alteração da versão original pois acrescentamos o hit mark(quantos acertos teve)e o accuracy(quantos acertos teve dividido pelo total), alem de quantos valores positivos(Vitoria do time Radiant) e valores negativos(Vitoria do time Dire), que ja continham no código original, separamos também o Ground truth test do arquivo original, onde ocorre a verificação de acertos do treinamento do algoritmo com a resposta original do dataset.

	O dataset utilizado foi de um jogo online do estilo MOBA, chamado dota2,o jogo consistem e uma batalha de 5 herois de cada time tentando destruir a base do outro(Radiant e Dire), onde, no arquivo de entrada csv, a primeira coluna está descrevendo a região aonde o jogo foi jogado, a segunda é o estilo de jogo, a terceira é o tipo de jogo, e da quarta até a penultima os herois escolhidos no jogo, já o ultimo é o Ground Truth test, onde demonstra qual time ganhou a partida.


Link do Data set:
https://archive.ics.uci.edu/ml/datasets/Dota2+Games+Results






