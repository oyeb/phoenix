import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import javax.swing.*;
import java.util.ArrayList;
import java.util.Objects;

/**
 * Created by Aakash and Sourav on 2/19/2017.
 */

/**Disclaimer* this library doesn't have the feature to edit fields of a JSON directly
   so, it was a pain in the ass to make all the functions that required editing */
public class Bot {
    JSONObject gameState;
    String name;
    JSONArray moveObject = new JSONArray();
    Bot(JSONObject json, String s) {
        gameState = json;
        name = s;
        JSONArray bots= (JSONArray) gameState.get("bots");


        for(int i=0; i<bots.size(); i++){
            Object obj = bots.get(i);
            JSONObject temp = (JSONObject) obj;
            if(temp.get("botname").equals(name)){
                long index =  (long) temp.get("childno");
                JSONObject jsonObject = new JSONObject();
                jsonObject.put("childno", index);
                jsonObject.put("relativeangle", 0);
                jsonObject.put("ejectmass", Boolean.FALSE);
                jsonObject.put("split", Boolean.FALSE);
                jsonObject.put("pause", Boolean.FALSE);
                moveObject.add((int)index, jsonObject);
            }
        }



    }
    void changeDirection(int childNo, float relativeAngle){
        JSONObject object = (JSONObject) moveObject.get(childNo);
        JSONObject temp = new JSONObject();
        temp.put("childno", childNo);
        temp.put("relativeangle", relativeAngle);
        temp.put("ejectmass", object.get("ejectmass"));
        temp.put("split", object.get("split"));
        temp.put("pause", object.get("pause"));
        moveObject.set(childNo, temp);

    }
    void ejectMass(int childNo){
        JSONObject object = (JSONObject) moveObject.get(childNo);
        JSONObject temp = new JSONObject();
        temp.put("childno", childNo);
        temp.put("relativeangle", object.get("relativeangle"));
        temp.put("ejectmass", Boolean.TRUE);
        temp.put("split", object.get("split"));
        temp.put("pause", object.get("pause"));
        moveObject.set(childNo, temp);
    }
    void split(int childNo){
        JSONObject object = (JSONObject) moveObject.get(childNo);
        JSONObject temp = new JSONObject();
        temp.put("childno", childNo);
        temp.put("relativeangle", object.get("relativeangle"));
        temp.put("ejectmass", object.get("ejectmass"));
        temp.put("split", Boolean.TRUE);
        temp.put("pause", object.get("pause"));
        moveObject.set(childNo, temp);
    }
    void pause(int childNo){
        JSONObject object = (JSONObject) moveObject.get(childNo);
        JSONObject temp = new JSONObject();
        temp.put("childno", childNo);
        temp.put("relativeangle", object.get("relativeangle"));
        temp.put("ejectmass", object.get("ejectmass"));
        temp.put("split", object.get("split"));
        temp.put("pause", Boolean.TRUE);
        moveObject.set(childNo, temp);
    }
    String makeMove(){
        return moveObject.toJSONString();
    }
    ArrayList<JSONObject> getChildren(){
        ArrayList<JSONObject> returnArray = new ArrayList<>();
        JSONArray object = (JSONArray) gameState.get("bots");
        for(int i=0; i<object.size(); i++){
            JSONObject temp = (JSONObject) object.get(i);
            if(temp.get("botname")==name){
                returnArray.add(temp);
            }

        }
        return returnArray;
    }
    ArrayList<JSONObject> getBots(){
        ArrayList<JSONObject> returnArray = new ArrayList<>();
        JSONArray object = (JSONArray) gameState.get("bots");
        for(int i=0; i<object.size(); i++){
            JSONObject temp = (JSONObject) object.get(i);
            if(temp.get("botname")!=name){
                returnArray.add(temp);
            }

        }
        return returnArray;
    }
    JSONArray getFood(){
        JSONArray returnArray = (JSONArray) gameState.get("food");
        return returnArray;
    }
    JSONArray getViruses(){
        JSONArray returnArray = (JSONArray) gameState.get("virus");
        return  returnArray;
    }
    JSONArray getFfieldCircle(){
        JSONArray returnArray = (JSONArray) gameState.get("ffieldcircle");
        return returnArray;
    }
    JSONArray getFfieldSquareCircle(){
        JSONArray returnArray = (JSONArray) gameState.get("ffieldsquare");
        return returnArray;
    }



}
