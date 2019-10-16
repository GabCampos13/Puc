import java.io.*;
import java.net.BindException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;

public class Server {

    private static ServerSocket serverSocket;
    private static int port;


    public static String serverFile = "grids/serverGrid.txt";
    public static short[][] serverGrid = new short[ 10 ][ 10 ];
    private static short[][] shotsDone = new short[ 10 ][ 10 ];

    Server(int port){
        this.port = port;
        for(int i = 0; i < 10; i++){
            for(int j = 0; j < 10; j++){
                shotsDone[i][j] = 0;
            }
        }
    }


    public static Socket waitClientConnection(){
        while(true){
            try {
                System.out.println("Waiting client connection ...");
                Socket socket = serverSocket.accept();
                System.out.println("Client successfully connected!");
                return socket;
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public static void startServer() throws IOException {
        try {
            serverSocket = new ServerSocket(port);
            System.out.println("Server started.");
        } catch (BindException portUsedException) {
            System.out.println("Port already in use. Try to use another! \n" +
                    "Thanks!");
        }
    }

    /**
     * Wait for client request
     *
     * @return
     * @throws IOException
     */
    public static PlayerShot getPlayerShot() throws IOException, ClassNotFoundException {
        while(true){
            System.out.println("Waiting player move ...");
            Socket socket = serverSocket.accept();
            ObjectInputStream inputStream = new ObjectInputStream(socket.getInputStream());

            String playerShoot = (String) inputStream.readObject();

            short column = Short.parseShort(playerShoot.split(",")[0]);
            short line = Short.parseShort(playerShoot.split(",")[1]);

            boolean hit = serverGrid[ column ][ line ] == 1;

            return new PlayerShot(socket,hit);
        }
    }

    /**
     * Create server grid and randomly set ships positions
     */
    public static void setFleetPositions() {
        // [ShipType][Numbers left to be positioned]
        // [0] = Aircraft Carrier
        // [1] = Tank Ship
        // [2] = Destroyer
        // [3] = Submarine
        short fleet[] = new short[ 4 ];
        short shipSize[] = new short[ 4 ];

        // Set number of ships that should be positioned
        fleet[ 0 ] = 1;
        for (int i = 1; i < fleet.length; i++) {
            fleet[ i ] = (short) (fleet[ i - 1 ] + 1);
        }

        // Set the size of each ship
        shipSize[ 0 ] = 5;
        for (int i = 1; i < shipSize.length; i++) {
            shipSize[ i ] = (short) (shipSize[ i - 1 ] - 1);
        }

        // Initialize server grid with 0
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                serverGrid[ i ][ j ] = 0;
            }
        }


        int line,column;
        Random random = new Random();
        boolean orientation[];
        int ori;
        for(int i = 0; i < fleet.length; i++){
            for(int j = 0; j < fleet[i]; j++){
                boolean validPosition = false;
                orientation = new boolean[4];
                do{
                    do{
                        line = random.nextInt((10));
                        column = random.nextInt((10));
                    } while(serverGrid[line][column] == 1);

                    do{
                        ori = random.nextInt((4));
                    } while(orientation[ori]);
                    switch (ori){
                        case 0:
                            // Check if it's horizontal to the right -->
                            if(column + shipSize[i] <= 9){
                                validPosition = true;
                                for(int k = 0; k < shipSize[i] && validPosition; k++){
                                    if(serverGrid[line][column + k] == 1) validPosition = false;
                                }
                            }
                            orientation[ori] = true;
                            if(validPosition){
                                for(int k = 0; k < shipSize[i]; k++){
                                    serverGrid[line][column + k] = 1;
                                }
                            }
                            break;
                        case 1:
                            // Check if it's horizontal to the left <--
                            if(column - shipSize[i] >= 0){
                                validPosition = true;
                                for(int k = 0; k < shipSize[i] && validPosition; k++){
                                    if(serverGrid[line][column - k] == 1) validPosition = false;
                                }
                            }
                            orientation[ori] = true;
                            if(validPosition){
                                for(int k = 0; k < shipSize[i]; k++){
                                    serverGrid[line][column - k] = 1;
                                }
                            }
                            break;
                        case 2:
                            // Check if it's vertical to down
                            if(line + shipSize[i] <= 9){
                                validPosition = true;
                                for(int k = 0; k < shipSize[i] && validPosition; k++){
                                    if(serverGrid[line + k][column] == 1) validPosition = false;
                                }
                                orientation[ori] = true;
                                if(validPosition){
                                    for(int k = 0; k < shipSize[i]; k++){
                                        serverGrid[line + k][column] = 1;
                                    }
                                }
                            }
                            break;
                        case 3:
                            // Check if it's vertical up
                            if(line - shipSize[i] >= 0){
                                validPosition = true;
                                for(int k = 0; k < shipSize[i] && validPosition; k++){
                                    if(serverGrid[line - k][column] == 1) validPosition = false;
                                }
                            }
                            orientation[ori] = true;
                            if(validPosition){
                                for(int k = 0; k < shipSize[i]; k++){
                                    serverGrid[line - k][column] = 1;
                                }
                            }
                            break;
                    }
                } while(!validPosition);

            }
        }


//        serverGrid[0][0] = 1;
//        serverGrid[4][8] = 1;
//        serverGrid[7][2] = 1;

        int soma = 0;
        for(int i = 0; i < 10; i++){
            for(int j = 0; j < 10; j++){
                soma += serverGrid[i][j];
            }
        }
        System.out.println(soma);

    }

    /**
     * Print grid
     */
    public static void printGrid(){
        for(int i = 0; i < 10; i++){
            for(int j = 0; j < 10; j++){
                System.out.print(serverGrid[i][j]);
            }
            System.out.print("\n");
        }
    }

    public static String calculateShotPosition(String shot) {
        Random random = new Random();
        short column = 0;
        short line = 0;
        boolean newShot = false;

        if (shot.length() > 0) {
            int lineOrColumn, addOrSub;
            short tempLine, tempColumn;
            boolean positionsTry[][] = new boolean[ 2 ][ 2 ];
            line = Short.parseShort(shot.split(",")[ 0 ]);
            column = Short.parseShort(shot.split(",")[ 1 ]);

            for(int i = 0; i < 4 && !newShot; i++){
                do{
                    lineOrColumn = random.nextInt(2);
                    addOrSub = random.nextInt(2);
                } while(positionsTry[lineOrColumn][addOrSub]);

                if(lineOrColumn == 0){
                    if(addOrSub == 0){
                        tempLine = (short) (line - 1);
                    } else {
                        tempLine = (short) (line + 1);
                    }
                    positionsTry[lineOrColumn][addOrSub] = true;
                    if(tempLine >= 0 && tempLine <= 9 && shotsDone[tempLine][column] != 1){
                        newShot = true;
                        line = tempLine;
                    }
                } else {
                    if(addOrSub == 0){
                        tempColumn = (short) (column - 1);
                    } else {
                        tempColumn = (short) (column + 1);
                    }
                    positionsTry[lineOrColumn][addOrSub] = true;
                    if(tempColumn >= 0 && tempColumn <= 9 && shotsDone[line][tempColumn] != 1){
                        newShot = true;
                        column = tempColumn;
                    }
                }
            }
        }

        if(!newShot){
            do{
                line = (short) random.nextInt((10));
                column = (short) random.nextInt((10));
            } while(shotsDone[line][column] == 1);
        }
        shotsDone[line][column] = 1;
        return line + "," + column;
    }

    /**
     * Send shoot cordinates to player
     * @param socket
     * @throws IOException
     */
    public static void shootShot(Socket socket, String shot) throws IOException {
        ObjectOutputStream  oos = new ObjectOutputStream(socket.getOutputStream());
        oos.writeObject(shot);
        oos.close();
    }

    /**
     * Send player if shot hit or not
     * @param playerShot
     * @throws IOException
     */
    public void sendPlayerShotResult(PlayerShot playerShot) throws IOException {
        ObjectOutputStream  oos = new ObjectOutputStream(playerShot.socket.getOutputStream());
        String message = (playerShot.hit) ? "HIT" : "WATER";
        if(playerShot.hit){
            System.out.println("Player hit shot");
        } else {
            System.out.println("Player missed shot");
        }
        oos.writeObject(message);
    }

    /**
     * Receive player request to discover if shot was hit or not
     * @return
     * @throws IOException
     * @throws ClassNotFoundException
     */
    public PlayerShot getShotResult() throws IOException, ClassNotFoundException {
        Socket socket = serverSocket.accept();
        ObjectInputStream is = new ObjectInputStream(socket.getInputStream());

        String message = (String)is.readObject();

        boolean result = message.equals("HIT");
        if(result){
            System.out.println("Server hit shot");
        } else {
            System.out.println("Server missed shot");
        }
        return new PlayerShot(socket,result);
    }
}
