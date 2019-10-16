import java.io.*;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class ClientSide {

    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {
        Scanner sc = new Scanner(System.in);
        Client client = new Client(12345);

        client.getGridStartPosition(Client.gridFile);
        boolean serverHit;
        String move;
        boolean playerWin, serverWin;

        playerWin = serverWin = false;
        while(!playerWin && !serverWin){
            do{
                playerWin = client.sumPlayer == 30;
                if(playerWin) break;
                TimeUnit.SECONDS.sleep(2);
                System.out.println("Make your move");
                move = client.getShootCoordinates(sc.nextLine());
                if(move.toLowerCase().equals("p")){
                    client.printGrid(Client.knownServerGrid);
                    client.printGrid(Client.serverGridHits);
                    continue;
                }
                client.shootShot(move);
            } while(client.getShotResults(move));

            if(!playerWin){
                do{
                    serverHit = client.waitServerMove();
                    client.sendServerShotResult(serverHit);
                    serverWin = client.sumServer == 30;
                } while(serverHit && !serverWin);
            }
        }

        if(playerWin){
            System.out.println("CONGRATS! YOU WIN!");
            client.printGrid(client.knownServerGrid);
        } else {
            System.out.println("YOU LOSE! SERVER WON!");
            client.printGrid(client.serverGridHits);
        }
    }
}