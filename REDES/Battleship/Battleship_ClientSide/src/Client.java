import java.io.*;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class Client {

    private static int port;
    private static Socket clientSocket;
    private static InetAddress host;

    public static String gridFile = "grids/playerGrid.txt";
    public static short[][] grid;
    public static short[][] knownServerGrid;
    public static short[][] serverGridHits;

    public static short sumPlayer = 0;
    public static short sumServer = 0;

    Client(int port) throws UnknownHostException {
        this.port = port;
        host = InetAddress.getLocalHost();

        knownServerGrid = new short[10][10];
        serverGridHits = new short[10][10];
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                knownServerGrid[ i ][ j ] = -1;
                serverGridHits[ i ][ j ] = -1;
            }
        }
    }

    /**
     * Establish connect to the server
     * @return
     */
    public boolean openConnection(){
        boolean connection = true;
        try {
            clientSocket = new Socket(host.getHostName(), port);
        } catch (Exception ex){
            System.out.println("Unable to connect to server!");
            connection = false;
        }

        return connection;
    }

    /**
     * Read player coordinates and check if it's correct
     * @param rawMove
     * @return
     */
    public String getShootCoordinates(String rawMove){
        String coordinates = rawMove;
        if(coordinates.length() == 2){
            coordinates = coordinates.charAt(0) + "," + coordinates.charAt(1);
        }
        return coordinates;
    }

    /**
     * Wait and read server shoot
     */
    public boolean waitServerMove(){
        //Get the return message from the server
        try {
            System.out.println("Waiting server move");
            ObjectInputStream is = new ObjectInputStream(clientSocket.getInputStream());
            String move = (String)is.readObject();

            short line = Short.parseShort(move.split(",")[0]);
            short column = Short.parseShort(move.split(",")[1]);

            System.out.println("Server move: " + move);

            boolean hit = grid[ line ][ column ] == 1;
            if(hit){
                serverGridHits[ line ][ column ] = 1;
                sumServer++;
            } else {
                serverGridHits[ line ][ column ] = 0;
            }
            return hit;

        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }

        return false;
    }

    /**
     * Send a request to server with shot coordinates
     * @throws IOException
     * @throws ClassNotFoundException
     */
    public void shootShot(String coordinates) throws IOException, ClassNotFoundException {
        openConnection();
        ObjectOutputStream  oos = new ObjectOutputStream(clientSocket.getOutputStream());
        oos.writeObject(coordinates);
        oos.flush();
    }


    /**
     * Read file that contains grid and return fleet position
     * @throws FileNotFoundException
     */
    public static void getGridStartPosition(String fileName) throws FileNotFoundException {
        File file = new File(fileName);
        Scanner sc = new Scanner(file);
        int j,i = 0;
        grid = new short[10][10];

        String line;
        short value;
        while(sc.hasNextLine()){
            line = sc.nextLine();
            for(j = 0; j < 10; j++){
                grid[i][j] = Short.parseShort(String.valueOf(line.charAt(j)));
            }
            i++;
        }
    }

    public boolean getShotResults(String move) throws IOException, ClassNotFoundException {
        if(move.toLowerCase().equals("p")) return true;
        ObjectInputStream is = new ObjectInputStream(clientSocket.getInputStream());
        String message = (String)is.readObject();
        System.out.println(message);

        boolean result = (message.equals("HIT")) ? true : false;
        short line = Short.parseShort(move.split(",")[0]);
        short column = Short.parseShort(move.split(",")[1]);
        if(result){
            knownServerGrid[line][column] = 1;
            sumPlayer++;
        } else {
            knownServerGrid[line][column] = 0;
        }
        return result;
    }

    public void printGrid(short[][] grid) {
        char print = '-';
        String alph = "ABCDEFGHIJ";
        System.out.println("   1 2 3 4 5 6 7 8 9 10");
        for(int i = 0; i < 10; i++){
            System.out.print(alph.charAt(i) + "| ");
            for(int j = 0; j < 10; j++){
                switch (grid[i][j]){
                    case -1:
                        print = '-';
                        break;
                    case 0:
                        print = 'W';
                        break;
                    case 1:
                        print = 'S';
                }
                System.out.print(print + "|");
            }
            System.out.print("\n");
        }
    }

    public void sendServerShotResult(Boolean serverShot) throws IOException {
        String message = (serverShot) ? "HIT" : "WATER";
        if (serverShot) {
            System.out.println("Server hit shot");
        } else {
            System.out.println("Server missed shot");
        }

        openConnection();
        ObjectOutputStream  oos = new ObjectOutputStream(clientSocket.getOutputStream());
        oos.writeObject(message);
        oos.flush();
    }
}
