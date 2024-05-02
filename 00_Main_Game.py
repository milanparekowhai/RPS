def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        print("please enter yes / no")


def find_rounds(question):
    responce = input(question)

    try:
        num_rounds = int(responce)

        if num_rounds >= 1:
            return num_rounds


        else:
            print("")

    except ValueError:
        print()

    print("enter a whole number 1 and above")


want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    print('''
    ***** instrutions *****
     to start there will be a chosen amount of rounds
      To win rps you will have to chose an attack
     Rock paper or scissors.
     for a simple explonaetion
     
     R = rock S = scissors P = paper
     p beats r, r best s, s beats p,
      
     if you choose the same then it will be a tie and we will restart
     if you win the round you will get a point and same for you opp
     the person with the most points at the end of the round will win win
    ''')
else:
    print()

round = find_rounds("how many rounds do you want to play? ")