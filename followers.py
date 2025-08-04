import game_database,random

end_of_game = False
score = 0
while not end_of_game:
    info1 = random.choice(game_database.data)
    info2 = random.choice(game_database.data)
    print(f'compare 1: {info1['name']}, a {info1['description']}, from {info1["country"]} ')
    print(f'compare 2: {info2['name']}, a {info2['description']}, from {info2["country"]}')
    more_followers = input("who has more followers? type '1' or '2' ")
    if more_followers == '1':
        if info1['follower_count']>info2['follower_count']:
            score += 1

            print(f'you are right.Your score is {score}')
        else:
            score -= 1
            print(f'you are wrong. Your score is {score}')
            break
    else:
        if info2['follower_count']>info1['follower_count']:
            score += 1
            print(f'you are right.Your score is {score}')
        else:
            score -= 1
            print(f'you are wrong. Your score is {score}')
            break

