import java.net.Socket;

public class PlayerShot {
    public Socket socket;
    public boolean hit;

    PlayerShot(Socket socket, boolean hit){
        this.socket = socket;
        this.hit = hit;
    }
}
