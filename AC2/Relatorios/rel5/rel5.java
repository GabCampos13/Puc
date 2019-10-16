import java.io.*;
import java.util.*;

public class rel5{
   public static void main(String[]args){
      try{
         int i=0;
         ProcessBuilder pb,pb1,pb2,pb3,pb4,pb5;
         Process p,p1,p2,p3,p4,p5;
         Scanner sc = new Scanner(System.in);
         String port = "com3"
         sc.nextLine();

      //Comeca funcionamento
         while(i==0){
         //=====================TABELA===========================
         //SINAL     Vermelho | Amarelo | Verde

         //SINALP        2    | xxxxxxx |   3

         //SINAL1        6    |    5    |   4

         //SINAL2        9    |    8    |   7

         //=======================TABELA=========================

         //=======================TEMPO1=========================

         //SINAL1 = Vermelho   /SINAL2 =  Verde   /SINALP = Vermelho
            pb1 = new ProcessBuilder("envia.exe",port,"A");
            p1 = pb1.start();
            sc.nextLine();

         //=======================TEMPO2=========================
            pb2 = new ProcessBuilder("envia.exe",port,"B");
            p2 = pb2.start();
            sc.nextLine();


         //=======================TEMPO3=========================
            pb3 = new ProcessBuilder("envia.exe",port,"C");
            p3 = pb3.start();
            sc.nextLine();


         //=======================TEMPO4=========================
            pb4 = new ProcessBuilder("envia.exe",port,"D");
            p4 = pb4.start();
            sc.nextLine();


         //=======================TEMPO5=========================
            pb5 = new ProcessBuilder("envia.exe",port,"E");
            p5 = pb5.start();
            sc.nextLine();


         }
      }
      catch(Exception e){}
   }
}
