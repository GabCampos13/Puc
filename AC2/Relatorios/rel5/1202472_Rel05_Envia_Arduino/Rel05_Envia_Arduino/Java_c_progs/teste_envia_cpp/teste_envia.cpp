#include <iostream>
#include <windows.h>
#include <cstdlib>
#include <string.h>

// Para este programa o arduino dever� estar esperando dois n�meros !
using namespace std;

int main()
{

    string p1, p2, porta, linha;
    char *manda;

// Na linha abaixo voc� deve substituir com1 pela porta onde o Arduino est�
    system ("envia.exe com1 0 1");
    system("pause");

    cout<<"\n Digite a porta ->";
    cin>>porta;


    for(int i=0;i<10;i++)
    {
        linha = "envia.exe ";
        if(i%2==0) p1="1";
        else p1="0";
        p2="1";
        linha = linha + porta + " " + p1 + " " + p2;
        manda = new char[linha.length()+1];
        memcpy(manda, linha.c_str(), linha.length() + 1);
      //system("pause");
        system(manda);

    }


    linha = "envia.exe ";
    cout<<"\n\n\n Digite primeiro numero ->";
    cin>>p1;
    cout<<"\n Digite segundo numero ->";
    cin>>p2;

    linha = linha + porta + " " + p1+ " "+p2;
    manda = new char[linha.length()+1];
    memcpy(manda, linha.c_str(), linha.length() + 1);
    cout<<linha;
    system(manda);

    return 0;
}
