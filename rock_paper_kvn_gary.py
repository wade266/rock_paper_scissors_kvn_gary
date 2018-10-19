from random import randint

options = ["ROCK", "PAPER", "SCISSORS", "KVN", "GARY"]
message = {
        "tie" : "Yawn it's a tie. KVN wants action!",
        "lose_0" : "Haha KVN beat you! Embrace the KVN.",
        "won_rock_0" : "Yay you crushed the scissors and took victory!",
        "won_rock_1" : "Victory. You bashed KVN over the head good job!",
        "won_paper_0" : "Hurray you for throwing your paper on a rock and ignoring it's exsistence!",
        "won_paper_1" : "Sweet, your paper notes confused Gary. You won!",
        "won_scissors_0" : "You sliced and diced that paper good, dining on victory. Wait don't eat it!",
        "won_scissors_1" : "You stabbed KVN in the eye, Gary is super happy right now! You take victory with you!",
        "won_KVN_0" : "You chose KVN, KVN eats the paper, KVN saves the day!",
        "won_KVN_1" : "Gary is KVN's best friend, KVN always wins! ",
        "won_gary_0" : "Gary throws the rock far away and forgets about it. Take that Rock, Yeah!",
        "won_gary_1" : "Gary shows the scissors the real raw Gary!, the scissors break in awe of what they have seen."
        }

def decide_winner(user_choice_0, computer_choice):
    print "You selected: %s" % user_choice_0
    print "KVN selected: %s" % computer_choice
    if user_choice_0 == computer_choice:
        print message["tie"]
    elif user_choice_0 == options[0] and computer_choice == options[2]:
        print message["won_rock_0"]
    elif user_choice_0 == options[0] and computer_choice == options[3]:
        print message["won_rock_1"]
    elif user_choice_0 == options[1] and computer_choice == options[0]:
        print message["won_paper_0"]
    elif user_choice_0 == options[1] and computer_choice == options[4]:
        print message["won_paper_1"]
    elif user_choice_0 == options[2] and computer_choice == options[1]:
        print message["won_scissors_0"]
    elif user_choice_0 == options[2] and computer_choice == options[3]:
        print message["won_scissors_1"]
    elif user_choice_0 == options[3] and computer_choice == options[1]:
        print message["won_KVN_0"]
    elif user_choice_0  == options[3] and computer_choice == options[4]:
        print message["won_KVN_1"]
    elif user_choice_0 == options[4] and computer_choice == options[0]:
        print message["won_gary_0"]
    elif user_choice_0 == options[4] and computer_choice == options[2]:
        print message["won_gary_1"]
    else:
        print message["lose_0"]

def play_RPSG_kvn(turn):
    if turn == 0:
        print("Hi I am KVN, your insanity avoidance robot.\nLets play some Rock, Paper, KVN, Gary!")
    user_choice_0 = raw_input("Enter Rock, Paper, Scissors, Gary or KVN: ")
    user_choice_0 = user_choice_0.upper()
    computer_choice = options[randint(0,4)]
    decide_winner(user_choice_0, computer_choice)

"""
def play_RSPG_human():
    print("")
    user_choice_0 = raw_input("Human 1 Enter: Rock, Paper, Scissors, Gary or KVN: ")
    user_choice_1 = raw_input("Human 2 Enter: Rock, Paper, Scissors, Gary or KVN: ")
"""
def mode(x):
    turn = 0
    if x == 1:
        while turn < 3:
            play_RPSG_kvn(turn)
            turn += 1
        if  score_0 > score_1:
            print("Congratulations you beat Kevin with a score of %d" % score_0)
        elif score_0 < score_1:
            print("You let KVN beat you. His score %d is much greater than yours, maybe next time?" % score_1)
    elif x == 2:
        while turn < 3:
            play_RPSG_human()
            turn += 1
    else:
        print("If you want the chance to win a cookie. I suggest you get off my cheeks and enter the correct number I asked for.")
        choice = raw_input("Try again.")

choice = int(raw_input("Hello I am H.U.E.\nWelcome to Rock, Paper, Scissors, KVN, Gary or R.S.P.G. for short.\nThe K is silent, as KVN is a Jag-off.\nPlease enter 1 or 2 for game mode.\n  1 = You vs KVN\n  2 [Coming Soon] = You vs The Real Raw You\n"))

mode(choice)
