# FizzBuzz!

# functions

# load correct answer
def correct_answer_is(current_number):
    if current_number % 15 == 0:
        return "FizzBuzz"
    elif current_number % 5 == 0:
        return "Buzz"
    elif current_number % 3 == 0:
        return "Fizz"
    else:
        return ""


def play():
    i = 1

    while True:

        player_answer = input(f"{i}: ")

        if player_answer == correct_answer_is(i):
            i += 1
        else:
            print("Ouuuuch!")
            print("Game Over")
            exit(1)


#=============================================
# main main main
#=============================================

print("Willkommen beim Spiel FizzBuzz!")

play()


    

    



