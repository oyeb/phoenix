# **Terra** (every new game should implement the following classes (game-api))
---

### **class Move:**
+ **Move create_move(JSON_OBJ move) / Constructor:** converts json obj to python obj(Move object here, json object is supposed to be retrieved from the message queue after the bots write to the message queue).

### **class State:**
+ **State create_state(file map_file) / constructor:**

+ **JSON_OBJ to_json():**  converts a state object into (to put the json object in the message queue to make it available to the bots)

### **class game:**
+ **bool is_valid_move(Move obj):** return true or false by getting the Move obj

+ **bool[] are_valid_moves(Move[] obj):** returns true or false array

+ **State next_state_continuous(State prev, Move[] cur):** returns new state after processing an array of new moves from bots and current state (this method is specially for continuous games)

+ **State next_state_discrete(State prev, Move cur):** returns new state after processing the previous state and one move object (this method is specially for discrete games)

---
