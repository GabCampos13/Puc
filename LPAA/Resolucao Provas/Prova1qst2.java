import java.util.Scanner;

public class qst2 {
	public static void main(String[]args){
		Scanner leia = new Scanner(System.in);
		int[] preco = new int[100];
		int[] peso = new int[100];
		int pesoMax;
		for(int lista = leia.nextInt();lista != 0;lista = leia.nextInt()){
			for(int x = 0;x < lista;x++){
				preco[x] = leia.nextInt();
				peso[x] = leia.nextInt();
			}
			pesoMax = leia.nextInt();
			calcularvol(pesoMax,preco,peso);
			for(int x = 0;x < preco.length;x++){
				preco[x] = 0;
				peso[x] = 0;
			}
		}
	}
		public static void calcularvol(int pesoMax,int[] preco,int[] peso){
		int pesoLista = 0;
		int precoLista = 0;
		for(int x = 0;x < preco.length ;x++){
			if(pesoLista + peso[x] < pesoMax){
				pesoLista = pesoLista + peso[x];
				precoLista = precoLista + preco[x];
			}
		}System.out.println(precoLista);
	}
}

