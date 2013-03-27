"""
This example is inspired by Zed A. Shaw's "Learn Python The Hard Way", Release 0.9
If you are keen on learning about Python's concepts through writing some test adventures (and some other stuff^^),
I would recommend you having a look at the whole tutorial at http://learnpythonthehardway.org/book/
"""


def pink_room():
    surroundings = """
    You are in a round room 3x3.
    It is all painted candy pink.
    Some candy is glued on the wall.
    More candy is scattered on the floor.
    In the middle there is a big table with muffins and waffles and stuff.
    You suddenly feel very hungry.
    What do you help yourself to?
    Some candy from the floor? Candy from the wall? A muffin? A waffle?
    """
    print(surroundings)

    next_move = input("> ")

    if "candy" in next_move.lower() and "floor" in next_move.lower():
        pink_room()

    elif "candy" in next_move.lower() and "wall" in next_move.lower():
        print("You fell asleep\n....")
        start()

    elif "muffin" in next_move.lower():
        ponnies_room()

    elif "waffle" in next_move.lower():
        cat_baies_room()

    else:
        dead("You just starved yourself to dead.")

def ponnies_room():
    #####TODO decide what this room does ###############
    print("blup")

def cat_babies_room():
    surroundings = """
    """
    print(surroundings)
    lala = False

    while True:
        next_move = input("> ")

    print("anyway")


########### TODO put some extra room(s) here ##############

######################################################

def dead(reason):
    print(reason)
    print("You're dead. It was a pleasure playing with you.")

def start():
    surroundings = """
    You are standing in the middle of a violets' field.
    There is one door on your right and one on your left.
    An angry unicorn is running right at you.
    You can escape trough one of the doors.
    Which one do you choose?
    """

    print(surroundings)

    next_move = input("> ")

    if "left" in next_move:
        pink_room()
    elif "right" in next_move:
        cat_babies_room()
    else:
        dead("Sorry bro/sis, you didn't make it to either door.\nThe unicorn was faster.")


start()
