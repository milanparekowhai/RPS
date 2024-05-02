# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans):

    error = f"Please enter a vaild option: {valid_ans} "

    while True:

        # Get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the lst
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of a item in the list.

            elif user_response == item:
                return item

                # print error if user dose not enter something that is valid
        print(error)


# main route goes here
yes_no = ["yes", "y", "no", "n"]
rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker("Do you want to see the instructions? ",yes_no )

if want_instructions == "yes" or "y":
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
     the person with the most points at the end of the round will win win'''
      )
