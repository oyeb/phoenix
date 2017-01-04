# phoenix
This is the AI Challenge backend for Anokha 2017.
[saber](http://www.github.com/arrow-/saber) shall be reborn as phoenix this year :wink:.

#TODO

Look at the issues

#Architecture

```
Game <---> Engine <-.
                    |
                    +--> Bot
                    |
                    +--> Bot
                    |
                    .
                    .
```

Hence we require 2 APIs

* **Game-Engine** Interface (let's call it `terra`) is the backbone of our operation.
    - `Game` gets inputs, transforms its **"state"**, and returns it to the `Engine`.
    - `Engine` can query status, scores, etc from `Game`.
* **Engine-Bot** Interface (let's call this `sky`)
    - Parses Bot moves (possibly even validates them)
    - Bot gets game-state, commands and logs.

So,
* Bot **gets** `Game` details by `sky`.
* `Engine` **uses** `sky` to control Bot process and its function and also to handover `Game` state, score and logs to them.
* `Engine` **uses** `terra` to send Bot moves and `Bot` status to `Game`.
* `Game` **uses** `terra` to return latest game-state, scores and logs to `Engine` which are forwarded).

>Whatever be the Game, we can start work on the APIs and the Engine. We already know what the responsibilities of the Engine are.

#Engine

## Responsibilities

* Start Game process.
    - Also open log file handles
* Start Bot processes.
* Pass Game State to Bots.
* Pass moves to Game
* Pass end-game logs, scores etc. to Bots
* Handling Bot errors
    - Unresponsive, Invalid or even Malicious
* Security
* Subprocess management
    - start, end, resource (mem, cpu, "real" time), privileges

#Security

We can protect our system by running bot process in `chroot` jails which help in minimising damages when scripts attempt privilege escalation or arbit code injection.

But a scarier attack would be something like a fork bomb. Such attacks hog CPU and I/O resources. If we do not detect it and stop it in it's early stage -- or prevent it altogether, the server would crash.

How do we make sure processes cannot open any kind of `file descriptors`? Be it for IPC or network sockets?
