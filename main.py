import random


# def guess(x):
#     num = random.randint(0, x)
#     incorrect = True
#     while incorrect:
#         gnum = input(f"Guess a num between 0 and {x}: ")
#         if int(gnum) == num:
#             print("You guess correct!!!")
#             incorrect = False
#         elif int(gnum) < num:
#             print("Guess a little higher")
#         else:
#             print("Guess a little lower.")
#
#     print(f"The correct guess is {num}")
#
#
# guess(20)

def comp_guess(x):
    low = 0
    high = x
    feedback = ''
    incorrect = True
    print(f"Guess a number between 0 and {x}")
    while incorrect:
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high(H), too low(L), or correct(C) : ".lower())
        if feedback == 'l':
            low = guess + 1

        elif feedback == 'h':
            high = guess - 1

        else:
            incorrect = False

    print(f"The number comp guessed correctly is {guess}")


comp_guess(20)
