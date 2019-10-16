//Created by Gabriel Campos
#include <stdio.h>
#define N 30398
//Return: Main function,no returns
//Method: Pesquisa o numero de maneiras para compor a quantidade de dollares
long int * moedas_meios(long quantidade[]){
	int i,j;
	int moedas[] = {5,10,20,50,100,200,500,1000,2000,5000,10000};//dollar ja transformado em cents
        quantidade[0] = 1;
        for(int i = 0;i < 11;i++){
                for(j = moedas[i];j < N;j++){
                        quantidade[j] += quantidade[j - moedas[i]];
                }
        }return quantidade;
}
int main(){
	long quantidade[N];
	moedas_meios(quantidade);
        float valores;
        while(scanf("%f", &valores) == 1 && valores){//quando for zero parar
                int moeda = ((valores + 0.001)*100);//arredondamento
                printf("%6.2f%17ld\n",valores,quantidade[moeda]);
        }return 0;
}

