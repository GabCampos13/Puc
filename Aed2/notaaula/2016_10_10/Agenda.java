class Agenda {
   private No raiz;
   public Agenda (){
      raiz = null;
      //Inserir cada um dos 26 nos da arvore.
      inserir('M');
      inserir('G');
      inserir('T');
      //inseir as demais letras (...)
   }
   private void inserir(char letra){
		raiz = inserir(letra, raiz);
	}

	private No inserir(char letra, No i) throws Exception {
		if (i == null) {
         i = new No(letra);

      } else if (letra < i.elemento) {
         i.esq = inserir(letra, i.esq);

      } else if (letra > i.elemento) {
         i.dir = inserir(letra, i.dir);

      } else {
         throw new Exception("Erro ao inserir na arvore binaria!");
      }

		return i;
	}

   public void inserir(Contato contato){
   }
   public void remover(String nome){
   }
	public boolean pesquisarNome(String nome) {
		return pesquisarNome(raiz, nome);
	}

	private boolean pesquisarNome(No no, String nome) {
      boolean resp;
		if (no == null) { 
         resp = false;

      } else if (Char.toUpper(nome.charAt(0)) == no.letra) { 
         resp = pesquisarNome(no.primeiro.prox, nome);

      } else if (Char.toUpper(nome.charAt(0)) < no.letra) { 
         resp = pesquisarNome(no.esq, nome); 

      } else { 
         resp = pesquisarNome(no.dir, nome); 
      }
      return resp;
	}

   private boolean pesquisarNome(Celula i, String nome) {
      boolean resp = false;
      for(; i != null; i = i.prox){
         if(i.nome.equals(nome) == true){        
            resp = true;
         }
      }
      return resp;
   }

   public boolean pesquisar(int cpf){
      return pesquisa(raiz, cpf);
   }

   public boolean pesquisar(No i, int cpf)
      boolean resp = false;
      if(i != null){
         resp = pesquisar(i.primeiro.prox, cpf);
         if(resp == false){
            resp = pesquisar(i.esq, cpf);
         }
         if(resp == false){
            resp = pesquisar(i.dir, cpf);
         }
      }
      return resp;
   }

   public boolean pesquisar(Celula i, int cpf){
      boolean resp = false;
      while(i != null){
         if(i.contato.cpf == cpf){
            resp = true;
            i = null;
         } else {
            i = i.prox;
         }
      }
      return resp;
   }
}





