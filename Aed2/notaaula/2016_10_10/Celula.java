class Celula {
   public Contato contato;
   public Celula prox;

   public Celula (){
      this.contato = new Contato();
      this.prox = null;
   }
}
