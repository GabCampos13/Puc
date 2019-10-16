
import java.util.Scanner;
import java.text.DecimalFormat;
import java.util.ArrayList;
class Prato{
    public static int[] custo = new int[100];
    public static double[][][] lucro = new double[50][100][2000];;
    public static int [] beneficio = new int[100];
    public static int[][][] mem1 = new int[50][100][2000];
    public static int[][][] mem2 = new int[50][100][2000];;
    
    public Prato(int [] custo,double [][][] lucro){
        this.custo = custo;
        this.lucro = lucro;
    }
    
}
//Class Culinaria
class Culinaria{
    public static int dias;
    public static int pratos;
    public static int orcamento;
}
class TPDinamico{
      
    public static void main(String[] args){
        DecimalFormat deci = new DecimalFormat("0.0");
 
        Scanner leia = new Scanner(System.in);
        Culinaria culinaria = new Culinaria();
        culinaria.dias = leia.nextInt();
        culinaria.pratos = leia.nextInt();
        culinaria.orcamento = leia.nextInt();
 
        Scanner scan = new Scanner(System.in);
         
            while(culinaria.dias != 0 && culinaria.pratos != 0 && culinaria.orcamento !=0){
                CriaPrato(culinaria);
                Executa(culinaria,deci);
                culinaria.dias = leia.nextInt();
                culinaria.pratos = leia.nextInt();
                culinaria.orcamento = leia.nextInt();
            }
        }
    // Função CriaPrato: coloca o custo e beneficio dos pratos
    public static void CriaPrato(Culinaria culinaria){
        Scanner leia = new Scanner(System.in);
        for(int i = 1;i <= culinaria.pratos;i++){
            Prato.custo[i] = leia.nextInt();
            Prato.beneficio[i] = leia.nextInt();
        }
        
    }
    //Função executa: cria a tabela de programacao dinamica e depois mostra o resultado do problema
        public static void Executa(Culinaria culinaria, DecimalFormat deci){
            for (int i = 0; i <= culinaria.dias; i++){
                for (int j = 0; j <= culinaria.pratos; j++){
                    for (int k = 0; k <= culinaria.orcamento; k++){
                        if (i == 0){
                            Prato.lucro[i][j][k] = 0;
                        }else{
                            Prato.lucro[i][j][k] = -1;
                        }
                        Prato.mem1[i][j][k] = 0;
                        Prato.mem2[i][j][k] = 0;
                    }
                }
            }
            
            for (int i = 1; i <= Culinaria.dias; i++){
                for (int j = 1; j <= Culinaria.pratos; j++){
                    for (int k = 0; k <= Culinaria.orcamento; k++){
                        for (int l = 1; l <= i; l++){
                            if (k >= l*Prato.custo[j]){
                                for (int m = 1; m <= Culinaria.pratos; m++){ 
                                    if (m != j && Prato.lucro[i-l][m][k-l*Prato.custo[j]] != -1){
                                        double beneficioExtra = Prato.beneficio[j];
                                        if (l >= 2){
                                            beneficioExtra = 1.5 * Prato.beneficio[j];
                                        }
                                        if (Prato.lucro[i-l][m][k-l*Prato.custo[j]] + beneficioExtra > Prato.lucro[i][j][k] || (Prato.lucro[i-l][m][k-l*Prato.custo[j]] + beneficioExtra == Prato.lucro[i][j][k] &&
                                           (Prato.mem1[i][j][k] == 0 || Prato.mem2[i][j][k] * Prato.custo[Prato.mem1[i][j][k]] > l*Prato.custo[m]))){
                                 
                                            Prato.lucro[i][j][k] = Prato.lucro[i-l][m][k-l*Prato.custo[j]] + beneficioExtra;      
                                            Prato.mem1[i][j][k] = m;
                                            Prato.mem2[i][j][k] = l;
                                        }
                                    }
                                }    
                            }
                        }
                    }
                }    
            }
 
            int indiceTemporario = 1;
            for (int j = 2; j <= Culinaria.pratos; j++)
                if(Prato.lucro[Culinaria.dias][indiceTemporario][Culinaria.orcamento] < Prato.lucro[Culinaria.dias][j][Culinaria.orcamento]){
                    indiceTemporario = j;
                }
              
            if (Prato.lucro[Culinaria.dias][indiceTemporario][Culinaria.orcamento] == -1){
                System.out.println("0.0");
            }else{
                System.out.println(deci.format(Prato.lucro[Culinaria.dias][indiceTemporario][Culinaria.orcamento]));
                 
                int auxDias = Culinaria.dias;
                int auxOrcamento = Culinaria.orcamento;
                int tg1, tg2; 
                while (auxDias > 0){
                    tg1 = Prato.mem1[auxDias][indiceTemporario][auxOrcamento];
                    tg2 = Prato.mem2[auxDias][indiceTemporario][auxOrcamento];
                    for (int i = 0 ; i < tg2 ; i++){
                        System.out.print(indiceTemporario); 
                        if (i != tg2 - 1){
                            System.out.print(" "); 
                        }
                    }
                    auxDias = auxDias - tg2;
                    auxOrcamento = auxOrcamento - tg2 * Prato.custo[indiceTemporario];
                    indiceTemporario = tg1;
                    if (auxDias > 0){
                        System.out.print(" "); 
                    }
                }
                System.out.println();
 
            }
            System.out.println();
        }
   }
