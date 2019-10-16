import java.util.*;
public class Prova {
	public static void main(String[]args){
		Scanner leia = new Scanner(System.in);
		int NumSuper = leia.nextInt();
		int Relacionamentos = leia.nextInt();
		while(NumSuper != 0 && Relacionamentos != 0){
			int[][] grafo = new int[NumSuper][NumSuper];
			for(int i = 0;i < Relacionamentos;i++){
			
				int s1 = leia.nextInt();
				int s2 = leia.nextInt();
			
				grafo[s1-1][s2-1] = 1;
				
			}	
			ResolveProb(grafo,NumSuper);
			NumSuper = leia.nextInt();
			Relacionamentos = leia.nextInt();
			
		}
		
		
		
	}
	public static void ResolveProb(int[][] grafo,int num){
		boolean resp = false;
		boolean definitivo = false;
		for(int i = 0;i < grafo.length;i++){
			for(int j = 0; j < grafo.length;j++){
				if(grafo[i][j] == 1){
				
					resp = CheckResto(grafo,i,j);
					if(resp == true)definitivo = true;

				}
			}
		}
		if(definitivo == true){
			System.out.println("Y");
		}else{
			System.out.println("N");
		}
	}
	public static boolean CheckResto(int[][] grafo,int i,int j){
		for(int x = 0;x < grafo.length;x++){
			for(int z = 0; z < grafo.length;z++){
				if(x != i && x != j && z !=i && z != j && grafo[x][z] == 1){

					return false;
					
				}
			}
		}
		return true;	
	}
}
