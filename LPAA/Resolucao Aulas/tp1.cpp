//Created by Gabriel Campos
#include <stdio.h>
#include <stdlib.h>
#define TAM 100
void completaMatriz(int tamanho);
void somaRetangulo(int tamanho,int matriz[][TAM]);
void PrintSoma(int maior);
//Funcao(Main): Metodo principal,Apenas pega o tamanho da matriz
int main(){
	int tamanho;
	scanf(" %d\n",&tamanho);
	completaMatriz(tamanho);
	return(0);	
}
//Funcao(completaMatriz): Cria a matriz com os valores gerados pelo usuario
//Retorna: Nada
void completaMatriz(int tamanho){
	int i,j;
	int matriz[TAM][TAM];
	for(i = 0;i < tamanho;i++){
		for(j = 0;j < tamanho;j++){

			scanf(" %d",&matriz[i][j]);

		}
	}
	somaRetangulo(tamanho,matriz);
}
//Funcao(somaRetangulo): Compara todos os possiveis retangulos da matriz para descobrir o retangulo de maior valor
//Retona: Nada
void somaRetangulo(int tamanho,int matriz[][TAM]){

	int maior = 0;
	int soma = 0;
	int i,j,k,l,m,n;
	for(i = 0;i < tamanho;i++){
		for(j = 0;j < tamanho;j++){
			for(k = 0;k < tamanho;k++){
				for(l = 0;l < tamanho;l++){
					for (m = i;m <= k;m++){
						for (n = j;n <= l;n++){

							soma = soma +  matriz[m][n];

						}
					}
					if(soma > maior){
						maior = soma;
					}
					soma = 0;
				}		
			}
		}
	}
	PrintSoma(maior);
}
//Funcao: Printa a maior soma de dentro do retangulo da matriz
//Retorna: Nada
void PrintSoma(int maior){
	printf("%d\n",maior);
}

