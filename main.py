import random

print()
print()
print("\t\t\t\tNice Shootin', Tex...")
print("\t\t\t\t---by MannyCutya---\n\n")

inventory = ['Wallet', 'Dog Tags']
wallet = ['5 Dollars', 'Trunk Key', 'Expired Condom']


def action(cmd):

    if "inv" in cmd:
        inv_control("check")
    else:
        return cmd


def not_understood(cmd):

    cmd = cmd.lower()
    naughty_words = ['fuck', 'shit', 'cunt', 'asshole', 'bitch', 'dick']

    if cmd in naughty_words:
        print("Kiss your mother with that mouth? I do...")
        if "dick" in cmd:
            print("Ya know, dick isn't necessarily a bad word, you Richard.")

        return f"Try again, you {cmd}"

    retorts = [
        "Yeah, I don't get what you're saying...",
        f"I don't understand \"{cmd}\"",
        f"\"{cmd}\"? Try again, chief...",
        f"You would try \"{cmd}\", but that's not how this works..."
    ]

    return random.choice(retorts)


def inv_control(cmd):

    if "check" in cmd:
        for item in inventory:
            print(item)
    else:
        print("I don't understand ")


def room_quarters(first_run):

    trunk = ['Pants', 'Boots', 'Shirt']
    trunk_locked = True
    trunk_open = False
    rifle_on_rack = True
    in_room = True
    boots_on = False
    pants_on = False

    room_desc= """
    Sleeping Quarters:
    
    The room is now empty. A chest rests at the end of your bed. Bunks and rifle racks adorn an otherwise
    spartan room. The doorway to the halls is left of your bunk across the room.
    """

    if first_run:
        print("...muffled sounds...")
        print("...everything's blurry...")
        print("""
        As things come into focus, you realize you're in your bunk, as a cacophony of alarms scream
        down the corridor into the sleeping quarters. 
        
        You're Pvt. Tex Bullseye. Near-sighted sharpshooter. Mediocre extraordinaire.
        
        As the last of a panicked troop spills out of the sleeping quarters and into the hall, you damn your sleep-
        heavy tendencies as your sit up at the edge of your bed sporting only a pair of black-spotted boxers. 
        
        The room is now empty. A chest rests at the end of your bed. Bunks and rifle racks adorn an otherwise 
        spartan room. The doorway to the halls is left of your bunk across the room.
        """)

        print("What's your first move, private?")

        while in_room:

            prompt = input(">>> ")

            if action(prompt) == "look":
                print(room_desc)
            elif action(prompt) == "open trunk":
                if trunk_locked:
                    print("The trunk is locked. What did you do with your key?")
                elif trunk_open:
                    print("The trunk is already open.")
                else:
                    print("You open the trunk.\n")
                    print("Now that you've managed the daunting task of opening your trunk, you find")
                    print("the following contents inside:")

                    trunk_open = True

                    for items in trunk:
                        print(items)
            elif action(prompt) == "unlock trunk":
                if "Trunk Key" in wallet:
                    print("You unlock your trunk. Nicely done!")
                    trunk_locked = False
            else:
                print(not_understood(action(prompt)))



    else:
        print("You are in the sleeping quarters.")

        prompt = input(">>> ")

        if "open trunk" in prompt and trunk_locked:
            print("You trunk is locked.")


room_quarters(True)
