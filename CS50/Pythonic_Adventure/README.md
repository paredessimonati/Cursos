# Pythonic Adventure

#### Video Demo: https://www.youtube.com/watch?v=qjAHLNDSsP4

#### Description:


#### A few words...

I wanted to create a fun final project for my CS50 class.

This is it! A text adventure game, like the ones I grew up playing.

I want to thank my wife for beta testing the game and helping me correct a lot 
of dialogue lines misspellings.


#### Back to the project.

### project.py
The game is a simple adventure game, in a medieval fantasy setting. The goal of
the game is to exit the dungeon with as much loot as possible.

The main file, project.py, takes care of some settings for the game, like debug
mode to skip intro sequence, difficulty which increases damage dealt by the 
enemies and enemy spawning which defines the chance an enemy will appear in the
room.

There's also a room counter, which tracks the players progress and also define
some dialog options.

Finally the file starts the game by calling the intro sequence.

### text.py
I wanted to have an ascii picture when the game started and I opened a box 
I couldnt really close. I starting going to many ascii art websites and i 
found a simple drawing i really liked. [Asciiart](https://www.asciiart.eu/)

Then i dug deeper and found how to control the cursor in the terminal, i used
ANSI escape codes to move it, and with time and print i made some little effects
im quite proud of haha.

Then i found out i could change colors with other ANSI escape codes so i started
playing with that too.

With all those tools i had available i decided to create a separate text.py file
with many functions, a color class and some variables to handle all the 
text-related settings.

Somehow i managed to create something that i feel looks nice, with player's
health displayed on top of the screen and a command menu at the bottom.

Almost all of the text in the game is printed through the text.py functions.

### room.py
In this file all the room logic happens. It has a class, Room, that handles
everything. 

The init function stores some variables, there are a few functions that only
return values and then the 3 big ones:

new_room() handles a lot of stuff, i even did a docstring to help me remember.
First it generates a dictionary with all the text variables for the current
room. Then it generates a random 10 digit seed that i use for various functions
inside the game such as the room itself (trapdoors, loot and potions appearing),
enemy spawning (they always spawn, they just dont interact with the player),
and if they do, if they aggro or not. 

I had to go with the seed route because it was easier to keep the game from 
suddenly generate random stuff when it was not supposed to.

describe_room() handles all the concatenation of the many many variables. Some 
dialog lines are forced or deleted depending of the random generation and this 
function handles all that.

room_search() handles the exits, items and potions in the room. Here i can 
modify the chances trapdoors, items and potions appear and sends all the info 
to the caller.

#### attr.py 
In the attr.py file there's 22 lists and directories containing
many lines of items, attributes and text in general for the game. I spent hours
figuring out how to better make random concatenated lines to sound and look 
decent. Also spent hours coming up with ideas, even though i borrowed a lot from
old rpg manuals, forums and stuff like that.

There's nothing much going on in the file other than that.

Enemies and Items are stored in dictionaries, the enemies have individual lines
of text for many scenarios like attack, defeat, after defeat or noattack, theres
also values for HP and agresiveness.

#### game_logic.py
Here's where most of the magic happens. I have 2 main functions and 2 smaller
ones. The search_first() function just checks if the player searched the room
before allowing him to do certain actions, the command() function is the one
tasked to mediate between the text functions in text.py and all the stuff that's
happening in the main loop... talking of which...

main_loop() The main loop calls the Room class to generate a new room every time
the player exits a door. Room returns the variables here and main_loop takes care
of interacting with text.py to print all the text in the terminal.

It handles the logic of what to do if the enemy spawned, if it aggroed, etc. 

Then it goes through every command the player has at his disposal like search,
open, exit, etc.

If a player loots something, main_loop takes care of making sure the item
disappears from the room, takes care of the doors, etc. But the best part, even
though it was one of the easier ones to do...

fight_loop() All the fun stuff happens here, gets data from the player and the
enemy, randomizes some numbers to make the fight screen be more dynamic, like
adding a chance to miss an attack or to do more or less damage.

The fighting is really simple and automatic, is not at all interactive other than
pressing enter to watch some numbers go up or down, but its really fun all the 
same haha. It handles win and lose condition, despawns the enemy if the player 
wins and also despawns the player if he loses with a nice sys.exit message.

#### enemy.py
Just a small class for the enemy, it has some variables like alive, visible,
aggro, hp, and others. Handles part of the seed value to check against the
enemy's attributes if he aggros or not. It handles a little of the logic for the
description of the enemy in the main loop.

#### player.py
Basically the same than the enemy but much much simpler, it just stores the 
player class with some attributes and some functions to recall values.



And that's it basically.

I really enjoyed doing this project and the class in general. Ive always loved
computers but i never got into coding. Im in my 40s now and i never thought i 
was going to be able to learn how to code.

The CS50 class was really hard, a couple of times i almost gave up but my wife 
encouraged me to keep going and im glad i did.

I wanted to thank David, Brian, Carter, all the staff behind the scenes and also
Harvard to give me and so many others the chance to do this course for free.

And also to all of stackoverflow for helping me get unstuck with this project.

Thanks!

Alejandro Paredes.
Santiago, Chile
