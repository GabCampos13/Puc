class No {
   public Celula primeiro;
   public Celula ultimo;
   public No esq;
   public No dir;
   public char letra;

   public No (char letra){
      this.letra = letra;
      this.esq = this.dir = null;
      this.primeiro = this.ultimo = new Celula();
   }

}
