# Phoenix (AI Challenge backend for Anokha 2017)

[saber](http://www.github.com/arrow-/saber) shall be reborn as phoenix this year :wink:.

Games are configured by a single JSON file and are run inside the environment of an `arena`. Here's a description of what is to be contained in each directory:
```
├──api
│  └── The APIs, one in each folder.
├──errorlogs
│  └── Unique error logs for each game (DB stores filename alone)
├──debuglogs
│  └── Unique debug logs for each game (DB stores filename alone)
├──replays
│  └── Unique replays for each game (DB stores filename alone)
├──maps
│  └── The maps
├──bots
│  └── The bots submitted by users. They implement `__main__.py`
├──sample_bots
│  └── The bots created by us. They implement `__main__.py`
└──arena
   └── temp folder(s)
```

## Prepare your environment

1. Create the following directories (write a shell script for this?)
```bash
mkdir -p out/errorlogs
mkdir out/debuglogs
mkdir out/movelogs
mkdir out/replays
```

2. Move the Bot APIs to `/api`. So this is how your `/api` dir should look:
```
api
├── python2
│   └── src
│       ├── botapi.py
│       └── __init__.py
└── python3
    └── src
        ├── botapi.py
        └── __init__.py
```

You can see that this folder lacks `__main__.py`.

3. Copy the `__main__.py` of the bots into `/bots`
```
bots
├── py2_bot.py
└── py3_bot.py
```

4. Create atleast 1 `arena` folder, this is where bot codes are copied, and logs are generated. `gameloop.commit` moves them to the `/out` folders.
```bash
mkdir arena_a
```

## Instructions for running the Game locally:

***NEW***

+ Add a `game_config.json` to the root dir. Here's an example,
`<PHOENIX>` stands for absolute path-to-phoenix
```json
{
    "bots": [
        ["kevin", ["/usr/bin/python2", "python2", "<PHOENIX>/bots/py2_bot.py"]],
        ["joker", ["/usr/bin/python3", "python3", "<PHOENIX>/bots/py3_bot.py"]]
    ],
    "map": "<PHOENIX>/maps/fakemap.json",
    "arena" : "<PHOENIX>/arena",
    "filenames" : {
        "error" : "elog.json",
        "debug" : "dlog.json",
        "replay" : "replay.json",
        "move" : "moves.json"
    },
    "commit_paths" : {
        "error" : "<PHOENIX>/out/errorlogs",
        "debug" : "<PHOENIX>/out/debuglogs",
        "replay" : "<PHOENIX>/out/replays",
        "move" : "<PHOENIX>/out/movelogs"
    },
    "max_iters" : 1000,
    "timeout" : 2,
    "api_dir" : "<PHOENIX>/api"
}
```

+ Run `python2 src`

***OLD***

+ modify `bots_config.json` and `map_config.json` appropriately
+ run the command "python src" from phoenix directory.


## Dependencies

+ libseccomp ([install it from source](https://vasanthaganeshk.wordpress.com/2016/12/24/libseccomp-for-python2-7/))
+ cython (pip)
+ python-dev (for Ubuntu), python-devel (for Fedora)
+ libcap-dev (for Ubuntu), libcap-devel (for Fedora)
+ python-prctl (pip)
+ redhat-rpm-config (for Fedora only)
+ build-essential (for Ubuntu), glibc-devel (for Fedora)
+ jsonschema (pip)
+ tqdm (pip)
+ This code can only run on linux and not any unix.

##TODO

+ Define API for writing the bot (lets call this Titanic). This will be game dependent and language dependent. For example `move_left()` or `split_two()`.
+ Add more syscalls to syscalls_filter(). Such as networking related ones etc.
+ Fine tune the syscalls like open etc. So that they can only open some stuff.
+ Documentation with Sphinx(low priority)
+ Look at the issues
+ Create a pip package(low priority)
+ need proper exception handling

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

## Bots

+ The bots' information must be stored in `bots_config.json` as JSON objects. They must be directly usable by system calls such as exec*

#Security

We can protect our system by running bot process in `chroot` jails or `containers` (LXD, LXC or Docker) which help in minimising damages when scripts attempt privilege escalation or arbit code injection.

How do we make sure processes cannot open any kind of `file descriptors`? Be it for IPC or network sockets?
