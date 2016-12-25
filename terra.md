# Terra (game-engine API)

class Bot:

    static (common to all bots)
        opens the file descriptor for log-file-global in write mode
    function start(String path, String name_of_file) / constructor()
        inits seccomp-bpf filter, creates new named pipe, log-file-local
        created, returns success or failure
    function get_move()
        waits for n seconds and gets the move played by bot and returns (json
        object?), else returns null, also writes the move to log-file-local
    function post_state()
        writes new game state Obj (json object?) into named pipe, writes to
        log-file-global
    function terminate(String reason)
        default reason="Incorrect bot behavior"
        abort process, close fds, close filter, returns success or failure
    function is_running()
        True or False

