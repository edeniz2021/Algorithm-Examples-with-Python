import random
print("Welcome to the Number Guessing Game\n")
print("I am thinking of a number between 1 and 100.\n")
num = random.randrange(1,101)

easy = 10
hard = 5
def sec():
    a = input("Choose a difficulty 'hard' or easy 'easy' ?")
    if a == "easy":
        return easy
    elif a == "hard":
        return hard
b=0
def check_answer(guess, answer, turns):

  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")
c = sec()
while num!= b:
    b =int(input("Make a guess: "))
    if num != b:

        c = check_answer(b, num,c)
        print("Guess again")
        if c == 0:
            print("you lose")
            break
    else:
        print("you won ")






