//Suponha que nossa Fila não tem o ponteiro último e faça o método de inserir.
//
public class FilaSemUltimo {
	private Celula primeiro;

	public Fila() {
		primeiro = new Celula();
	}

	/*
   public void inserir(int x) {
		ultimo.prox = new Celula(x);
		ultimo = ultimo.prox;
	}
   */

   public void inseir(int x){
      Celula i = primeiro;
      while(i.prox != null){
         i = i.prox;
      }
      i.prox = new Celula(x);
      i = null;
   }
}













