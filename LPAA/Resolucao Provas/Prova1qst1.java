import java.util.*;
	
	public class qst1 {
		public static void main(String[]args){
			    Scanner leia = new Scanner(System.in);
			    for(int diaFim = leia.nextInt();diaFim != 0;diaFim = leia.nextInt()){
				int bac1 = leia.nextInt();
				int bac2 = leia.nextInt();
				int bac3 = leia.nextInt();
				int bac4 = leia.nextInt();
				System.out.println(varDiasBac(diaFim,bac1,bac2,bac3,bac4));
			    }
		
		}
		public static int varDiasBac(int diaFim,int bac1,int bac2,int bac3,int bac4){
			int dia = 4;
			int total = bac1 + bac2 + bac3 + bac4;
			total = (total*2)-bac1;
			int var1 = total;
			dia = 5;
			if(diaFim == dia)return total;
			total = (total*2)-bac2;
			int var2 = total;
			dia = 6;
			if(diaFim == dia)return total;
			total = (total*2)-bac3;
			int var3 = total;
			dia = 7;
			if(diaFim == dia)return total;
			total = (total*2)-bac4;
			int var4 = total;
			dia = 8;
			if(diaFim == dia)return total;
	
			if(diaFim == dia)return total;
			for (int x = dia;x < diaFim;x++){
				if(dia % 4 == 1){
					total = total - var1;
					var1 = total;
				}if(dia % 4 == 2){
					total = total - var2;
					var2 = total;
				}if(dia % 4 == 3){
					total = total - var3;
					var3 = total;
				}if(dia % 4 == 0){
					total = total - var4;
					var4 = total;
				}
			}return total;
		}
	}

