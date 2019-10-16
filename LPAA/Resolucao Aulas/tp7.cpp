#include <iostream>
#include <vector>
#include <stack>

using namespace std;

struct Pico {
  int Destino;
  int distancia;
};

void printGrafo(vector<vector<Pico>> &grafo) {
  for(int i = 0; i < grafo.size(); i++ ) {
      cout << i << ": ";
      for (int j = 0; j < grafo[i].size(); j++ ) {
        cout << "(" << grafo[i][j].Destino << ", ";
        cout << grafo[i][j].distancia << ") | ";
      }
      cout << endl;
    }
}
 
void ConstructColonias (int tam, vector<vector<Pico>> &grafo) {
  int vertice, distancia;
  for(int i = 0; i < tam-1; i++) {
    cin >> vertice >> distancia;
    grafo[i+1].push_back({vertice, distancia});
    grafo[vertice].push_back({(i+1),distancia});
  }
}

long DFS (vector<vector<Pico>> grafo, int origem, int Destino) {
  stack<int> x;
  vector<bool> visitado (grafo.size(),false);
  vector<long>  distancias (grafo.size(), 0);
  x.push(origem);
  
  while(!x.empty() && !visitado[Destino]) {
    int var = x.top();
    x.pop();
    if(!visitado[var]) {
      visitado[var] = true;
      for(int i = 0 ; i < grafo[var].size() ; i++ ){
        x.push(grafo[var][i].Destino);
        distancias[grafo[var][i].Destino] = grafo[var][i].distancia + distancias[var];
      }
    }
  }
  
  return distancias[Destino];  
}
int main () {
  int Colonias, Testes, Entrada, Destino;
  cin >> Colonias;
  while( Colonias != 0 ) {
    vector<vector<Pico>> grafo (Colonias);
    ConstructColonias(Colonias, grafo);
    cin >> Testes; 
    for(int i = 0; i < Testes; i++){
      cin >> Entrada >> Destino;
      cout << DFS(grafo,Entrada,Destino) << " ";
    }
    cout << endl;
    cin >> Colonias;
    
  }
  
  return 0;
}
