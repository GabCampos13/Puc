#include<stdio.h>
#include<string.h>
#include<utility>
#include<string>
#include<iostream>

using namespace std;

pair<int,int> Posicionamento(){

  char tamanho[3], tamanho2[3];
  int posicao,posicao2;
  scanf("%s",tamanho);
  scanf("%s",tamanho2);
        if (strcmp(tamanho, "XS") == 0) {

                posicao = 0;

        } else if (strcmp(tamanho, "S") == 0) {

                posicao = 1;

        } else if (strcmp(tamanho, "M") == 0) {

                posicao = 2;

        } else if (strcmp(tamanho, "L") == 0) {

                posicao = 3;

        } else if (strcmp(tamanho, "XL") == 0) {

                posicao = 4;

        } else if (strcmp(tamanho, "XXL") == 0) {

                posicao = 5;

        }
        if (strcmp(tamanho2, "XS") == 0) {

          posicao2 = 0;

        } else if (strcmp(tamanho2, "S") == 0) {

          posicao2 = 1;

        } else if (strcmp(tamanho2, "M") == 0) {

          posicao2 = 2;

        } else if (strcmp(tamanho2, "L") == 0) {

          posicao2 = 3;

        } else if (strcmp(tamanho2, "XL") == 0) {

          posicao2 = 4;

        } else if (strcmp(tamanho2, "XXL") == 0) {

          posicao2 = 5;

        }
  return make_pair(posicao,posicao2);
}


bool testaCamisa() {
	int camisa[6] = {0};

	pair<int,int> x;

	bool var = true;

	int n, m;

	scanf("%d",&n);

	scanf("%d",&m);



	for (int i = 0; i < m; i++) {

	  x = Posicionamento();

	  if(camisa[x.first] < (n/6)) {

	    camisa[x.first] = camisa[x.first] + 1; 

	  }else if (camisa[x.second] < (n/6)) {

	    camisa[x.second] = camisa[x.second] + 1;

	  }else {

	    var = false;
	  }

	}	

	return var;

}

int main() {

        int n;

        scanf("%d",&n);

        for (int i = 0; i < n; i++) {

                if (testaCamisa()) {

                        printf("YES\n");

                } else {

                        printf("NO\n");

                }

        }



        return 0;

}

