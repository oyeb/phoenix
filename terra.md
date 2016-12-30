# **Terra** (every new game should implement the following classes (game-api?))
---

### **class Move:**
+ **Move create_move(JSON_OBJ move) / Constructor:** converts json obj to python obj(Move object here)

### **class State:**
+ **State create_state(JSON_OBJ state) / Constructor:**
+ **State create_state(file map_file) / constructor:**

### **class game:**
+ **bool is_valid(Move obj):** return true or false by getting the Move obj
+ **State next_state(State prev, Move cur):**returns new state after processing the new move and current state

---
