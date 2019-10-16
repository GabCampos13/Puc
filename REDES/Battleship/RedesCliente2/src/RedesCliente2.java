import java.io.*;
import java.net.*;
 
class UDPClient {
    public static void casoPesquisa(byte[] sendData,byte[] receiveData, DatagramSocket clientSocket)throws Exception{
            BufferedReader inFromUser = new BufferedReader(new InputStreamReader(
				System.in));
            int porta = 9876;
            InetAddress IPAddress = InetAddress.getByName("localhost");
            
            System.out.println("Pesquisa Selecionado: ");
                    
            System.out.println("Selecione alguma das opcoes: ");
            System.out.println("1 - Diesel" 
                    + "\n2 - Alcool"
                    + "\n3 - Gasolina");
                                
            String opcao = inFromUser.readLine();
            sendData = opcao.getBytes();
            DatagramPacket sendPacket = new DatagramPacket(sendData,
		sendData.length, IPAddress, porta);
                
            clientSocket.send(sendPacket);
 
            DatagramPacket receivePacket = new DatagramPacket(receiveData,
		receiveData.length);
            System.out.println("Digite o valor do raio da busca em quilometros: ");
            
            String opcao2 = inFromUser.readLine();
            sendData = opcao2.getBytes();
            DatagramPacket sendPacket2 = new DatagramPacket(sendData,
		sendData.length, IPAddress, porta);
                
            clientSocket.send(sendPacket2);
 
            DatagramPacket receivePacket2 = new DatagramPacket(receiveData,
		receiveData.length);

            System.out.println("Digite as coordenadas do centro da busca no formato Latitude x Longitude (Exemplo: 55.08 x 72.09) ");
            String opcao3 = inFromUser.readLine();
            sendData = opcao3.getBytes();
            DatagramPacket sendPacket3 = new DatagramPacket(sendData,
		sendData.length, IPAddress, porta);
                
            clientSocket.send(sendPacket3);
 
            DatagramPacket receivePacket3 = new DatagramPacket(receiveData,
		receiveData.length);
            //ABRIR ARQUIVO COM OS VALORES E CALCULAR
        }
        public static void casoDados(byte[] sendData,byte[] receiveData, DatagramSocket clientSocket)throws Exception{
            BufferedReader inFromUser = new BufferedReader(new InputStreamReader(
				System.in));
            int porta = 9876;
            InetAddress IPAddress = InetAddress.getByName("localhost");
            
            System.out.println("Dados Selecionado: ");
                    
            System.out.println("Selecione alguma das opcoes: ");
            System.out.println("1 - Diesel" 
                    + "\n2 - Alcool"
                    + "\n3 - Gasolina");
                                
            String opcao = inFromUser.readLine();
            sendData = opcao.getBytes();
            DatagramPacket sendPacket = new DatagramPacket(sendData,
		sendData.length, IPAddress, porta);
                
            clientSocket.send(sendPacket);
 
            DatagramPacket receivePacket = new DatagramPacket(receiveData,
		receiveData.length);
            
            System.out.println("Digite o preco em reais com 3 casas decimais (Exemplo: R$3,299 = 3299): ");
            
            String opcao2 = inFromUser.readLine();
            sendData = opcao2.getBytes();
            DatagramPacket sendPacket2 = new DatagramPacket(sendData,
		sendData.length, IPAddress, porta);
                
            clientSocket.send(sendPacket2);
 
            DatagramPacket receivePacket2 = new DatagramPacket(receiveData,
		receiveData.length);

            System.out.println("Digite as coordenadas geográficas no formato Latitude x Longitude com 2 casas decimais (Exemplo: 55.02 x 102.08): ");
            String opcao3 = inFromUser.readLine();
            sendData = opcao3.getBytes();
            DatagramPacket sendPacket3 = new DatagramPacket(sendData,
		sendData.length, IPAddress, porta);
                
            clientSocket.send(sendPacket3);
 
            DatagramPacket receivePacket3 = new DatagramPacket(receiveData,
		receiveData.length);
            //SALVAR OS VALORES EM UM ARQUIVO

        }
        public static void EscolheDadosPesquisa(byte[] sendData,byte[] receiveData, DatagramSocket clientSocket)throws Exception{
            BufferedReader inFromUser = new BufferedReader(new InputStreamReader(
				System.in));
		int porta = 9876;
		InetAddress IPAddress = InetAddress.getByName("localhost");
            System.out.println("Usuario deseja Dados (D) ou Pesquisa (P): ");
            String sentence = inFromUser.readLine();
            sendData = sentence.getBytes();
            DatagramPacket sendPacket = new DatagramPacket(sendData,
		sendData.length, IPAddress, porta);
            clientSocket.send(sendPacket);
            DatagramPacket receivePacket = new DatagramPacket(receiveData,
			receiveData.length);
            clientSocket.receive(receivePacket);
            if(sentence.charAt(0) == 'D') casoDados(sendData,receiveData,clientSocket);
            else if(sentence.charAt(0) == 'P') casoPesquisa(sendData,receiveData,clientSocket);
        }
	public static void main(String args[]) throws Exception {
 
		BufferedReader inFromUser = new BufferedReader(new InputStreamReader(
				System.in));
 
		DatagramSocket clientSocket = new DatagramSocket();
 
		String servidor = "localhost";
		int porta = 9876;
 
		InetAddress IPAddress = InetAddress.getByName(servidor);
 
		byte[] sendData = new byte[1024];
		byte[] receiveData = new byte[1024];
                EscolheDadosPesquisa(sendData,receiveData,clientSocket);
 
                 
 
		System.out.println("Pacote UDP recebido...");
 
		clientSocket.close();
		System.out.println("Socket cliente fechado!");
	}
}