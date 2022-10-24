import random
name = input("What's your name? ")
print(f"Hello, {name}! You're on your journey to find the Data Analytics Medal.")

rooms = ["Hometown", "Market", "Forest", "Tower", "Lonely Clearing"]
descriptions = {"Hometown": "Here you\'ll need to answer a question to win 5 coins that you can use later. Good luck!", 
                "Market": "Here you\'ll need to find the beekeeper and buy honey from him using the 5 coins you won on the previous step. We have a long way to go, so let\'s not stay long here!", 
                "Forest": "You’ll need to go through the forest to reach Tower where the mage lives. Be careful as there’s a bear that doesn’t let anyone pass the forest. When you meet him, just give him the honey you bought from the beekeeper :)", 
                "Tower": "Here you’ll need to find the mage and ask him to tell you the magic spell to unlock the medal. So let’s go find him.", 
                "Lonely Clearing": "This is our last room and you can already see the medal :) To unlock the medal, go ahead and say the magic spell that the mag told you."}        

print("""
You\'ll visit 5 rooms where you\'ll need to complete certain tasks to move forward. 
===================

""")
print(f'Your quest starts in {rooms[0]}.')
print(descriptions["Hometown"])

#to get the money and move to the next room the player needs to solve a simple math operation
hometown_task = input("What\'s 2 * 2? Enter your answer here: ")

while hometown_task != "4":
    hometown_task = input("Not quite, try again: ")

print("That\'s correct! You've collected 5 coins. Save them for later and let's move on :)")

# maybe I'll give the player an option to choose the next location between Market and Forest
# use dictionaries and Katmandu example from study materials + while loop to change locations
# while room == rooms[0]:
    # input("Where would you like to go: Forest or Market? ")
    # if input is Market:
    # print(f'You\'re now came to the {rooms[1]}.', descriptions["Market])
    # else:
    # print(f'Now you\'re in the {rooms[2]}.', descriptions["Forest"])
    
print(f'You\'re now came to the {rooms[1]}.')
print(descriptions["Market"])

# The player needs to buy honey from the beekeeper with 5 coins he won on the previous step.
# The code checks if the player has enough coins to buy the honey and if so, the player can grab one pot and move one.
honey = False

if honey is False:
    print("Give the beekeeper 5 coins.")
    honey = True

coins = 0
while coins < 5:
    coins = coins + 1
    print(coins)

print(f"The total amount of coins is {coins}. You can take a pot of honey now and move forward.")

print(f'Now you\'re in the {rooms[2]}.')
print(descriptions["Forest"])

# The player moves on to the forest where he leaves the honeypot to the bear and sneaks through the forest
if honey is True:
    print("Leave the honeypot for the bear and carefully sneak by.")
else:
    print("There is a BEAR in the forest!!! You run away.")
    
print(f"""
{name}, you successfully passed the forest!
""")
        
print(f"{name}, now you're in the {rooms[3]}.")
print(descriptions["Tower"])

# Player needs a magic spell to unlock the medal.  
# Mage doesn't want to give it away easily and suggests the player to play "Rock Paper Scissors" game. 
# If player wins, mage will tell him the magic spell. If not, they'll keep playing.

magic_spell = False
player_wins = False

if magic_spell is not True:
    print("Play the \"Rock, Paper, Scissors\" game with the mage. If you win, the mage will tell you the magic spell")
        
while player_wins == False: 
    player = input("Please enter R, P or S (for [R]ock, [P]aper and [S]cissors) ")
    mage = random.choice('RPS')
    print(f'The Mage has {mage} and the player has {player}')
    if player == 'R' and mage == 'S' or player == 'S' and mage == 'P' or player == 'P' and mage == 'R':
        print("Player wins")
        player_wins = True
        magic_spell = True
    elif player == 'R' and mage == 'P' or player == 'S' and mage == 'R' or player == 'P' and mage == 'S':
        print("Mage wins")
    elif player == mage:
        print("It's a draw")
    else:
        print("Not a valid input. Try again.")
        
if magic_spell == True:
    print(f"Mage: {name}, the magic spell is \"ratatata\".\nGood job! You're moving on to your last stop :)")
    
print(f"{name}, you’re very close to achieving your goal because you've reached the {rooms[4]}")
print(descriptions["Lonely Clearing"])

magic_spell = "ratatata"
player_input = input("Say the magic spell: ")

if player_input:
    player_input.lower()
    if magic_spell == player_input:
        print("Congrats! You unlocked the Data Analytics medal!")

print("""
Your quest has been successful!
""")


