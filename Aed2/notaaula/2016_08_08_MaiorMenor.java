class MaiorMenor {
   //...
   int maior, menor;

   if(vet[0] > vet[1]){
      maior = vet[0];
      menor = vet[1];
   } else {
      maior = vet[1];
      menor = vet[0];
   }

   for(int i = 2; i < n; i++){
      if(maior < vet[i]){
         maior = vet[i];
      }
      if(menor > vet[i]){
         menor = vet[i];
      }
   }

}
