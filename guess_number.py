import random
print('let me think of a number between 1 to 50')
easy_or_hard = input("choose a level of difficulty...Type 'easy' or 'hard': ")
number = random.randint(1,50)
print(f'the number is {number}')

if easy_or_hard == 'easy':
    attempts = 10

    print(f'you have {attempts} attempts remaining to guess the number')
else:
    attempts = 5
    print(f'you have {attempts} attempts remaining to guess the number')




game_over = False
while not game_over:
    guess = int(input("enter a guess: "))
    print(f'make a guess: {guess} ')

    if easy_or_hard == 'easy':



        if guess<number:
            print(f'your guess is too low')
            print('guess again')
            attempts -= 1
            print(f'you have {attempts} attempts remaining to guess the number')
            if attempts == 0:
                game_over = True
        elif guess>number:
            print(f'your guess is too high')
            print('guess again')
            attempts -= 1
            print(f'you have {attempts} attempts remaining to guess the number')
            if attempts == 0:
                game_over = True
        elif guess==number:

            print(f'your guess is right...The answer was {guess}')
            break
    else:
        

        if guess<number:
            print(f'your guess is too low')
            print('guess again')
            attempts -= 1
            print(f'you have {attempts} attempts remaining to guess the number')
            if attempts == 0:
                game_over = True
        elif guess>number:
            print(f'your guess is too high')
            print('guess again')
            attempts -= 1
            print(f'you have {attempts} attempts remaining to guess the number')
            if attempts == 0:
                game_over = True
        elif guess==number:

            print(f'your guess is right...The answer was {guess}')
            break


