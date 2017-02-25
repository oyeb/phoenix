# Writing a bot (in Python)

You can technically write a bot in any language, but we only have
Python2 API ready. We'll go through the entire code step by step.

## Prerequisites

+ You should have read the `gameRules.md` and `diff-agario-bitjitsu.md`
+ You should know Python.

## Explanation
The basic bot comes in a nice structure.

```
python2/
└── src
    ├── botapi.py
    ├── __init__.py
    └── __main__.py

1 directory, 3 files

```

The bot starts its execution in `__main__.py`. The first line imports a `game`
class from `botapi.py`. The next line we just import the good old `sys` module
(it is a builtin module). Then, we print `I'm Poppy!` (with a newline
character at the end). Every bot has to do this as its first move for the
engine to acknowledge the bot. Then in an infinite loop, we get the input with
`raw_input()` this is a `JSON` object of the current state. You don't have to
worry what that is, all you have to do is create an object of class `game` with
the paramater to its constructor as the name of the bot that you gave when you
submitted and a string that you got from `STDIN`. You must have noticed that
we are doing an explicit `flush`  after each `print` statement this is because
only when you flush the buffer, the engine gets to know that you have made a
move. If you are wondering what is happening here and are asking _"Doesn't 
python flush its buffer automatically?"_, normally it does, but we have set the
size of the pipe buffer to a bigger size (yes we use PIPEs for our IPC), so that
the buffer is big enough for all your sixteen blobs (if you create 16 blobs by
split or eating a virus) to make its move.

Now lets take a look at what is available to us. The only thing that is available
to us is the `botapi.py`. Make sure that you use the name that you submitted to
server and the name that you are using are the same ones (even the case).
Otherwise you bot will just fail.

## The list of queries that you can make about the current `Game-State`

+ `game.get_children()` returns a list of `dict`s of the following fields of
all of your blobs that your bot owns.

```
{
    'botname':'kevin',
    'childno':0,
    'center':[x, y],
    'mass':20,
    'angle':0,
    'radius':10
}
```

+ `game.get_bots()` returns a list of `dict`s of all the blobs that are not
yours of the same format as mentioned above.

+ `game.get_foods()` returns a list of tuples containing coordinates of all
the foods.

+ `game.get_viruses()` returns a list of tuples containing coordinates of all
the viruses


## List of methods that you can make on your blobs

Each blob has a unique number and this number this is identified by `childno`.

+ `game.change_direction(childno, relative_angle)` here the relative angle is
in degrees (it can only take values between 0 and 359). The `childno` is the
unique number given to the blob, you can only make these queries on your bot!

+ `game.eject_mass(childno)` this makes the particular blob to loose its mass,
its further explained in `gameRules.md`

+ `game.split(childno)` this makes the particular blob to perform the `split`
operation.

+ `game.pause(childno)` this makes the particular blob to perform the pause
operation.

## Finally,

+ **`game.make_move()` this generates a `JSON` string of the move of all the
blobs. You print this to `STDOUT` and flush the buffer.

### Note:

+ It is advised that you do not modify `botapi.py`, but you can do what ever
you want if you know what you are doing.

---

<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/3.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.