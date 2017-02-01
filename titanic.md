# Titanic (bot-api that the contestants can use)

## Setters (or the functions that affect the state)

  + **change_direction(child_no:Int, relative_angle:Float)**: After splitting if there are 3 bots, then child_no identifies each one uniquely. relative_angle is +30<sup>o</sup> or -20<sup>o</sup>

  + **eject_mass(child_no:Int)**: ejects some fixed amount of mass for child_no

  + **split(child_no)**: if the size is big enough to split then the split is done in the given direction, If the mass is not enough to split, this command is simply ignored.

  + **pause(child_no)**: it makes the bot to come to a stand-still.

## Getters (functions that do not affect the state)

   + **get_bots()**: returns a list of dicts with bot coordinates, bot radius, bot mass, bot score, direction(angle)

   + **get_foods()**: returns a list of tuples with food coordinates.

   + **get_viruses()**: returns a list of tuples with virus coordinates.

   + **get_ffields()**: returns a list of dicts representing force-field/water-stream coordinates and other details.