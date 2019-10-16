//Created by Gabriel Campos
#include<stdio.h>
#include<string.h>

#define N 100000

static int Pai[N];
static int Rank[N];
static int Elementos[N];

//all methods
void CriaGrupos(int n);
int ProcuraGrupo(int x);
bool GrupoIgual(int x,int y);
void Agrupa(int x,int y);
void Uniao(int x,int y);

int max;
//Return: main function,no returns;
//Method: Descobrir maior quantidade de amigos em um grupo(amigo do meu amigo tambem e meu amigo)
int main(){

	int x, y, i, j, qntd;
	scanf("%d", &qntd);
	for(int z = 0;z < qntd;qntd--){
		max = 1;
		scanf("%d%d", &x, &y);
		CriaGrupos(x);
		for(int p = 0;p < y;y--){
			scanf("%d%d", &i, &j);
			i--, j--;
			Uniao(i, j);
		}
		printf("%d\n", max);
	}
	return 0;
}
//Return: void
//Method: Seta valores iniciais nos arrays
void CriaGrupos(int j){
	for(int i = 0;i < j;i++){
		Pai[i]  = i;
		Rank[i] = 0;
		Elementos[i] = 1;
	}
}
//Return: int,FatherArray
//Method: Procura a qual grupo o elemento pertence
int ProcuraGrupo(int x){
	if( x != Pai[x] )
		Pai[x] = ProcuraGrupo(Pai[x]);
	return Pai[x];
}
//Return: bool,se um grupo for igual ao outro
//Method: compara se um grupo e igual ao outro
bool GrupoIgual(int x, int y){
	return ProcuraGrupo(x) == ProcuraGrupo(y);
}
//Return: void
//Method: Agrupa os grupos que tem amigos de amigos(amigo do meu amigo tambem e meu amigo)
void Agrupa(int x, int y){
	if( !GrupoIgual(x, y) ){
		if( Rank[x] > Rank[y] ){
			Pai[y] = x;
			Elementos[x] += Elementos[y];
			if(max < Elementos[x])max = Elementos[x];
		}
		else{
			Pai[x] = y;
			Elementos[y] += Elementos[x];
			if(max  < Elementos[y])max = Elementos[y];
			if(Rank[x] == Rank[y]){
				Rank[y] = Rank[y] + 1;
			}        
		}
	}

}
//Return: void
//Method: chama o metodo de agrupar usando grupos quem tem mesmos amigos
void Uniao(int x, int y){
	Agrupa(ProcuraGrupo(x), ProcuraGrupo(y));
}

