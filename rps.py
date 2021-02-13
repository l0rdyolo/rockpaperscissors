import random
import datetime
GAME_CHOISE = ["Paper", "Rock", "Scissors"]
def menu():
    print("============== Menu ==============")
    print("1 - START GAME")
    print("2 - Show KDA")
    print("3 - How to Play")
    print("4 - Exit")
    print("==================================")
    print()
def howToPlay():
    print("bla bla bla explain how to play")
    print("If you ready to play Press 'P' for start the game")
def userMenuInput():
    user_input = int(input("Make your choise\n>>> "))
    return user_input
def startGame():
    print("Choise game style")
    print("1 - First 3 points win")
    print("2 - Endless game")
    print("3 - You can not win :) ")
    print("4 - Return menu ")
    ui = userMenuInput()
    if ui == 1:
        startBotGame()
    if ui == 2:
        startEndlessGame()
    if ui == 3:
        startUcantWinGame()
    if ui == 4:
        menu()
def startBotGame():
    user = 0
    computer = 0
    draw = 0
    while True:
        try:
            print("Paper - 1 Rock - 2 Scissors - 3")
            iu = userMenuInput()
            computer_choise = random.randint(0, 3)
            if iu == 1 and computer_choise == 0:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("Its draw")
                draw += 1
            if iu == 1 and computer_choise == 1:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("You win!!")
                user += 1
            if iu == 1 and computer_choise == 2:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("Computer Win!!")
                computer += 1
            if iu == 2 and computer_choise == 0:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("Computer Win!!")
                computer += 1
            if iu == 2 and computer_choise == 1:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("Its Draw")
                draw += 1
            if iu == 2 and computer_choise == 2:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("You Win!!")
                user += 1
            if iu == 3 and computer_choise == 0:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("You Win!!")
                user += 1
            if iu == 3 and computer_choise == 1:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("Computer Win!!")
                user += 1
            if iu == 3 and computer_choise == 2:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("Its Draw")
                draw += 1
            if user == 3:
                print("You > ", user, "-", computer, "< Computer")
                print("You win this game ! ")
                break
            if computer == 3:
                print("You > ", user, "-", computer, "< Computer")
                print("Computer win this game !")
                break
            if iu < 0 or iu > 3:
                print("Wrong choise please make a correct choise")
        except:
            print("Wrong choise please make a correct choise")
            continue
    logfile = open("rpsLog.txt", "a")
    today = datetime.datetime.now()
    today = str(today)
    logfile.write(today[0:19] + " Played game mode 1 (best of three)\n" + "User :" + str(user) + " Computer : " + str(
        computer) + " Draw : " + str(draw)+"\n")
    logfile.write("-----------------------------------------------------------------------------\n")
    logfile.close()
def startEndlessGame():
    print("For end game press '99' when you choise ")
    user = 0
    computer = 0
    draw = 0
    while True:
        try:
            print("Paper - 1 Rock - 2 Scissors - 3")
            iu = userMenuInput()
            if iu == 99:
                logfile = open("rpsLog.txt", "a")
                today = datetime.datetime.now()
                today = str(today)
                logfile.write(
                    today[0:19] + " Played game mode 1 (best of three)\n" + "User :" + str(user) + " Computer : " + str(
                        computer) + " Draw : " + str(draw) + "\n")
                logfile.write("-----------------------------------------------------------------------------\n")
                logfile.close()
                break
            computer_choise = random.randint(0, 3)
            if iu == 1 and computer_choise == 0:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("Its draw")
                draw+=1
            if iu == 1 and computer_choise == 1:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("You win!!")
                user += 1
            if iu == 1 and computer_choise == 2:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("Computer Win!!")
                computer += 1
            if iu == 2 and computer_choise == 0:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("Computer Win!!")
                computer += 1
            if iu == 2 and computer_choise == 1:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("Its Draw")
                draw += 1
            if iu == 2 and computer_choise == 2:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("You Win!!")
                user += 1
            if iu == 3 and computer_choise == 0:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("You Win!!")
                user += 1
            if iu == 3 and computer_choise == 1:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("Computer Win!!")
                computer+=1
            if iu == 3 and computer_choise == 2:
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", GAME_CHOISE[computer_choise],
                      " <- Computer choise is")
                print("Its Draw")
                draw += 1

            if iu <= 0 or iu > 3:
                print("Wrong choise please make a correct choise")
        except:
            print("Wrong choise please make a correct choise")
            continue
def startUcantWinGame():
    computer = 0
    print("When you bored to loss press '99' for exit xD ")
    while True:
        try:
            print("Paper - 1 Rock - 2 Scissors - 3")
            iu = userMenuInput()
            if iu==99:
                logfile = open("rpsLog.txt", "a")
                today = datetime.datetime.now()
                today = str(today)
                logfile.write(
                    today[0:19] + " Played game mode 3 (You cant win mode)\n Computer : "+ str(computer)+" You : 0 We told you you cant win...\n")
                logfile.write("-----------------------------------------------------------------------------\n")
                logfile.close()
                break
            if iu == 1:
                computer_choise = GAME_CHOISE[2]
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", computer_choise,
                      " <- Computer choise is")
                print("Computer Win!!")
                computer += 1
            if iu == 2:
                computer_choise = GAME_CHOISE[0]
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", computer_choise,
                      " <- Computer choise is")
                print("Computer Win!!")
                computer += 1
            if iu == 3:
                computer_choise = GAME_CHOISE[1]
                print("Your choise is -> ", GAME_CHOISE[iu - 1], " \VS/ ", computer_choise,
                      " <- Computer choise is")
                print("Computer Win!!")
                computer += 1
            if iu <= 0 or iu > 3:
                print("Wrong choise please make a correct choise")
        except:
            print("Wrong choise please make a correct choise")
            continue
def showKDA():
    outfile = open("rpsLog.txt","r")
    name_file = outfile.readline()
    while name_file != "":
        name_file = name_file.rstrip("\n")
        print(name_file)
        name_file = outfile.readline()
def endGame(isGameOver):
    isGameOver = False
    return isGameOver
def main():
    isGameOver = True
    print("###################################################################################")
    print("################################ROCK PAPER SCISSORS################################")
    print("###################################################################################")
    print()
    while isGameOver:
        menu()
        user_input = userMenuInput()
        if user_input == 1:
            startGame()
        if user_input == 2:
            showKDA()
        if user_input == 3:
            howToPlay()
        if user_input == 4:
            isGameOver = endGame(isGameOver)
main()
