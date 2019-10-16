import java.net.Socket;
import java.net.ServerSocket;
import java.io.*;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Server extends Thread {

	private static int port = 7000;
	private static ServerSocket socktServ;
	private static int totalPlayers = 0;
	private static List<Integer> plays = new ArrayList<Integer>();
	private static List<Server> clients = new ArrayList<Server>();
	private ObjectOutputStream writer;
	private static int winner;
	private Socket conSer;
	private static int numberOfPlayers = 3;
	private int play = -1;
	private static Boolean calculated = false;
	private int id = 0;

	public Server(Socket conSer) {
		this.id = totalPlayers;
		this.conSer = conSer;
		totalPlayers++;
	}

	public static void main(String args[]) {
		try {
			socktServ = new ServerSocket(port);	// Criação do servidor (Escutar conexoes de clientes)
			System.out.println("Aguardando conexões ...");
		} catch (Exception ex) {
			System.out.println("Ocorreu o seguinte erro: " + ex.toString());
		}
		for (int i = 0; i < numberOfPlayers; i++) {	// Espera-se um numero de jogadores definidos acima
			try {
				Socket conSer = socktServ.accept();	// Nova conexao do cliente
				Server currentServer = new Server(conSer); // Instancia do cliente
				currentServer.writer = new ObjectOutputStream(conSer.getOutputStream()); // OutputStream para envio de mensagem para o cliente

				clients.add(currentServer);	// Adiciona o cliente em uma lista de clientes
				currentServer.start();	// Inicializa a thread do cliente
			} catch (Exception ex) {
				System.out.println("Ocorreu o seguinte erro: " + ex.toString());
			}
		}
	}

	public void closeConnection() {	// Fecha a conexao do cliente
		try {
			this.conSer.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		System.out.println("Conexao finalizada...");
	}

	public static void sendResultToAll(int winner) {	// Envia mensagem para todos os clientes
		for (int i = 0; i < clients.size(); i++) {
			try {
				if(winner == -1) clients.get(i).writer.writeObject("Empate"); // Envia mensagem de empate para todos
				else if(winner == clients.get(i).play) clients.get(i).writer.writeObject("Venceu"); // Verifica se foi o vencedor, e envia mensagem de vencedor
				else clients.get(i).writer.writeObject("Perdeu");	// Verificia se foi o perdedor e envia mensagem de derrota
			} catch (IOException e) {
				e.printStackTrace();
			};
		}
	}

	public static void clearPlays() {	// Limpa as jogadas para uma nova rodada
		plays = new ArrayList<Integer>();
	}

	public void run() {
		try
		{						
			System.out.println((this.id+1)+"º jogador conectado");
	
			ObjectInputStream sServIn = new ObjectInputStream(conSer.getInputStream());	// InputStream para leitura da mensagem do cliente
			System.out.println("Aguardando jogada do " + (this.id + 1) + "º jogador ...");

			Object msgIn = sServIn.readObject();	// Aguarda e lê a mensagem do cliente
			plays.add(Integer.parseInt(msgIn.toString()));	// Adiciona a jogada do cliente as jogadas globais
			this.play = Integer.parseInt(msgIn.toString());	// Salva a jogada do cliente em sua instância	
			
			while(plays.size() < clients.size()) this.sleep(1000);	// Verifica se todos os jogadores já jogaram

			synchronized(this) {
				if (plays.size() == numberOfPlayers && !calculated) {	// Verifica se todos os jogadores já jogaram e faz com que somente 1 thread 
																		//realize o cálculo e solicite o envio de mensagem para os outros clientes
					winner = getWinner(plays);
					sendResultToAll(winner);
					calculated = true;
				}
			}
		}
		catch(Exception e)
		{
			System.out.println("O seguinte problema ocorreu : \n" + e.toString());
		}
	}

	public static int getWinner(List<Integer> plays) {	// Calcula o vencedor
		int totalOne = Collections.frequency(plays, 1);	// Numero de jogadas = 1
		int totalTwo = Collections.frequency(plays, 2); // Numero de jogadas = 2
		int winner = -1;	// Numero vencedor (-1 = empate)
		if (totalOne == 1) {	// Caso somente 1 jogada do tipo 1, entao o jogador que fez a jogada 1 vence
			winner = 1;
		} else if (totalTwo == 1) { // Caso somente 1 jogada do tipo 2, entao o jogador que fez a jogada 2 vence
			winner = 2;
		}
		return winner;
	}
}