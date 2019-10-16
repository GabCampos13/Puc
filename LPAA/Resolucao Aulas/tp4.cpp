#include <stdio.h>
#include <stdlib.h>
const int movx[8]={ 1, 2, 2, 1,-1,-2,-2,-1},

          movy[8]={-2,-1, 1, 2, 2, 1,-1,-2};

char matrizEntrada[5][5];
char matrizPadrao[5][5]={

    '1', '1', '1', '1', '1',

    '0', '1', '1', '1', '1',

    '0', '0', ' ', '1', '1',

    '0', '0', '0', '0', '1',

    '0', '0', '0', '0', '0'

};

int movimentos;
void trocaPosicao(int Xini,int Yini,int XFinal,int Yfinal);//Faz os movimentos dos cavalos no tabuleiro
void printaMatriz();//Printa a matriz final
void DFS(int Trocas,int x,int y);//Faz a busca em profundidade para verificar as movimentacoes dos cavalos no tabuleiro
void arrumaTabuleiro();//Arruma o tabuleiro inicial do problema

int main ()

{
    int conjuntos;
    movimentos = 11;

    scanf("%d", &conjuntos);

    for(int x=0; x < conjuntos; x++){

        for(int i=0; i<5; i++){

            for(int j=0; j<5; j++) {

                scanf("%c", &matrizEntrada[i][j]);

                if(matrizEntrada[i][j] == '\n'){

                    scanf("%c", &matrizEntrada[i][j]);

                }

            }

        }

        arrumaTabuleiro();

        if(movimentos == 11){

            printf("Unsolvable in less than 11 move(s).\n");

        } else{

            printf("Solvable in %d move(s).\n", movimentos);

        }

    }



    return 0;

}



void trocaPosicao (int Xini, int Yini, int XFinal, int YFinal) {

    char aux = matrizEntrada[XFinal][YFinal];

    matrizEntrada[XFinal][YFinal] = matrizEntrada[Xini][Yini];

    matrizEntrada[Xini][Yini] = aux;

}


void printaMatriz(){

    for(int i=0;i<5; i++){

        for(int j=0;j<5; j++){

            printf("[%c] ", matrizEntrada[i][j]);

        }

        printf("\n");

    }

}

int comparacoes(){

  for(int i=0; i<5; i++){

        for(int j=0; j<5; j++){

            if(matrizEntrada[i][j] != matrizPadrao[i][j]){

                return 0;

            }

        }

    }
    return 1;

}

int validacoes(int x,int y){

  if(x < 5 && x >= 0 && y < 5 && y >= 0){

                return 1;

  }return 0;


}

void DFS (int Trocas,int x, int y) {

    if(Trocas == 11){

        return;

    }

    if(comparacoes()){

        if(movimentos > Trocas){

            movimentos = Trocas;

        }

        return;

    }



    for(int i=0; i<8; i++){

        int Novo_Tab_H = x + movx[i];

        int Novo_Tab_V = y + movy[i];

        if(validacoes(Novo_Tab_H,Novo_Tab_V)){

            trocaPosicao(x, y, Novo_Tab_H, Novo_Tab_V);

            DFS(Trocas+1, Novo_Tab_H, Novo_Tab_V);

            trocaPosicao(x, y, Novo_Tab_H, Novo_Tab_V);

        }

    }

}

void arrumaTabuleiro() {

    int Horizontal,Vertical = -1;

    for(int i=0;i<5; i++){

        for(int j=0;j<5; j++){

            if(matrizEntrada[i][j] == ' '){

                Horizontal = i;

                Vertical = j;

            }

        }

    }

    DFS(0,Horizontal, Vertical);

}

