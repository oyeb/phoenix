# Phoenix (AI Challenge backend for Anokha 2017)

[saber](http://www.github.com/arrow-/saber) shall be reborn as phoenix this year :wink:.

## Instructions for running the Game:

+ run the command "python src" from phoenix directory.

## Dependencies

+ libseccomp ([install it from source](https://vasanthaganeshk.wordpress.com/2016/12/24/libseccomp-for-python2-7/))
+ cython (pip)
+ python-dev (for Ubuntu), python-devel (for Fedora)
+ libcap-dev (for Ubuntu), libcap-devel (for Fedora)
+ python-prctl (pip)
+ redhat-rpm-config (for Fedora only)
+ build-essential (for Ubuntu), glibc-devel (for Fedora)

##TODO

+ Define API for writing the bot (lets call this Titanic). This will be game dependent and language dependent. For example `move_left()` or `split_two()`.
+ Add more syscalls to syscalls_filter(). Such as networking related ones etc.
+ Fine tune the syscalls like open etc. So that they can only open some stuff.
+ Documentation with Sphinx(low priority)
+ Look at the issues
+ Create a pip package(low priority)

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

We can protect our system by running bot process in `chroot` jails or `containers` (LXD, LXC or Docker) which help in minimising damages when scripts attempt privilege escalation or arbit code injection.

How do we make sure processes cannot open any kind of `file descriptors`? Be it for IPC or network sockets?
