#Python imports
from random import randint
import random
from colorama import Fore, Back, Style
from time import sleep
import sys


#Text effect
def char_delay(text, delay):
  for letter in text:
    print(letter, end="")
    sleep(delay)
    sys.stdout.flush()


char_delay(Style.BRIGHT + "Programmed by Krish Patel & Nicole Wang.\n\n", 0.03)


#This is an overarching while loop. This purpose of this loop will be shown at the end, allowing the user to choose whether or not they would like to play again...
while True:
  print("\n--------------------------------------------")
  print(Fore.WHITE + Back.CYAN + "New game!" + Back.RESET)
  print(Style.RESET_ALL + Back.RESET)
  

  #Introduction
  char_delay("Welcome to the rock, paper, scissors, lizard, spock game!", 0.03)
  #Asks player for their name
  p1_name = input(Fore.BLUE + Style.BRIGHT + "\nPlayer 1, enter your name." + Back.RESET + Style.DIM + " ")
  p1_name = p1_name.upper()
  print(Fore.RESET + Style.RESET_ALL + "Hello " + Fore.BLUE + Style.BRIGHT + p1_name + ".")


  #Ask user what they winning score they would like to play to
  winning_score = input(Fore.RESET + Style.RESET_ALL + "\nWhat is the winning score you would  like to play to?\n🟧 Keep in mind you must play to at least 7 points... ")
  

  #Conditional statement requiring user to have at least 7 rounds.
  if winning_score.isnumeric() == True and int(winning_score) < 7:
    print(Back.BLUE + "You must have at least SEVEN (7) rounds." + Back.RESET)
    winning_score = input("Please enter the winning score you would like to play to. This time, rememeber the miniumun is SEVEN (7) rounds. ")
    print("Great, so...")
    

  #Conditional statement for making sure that the user input is a numerical value.
  if winning_score.isnumeric() == True:
    print("\nGame specifications:\n🟨 You will play to " + winning_score + " points.\n🟪 Your opponent is the CPU player.\n")
  if winning_score.isnumeric() != True:
    print("Invalid input!!\nRemember to only enter a NUMERICAL value.")
    winning_score = input("So... what is the winning score you would like to play to? The miniumun score you have to play to is seven (7): ")
    print("\Alrighty " + p1_name + ", let's play a game of rock paper scissor lizard spock! You will play to " + str(winning_score) + " points.\n")


  #Tell user a bit about the game.
  print(Back.YELLOW + Style.BRIGHT + "Remember, this is a special verision of Rock, Paper, Scissors, meaning you may choose to play either rock, paper, scissors, lizard, or spock!." + Fore.RESET + Back.RESET + Style.RESET_ALL)


  #Starting scores for the user and CPU player.
  p1_score = 0
  cpu_score = 0
  p1_list = ["randomvariable"] #for the no repetition code
  cpu_list = ["samething"]
  list = ["rock", "paper", "scissors", "lizard", "spock"]      #CPU list to randomly pick 
  #for the streak bonus
  p1_win = False #sets the player to not winning first
  cpu_streak = 0 #streak of zero
  cpu_win = False
  p1_streak = 0


  #While loop w/ condition to prevent infinite looping, stops the loop when player or cpu gets to the winning score.
  while p1_score < int(winning_score) or cpu_score < int(winning_score):
    

    print("\n------------------------------") #Little BUFFER between each round
    p1_choice = input(Fore.MAGENTA + "What is your play? " + Fore.RESET + Style.RESET_ALL).lower()
    p1_list.append(str(p1_choice)) #adds player choice to list for a repetition check
    if p1_list[0] != p1_list[1]:#statement that deletes the first variable on the list so it can compare the input that the player put in to the next input
      del p1_list[0]#takes out the first variable of the list so the next one can be added and compared
    else:
      print(Fore.RED + "\nYou cannot choose the same thing twice; try again. ❌" + Fore.RESET)
      del p1_list[1]#deletes the most recent input so the players next input can be compared to the one they had last round
      continue#starts the while loop over
      

    #This is the computer's randomized choice!
    computer = random.choice(list)#generate random
    cpu_list.append(str(computer))#adds variable to list
    while cpu_list[0] == cpu_list[1]:#compares this round and last rounds input and if they are the same...
      computer = random.choice(list)#make another random
      del cpu_list[1]#take out the variable before and add the new variable
      cpu_list.append(str(computer))
    #the while loop above repeats as many times as possible until the last round and current round does not have the same choice
    del cpu_list[0]
    print(Fore.RED + "The cpu player has randomly picked " + computer + ".\n" + Fore.RESET)

    
    #Conditionals code for the game.
    if computer == p1_choice:#both have the same choice is draw
      print("It's a draw!")
      print("No player gets the points for this game.")
    

    elif computer == "rock" and p1_choice == "scissors":
      print(Fore.BLUE + Style.BRIGHT + p1_name + Fore.RESET + Style.RESET_ALL + ", you lose 😞 b/c rock crushes scissors!")#printed statement
      cpu_score += 1#adds one to winner
      cpu_win = True#makes winners win variable true
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "rock" and p1_choice == "lizard":
      print(Fore.BLUE + Style.BRIGHT + p1_name + Fore.RESET + Style.RESET_ALL + ", you lose 😞 b/c rock crushes lizard!")
      cpu_score += 1
      cpu_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "paper" and p1_choice == "rock":
      print(Fore.BLUE + Style.BRIGHT + p1_name + Fore.RESET + Style.RESET_ALL + ", you lose 😞 b/c paper covers rock!")
      cpu_score += 1
      cpu_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "paper" and p1_choice == "spock":
      print(Fore.BLUE + Style.BRIGHT + p1_name +Fore.RESET + Style.RESET_ALL + ", you lose 😞 b/c paper disproves spock!")
      cpu_score += 1
      cpu_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "scissors" and p1_choice == "paper":
      print(Fore.BLUE + Style.BRIGHT + p1_name + Fore.RESET + Style.RESET_ALL + ", you lose 😞 b/c scissors cuts paper!")
      cpu_score += 1
      cpu_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "scissors" and p1_choice == "lizard":
      print(Fore.BLUE + Style.BRIGHT + p1_name + Fore.RESET + Style.RESET_ALL + ", you lose 😞 b/c scissors decapitates lizard!")
      cpu_score += 1
      cpu_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "lizard" and p1_choice == "paper":
      print(Fore.BLUE + Style.BRIGHT + p1_name + Fore.RESET + Style.RESET_ALL + ", you lose 😞 b/c lizard eats paper!")
      cpu_score += 1
      cpu_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "lizard" and p1_choice == "spock":
      print(Fore.BLUE + Style.BRIGHT + p1_name + Fore.RESET + Style.RESET_ALL + ", you lose 😞 b/c lizard eats paper!")
      cpu_score += 1
      cpu_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "spock" and p1_choice == "rock":
      print(Fore.BLUE + Style.BRIGHT + p1_name + Fore.RESET + Style.RESET_ALL + ", you lose 😞 b/c spock vaporizes rock!")
      cpu_score += 1
      cpu_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "spock" and p1_choice == "scissors":
      print(Fore.BLUE + Style.BRIGHT + p1_name + Fore.RESET + Style.RESET_ALL + ", you lose 😞 b/c spock smashes scissors!")
      cpu_score += 1
      cpu_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    #CODE FOR IF USER WINS!


    elif computer == "paper" and p1_choice == "scissors":
      print("You win 🙃 b/c scissors cuts paper.")
      p1_score += 1
      p1_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "rock" and p1_choice == "paper":
      print("You win 🙃 b/c paper covers rock.")
      p1_score += 1
      p1_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "lizard" and p1_choice == "rock":
      print("You win 🙃 b/c rock crushes lizard.")
      p1_score += 1
      p1_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "spock" and p1_choice == "lizard":
      print("You win 🙃 b/c lizard posions spock.")
      p1_score += 1
      p1_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "scissors" and p1_choice == "spock":
      print("You win 🙃 b/c spock smashes scissors.")
      p1_score += 1
      p1_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)
    

    elif computer == "scissors" and p1_choice == "rock":
      print("You win 🙃 b/c rock crushes scissors.")
      p1_score += 1
      p1_win = True
      print("\nYou have " + str(p1_score) + " points!! 🤑\nThe computer has " + str(cpu_score) + " points.")


    elif computer == "lizard" and p1_choice == "scissors":
      print("You win 🙃 b/c scissors decapitates lizard.")
      p1_score += 1
      p1_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "paper" and p1_choice == "lizard":
      print("You win 🙃 b/c lizard eats paper.")
      p1_score += 1
      p1_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "spock" and p1_choice == "paper":
      print("You win 🙃 b/c paper disproves spock.")
      p1_score += 1
      p1_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "rock" and p1_choice == "spock":
      print("You win 🙃 b/c spock vaporizes rock.")
      p1_score += 1
      p1_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    elif computer == "scisscors" and p1_choice == "rock":
      print("You win 🙃 b/c rock crushes scissors.")
      p1_score += 1
      p1_win = True
      print(Fore.BLUE + "\nYou have " + Fore.CYAN + str(p1_score) + Fore.BLUE + " points." + Fore.RED + "\nThe computer has " + Fore.CYAN + str(cpu_score) + Fore.RED +  " points!! 🤑" + Fore.RESET)


    #If invalid user input.
    else:
      print("\nThis is not a play! You should enter rock, paper, scissors, lizard, or spock.")


    #STREAK BONUS Code
    if p1_win == True: #if the player wins
      cpu_streak = 0#cpu streak is set to zero
      p1_streak += 1#player streak added by one
      p1_win = False #sets the players win back to false
      print(Fore.BLUE + "\n" + p1_name + ", you have a streak of: " + str(p1_streak) + Fore.RED + "\ncpu has a streak of: " + str(cpu_streak) + Fore.RESET)
      
      
      if p1_streak == 3:#when player has a streak of 3
        p1_score += 2#bonus 2 points added to score
        p1_streak = 0#set streak back to zero
        print(Fore.BLUE + p1_name +  ", you got bonus points because of streak bonus!!! \nYou now have " + str(p1_score) + " points.")
    
    
    elif cpu_win == True:
      p1_streak = 0
      cpu_streak += 1
      cpu_win = False
      print(Fore.BLUE + "\n" + p1_name + ", you have a streak of: " + str(p1_streak) + Fore.RED + "\ncpu has a streak of: " + str(cpu_streak) + Fore.RESET)
      
      
      if cpu_streak == 3:
        cpu_score += 2
        cpu_streak = 0
        print(Fore.RED + "The CPU got bonus points because of streak bonus!!!\nThey now have " + str(cpu_score) + " points.")
    
    
    elif cpu_win == False and p1_win == False:
      cpu_streak = 0
      p1_streak = 0
      print(Fore.BLUE + "\n" + p1_name + ", you have a streak of: " + str(p1_streak) + Fore.RED + "\ncpu has a streak of: " + str(cpu_streak) + Fore.RESET)


    if p1_score >= int(winning_score) or cpu_score >= int(winning_score):
      break


  #To determine WINNER
  print(Fore.RESET + Style.RESET_ALL + Back.RESET + "\n")
  char_delay("WE", 0.05)
  char_delay("\nHAVE", 0.05)
  char_delay("\nA", 0.05)
  char_delay("\nWINNER!!\n\n", 0.05)


  if p1_score > cpu_score:
    char_delay(Fore.CYAN + p1_name + ", YOU WIN!!!!", 0.1)


  else:
    char_delay(Fore.CYAN + "You lose; the CPU WINS.", 0.1)


  #To play game again
  #REMEBER THE INITIAL WHILE LOOP... Can restart game if user input = play_again = TRUE.
  play_again = input("\n\nWould you like to play again? ")
  play_again = play_again.lower()


  if play_again == "yes" or play_again == "sure" or play_again == "yeah" or play_again == "okay" or play_again == "ok" or play_again == "ye" or play_again == "of course" or play_again == "ofc":
    play_again = True
    char_delay(Fore.RESET + Style.RESET_ALL + Back.RESET + "\nYay 🤗\n\n", 0.03)
    continue


  else:
    play_again = False
    char_delay(Fore.RESET + Style.RESET_ALL + Back.RESET + "\nNo worries! See you next time. 👋", 0.01)
    break