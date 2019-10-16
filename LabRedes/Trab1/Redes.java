package redes;

import java.net.Socket;
import java.io.*;
import java.util.Scanner;

public class Redes {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
		try
		{
			//ENDERE�O DO SERVIDOR
            Scanner leia = new Scanner(System.in);
			String IPServidor = "127.0.0.1";
			int PortaServidor = 7000;
			
			//ESTABELECE CONEX�O COM SERVIDOR
			System.out.println(" -C- Conectando ao servidor ->" + IPServidor + ":" +PortaServidor);
			Socket socktCli = new Socket (IPServidor,PortaServidor);
			System.out.println(" -C- Detalhes conexao :" + socktCli.toString()); //DETALHAMENTO (EXTRA)
			
			//CRIA UM PACOTE DE SA�DA PARA ENVIAR MENSAGENS, ASSOCIANDO-O � CONEX�O (c)
			ObjectOutputStream sCliOut = new ObjectOutputStream(socktCli.getOutputStream());
			System.out.println("Digite o valor 1 ou 2 para o jogo dois ou um.");
                        int DoisOuUm = leia.nextInt();
                        while(DoisOuUm != 1 && DoisOuUm != 2){
                            System.out.println("Valor inválido, tente novamente");
                            DoisOuUm = leia.nextInt();
                        
                        }
                        sCliOut.writeObject(DoisOuUm);//ESCREVE NO PACOTE
                        System.out.println(" -C- Enviando mensagem...");
                        sCliOut.flush(); //ENVIA O PACOTE

			//CRIA UM PACOTE DE ENTRADA PARA RECEBER MENSAGENS, ASSOCIADO � CONEX�O (c)
			ObjectInputStream sCliIn = new ObjectInputStream (socktCli.getInputStream());
			System.out.println(" -C- Recebendo mensagem...");
			String strMsg = sCliIn.readObject().toString(); //ESPERA (BLOQUEADO) POR UM PACOTE
		
			//PROCESSA O PACOTE RECEBIDO
			System.out.println(" -C- Mensagem recebida: " + strMsg);

			//FINALIZA A CONEX�O
			socktCli.close();
			System.out.println(" -C- Conexao finalizada...");
		}
		catch(Exception e) //SE OCORRER ALGUMA EXCESS�O, ENT�O DEVE SER TRATADA (AMIGAVELMENTE)
		{
			System.out.println(" -C- O seguinte problema ocorreu : \n" + e.toString());
		}
	}

    
}
