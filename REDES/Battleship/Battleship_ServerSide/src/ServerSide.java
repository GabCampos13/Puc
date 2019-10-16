import java.io.IOException;
import java.net.Socket;
import java.util.concurrent.TimeUnit;

public class ServerSide {

    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {
        Server server = new Server(12345);

        server.startServer();
        server.setFleetPositions();

        boolean firstShoot;
        String shot;
        PlayerShot ps;
        while(true){
            do{
                ps = server.getPlayerShot();
                server.sendPlayerShotResult(ps);
                Socket socket = ps.socket;
            } while(ps.hit);
            firstShoot = true;
            shot = "";
            do{
                TimeUnit.SECONDS.sleep(2);
                shot = server.calculateShotPosition(shot);
                server.shootShot(ps.socket, shot);
            } while((ps = server.getShotResult()).hit);
        }
    }
}
