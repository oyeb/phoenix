import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
import org.json.simple.JSONObject;
import org.json.simple.JSONValue;

/**
 * Created by Aakash and Sourav on 2/19/2017.
 */
public class Main {
    public static void main(String[] args) throws IOException {
        /*BufferedReader reader = new BufferedReader(new FileReader("JSONFiles/jsonjson"));
        StringBuilder stringBuilder = new StringBuilder(2048);
        String jsonText;
        while((jsonText = reader.readLine())!=null){
            stringBuilder.append(jsonText);
        }*/
        String stringBuilder = new String();
        Scanner in = new Scanner(System.in);
        stringBuilder=in.next();
        System.out.println(stringBuilder);
        JSONObject gameState = (JSONObject) JSONValue.parse(stringBuilder.toString());

        Bot game = new Bot(gameState, "kevin");
        System.out.println(game.makeMove());

    }
}
