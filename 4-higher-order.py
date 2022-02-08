import random
from datetime import datetime

random.seed(datetime.now())


def make_move():
    # Update this function to allow the 2
    # functions below to work correctly using
    # a higher order function
    rnd = random.randrange(0, 3)
    if rnd == 0:
        return "Rock"
    elif rnd == 1:
        return "Paper"
    else:
        return "Scissors"


def make_random_move():
    # Should always be a random move
    move = make_move()
    print(move)


def always_paper():
    # Should always print "Paper"
    # Only update the call to make_move
    move = make_move()
    print(move)


make_random_move()
always_paper()
