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

    print("plz enter a number above 1")
    return num_rounds



round = find_rounds("how many rounds between 1-10 do you want to play? ")

