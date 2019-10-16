import java.net.Socket;

public class ServerShot {
    public Socket socket;
    public boolean hit;

    ServerShot(Socket socket, boolean hit){
        this.socket = socket;
        this.hit = hit;
    }
}
