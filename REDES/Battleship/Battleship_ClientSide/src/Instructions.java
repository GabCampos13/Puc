public class Instructions {

    /**
     * Messages that appear at game start
     * 1) Welcome message
     * 2) Game rules
     * 3) How to play the game
     */
    public static void gameStartInstructions(){
        welcome();
//        howToPlay();
    }

    /**
     * Game welcome
     */
    public static void welcome(){
        System.out.println("==============================\n" +
                           "===         WELCOME        ===\n" +
                           "==============================");
    }

    /**
     * Game rules
     */
    public static void rules(){

    }


    /**
     * How to play the game
     */
    public static void howToPlay(){
        System.out.println("-------------------- HOW TO PLAY --------------------");
        System.out.println("ClientSide is a strategy game, played by 2 persons at time.");
        System.out.println("Each player set your fleet in a board, and to win try to guess where is the opponent fleet and shoot on them.");
        System.out.println("The objective is destroy the opponent fleet");
    }
}
