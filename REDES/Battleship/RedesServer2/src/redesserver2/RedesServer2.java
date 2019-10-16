package redesserver2;

import java.io.*;
import java.net.*;
 
class UDPServer {
	public static void main(String args[]) throws Exception {
 
		int porta = 9876;
		int numConn = 1;
		
		DatagramSocket serverSocket = new DatagramSocket(porta);
 
		while (true) {
                    byte[] receiveData = new byte[1024];
                    byte[] sendData = new byte[1024];
 
			DatagramPacket receivePacket = new DatagramPacket(receiveData,
					receiveData.length);
			System.out.println("Esperando por datagrama UDP na porta " + porta);
			serverSocket.receive(receivePacket);
			System.out.print("Datagrama UDP [" + numConn + "] recebido...");
 
			String sentence = new String(receivePacket.getData());
			System.out.println(sentence);
			
			InetAddress IPAddress = receivePacket.getAddress();
 
			int port = receivePacket.getPort();
 
			String capitalizedSentence = sentence.toUpperCase();
 
			sendData = capitalizedSentence.getBytes();
 
			DatagramPacket sendPacket = new DatagramPacket(sendData,
					sendData.length, IPAddress, port);
			//DADOS
			if(capitalizedSentence.charAt(0) == 'D'){
                            System.out.println("Dados selecionado");
                            serverSocket.send(sendPacket);                            
                            serverSocket.receive(receivePacket);                           
                            String opcao = new String(receivePacket.getData());
                            //System.out.println(opcao);
                            String valor = opcao.toUpperCase();

                            
                            serverSocket.receive(receivePacket);                            
                            String opcao2 = new String(receivePacket.getData());
                           //System.out.println(opcao2); 
                            String valor2 = opcao2.toUpperCase(); 

                           
                            serverSocket.receive(receivePacket);                            
                            String opcao3 = new String(receivePacket.getData());
                            //System.out.println(opcao3); 
                            String valor3 = opcao3.toUpperCase(); 

                            
                            if(valor.charAt(0) == '1'){
                                System.out.println("Diesel Selecionado");
                            }
                            else if(valor.charAt(0) == '2'){
                                System.out.println("Alcool Selecionado");
                            }
                            else if(valor.charAt(0) == '3'){
                                System.out.println("Gasolina Selecionada");
                            }
                            System.out.println("Preco inserido: "+ valor2);
                            System.out.println("Coordenadas geograficas: "+valor3);
                        }
                        //PESQUISA
                        else if(capitalizedSentence.charAt(0) == 'P'){
                            System.out.println("Pesquisa selecionada");
                            serverSocket.send(sendPacket);
                            serverSocket.receive(receivePacket);
                            String opcao = new String(receivePacket.getData());
                            //System.out.println(opcao);
                            String valor = opcao.toUpperCase();
 
                            serverSocket.receive(receivePacket);                            
                            String opcao2 = new String(receivePacket.getData());
                           //System.out.println(opcao2); 
                            String valor2 = opcao2.toUpperCase(); 

                           
                            serverSocket.receive(receivePacket);                            
                            String opcao3 = new String(receivePacket.getData());
                            //System.out.println(opcao3); 
                            String valor3 = opcao3.toUpperCase(); 

                            if(valor.charAt(0) == '1'){
                                System.out.println("Diesel Selecionado");
                            }
                            else if(valor.charAt(0) == '2'){
                                System.out.println("Alcool Selecionado");
                            }
                            else if(valor.charAt(0) == '3'){
                                System.out.println("Gasolina Selecionada");
                            }
			    System.out.println("Valor do centro inserido: "+ valor2);
                            System.out.println("Coordenadas geograficas: "+valor3);
                        }
                        else {
                            System.out.println("Digito errado");
                        }
 
			serverSocket.send(sendPacket);
			System.out.println("OK\n");
		}
	}
}