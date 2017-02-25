# Game Rules

## Overview

This guide gives a detailed description of **Bit-Jitsu** game play.

## The Game

+ This game is inspired by [agar.io](https://agar.io/). We recommend that you
play this game, its available on Google Play Store, App Store(iOS) and on that link
above.

+ Initially you will start out in a random place on the map with a mass of 20 units.

+ You must be 80% bigger than anything that you wish to consume.

+ You can eat other blobs, you can eat viruses (the medium sized blue colored
circles), you can also eat food (the small red colored dots).

+ Split operation makes you to split yourself into two equal halves. One blob moves
in the direction that you are moving and the other blob will move in opposite
direction. Both the bots will move at a very high velocity. And Cover a distance
of `700 + Radius Units`

+ You must have a minimum mass of 36 units before you can perform a split
operation.

+ There can only be 16 blobs of the same bot on a map.

+ You will split into two when you eat a virus if your total number of blobs is
less than 16. You will gain a mass of 70 units when you eat a virus. You will
also gain 210 points for eating a virus (Don't forget the 80% bigger rule, your
mass must be 130 for you to consume a virus).

+ Eating a food particle will give you an increase in mass by 2 units and fetch
you two points.

+ Eating a blob will result in a mass equivalent to the sum of your blob and the
blob that you ate. Eating a blob of your own won't increase points but if you
eat an opponent blob your points will rise by ten times the mass of the bot that
you ate.

+ Eject mass operation reduces your mass by two units and the food is ejected `50 + radius units`
away and in a direction opposite to motion of the blob.

+ Pause operation allows you to be stationary.

+ Blobs will experience a decay given by the formula: (0.002 * mass) units s<sup>-1</sup>,
thus its hard to maintain the mass. Greater the mass, greater the decay.

+ radius of anything = (mass / 2) units

+ Speed of a blob is given by the following formula: 2.2 * (mass <sup>-0.439</sup>) units s<sup>-1</sup>

+ Number of viruses are fixed for a map. If a virus is eaten then it re-emerges imediately.

+ Map dimensions (16:9) 4992 X 2808 units <sup>2<sup>

+ For each move you get `2 s`, you must make a move within that time otherwise your bot will be
disqualified. If you make an invalid move, you will be disqualified. Refrain yourself from
writing anying to STDOUT, because the game engine pipes the STDOUT of the bot to read the moves.
Feel free to write anyting to `STDERR`, you can use this for debugging purposes. You will get back your
`STDERR` after running the game on our servers.

+ You can change the direction of your bot relative to your current direction
(+30 <sup>o</sup> or -30 <sup>o</sup>). Changing direction does not have a penalty
on speed of the blob. 

+ You must print `I'm Poppy!` at the start for your bot to be acknowledged.

**The origial is available [here](http://agar.gcommer.com/index.php?title=Main_Page)**

---

<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/3.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.