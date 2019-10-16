/**
 *
 * @author gabriel oliveira campos
 */
import java.util.Scanner;
import java.util.ArrayList;

//Class Prato
class Prato{
    public double custo;
    public double lucro;
    public double beneficio;
    
    public Prato(double custo,double lucro){
        this.custo = custo;
        this.lucro = lucro;
        this.beneficio = lucro/custo;
    }
    
}
//Class Culinaria
class Culinaria{
    public int dias;
    public int pratos;
    public double orcamento;
    int ultimoPrato = -1;
    int pratoRepetido = 0;
    ArrayList<Prato> list_pratos = new ArrayList<Prato>();
}
public class TP1 {

    public static void main(String[]args){
        double resposta = 0;
        Scanner leia = new Scanner(System.in);
        Culinaria culinaria = new Culinaria();
        culinaria.dias = leia.nextInt();
        culinaria.pratos = leia.nextInt();
        culinaria.orcamento = leia.nextDouble();
        
        while(culinaria.dias != 0 && culinaria.pratos != 0 && culinaria.orcamento !=0){
            ArrayList<Integer>cardapio = new ArrayList<Integer>();
            preencheCulinaria(culinaria);
            resposta = AlgGuloso(culinaria,cardapio);
            System.out.println(resposta);
            ImprimirCardapio(cardapio,resposta,culinaria);
            ZeraTudo(cardapio,culinaria);
            cardapio.clear();
            culinaria.dias = leia.nextInt();
            culinaria.pratos = leia.nextInt();
            culinaria.orcamento = leia.nextDouble();
        }
    }
    /*
    Função ZeraTudo: volta os valores iniciais para uma nova busca de pratos
    */
    public static void ZeraTudo(ArrayList cardapio,Culinaria culinaria){
            culinaria.list_pratos.clear();
            culinaria.ultimoPrato = -1;
            culinaria.pratoRepetido = 0;
    }
    /*
    Função ImprimirCardapio: Imprime quais pratos serão feitos em ordem de dias
    */
    public static void ImprimirCardapio(ArrayList cardapio, double resposta,Culinaria culinaria){
        if(resposta != 0.0){
            for (int i = 0; i < culinaria.dias ; i++){
                System.out.print(cardapio.get(i) + " ");
            }
        }
    }
    /*
    Função preencheCulinaria: Prenche em uma lista os custos de cada prato disponivel
    */
    public static void preencheCulinaria(Culinaria culinaria){
        Scanner leia = new Scanner(System.in);
        double custo,lucro;
        for(int i = 0;i < culinaria.pratos;i++){
            custo = leia.nextDouble();
            lucro = leia.nextDouble();
            culinaria.list_pratos.add(new Prato(custo,lucro));
        }
    }
    /*
    Função AlgGuloso: Verifica se o orcamento é possivel para os dias com o prato menos custoso
                      Agrega o lucro maximo obtido dos pratos de maior beneficio
    */
    public static double AlgGuloso(Culinaria culinaria,ArrayList cardapio){
        double var = 0;
        double resposta = 0.0;
        int maisBarato = MaisBarato(culinaria);
        if ((culinaria.dias * culinaria.list_pratos.get(maisBarato).custo) > culinaria.orcamento){
            return resposta;
        }   
        for (int i = 0; i < culinaria.dias; i++){
            var = ProximoPratoFeito(culinaria,cardapio);
            resposta += var;

            if (var == -1){//caso estoure orcamento
                    return 0.0;
            }
        }

            return resposta;

    }
    /*
    Função ProximoPratoFeito: Escolhe o melhor prato para cada dia verificando se ele ja foi repetido uma ou mais vezes,pois se tiver sido ele terá menos beneficio
                              Adiciona a lista do cardapio o melhor prato para o dia
    */
    public static double ProximoPratoFeito(Culinaria culinaria,ArrayList cardapio){
            int pratoEscolhido = 0;
            double melhorBeneficio = 0;
            double melhorLucro = 0;
            double auxBeneficio = 0;
            double auxLucro = 0;

            for (int i = 0; i < culinaria.pratos; i++){
                if (i == culinaria.ultimoPrato) {
                    if (culinaria.pratoRepetido > 1) {
                        auxBeneficio = 0;
                        auxLucro = 0;
                    }
                    else {
                        auxLucro = culinaria.list_pratos.get(i).lucro * 0.5;
                        auxBeneficio = auxLucro/culinaria.list_pratos.get(i).custo;
                        
                    }
                }
                else {
                    auxBeneficio = culinaria.list_pratos.get(i).beneficio;
                    auxLucro = culinaria.list_pratos.get(i).lucro;
                }

                if (auxBeneficio > melhorBeneficio) {
                    pratoEscolhido = i;
                    melhorBeneficio = auxBeneficio;
                    melhorLucro = auxLucro;
                }
            }


            if (culinaria.list_pratos.get(pratoEscolhido).custo <= culinaria.orcamento){
                culinaria.orcamento -= (int)culinaria.list_pratos.get(pratoEscolhido).custo;
            }
            else{
                return -1; 
            }
            if (pratoEscolhido == culinaria.ultimoPrato){
                culinaria.pratoRepetido++;
            }
            else{
                culinaria.ultimoPrato = pratoEscolhido; // Se o prato não tiver sido repetido, eu zero o ultimo vezes.
                culinaria.pratoRepetido = 0;
            }
            cardapio.add(pratoEscolhido + 1);
            return melhorLucro;
    }
    public static int MaisBarato(Culinaria culinaria){
        int resposta = 0;
        int custoAtual = (int)culinaria.list_pratos.get(0).custo;
        for (int i = 0; i < culinaria.pratos; i++){
            if (custoAtual > culinaria.list_pratos.get(i).custo){
                resposta = i;
                custoAtual = (int)culinaria.list_pratos.get(i).custo;
            }
        }
        return resposta;
        
    }
}